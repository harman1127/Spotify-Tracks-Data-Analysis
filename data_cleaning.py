import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully!\n")

# ================================
# BASIC CHECKS
# ================================

# Shape
print("Shape of dataset:", df.shape)

# Info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Column names
print("\nColumn Names:")
print(df.columns)

# Remove unwanted column (if exists)
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
    print("\nRemoved unnecessary column: Unnamed: 0")

# Handle very few missing values (only 1 row)
df = df.dropna()

print("\nAfter Cleaning:")
print("Missing Values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")