#Customer Loan Approval Using Voting Classification

##########################################################
#
#   Import Required Libraries
#
##########################################################

import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt


##########################################################
#
#   Function name :     LoadData
#   Input :             Name of csv file
#   Output :            Dataframe
#   Description :       Load data from csv
#   Date :              01/09/2026
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

    print("\nColumn Names:")
    print(df.columns)

    return df


##########################################################
#
#   Function name :     PreProcessed
#   Input :             Dataframe
#   Output :            Updated Dataframe
#   Description :       Performs Data Preprocessing
#   Date :              01/09/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def PreProcessed(df):

    # Remove spaces from column names

    df.columns = df.columns.str.strip()

    # Check missing values

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Handle missing numerical values

    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numerical_columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].median()
            )

    print("\nData after preprocessing:")
    print(df.head())

    print("\nData Preprocessing completed")

    return df


##########################################################
#
#   Function name :     SplitData
#   Input :             Dataframe
#   Output :            X_train, X_test, Y_train, Y_test
#   Description :       Split data into training and testing
#
##########################################################

def SplitData(df):

    # Separate input and output

    X = df.drop(
        "LoanApproved",
        axis=1
    )

    Y = df["LoanApproved"]

    # Split data

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Dataset:")
    print(X_train.shape)

    print("\nTesting Dataset:")
    print(X_test.shape)

    return X_train, X_test, Y_train, Y_test


##########################################################
#
#   Function name :     ScaleData
#   Input :             X_train, X_test
#   Output :            Scaled data
#   Description :       Performs Standard Scaling
#
##########################################################

def ScaleData(X_train, X_test):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(
        X_train
    )

    X_test_scaled = scaler.transform(
        X_test
    )

    print("\nFeature Scaling completed")

    return X_train_scaled, X_test_scaled, scaler


##########################################################
#
#   Function name :     TrainModels
#   Input :             Training data
#   Output :            Models
#   Description :       Train individual ML models
#
##########################################################

def TrainModels(
    X_train_scaled,
    X_train,
    Y_train
):

    ######################################################
    # Logistic Regression
    ######################################################

    logistic_model = LogisticRegression(
        max_iter=5000,
        random_state=42
    )

    logistic_model.fit(
        X_train_scaled,
        Y_train
    )

    print(
        "\nLogistic Regression training completed"
    )

    ######################################################
    # Decision Tree
    ######################################################

    decision_tree_model = DecisionTreeClassifier(
        random_state=42
    )

    decision_tree_model.fit(
        X_train,
        Y_train
    )

    print(
        "Decision Tree training completed"
    )

    ######################################################
    # KNN
    ######################################################

    knn_model = KNeighborsClassifier(
        n_neighbors=5
    )

    knn_model.fit(
        X_train_scaled,
        Y_train
    )

    print(
        "KNN training completed"
    )

    return (
        logistic_model,
        decision_tree_model,
        knn_model
    )


##########################################################
#
#   Function name :     EvaluateModel
#   Input :             Model, Test Data, Model Name
#   Output :            Accuracy
#   Description :       Evaluate ML model
#
##########################################################

def EvaluateModel(
    model,
    X_test,
    Y_test,
    model_name
):

    Y_pred = model.predict(
        X_test
    )

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print("\n")
    print("==========================================")
    print(model_name)
    print("==========================================")

    print(
        "Accuracy :",
        accuracy
    )

    print(
        "Accuracy Percentage :",
        accuracy * 100,
        "%"
    )

    print("\nConfusion Matrix:")

    print(
        confusion_matrix(
            Y_test,
            Y_pred
        )
    )

    print("\nClassification Report:")

    print(
        classification_report(
            Y_test,
            Y_pred,
            zero_division=0
        )
    )

    return accuracy


##########################################################
#
#   Function name :     CreateVotingModels
#   Input :             Individual Models
#   Output :            Voting Models
#   Description :       Create Hard and Soft Voting models
#
##########################################################

def CreateVotingModels():

    ######################################################
    # Hard Voting
    ######################################################

    hard_voting_model = VotingClassifier(

        estimators=[
            (
                "lr",
                LogisticRegression(
                    max_iter=5000,
                    random_state=42
                )
            ),

            (
                "dt",
                DecisionTreeClassifier(
                    random_state=42
                )
            ),

            (
                "knn",
                KNeighborsClassifier(
                    n_neighbors=5
                )
            )
        ],

        voting="hard"
    )

    ######################################################
    # Soft Voting
    ######################################################

    soft_voting_model = VotingClassifier(

        estimators=[
            (
                "lr",
                LogisticRegression(
                    max_iter=5000,
                    random_state=42
                )
            ),

            (
                "dt",
                DecisionTreeClassifier(
                    random_state=42
                )
            ),

            (
                "knn",
                KNeighborsClassifier(
                    n_neighbors=5
                )
            )
        ],

        voting="soft"
    )

    return (
        hard_voting_model,
        soft_voting_model
    )


##########################################################
#
#   Function name :     main
#   Input :             Command Line Arguments
#   Description :       Entry point of function
#
##########################################################

def main():

    ######################################################
    # Step 1 : Load Data
    ######################################################

    df = LoadData(
        "Customer_Loan_Approval.csv"
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
    ) = SplitData(df)

    ######################################################
    # Step 4 : Feature Scaling
    ######################################################

    (
        X_train_scaled,
        X_test_scaled,
        scaler
    ) = ScaleData(
        X_train,
        X_test
    )

    ######################################################
    # Step 5 : Train Individual Models
    ######################################################

    (
        logistic_model,
        decision_tree_model,
        knn_model
    ) = TrainModels(
        X_train_scaled,
        X_train,
        Y_train
    )

    ######################################################
    # Step 6 : Evaluate Logistic Regression
    ######################################################

    logistic_accuracy = EvaluateModel(
        logistic_model,
        X_test_scaled,
        Y_test,
        "Logistic Regression"
    )

    ######################################################
    # Step 7 : Evaluate Decision Tree
    ######################################################

    decision_tree_accuracy = EvaluateModel(
        decision_tree_model,
        X_test,
        Y_test,
        "Decision Tree"
    )

    ######################################################
    # Step 8 : Evaluate KNN
    ######################################################

    knn_accuracy = EvaluateModel(
        knn_model,
        X_test_scaled,
        Y_test,
        "K-Nearest Neighbors"
    )

    ######################################################
    # Step 9 : Create Voting Models
    ######################################################

    (
        hard_voting_model,
        soft_voting_model
    ) = CreateVotingModels()

    ######################################################
    # Step 10 : Train Hard Voting
    ######################################################

    hard_voting_model.fit(
        X_train_scaled,
        Y_train
    )

    print(
        "\nHard Voting training completed"
    )

    ######################################################
    # Step 11 : Evaluate Hard Voting
    ######################################################

    hard_voting_accuracy = EvaluateModel(
        hard_voting_model,
        X_test_scaled,
        Y_test,
        "Hard Voting Classifier"
    )

    ######################################################
    # Step 12 : Train Soft Voting
    ######################################################

    soft_voting_model.fit(
        X_train_scaled,
        Y_train
    )

    print(
        "\nSoft Voting training completed"
    )

    ######################################################
    # Step 13 : Evaluate Soft Voting
    ######################################################

    soft_voting_accuracy = EvaluateModel(
        soft_voting_model,
        X_test_scaled,
        Y_test,
        "Soft Voting Classifier"
    )

    ######################################################
    # Step 14 : Accuracy Comparison
    ######################################################

    print("\n")
    print("==========================================")
    print("       MODEL ACCURACY COMPARISON")
    print("==========================================")

    print(
        "\nLogistic Regression :",
        logistic_accuracy * 100,
        "%"
    )

    print(
        "Decision Tree       :",
        decision_tree_accuracy * 100,
        "%"
    )

    print(
        "KNN                 :",
        knn_accuracy * 100,
        "%"
    )

    print(
        "Hard Voting         :",
        hard_voting_accuracy * 100,
        "%"
    )

    print(
        "Soft Voting         :",
        soft_voting_accuracy * 100,
        "%"
    )

    ######################################################
    # Step 15 : Create Comparison DataFrame
    ######################################################

    comparison = pd.DataFrame({

        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "KNN",
            "Hard Voting",
            "Soft Voting"
        ],

        "Accuracy": [
            logistic_accuracy,
            decision_tree_accuracy,
            knn_accuracy,
            hard_voting_accuracy,
            soft_voting_accuracy
        ]
    })

    print("\nFinal Comparison:")
    print(comparison)

    ######################################################
    # Step 16 : Plot Accuracy
    ######################################################

    plt.figure(
        figsize=(10, 6)
    )

    plt.bar(
        comparison["Model"],
        comparison["Accuracy"]
    )

    plt.title(
        "Model Accuracy Comparison"
    )

    plt.xlabel(
        "Machine Learning Model"
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
    # Step 17 : Save Models
    ######################################################

    joblib.dump(
        logistic_model,
        "LogisticRegressionLoan.pkl"
    )

    joblib.dump(
        decision_tree_model,
        "DecisionTreeLoan.pkl"
    )

    joblib.dump(
        knn_model,
        "KNNLoan.pkl"
    )

    joblib.dump(
        hard_voting_model,
        "HardVotingLoan.pkl"
    )

    joblib.dump(
        soft_voting_model,
        "SoftVotingLoan.pkl"
    )

    joblib.dump(
        scaler,
        "LoanApprovalScaler.pkl"
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