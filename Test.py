import pandas as pd
from Helper import *

airlineMap =  {
    "Vistara":      30404.6467,
    "Air India":     23441.23999,
    "Indigo":        5322.84406,
    "GO FIRST":      5645.087267,
    "AirAsia":       4077.21932,
    "SpiceJet":       6195.428215,
    "StarAir":          4569.979167,
    "Trujet":           3258.222222
    }
typeMap = {
    'business': 52560.63138,
    'economy': 6568.125995
}
# testFile = input("Enter the file path\n")
testFile = "airline-test-samples-regression.csv"
columns = ["date", "airline", "dep_time", "time_taken", "stop", "type", "route", "price"]
data = pd.read_csv(testFile)
data = data[columns]
data["date"].fillna("12/2/2022", inplace=True)

handleDate(data)

print(data)