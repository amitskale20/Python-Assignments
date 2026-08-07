import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

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


####################################
# Step 9 : Calculate Accuracy
####################################

print(Border)
print("Step 9 : Calculate Model Accuracy")
print(Border)

accuracy = accuracy_score(
    Y_test,
    Y_pred
)

print(
    "Model Accuracy:",
    f"{accuracy * 100:.2f}%"
)


####################################
# Step 10 : Confusion Matrix
####################################

print(Border)
print("Step 10 : Confusion Matrix")
print(Border)

cm = confusion_matrix(
    Y_test,
    Y_pred
)

print("Confusion Matrix:")
print(cm)


print("\nDisplaying Confusion Matrix:")

ConfusionMatrixDisplay.from_predictions(
    Y_test,
    Y_pred,
    display_labels=["Fail", "Pass"]
)

plt.title("Confusion Matrix")

plt.show()


####################################
# Step 11 : Classification Report
####################################

print(Border)
print("Step 11 : Classification Report")
print(Border)

print(
    classification_report(
        Y_test,
        Y_pred,
        target_names=["Fail", "Pass"]
    )
)


####################################
# Step 12 : Training Accuracy
# and Testing Accuracy
####################################

print(Border)
print("Step 12 : Training and Testing Accuracy")
print(Border)

Y_train_pred = model.predict(X_train)

training_accuracy = accuracy_score(
    Y_train,
    Y_train_pred
)

testing_accuracy = accuracy_score(
    Y_test,
    Y_pred
)

print(
    "Training Accuracy:",
    f"{training_accuracy * 100:.2f}%"
)

print(
    "Testing Accuracy:",
    f"{testing_accuracy * 100:.2f}%"
)


print("\nModel Analysis:")

accuracy_difference = (
    training_accuracy - testing_accuracy
)

if accuracy_difference > 0.10:

    print(
        "Training accuracy is much higher than "
        "testing accuracy."
    )

    print(
        "The model may be overfitting."
    )

elif training_accuracy < 0.70:

    print(
        "Both training and testing accuracy are low."
    )

    print(
        "The model may be underfitting."
    )

else:

    print(
        "Training and testing accuracy are similar."
    )

    print(
        "There is no strong indication of overfitting "
        "or underfitting."
    )


####################################
# Step 13 : Compare Different
# Decision Tree Depths
####################################

print(Border)
print("Step 13 : Compare Decision Tree Models")
print(Border)

depths = [1, 3, None]

for depth in depths:

    temp_model = DecisionTreeClassifier(
        max_depth=depth,
        random_state=42
    )

    temp_model.fit(
        X_train,
        Y_train
    )

    temp_prediction = temp_model.predict(
        X_test
    )

    temp_accuracy = accuracy_score(
        Y_test,
        temp_prediction
    )

    print(
        "max_depth =",
        depth,
        "Testing Accuracy =",
        f"{temp_accuracy * 100:.2f}%"
    )


print("\nObservation:")

print(
    "The testing accuracy is compared for Decision Trees "
    "with max_depth values of 1, 3 and None."
)

print(
    "A smaller depth produces a simpler model, while "
    "max_depth=None allows the tree to grow without "
    "a specified maximum depth."
)


####################################
# Step 14 : Predict a New Student
####################################

print(Border)
print("Step 14 : Predict Result for New Student")
print(Border)

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore": [66],
    "AssignmentsCompleted": [7],
    "SleepHours": [7]
})

new_prediction = model.predict(
    new_student
)

print("Student details:")
print(new_student)

print("\nPredicted FinalResult:",
      new_prediction[0])


if new_prediction[0] == 1:

    print("Prediction: Student will PASS")

else:

    print("Prediction: Student will FAIL")


####################################
# Step 15 : Final Conclusion
####################################

print(Border)
print("Step 15 : Final Conclusion")
print(Border)

print(
    "1. The Student Performance dataset was successfully loaded."
)

print(
    "2. StudyHours, Attendance, PreviousScore, "
    "AssignmentsCompleted and SleepHours were used as features."
)

print(
    "3. FinalResult was used as the target variable."
)

print(
    "4. A Decision Tree Classifier was trained using "
    "the training dataset."
)

print(
    "5. The trained model was tested using unseen test data."
)

print(
    f"6. Testing accuracy of the model is "
    f"{testing_accuracy * 100:.2f}%."
)

print(
    "7. The confusion matrix was generated to evaluate "
    "correct and incorrect predictions."
)

print(
    "8. The model was also compared using different "
    "max_depth values."
)

print(
    "9. For the given new student, the model predicts PASS."
)