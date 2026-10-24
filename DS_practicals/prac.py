# import pandas as pd
# import numpy as np
# import seaborn as sb
# from sklearn.preprocessing import MinMaxScaler, StandardScaler

# data=pd.read_csv(r"C:\Users\ASUS\Downloads\archive.zip")
# print(data.head())
# print(data.info())
# print(data.describe())
# print(data.isnull().sum())
# print(data.dtypes["track"])

# minmax=MinMaxScaler()
# std=StandardScaler()
# data['daily_stream']=minmax.fit_transform(data[['daily_stream_share_pct']])
# data['standard']=std.fit_transform(data[['daily_stream_share_pct']])
# print(data[['daily_stream_share_pct','daily_stream','standard']])

# from sklearn.preprocessing import LabelEncoder
# lb=LabelEncoder()
# data['encoder']=lb.fit_transform(data['track'])
# print(data[['track','encoder']])

# info={
#     'brands':['mazda','honda','nissan','toyota'],
#     'id':['123','na','334','889'],
#     'review':['5','3','5','na']
#       }
# print(pd.DataFrame(info))

# l=['harry','ram','shyam','shree','shiv','hari']
# for i in l:
#     if(i.startswith('s')):
#         print(i)

n=5
i=0
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)
       