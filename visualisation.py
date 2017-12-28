
import requests
import pymongo
from pymongo import MongoClient
import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


client = MongoClient('localhost',27017)
db=client.petya.petyatransac_data

df=pd.DataFrame(list(db.find({})))

import datetime

date=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%Y-%m-%d '))
    date.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%Y-%m-%d '))
df['date']=date

time=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%H:%M:%S'))
    time.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%H:%M:%S'))
df['real_time']=time


hour=[]
for i in df['time']:
    #print(datetime.datetime.fromtimestamp(int(i)).strftime('%H'))
    hour.append(datetime.datetime.utcfromtimestamp(int(i)).strftime('%H'))
df['hour']=hour

df['hour'] = df['hour'].apply(pd.to_numeric)


val=[]
l1=len(df['vout'])

for i in range(l1):
    l2=len(df['vout'][i])
    summ=0
    for j in range(l2):
        if df['vout'][i][j]['scriptPubKey']['addresses']==['1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX']:
            
            summ=summ+float(df['vout'][i][j]['value'])
    val.append(summ)
    print(val)            
               
                   
            

df['transaction_input']=val
df
