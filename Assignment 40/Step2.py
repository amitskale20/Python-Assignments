import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score


Border = "-" * 50


####################################
# Step 1 : Feature Importance
####################################

print(Border)
print("Step 1 : Feature Importance")
print(Border)

# Load dataset

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

# Independent variables

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]

# Dependent variable

Y = df["FinalResult"]


# Split dataset

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)


# Create and train model

model = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model.fit(X_train, Y_train)


# Feature importance

importance = model.feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_cols,
    "Importance": importance
})

importance_df = importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("Feature Importance:")
print(importance_df)

print(
    "\nMost important feature:",
    importance_df.iloc[0]["Feature"]
)

print(
    "Least important feature:",
    importance_df.iloc[-1]["Feature"]
)


####################################
# Step 2 : Remove SleepHours
####################################

print(Border)
print("Step 2 : Remove SleepHours")
print(Border)

feature_without_sleep = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X_without_sleep = df[feature_without_sleep]

X_train_2, X_test_2, Y_train_2, Y_test_2 = train_test_split(
    X_without_sleep,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

model_2 = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model_2.fit(X_train_2, Y_train_2)

Y_pred_2 = model_2.predict(X_test_2)

accuracy_2 = accuracy_score(
    Y_test_2,
    Y_pred_2
)

original_accuracy = accuracy_score(
    Y_test,
    model.predict(X_test)
)

print(
    "Original Accuracy:",
    f"{original_accuracy * 100:.2f}%"
)

print(
    "Accuracy without SleepHours:",
    f"{accuracy_2 * 100:.2f}%"
)

if accuracy_2 == original_accuracy:
    print("Removing SleepHours does not affect performance.")
elif accuracy_2 < original_accuracy:
    print("Removing SleepHours decreases performance.")
else:
    print("Removing SleepHours improves performance.")

