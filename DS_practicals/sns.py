import seaborn as sns
import matplotlib.pyplot    as plt
import numpy as np
import pandas as pd

data=pd.read_csv(r"C:\Users\ASUS\Downloads\test.csv")
print(data.head())

data.describe()

sns.boxplot(x='Flight Distance',y='Arrival Delay in Minutes')
plt.title("graph")
plt.show()

sns.scatterplot(x='Cleanliness',y='Inflight service')
plt.title("graph2")
plt.show()