import numpy as np 
import pandas as pd 
import csv
import requests
import matplotlib.pyplot as plt
import datetime
import matplotlib.dates as mdates
import mplcursors
path = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv'
df = pd.read_csv(path)

path2 = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_deaths_usafacts.csv'
df2 = pd.read_csv(path2)

confirmed = pd.DataFrame(df)
deaths = pd.DataFrame(df2)

confirmed_ca = confirmed[192:251]

deaths_ca = deaths[192:251]

deaths_ca = deaths_ca.drop(['1/22/20','1/23/20','1/24/20','1/25/20' ,'1/26/20' ,'1/27/20', 
'1/28/20' ,'1/29/20', '1/30/20','1/31/20','2/1/20' ,'2/2/20', '2/3/20', '2/4/20', '2/5/20', 
'2/6/20', '2/7/20','2/8/20', '2/9/20', '2/10/20', '2/11/20' ,'2/12/20' ,'2/13/20', '2/14/20',
 '2/15/20', '2/16/20', '2/17/20', '2/18/20' ,'2/19/20' ,'2/20/20' ,'2/21/20',
 '2/22/20', '2/23/20', '2/24/20', '2/25/20' ,'2/26/20', '2/27/20', '2/28/20',
 '2/29/20', '3/1/20', '3/2/20', '3/3/20' ,'3/4/20' ,'3/5/20' ,'3/6/20', '3/7/20',
 '3/8/20' ,'3/9/20', '3/10/20', '3/11/20' ,'3/12/20' ,'3/13/20', '3/14/20'],axis=1)

confirmed_ca = confirmed_ca.drop(['1/22/20','1/23/20','1/24/20','1/25/20' ,'1/26/20' ,'1/27/20', 
'1/28/20' ,'1/29/20', '1/30/20','1/31/20','2/1/20' ,'2/2/20', '2/3/20', '2/4/20', '2/5/20', 
'2/6/20', '2/7/20','2/8/20', '2/9/20', '2/10/20', '2/11/20' ,'2/12/20' ,'2/13/20', '2/14/20',
 '2/15/20', '2/16/20', '2/17/20', '2/18/20' ,'2/19/20' ,'2/20/20' ,'2/21/20',
 '2/22/20', '2/23/20', '2/24/20', '2/25/20' ,'2/26/20', '2/27/20', '2/28/20',
 '2/29/20', '3/1/20', '3/2/20', '3/3/20' ,'3/4/20' ,'3/5/20' ,'3/6/20', '3/7/20',
 '3/8/20' ,'3/9/20', '3/10/20', '3/11/20' ,'3/12/20' ,'3/13/20', '3/14/20'],axis=1)

dates = confirmed_ca.columns.values.tolist()
del dates[:4]
dates2 = deaths_ca.columns.values.tolist()
del dates2[:4]

# this is the function that calls both datasets for total deaths and cases and compiles them into 
# if the graphs do not work there are only two errors that could be happening
# 1. the link is broken and needs to be updated --> look into how to solve this issue
# 2. the end index of the for loop in the function is not correct and needs to be tweaked
def call_data(fips):
    y1_values = []
    y2_values = []
    x_values = [datetime.datetime.strptime(d,"%m/%d/%y").date() for d in dates]
    x2_values = [datetime.datetime.strptime(d,"%m/%d/%y").date() for d in dates2]
    rslt_df = confirmed_ca[confirmed_ca['countyFIPS'] == fips]
    rslt2_df = deaths_ca[deaths_ca['countyFIPS'] == fips]
    rslt_list = rslt_df.values.tolist()
    rslt2_list = rslt2_df.values.tolist()
    print(y1_values)
    for i in range (4,(len(dates)+4)):
        y1_values.append(rslt_list[0][i])
        y2_values.append(rslt2_list[0][i])
    plt.plot(x_values,y1_values, label="Confirmed Cases")
    plt.plot(x2_values,y2_values, label="Deaths")
    plt.xlabel("Dates")
    plt.ylabel("Count")
    plt.title("Covid 19 Cases and Deaths for {}".format(rslt_list[0][1]))
    plt.legend()
    plt.show()
