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

print(df)
