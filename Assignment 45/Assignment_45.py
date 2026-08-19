import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
from sklearn.preprocessing import MinMaxScaler
 
 
# ==================================================
# CREATE DATAFRAME
# ==================================================
 
data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}
 
df = pd.DataFrame(data)
 
 
# ==================================================
# CREATE TOTAL COLUMN
# ==================================================
 
df['Total'] = (
    df['Math'] +
    df['Science'] +
    df['English']
)
 
 
# ==================================================
# Q1. NORMALIZE MATH SCORES
# ==================================================
 
print("=" * 50)
print("Q1 - MIN-MAX NORMALIZATION")
print("=" * 50)
 
scaler = MinMaxScaler()
 
df['Math_Normalized'] = scaler.fit_transform(
    df[['Math']]
)
 
print(df)
 
 
# ==================================================
# Q2. CREATE GENDER + ONE-HOT ENCODING
# ==================================================
 
print("\n" + "=" * 50)
print("Q2 - GENDER AND ONE-HOT ENCODING")
print("=" * 50)
 
# Gender assignment
 
df['Gender'] = [
    'Male',
    'Male',
    'Female'
]
 
print("\nBefore Encoding:")
print(df)
 
 
# ==================================================
# Q3. GROUP BY GENDER
# ==================================================
 
print("\n" + "=" * 50)
print("Q3 - AVERAGE MARKS BY GENDER")
print("=" * 50)
 
gender_average = df.groupby(
    'Gender'
)[
    ['Math', 'Science', 'English']
].mean()
 
print(gender_average)
 
 
# ==================================================
# Perform One-Hot Encoding
# ==================================================
 
df = pd.get_dummies(
    df,
    columns=['Gender']
)
 
print("\nAfter One-Hot Encoding:")
print(df)
 
 
# ==================================================
# Q4. PIE CHART FOR SAGAR
# ==================================================
 
print("\n" + "=" * 50)
print("Q4 - SAGAR PIE CHART")
print("=" * 50)
 
sagar = df[
    df['Name'] == 'Sagar'
].iloc[0]
 
subjects = [
    'Math',
    'Science',
    'English'
]
 
marks = [
    sagar['Math'],
    sagar['Science'],
    sagar['English']
]
 
plt.figure(figsize=(7, 7))
 
plt.pie(
    marks,
    labels=subjects,
    autopct='%1.1f%%'
)
 
plt.title("Sagar's Subject Marks")
 
plt.show()
 
 
# ==================================================
# Q5. ADD STATUS COLUMN
# ==================================================
 
print("\n" + "=" * 50)
print("Q5 - PASS / FAIL STATUS")
print("=" * 50)
 
df['Status'] = np.where(
    df['Total'] >= 250,
    'Pass',
    'Fail'
)
 
print(df)
 
 
# ==================================================
# Q6. COUNT PASSED STUDENTS
# ==================================================
 
print("\n" + "=" * 50)
print("Q6 - PASSED STUDENTS")
print("=" * 50)
 
passed_count = (
    df['Status'] == 'Pass'
).sum()
 
print(
    "Number of students passed:",
    passed_count
)
 
 
# ==================================================
# Q7. EXPORT TO CSV
# ==================================================
 
print("\n" + "=" * 50)
print("Q7 - EXPORT CSV")
print("=" * 50)
 
df.to_csv(
    'Final_Student_Data.csv',
    index=False
)
 
print(
    "Final DataFrame exported successfully."
)
 
 
# ==================================================
# Q8. HISTOGRAM OF MATH MARKS
# ==================================================
 
print("\n" + "=" * 50)
print("Q8 - MATH HISTOGRAM")
print("=" * 50)
 
plt.figure(figsize=(8, 5))
 
plt.hist(
    df['Math'],
    bins=5
)
 
plt.xlabel("Math Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Math Marks")
 
plt.show()
 
 
# ==================================================
# Q9. RENAME MATH TO MATHEMATICS
# ==================================================
 
print("\n" + "=" * 50)
print("Q9 - RENAME COLUMN")
print("=" * 50)
 
df = df.rename(
    columns={
        'Math': 'Mathematics'
    }
)
 
print(df)
 
 
# ==================================================
# Q10. ENGLISH BOXPLOT
# ==================================================
 
print("\n" + "=" * 50)
print("Q10 - ENGLISH BOXPLOT")
print("=" * 50)
 
plt.figure(figsize=(6, 5))
 
plt.boxplot(
    df['English']
)
 
plt.ylabel("English Marks")
plt.title("English Marks Distribution")
 
plt.show()
plt.show
 