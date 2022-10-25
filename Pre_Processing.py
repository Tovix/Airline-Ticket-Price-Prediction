##############################
######## main program ########  
##############################

print("\n\n################################")
print("############# start ############")
print("################################\n\n")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Helper import *
from dateutil.parser import parse
import datetime
import time
import copy


###########################
######## read data ########
###########################

before=time.time()

data = pd.read_csv('airline-price-prediction.csv', header=0)
data.dropna(how='any',inplace=True)
orig=copy.deepcopy(data)
l=len(data.index)

after = time.time()
time_taken=int(after-before)
print(80*"#")
print("read data","successed  time taken : ",time_taken," sec")

#################################################################################################################################



#############################
######## handle stop ########
#############################

print(80*"#")

before=time.time()
data=stop(data)
after=time.time()
time_taken=int(after-before)

print("handle stop","successed  time taken : ",time_taken," sec")

#################################################################################################################################



###################################
######## handle time_taken ########
###################################

print(80*"#")

before=time.time()
data['duration']=copy.deepcopy(data['time_taken'])
data['duration']=data['duration'].str.replace(" ","")
data[['durationHOUR','durationMIN']]=data['duration'].str.split("h",expand=True)
data['durationMIN']=data['durationMIN'].str.replace("m","")
nan=data.isna().sum()
for i in data.index:
    print(f"\rhandle time_taken percentage : {math.ceil((i/l)*100)}%{spaces}",end="")
    h=str(data.loc[i,'durationHOUR'])
    m=str(data.loc[i,'durationMIN'])
    if h=="" or h=="00":
        data.loc[i,'durationHOUR']="0"
    if m=="" or h=="00":
        data.loc[i,'durationMIN']="0"

data['durationHOUR']=data['durationHOUR'].astype("float")
data['durationMIN']=data['durationMIN'].astype("float")
data['time_taken']=data['durationHOUR']*60+data['durationMIN']
# print(data['time_taken'].head(20))
print("")
print("handle time_taken","successed  time taken : ",time_taken," sec")


#################################################################################################################################



##############################
######## handle price ########
##############################
print(80*"#")

before=time.time()

len=240208
Y=data['price'].loc[0:len] #Label
Y=ptn(Y)
data['price']=pd.Series(Y)
data["price"]=data["price"].astype("float")

after = time.time()
time_taken=int(after-before)
print("handle price","successed  time taken : ",time_taken," sec")

#################################################################################################################################



#############################
######## handle date ########
#############################

print(80*"#")

before=time.time()

# unifying the date format across the whole column.
# ------------------------------------------------- #
pd.options.mode.chained_assignment = None
for i in data.index:
    print(f"\runifying the date format percentage : {math.ceil((i/l)*100)}%{spaces}",end="")
    data['date'][i] = parse(data['date'][i])
# converting to timestamp:
# --------------------------#
print(f"\runifying the date format percentage  percentage : {100}%{spaces}",end="")
print("")
for i in data.index:
    print(f"\rconverting to timestamp: percentage : {math.ceil((i/l)*100)}%{spaces}",end="")
    data['date'][i] = float(time.mktime(datetime.datetime.strptime(str(data['date'][i]), "%Y-%m-%d %H:%M:%S").timetuple()))
# data['date'] = pd.to_datetime(data['date']).dt.strftime("%d-%m-%Y")
# data['date'] = pd.to_datetime(data['date'], infer_datetime_format=True)
print(f"\rconverting to timestamp: percentage : {100}%{spaces}",end="")
print("")

after = time.time()
time_taken=int(after-before)
print("handle date","successed  time taken : ",time_taken," sec")

################################################################################################################################



#################################################
######## handle departure , arrival time ########
#################################################

print(80*"#")

before=time.time()
data["dep_hour"] = pd.to_datetime(data["dep_time"]).dt.hour
data["dep_min"] = pd.to_datetime(data["dep_time"]).dt.minute
data["arr_hour"] = pd.to_datetime(data["arr_time"]).dt.hour
data["arr_min"] = pd.to_datetime(data["arr_time"]).dt.minute
data['dep_time']=data['dep_hour'] * 60 + data['dep_min']
data['arr_time']=data['arr_hour'] * 60 + data['arr_min']

after = time.time()
time_taken=int(after-before)
print("handle departure , arrival time  time taken : ",time_taken," sec")

#################################################################################################################################



############################################
######## creat source , distination ########
############################################

print(80*"#")

before=time.time()
x=["source","destination",":","{","}"," ","'"]
for s in x:
    data['route']=data['route'].str.replace(str(s),"",regex=False)
data[['source','destination']]=data['route'].str.split(',',expand = True)
after = time.time()
time_taken=int(after-before)

print("creat source , distination","successed  time taken : ",time_taken," sec")

#################################################################################################################################


#################################
######## create distance ########
#################################
print(80*"#")
before=time.time()
data=creat_d(data)
after = time.time()
time_taken=int(after-before)
print("create distance","successed  time taken : ",time_taken," sec")

#################################################################################################################################

########################################################
######## feature with respect to avrage price ########
########################################################
print(80*"#")

before=time.time()

data['type']=avr_p(copy.deepcopy(data),"type","price")['type']
data["airline"]=avr_p(copy.deepcopy(data),"airline","price")['airline']
data["ch_code"]=avr_p(copy.deepcopy(data),"ch_code","price")['ch_code']
data["source"]=avr_p(copy.deepcopy(data),"source","price")['source']
data["destination"]=avr_p(copy.deepcopy(data),"destination","price")['destination']

after = time.time()
time_taken=int(after-before)
print("feature with respected to avrage price","successed  time taken : ",time_taken," sec")

#################################################################################################################################



#######################################
######## change type to float  ########
#######################################

print(80*"#")

before=time.time()

coltypeF=['type', 'airline','ch_code',"stop","date",'arr_time','dep_time','source','destination','distance']
data[coltypeF]=data[coltypeF].astype("float")

after = time.time()
time_taken=int(after-before)
print("change type to float","successed  time taken : ",time_taken," sec")

#################################################################################################################################
colmns=['date', 'airline', 'ch_code', 'num_code', 'dep_time', 'time_taken','stop', 'arr_time', 'type','source','destination','distance','price']
data=data[colmns]

###################################
######## show correlation  ########
###################################
print(80*"#")

before=time.time()
plt.subplots(figsize=(16, 12))
corr = data.corr()
sns.heatmap(corr, annot=True)
plt.show()
print(data.info())

# save data then modeling it
#__________________________________________________________________________________________

# data.to_csv("my_new_data3.csv",index=False)

print("\n\n################################")
print("############## end #############")
print("################################\n\n")