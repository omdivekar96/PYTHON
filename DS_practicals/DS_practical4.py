# DS Practical 4 - Data Visualization I
# Airline Flights Dataset - Exploring patterns in delays and flight distances

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the dataset
data = pd.read_csv(r"C:\Users\ASUS\Downloads\archive (1)\test.csv")
print("Dataset Shape:", data.shape)
print("\nFirst 5 rows:")
print(data.head())
print("\nDataset Info:")
print(data.describe())

# ============================================================
# PART 1: Explore patterns - How delays vary and how flight
#          distance affects delays
# ============================================================

# --- Plot 1: Distribution of Departure Delay vs Arrival Delay ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Departure Delay in Minutes', y='Arrival Delay in Minutes',
                data=data, alpha=0.3, edgecolor=None)
plt.title('Departure Delay vs Arrival Delay')
plt.xlabel('Departure Delay (Minutes)')
plt.ylabel('Arrival Delay (Minutes)')
plt.tight_layout()
plt.show()

# --- Plot 2: Average Delays by Travel Class ---
plt.figure(figsize=(10, 6))
delay_by_class = data.groupby('Class')[['Departure Delay in Minutes',
                                         'Arrival Delay in Minutes']].mean()
delay_by_class.plot(kind='bar', figsize=(10, 6), color=['#3498db', '#e74c3c'])
plt.title('Average Departure & Arrival Delay by Travel Class')
plt.xlabel('Travel Class')
plt.ylabel('Average Delay (Minutes)')
plt.xticks(rotation=0)
plt.legend(['Departure Delay', 'Arrival Delay'])
plt.tight_layout()
plt.show()

# --- Plot 3: Boxplot - Delays by Satisfaction Level ---
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(x='satisfaction', y='Departure Delay in Minutes', data=data,
            ax=axes[0], palette='Set2', showfliers=False)
axes[0].set_title('Departure Delay by Satisfaction')
axes[0].set_xlabel('Satisfaction')
axes[0].set_ylabel('Departure Delay (Minutes)')

sns.boxplot(x='satisfaction', y='Arrival Delay in Minutes', data=data,
            ax=axes[1], palette='Set2', showfliers=False)
axes[1].set_title('Arrival Delay by Satisfaction')
axes[1].set_xlabel('Satisfaction')
axes[1].set_ylabel('Arrival Delay (Minutes)')

plt.tight_layout()
plt.show()

# --- Plot 4: Flight Distance vs Arrival Delay ---
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Flight Distance', y='Arrival Delay in Minutes',
                hue='Class', data=data, alpha=0.4, palette='deep')
plt.title('Flight Distance vs Arrival Delay (by Class)')
plt.xlabel('Flight Distance')
plt.ylabel('Arrival Delay (Minutes)')
plt.legend(title='Class')
plt.tight_layout()
plt.show()

# --- Plot 5: Heatmap - Correlation between numerical features ---
plt.figure(figsize=(12, 8))
numeric_cols = data[['Flight Distance', 'Departure Delay in Minutes',
                     'Arrival Delay in Minutes', 'Age',
                     'Inflight wifi service', 'Seat comfort',
                     'Inflight entertainment', 'On-board service']].corr()
sns.heatmap(numeric_cols, annot=True, cmap='coolwarm', fmt='.2f',
            linewidths=0.5, square=True)
plt.title('Correlation Heatmap of Key Features')
plt.tight_layout()
plt.show()


# ============================================================
# PART 2: Histogram - Distribution of Flight Distance
# ============================================================

plt.figure(figsize=(10, 6))
sns.histplot(data['Flight Distance'], bins=50, kde=True,
             color='steelblue', edgecolor='black')
plt.title('Distribution of Flight Distances')
plt.xlabel('Flight Distance')
plt.ylabel('Frequency')
plt.axvline(data['Flight Distance'].mean(), color='red',
            linestyle='--', label=f"Mean = {data['Flight Distance'].mean():.0f}")
plt.axvline(data['Flight Distance'].median(), color='green',
            linestyle='--', label=f"Median = {data['Flight Distance'].median():.0f}")
plt.legend()
plt.tight_layout()
plt.show()

# Print summary statistics for Flight Distance
print("\n===== Flight Distance Summary Statistics =====")
print(f"Mean    : {data['Flight Distance'].mean():.2f}")
print(f"Median  : {data['Flight Distance'].median():.2f}")
print(f"Std Dev : {data['Flight Distance'].std():.2f}")
print(f"Min     : {data['Flight Distance'].min()}")
print(f"Max     : {data['Flight Distance'].max()}")
print(f"Skewness: {data['Flight Distance'].skew():.2f}")

print("\n===== Analysis =====")
print("""
The histogram reveals that the flight distance distribution is RIGHT-SKEWED
(positively skewed), meaning most flights cover shorter distances while
fewer flights cover very long distances.

- The majority of flights are concentrated in the 0-1000 range,
  indicating that short-haul flights dominate the dataset.
- The mean is greater than the median, confirming the right skew.
- There is a long tail extending towards higher distances, representing
  long-haul flights which are less frequent but cover significantly
  greater distances.
""")