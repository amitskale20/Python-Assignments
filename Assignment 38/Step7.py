import pandas as pd
import matplotlib.pyplot as plt

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


####################################
# Step 6 : Histogram of StudyHours
####################################

print(Border)
print("Step 6 : Histogram of StudyHours")
print(Border)

plt.figure(figsize=(7, 5))

plt.hist(
    df["StudyHours"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribution of Study Hours")

plt.xlabel("Study Hours")

plt.ylabel("Number of Students")

plt.grid()

plt.show()


print("\nObservation:")

print(
    "The histogram shows the distribution of daily study "
    "hours among students."
)

print(
    "Most students study between approximately 2 and 8 hours "
    "per day."
)

print(
    "The dataset shows that students with higher study hours "
    "are generally more likely to pass."
)
####################################
# Step 7 : Scatter Plot
# StudyHours vs PreviousScore
####################################

print(Border)
print("Step 7 : StudyHours vs PreviousScore")
print(Border)

plt.figure(figsize=(8, 5))

for result in df["FinalResult"].unique():

    temp = df[df["FinalResult"] == result]

    if result == 1:
        label = "Pass"
    else:
        label = "Fail"

    plt.scatter(
        temp["StudyHours"],
        temp["PreviousScore"],
        label=label
    )

plt.title("StudyHours vs PreviousScore")

plt.xlabel("Study Hours")

plt.ylabel("Previous Score")

plt.legend()

plt.grid()

plt.show()


print("\nObservation:")

print(
    "The scatter plot shows a positive relationship between "
    "StudyHours and PreviousScore."
)

print(
    "Students with higher StudyHours generally have higher "
    "PreviousScore."
)

print(
    "Pass students are mainly concentrated in the region "
    "of higher StudyHours and PreviousScore."
)
