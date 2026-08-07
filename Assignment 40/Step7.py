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


####################################
# Step 3 : StudyHours and Attendance
# Only
####################################

print(Border)
print("Step 3 : StudyHours and Attendance Only")
print(Border)

two_features = [
    "StudyHours",
    "Attendance"
]

X_two = df[two_features]

X_train_3, X_test_3, Y_train_3, Y_test_3 = train_test_split(
    X_two,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)

model_3 = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model_3.fit(X_train_3, Y_train_3)

Y_pred_3 = model_3.predict(X_test_3)

accuracy_3 = accuracy_score(
    Y_test_3,
    Y_pred_3
)

print(
    "Full Feature Accuracy:",
    f"{original_accuracy * 100:.2f}%"
)

print(
    "StudyHours + Attendance Accuracy:",
    f"{accuracy_3 * 100:.2f}%"
)

if accuracy_3 == original_accuracy:
    print("Model is still performing well.")
else:
    print("Model performance has changed.")


####################################
# Step 4 : Predict 5 New Students
####################################

print(Border)
print("Step 4 : Predict 5 New Students")
print(Border)

new_students = pd.DataFrame({

    "StudyHours": [2, 4, 6, 7, 9],

    "Attendance": [65, 75, 85, 90, 95],

    "PreviousScore": [45, 55, 66, 72, 85],

    "AssignmentsCompleted": [2, 4, 7, 8, 10],

    "SleepHours": [5, 6, 7, 7, 8]
})

new_prediction = model.predict(
    new_students
)

new_students["FinalResult"] = new_prediction

new_students["Prediction"] = new_students[
    "FinalResult"
].map({
    0: "Fail",
    1: "Pass"
})

print("Predictions:")
print(new_students)


####################################
# Step 5 : Manual Accuracy
####################################

print(Border)
print("Step 5 : Manual Accuracy Calculation")
print(Border)

Y_pred = model.predict(X_test)

correct_predictions = 0

for actual, predicted in zip(
    Y_test,
    Y_pred
):

    if actual == predicted:
        correct_predictions += 1


total_predictions = len(Y_test)

manual_accuracy = (
    correct_predictions /
    total_predictions
)


sklearn_accuracy = accuracy_score(
    Y_test,
    Y_pred
)


print(
    "Correct Predictions:",
    correct_predictions
)

print(
    "Total Predictions:",
    total_predictions
)

print(
    "Manual Accuracy:",
    f"{manual_accuracy * 100:.2f}%"
)

print(
    "Sklearn Accuracy:",
    f"{sklearn_accuracy * 100:.2f}%"
)

if manual_accuracy == sklearn_accuracy:
    print("Both accuracies match.")


####################################
# Step 6 : Misclassified Students
####################################

print(Border)
print("Step 6 : Misclassified Students")
print(Border)

test_students = df.loc[X_test.index].copy()

test_students["Actual"] = Y_test

test_students["Predicted"] = Y_pred


misclassified = test_students[
    test_students["Actual"] !=
    test_students["Predicted"]
]


print("Misclassified Students:")

print(misclassified)


print(
    "\nNumber of Misclassified Students:",
    len(misclassified)
)


if len(misclassified) == 0:

    print(
        "No students were misclassified."
    )

else:

    print(
        "Analyze StudyHours, Attendance and "
        "PreviousScore for common patterns."
    )



####################################
# Step 7 : Random State Comparison
####################################

print(Border)
print("Step 7 : Random State Comparison")
print(Border)

random_states = [0, 10, 42]

for state in random_states:

    X_train_rs, X_test_rs, Y_train_rs, Y_test_rs = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=state,
        stratify=Y
    )

    model_rs = DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    )

    model_rs.fit(
        X_train_rs,
        Y_train_rs
    )

    Y_pred_rs = model_rs.predict(
        X_test_rs
    )

    accuracy_rs = accuracy_score(
        Y_test_rs,
        Y_pred_rs
    )

    print(
        "random_state =",
        state,
        "Testing Accuracy =",
        f"{accuracy_rs * 100:.2f}%"
    )


print(
    "\nObservation:"
)

print(
    "Changing random_state can change the train-test split "
    "and therefore testing accuracy."
)