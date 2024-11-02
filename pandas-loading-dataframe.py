# Loading a DataFrame from a file using pandas

import pandas as pd

# CSV files consume take more space while, feather file format consumes less space and parquet consumes the least amount of space.
# Load data from a CSV file
# coffee = pd.read_csv("coffee.csv")
coffee = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv") 
# Raw csv file accessed by URL
# print(coffee.head())

# Loading data from a parquet file
# results = pd.read_parquet("results.parquet")

# Loading data from a feather file
results = pd.read_feather("results.feather")
print(results.head())
print(results.size)

# Use to_excel, to_parquet etc., if we want to resave the datasets