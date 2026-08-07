import pandas as pd

Border = "-" * 50


####################################
# Step 1 : Load the dataset
####################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("Dataset loaded successfully")

print("\nFirst 5 records:")
print(df.head())

print("\nLast 5 records:")
print(df.tail())

print("\nTotal number of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(list(df.columns))

print("\nData types of each column:")
print(df.dtypes)