################################
######## pre processing ########  
################################

import math
from sklearn.preprocessing import LabelEncoder
import csv
import numpy as np
import pandas as pd
from Geocoding import *
import math
import re
import seaborn as sns
import matplotlib.pyplot as plt
from dateutil.parser import parse
import datetime
import time
import copy


# with open("cd.csv",'w',newline='') as f :
#     fieldsTitle=['source','ditination','distance']
#     thewriter=csv.DictReader(f,fieldnames=fieldsTitle)
#     thewriter.writeheader()

spaces=10*" "

def Feature_Encoder(X,cols):
    for c in cols:
        lbl = LabelEncoder()
        lbl.fit(list(X[c].values))
        X[c] = lbl.transform(list(X[c].values))
    return X

def featureScaling(X,a,b):
    X = np.array(X)
    Normalized_X=np.zeros((X.shape[0],X.shape[1]))
    for i in range(X.shape[1]):
        Normalized_X[:,i]=((X[:,i]-min(X[:,i]))/(max(X[:,i])-min(X[:,i])))*(b-a)+a
    return Normalized_X

def ptn(Y):
    l=len(Y)
    for i in Y.index:
        print(f"\rhandle price fuction  percentage : {math.ceil((i/l)*100)}%{spaces}",end="")

        Y[i]=str(Y[i]).replace(",","")
    Y=Y.astype("float")
    print(f"\rhandle price fuction  percentage : {100}%{spaces}",end="")
    print("")
    return Y

def avr_p(data,col1,col2):
    l=len(data)
    z=data.groupby(col1).mean()[col2]
    for i in data.index:
        print(f"\ravrage of {col1}  percentage  : {math.ceil((i/l)*100)}%{spaces}",end="")

        P=data.loc[i,col1]
        data.loc[i,col1]=float(z[P])
    print(f"\ravrage of {col1}  percentage  : {100}%{spaces}",end="")
    print("")
    data[col1].astype("float")
    return data

def creat_d(data):
    l=len(data)
    # datacd = pd.read_csv('ss.csv',header=0)    
    for i in data.index:
        print(f"\rcreate distance function  percentage : {math.ceil((i/l)*100)}%{spaces}",end="")
        datacd = pd.read_csv('ss.csv',header=0)
        source=data.loc[i,'source']
        dest=data.loc[i,'destination']
        g=None
        for r in datacd.index:
            if (datacd.loc[r,'source']==source) & (datacd.loc[r,'destination']==dest )&(datacd.loc[r,'distance']!= None) :
                g=datacd.loc[r,'distance']
                break
                
        if(g==None):
            d=float(clc_d(ctl(source),ctl(dest)))
            data.loc[i,"distance"]=float(d)
            with open("ss.csv",'a',newline='') as f :
                row=[source,dest,d]
                thewriter=csv.writer(f,delimiter=',')
                thewriter.writerow(row)
            f.close()      
        else :
            data.loc[i,"distance"]=float(g)
    print(f"\rhandle price fuction  percentage : {100}%{spaces}",end="")
    print("")
    return data

def stop(data):
    l=len(data)
    for i in data.index:
        print(f"\rstop function percentage : {math.ceil((i/l)*100)}%{spaces}",end="")
        g=str(data.loc[i,"stop"])
        search = re.search('(\d)', g)
        if not search:
            g = float(0)
        else:
            g = float(search.group(1))
        # if g[0]=="1": g=float(1)
        # elif g[0]=="2": g=float(2)
        # else :g=float(0)
        data.loc[i,'stop']=g
    print(f"\rhandle price fuction  percentage : {100}%{spaces}",end="")
    print("")
    return data

def handleDate(data):
    # unifying the date format across the whole column.
    # ------------------------------------------------- #
    pd.options.mode.chained_assignment = None
    for i in data.index:
        print(data['date'][i])
        data['date'][i] = parse(data['date'][i])

    # converting to timestamp:
    # --------------------------#
    for i in data.index:
        data['date'][i] = float(
            time.mktime(datetime.datetime.strptime(str(data['date'][i]), "%Y-%m-%d %H:%M:%S").timetuple()))


def handl
