# Given a dataset of students’ study hours and exam scores,
#  the objective is to analyze their relationship.
#  Correlation is used to measure the strength and direction 
# of the association between the two variables. 
# Regression analysis is then used to predict exam scores based 
# on study hours and to estimate the expected change in scores for
#  a change in study time. Dataset Details:Dataset: Student
#  Performance Dataset Features: Study Hours, Attendance Target:
#  Exam Score Type: Small tabular dataset (CSV) 
# https://www.kaggle.com/datasets/nabeelqureshitiii/student-performance-dataset 


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv(r"C:\Users\ASUS\Downloads\archive\student_performance.csv")
print(data.head())
# print(data.isnull().sum)
print(data.describe())
#print(data.corr())

plt.scatter(data['weekly_self_study_hours'],data['total_score'])
plt.xlabel('weekly_self_study_hours')
plt.ylabel('total_score')
plt.title("Study Hours vs Exam Score")
plt.show()
print(data.columns)

# to convert non numerical into numerical...
grade_map={"A":90,"B":80,"C":70,"D":60}
data["grade"]=data["grade"].map(grade_map)
# heatmap..................
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# linear regression......
from sklearn.linear_model import LinearRegression
x=data[['weekly_self_study_hours','attendance_percentage']]
y=data[('total_score')]

model=LinearRegression()
model.fit(x,y)

print("intercept:",model.intercept_)
print("coefficients:",model.coef_)

#Prediction........
predicted_score=model.predict([[8,80]])#......students with 8hr study and 80% attendence
print("prediction:",predicted_score[0])

#visualise the regression line......
plt.scatter(data["weekly_self_study_hours"],data["total_score"],color="red")
plt.plot(data["weekly_self_study_hours"],model.predict(data[["weekly_self_study_hours",'attendance_percentage']]), color='green')

plt.xlabel('weekly_self_study_hours')
plt.ylabel('total_score')
plt.title("Regression Line: Study Hours vs Exam Score")
plt.show()
