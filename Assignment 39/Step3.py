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

print("\nShape of dataset:")
print(df.shape)

print("\nColumn names:")
print(list(df.columns))

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())


####################################
# Step 2 : Data Analysis
####################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Total number of students:",
      len(df))

print("\nFinalResult distribution:")
print(df["FinalResult"].value_counts())

print("\nStatistical information:")
print(df.describe())


####################################
# Step 3 : Decide Independent and
# Dependent Variables
####################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent variables / Features

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]

# Y : Dependent variable / Label

Y = df["FinalResult"]

print("X shape:", X.shape)

print("Y shape:", Y.shape)

print("\nFeatures used for prediction:")
print(feature_cols)

print("\nTarget variable:")
print("FinalResult")
