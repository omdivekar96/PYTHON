import pandas as pd
import numpy as np

data = {
    "Product_Category": [
        "Electronics", "Electronics", "Electronics", "Electronics",
        "Clothing", "Clothing", "Clothing", "Clothing",
        "Books", "Books", "Books", "Books",
        "Furniture", "Furniture", "Furniture", "Furniture"
    ],
    "Sale_Price": [
        250, 300, 150, 500,
        75, 50, 120, 200,
        20, 15, 25, 50,
        1000, 750, 1200, 950
    ],
    "Quantity_Sold": [
        3, 2, 5, 1,
        10, 8, 6, 4,
        15, 20, 12, 5,
        1, 2, 1, 3
    ]
}

df = pd.DataFrame(data)

# print(df)

# print(df.describe())
a=df['Sale_Price'].describe()
b=df['Quantity_Sold'].describe()

stats={
    
    'stats_Sale_Price':a,
    'stats_Quantity_sold':b
}
df_stats=pd.DataFrame(stats)
print(df_stats)

# Summary statistics of Sale_Price grouped by Product_Category
grouped_sale= df.groupby("Product_Category")["Sale_Price"].agg(
    mean="mean",
    median="median",
    min="min",
    max="max",
    std="std"
)

print(grouped_sale)

grouped_sold=df.groupby('Product_Category')['Quantity_Sold'].agg(
    mean='mean',
    median='median',
    min='min',
    max='max',
    std='std'
    
)
print(grouped_sold)


group=df.groupby('Product_Category')['Quantity_Sold']
print(group.agg(
    mean='mean',
    median="median"
))