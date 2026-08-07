import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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



####################################
# Step 4 : Visualization
####################################

print(Border)
print("Step 4 : Visualization")
print(Border)

plt.figure(figsize=(7, 5))

sns.scatterplot(
    data=df,
    x="StudyHours",
    y="PreviousScore",
    hue="FinalResult"
)

plt.title("StudyHours vs PreviousScore")

plt.xlabel("Study Hours")

plt.ylabel("Previous Score")

plt.grid()

plt.show()


####################################
# Step 5 : Split the dataset
# for training and testing
####################################

print(Border)
print("Step 5 : Split the dataset for training and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

print("Dataset splitting done")

print("\nX shape:", X.shape)
print("Y shape:", Y.shape)

print("\nX_train:", X_train.shape)
print("X_test:", X_test.shape)

print("Y_train:", Y_train.shape)
print("Y_test:", Y_test.shape)


####################################
# Step 6 : Build the Decision Tree
# Model
####################################

print(Border)
print("Step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

print("Decision Tree model created successfully")



####################################
# Step 7 : Train the model
####################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(
    X_train,
    Y_train
)

print("Model trained successfully")


####################################
# Step 8 : Predict results
####################################

print(Border)
print("Step 8 : Predict results")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing done")

print("\nActual values:")
print(Y_test.to_numpy())

print("\nPredicted values:")
print(Y_pred)


print("\nActual vs Predicted:")

result_df = pd.DataFrame({
    "Actual": Y_test.to_numpy(),
    "Predicted": Y_pred
})

print(result_df)

