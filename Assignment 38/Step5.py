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


####################################
# Step 4 : FinalResult Distribution
####################################

print(Border)
print("Step 4 : FinalResult Distribution")
print(Border)

result_count = df["FinalResult"].value_counts()

print("FinalResult distribution:")
print(result_count)

pass_percentage = (
    (df["FinalResult"] == 1).sum()
    / len(df)
) * 100

fail_percentage = (
    (df["FinalResult"] == 0).sum()
    / len(df)
) * 100

print("\nPass Percentage:",
      round(pass_percentage, 2), "%")

print("Fail Percentage:",
      round(fail_percentage, 2), "%")


print("\nIs the dataset balanced?")

if abs(pass_percentage - fail_percentage) <= 10:
    print("Yes, the dataset is approximately balanced.")
else:
    print("No, the dataset is not perfectly balanced.")

print(
    "Observation: The dataset contains 18 Pass students "
    "and 12 Fail students."
)




####################################
# Step 5 : StudyHours and Attendance
# Analysis
####################################

print(Border)
print("Step 5 : StudyHours and Attendance Analysis")
print(Border)

print("\nAverage StudyHours based on FinalResult:")

study_result = df.groupby("FinalResult")["StudyHours"].mean()

print(study_result)


print("\nAverage Attendance based on FinalResult:")

attendance_result = df.groupby("FinalResult")["Attendance"].mean()

print(attendance_result)


print("\nObservation:")

print(
    "1. Students who passed generally studied more hours "
    "than students who failed."
)

print(
    "2. The average StudyHours for Pass students is "
    f"{study_result[1]:.2f} hours."
)

print(
    "3. The average StudyHours for Fail students is "
    f"{study_result[0]:.2f} hours."
)

print(
    "4. Pass students also have higher average attendance "
    "than Fail students."
)

print(
    "5. Therefore, higher StudyHours and higher Attendance "
    "are associated with a higher chance of passing."
)

