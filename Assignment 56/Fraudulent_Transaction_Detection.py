#Fraudulent Transaction Detection
#########################################################
#
#   Import Required Libraries
#
##########################################################

import numpy as np
import pandas as pd
import joblib

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

import matplotlib.pyplot as plt


##########################################################
#
#   Function name :     LoadData
#   Input :             Name of csv file
#   Output :            Dataframe
#   Description :       Load data from csv
#   Date :              02/09/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def LoadData(filename):

    df = pd.read_csv(filename)

    print("Data loaded successfully")

    print("\nFirst 5 records:")
    print(df.head())

    print("\nDataset Shape:")
    print(df.shape)

    return df


##########################################################
#
#   Function name :     PreProcessed
#   Input :             Dataframe
#   Output :            Updated Dataframe
#   Description :       Performs Data Preprocessing
#   Date :              02/09/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def PreProcessed(df):

    ######################################################
    # Remove unnecessary spaces from column names
    ######################################################

    df.columns = df.columns.str.strip()

    ######################################################
    # Check missing values
    ######################################################

    print("\nMissing Values:")

    print(
        df.isnull().sum()
    )

    ######################################################
    # Handle missing numerical values
    ######################################################

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numerical_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].median()
            )

    ######################################################
    # Display data after preprocessing
    ######################################################

    print("\nData after preprocessing:")

    print(
        df.head()
    )

    print(
        "\nData Preprocessing completed"
    )

    return df


##########################################################
#
#   Function name :     SplitData
#   Input :             Dataframe
#   Output :            X_train, X_test, Y_train, Y_test
#   Description :       Separate input/output and split data
#
##########################################################

def SplitData(df):

    ######################################################
    # Separate Input and Output
    ######################################################

    X = df.drop(
        "Fraud",
        axis=1
    )

    Y = df["Fraud"]

    ######################################################
    # Train Test Split
    ######################################################

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Dataset Shape:")

    print(
        X_train.shape
    )

    print("\nTesting Dataset Shape:")

    print(
        X_test.shape
    )

    return (
        X_train,
        X_test,
        Y_train,
        Y_test
    )


##########################################################
#
#   Function name :     CreateModels
#   Input :             None
#   Output :            Dictionary of models
#   Description :       Create Ensemble Models
#
##########################################################

def CreateModels():

    ######################################################
    # Decision Tree
    ######################################################

    decision_tree = DecisionTreeClassifier(
        random_state=42
    )

    ######################################################
    # Bagging
    ######################################################

    bagging = BaggingClassifier(
        estimator=DecisionTreeClassifier(
            random_state=42
        ),
        n_estimators=10,
        random_state=42
    )

    ######################################################
    # Random Forest
    ######################################################

    random_forest = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    ######################################################
    # AdaBoost
    ######################################################

    adaboost = AdaBoostClassifier(
        n_estimators=50,
        random_state=42
    )

    ######################################################
    # Voting Classifier
    ######################################################

    voting = VotingClassifier(

        estimators=[

            (
                "decision_tree",
                DecisionTreeClassifier(
                    random_state=42
                )
            ),

            (
                "random_forest",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42
                )
            ),

            (
                "adaboost",
                AdaBoostClassifier(
                    n_estimators=50,
                    random_state=42
                )
            )

        ],

        voting="hard"
    )

    ######################################################
    # Store Models
    ######################################################

    models = {

        "Decision Tree": decision_tree,

        "Bagging": bagging,

        "Random Forest": random_forest,

        "AdaBoost": adaboost,

        "Voting": voting

    }

    return models


##########################################################
#
#   Function name :     EvaluateModel
#   Input :             Model
#   Input :             X_test
#   Input :             Y_test
#   Input :             Model Name
#   Output :            Dictionary of metrics
#   Description :       Evaluate Machine Learning model
#
##########################################################

def EvaluateModel(
    model,
    X_test,
    Y_test,
    model_name
):

    ######################################################
    # Prediction
    ######################################################

    Y_pred = model.predict(
        X_test
    )

    ######################################################
    # Calculate Metrics
    ######################################################

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    precision = precision_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    recall = recall_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    f1 = f1_score(
        Y_test,
        Y_pred,
        zero_division=0
    )

    cm = confusion_matrix(
        Y_test,
        Y_pred
    )

    ######################################################
    # Display Results
    ######################################################

    print("\n")
    print("==========================================")

    print(
        model_name
    )

    print("==========================================")

    print(
        "Accuracy  :",
        accuracy
    )

    print(
        "Precision :",
        precision
    )

    print(
        "Recall    :",
        recall
    )

    print(
        "F1 Score  :",
        f1
    )

    print("\nConfusion Matrix:")

    print(
        cm
    )

    print("\nClassification Report:")

    print(
        classification_report(
            Y_test,
            Y_pred,
            zero_division=0
        )
    )

    ######################################################
    # Return Metrics
    ######################################################

    return {

        "Model": model_name,

        "Accuracy": accuracy,

        "Precision": precision,

        "Recall": recall,

        "F1 Score": f1

    }


##########################################################
#
#   Function name :     main
#   Input :             Command Line Arguments
#   Output :            None
#   Description :       Entry point of function
#
##########################################################

def main():

    ######################################################
    # Step 1 : Load Data
    ######################################################

    df = LoadData(
        "Fraudulent_Transaction_Detection.csv"
    )

    ######################################################
    # Step 2 : Preprocessing
    ######################################################

    df = PreProcessed(
        df
    )

    ######################################################
    # Step 3 : Split Data
    ######################################################

    (
        X_train,
        X_test,
        Y_train,
        Y_test
    ) = SplitData(
        df
    )

    ######################################################
    # Step 4 : Create Models
    ######################################################

    models = CreateModels()

    ######################################################
    # Step 5 : Evaluate All Models
    ######################################################

    results = []

    for model_name, model in models.items():

        print(
            "\nTraining:",
            model_name
        )

        ##################################################
        # Train Model
        ##################################################

        model.fit(
            X_train,
            Y_train
        )

        ##################################################
        # Evaluate Model
        ##################################################

        result = EvaluateModel(
            model,
            X_test,
            Y_test,
            model_name
        )

        ##################################################
        # Store Result
        ##################################################

        results.append(
            result
        )

    ######################################################
    # Step 6 : Final Comparison
    ######################################################

    comparison = pd.DataFrame(
        results
    )

    print("\n\n")
    print("======================================================")
    print("             FINAL MODEL COMPARISON")
    print("======================================================")

    print(
        comparison
    )

    ######################################################
    # Step 7 : Display Accuracy in Percentage
    ######################################################

    print("\nAccuracy Comparison:")

    for index, row in comparison.iterrows():

        print(
            row["Model"],
            ":",
            row["Accuracy"] * 100,
            "%"
        )

    ######################################################
    # Step 8 : Plot Model Accuracy
    ######################################################

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        comparison["Model"],
        comparison["Accuracy"]
    )

    plt.title(
        "Fraud Detection Model Accuracy Comparison"
    )

    plt.xlabel(
        "Algorithm"
    )

    plt.ylabel(
        "Accuracy"
    )

    plt.ylim(
        0,
        1.1
    )

    plt.xticks(
        rotation=20
    )

    plt.tight_layout()

    plt.show()

    ######################################################
    # Step 9 : Save Models
    ######################################################

    joblib.dump(
        models["Decision Tree"],
        "DecisionTreeFraud.pkl"
    )

    joblib.dump(
        models["Bagging"],
        "BaggingFraud.pkl"
    )

    joblib.dump(
        models["Random Forest"],
        "RandomForestFraud.pkl"
    )

    joblib.dump(
        models["AdaBoost"],
        "AdaBoostFraud.pkl"
    )

    joblib.dump(
        models["Voting"],
        "VotingFraud.pkl"
    )

    print(
        "\nAll models saved successfully"
    )


##########################################################
#
#   Starter
#
##########################################################
if __name__ == "__main__":
    main()