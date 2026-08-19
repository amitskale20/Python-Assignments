import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==================================================
# Q1. Create DataFrame and display basic information
# ==================================================

data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(data)

print("=" * 50)
print("Q1 - DATAFRAME")
print("=" * 50)

print(df)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# ==================================================
# Q2. Descriptive Statistics
# ==================================================

print("\n" + "=" * 50)
print("Q2 - DESCRIPTIVE STATISTICS")
print("=" * 50)

print(df.describe())


# ==================================================
# Q3. Add Total Column
# ==================================================

print("\n" + "=" * 50)
print("Q3 - TOTAL MARKS")
print("=" * 50)

df['Total'] = (
    df['Math'] +
    df['Science'] +
    df['English']
)

print(df)


# ==================================================
# Q4. Science Marks > 85
# ==================================================

print("\n" + "=" * 50)
print("Q4 - SCIENCE MARKS GREATER THAN 85")
print("=" * 50)

result = df[
    df['Science'] > 85
]

print(result)


# ==================================================
# Q5. Replace Pooja with Puja
# ==================================================

print("\n" + "=" * 50)
print("Q5 - REPLACE NAME")
print("=" * 50)

df['Name'] = df['Name'].replace(
    'Pooja',
    'Puja'
)

print(df)


# ==================================================
# Q6. Sort by Total Descending
# ==================================================

print("\n" + "=" * 50)
print("Q6 - SORT BY TOTAL")
print("=" * 50)

df = df.sort_values(
    by='Total',
    ascending=False
)

print(df)


# ==================================================
# Q7. Bar Plot
# ==================================================

print("\n" + "=" * 50)
print("Q7 - BAR PLOT")
print("=" * 50)

plt.figure(figsize=(8, 5))

plt.bar(
    df['Name'],
    df['Total']
)

plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.title("Student Total Marks")

plt.show()


# ==================================================
# Q8. Amit Line Chart
# ==================================================

print("\n" + "=" * 50)
print("Q8 - AMIT'S MARKS")
print("=" * 50)

amit = df[
    df['Name'] == 'Amit'
].iloc[0]

subjects = [
    'Math',
    'Science',
    'English'
]

marks = [
    amit['Math'],
    amit['Science'],
    amit['English']
]

plt.figure(figsize=(8, 5))

plt.plot(
    subjects,
    marks,
    marker='o'
)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Marks")

plt.show()


# ==================================================
# Q9. Missing Values
# ==================================================

print("\n" + "=" * 50)
print("Q9 - MISSING VALUES")
print("=" * 50)

data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df2 = pd.DataFrame(data2)

print("\nBefore Filling:")
print(df2)


# Fill Math missing value with Math mean

df2['Math'] = df2['Math'].fillna(
    df2['Math'].mean()
)


# Fill Science missing value with Science mean

df2['Science'] = df2['Science'].fillna(
    df2['Science'].mean()
)

print("\nAfter Filling:")
print(df2)


# ==================================================
# Q10. Drop English Column
# ==================================================

print("\n" + "=" * 50)
print("Q10 - DROP ENGLISH COLUMN")
print("=" * 50)

df = df.drop(
    'English',
    axis=1
)

print(df)
