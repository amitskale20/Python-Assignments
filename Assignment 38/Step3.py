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

####################################
# Step 2 : Count Students
####################################

print(Border)
print("Step 2 : Count Students")
print(Border)

total_students = len(df)

passed_students = (df["FinalResult"] == 1).sum()

failed_students = (df["FinalResult"] == 0).sum()

print("Total number of students:", total_students)

print("Number of students Passed:", passed_students)

print("Number of students Failed:", failed_students)


####################################
# Step 3 : Calculate Statistics
####################################

print(Border)
print("Step 3 : Calculate Statistics")
print(Border)

average_study_hours = df["StudyHours"].mean()

average_attendance = df["Attendance"].mean()

maximum_previous_score = df["PreviousScore"].max()

minimum_sleep_hours = df["SleepHours"].min()

print("Average StudyHours:",
      round(average_study_hours, 2))

print("Average Attendance:",
      round(average_attendance, 2))

print("Maximum PreviousScore:",
      maximum_previous_score)

print("Minimum SleepHours:",
      minimum_sleep_hours)