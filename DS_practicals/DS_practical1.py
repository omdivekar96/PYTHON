#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as st
import numpy as np

# data=pd.read_csv(r"C:\Users\ASUS\Downloads\archive\student_performance.csv")
# print(data.head())
# print(data.describe())

#creating data frames using dictionary..........
info={
    'student':['om','shri','vedant','shrey'],
    'gender':['m','f','m','m'],
    'age':[20,17,21,20]
      }
data=pd.DataFrame(info)#...........it arranges the data into table format
print(data)
print(data.info())
print(data.isnull().sum)
print(data.describe())
print(data.dtypes['age'])
print(data.dtypes['student'])

#Normalization using minmax...........
from sklearn.preprocessing import MinMaxScaler, StandardScaler 
minmax=MinMaxScaler()
standard=StandardScaler()
data['age_minmax']=minmax.fit_transform(data[['age']])#...double brackets cuz it is dataframe
data['age_standard']=standard.fit_transform(data[['age']])#...single bracket means 1d series
print(data[['age','age_minmax','age_standard']])

#catagorical to numerical tranform......
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
data['encoded']=LE.fit_transform(data['gender'])
print(data[['gender','encoded']])





