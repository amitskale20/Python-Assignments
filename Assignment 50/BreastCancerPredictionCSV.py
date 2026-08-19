##########################################################
#
#   Import Required Libraries
#
##########################################################

import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt
import seaborn as sns


##########################################################
#
#   Function name :     LoadData
#   Input :             Name of csv file
#   Output :            Dataframe
#   Description :       Load data from csv
#   Date :              19/08/2026
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
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def PreProcessed(df):

    ######################################################
    # Remove unnecessary column
    ######################################################

    df = df.drop(
        [
            "CodeNumber"
        ],
        axis=1,
        errors="ignore"
    )

    ######################################################
    # Handle missing values
    ######################################################

    # BareNuclei contains '?' values

    df["BareNuclei"] = pd.to_numeric(
        df["BareNuclei"],
        errors="coerce"
    )

    # Replace missing values with median

    df["BareNuclei"] = df["BareNuclei"].fillna(
        df["BareNuclei"].median()
    )

    ######################################################
    # Convert CancerType
    #
    # 2 = Benign
    # 4 = Malignant
    ######################################################

    df["CancerType"] = df["CancerType"].replace({
        2: 0,
        4: 1
    })

    print("\nMissing values after preprocessing:")
    print(df.isnull().sum())

    print("\nData after preprocessing:")
    print(df.head())

    print("\nData Preprocessing completed")

    return df


##########################################################
#
#   Function name :     ExploreData
#   Input :             Dataframe
#   Output :            None
#   Description :       Performs Exploratory Data Analysis
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def ExploreData(df):

    ######################################################
    # Summary Statistics
    ######################################################

    print("\nSummary Statistics:")
    print(df.describe())

    ######################################################
    # Target Distribution
    ######################################################

    print("\nCancer Type Distribution:")
    print(df["CancerType"].value_counts())

    ######################################################
    # Target Visualization
    ######################################################

    plt.figure(figsize=(6, 4))

    sns.countplot(
        x="CancerType",
        data=df
    )

    plt.title("Benign vs Malignant Tumors")
    plt.xlabel("Cancer Type")
    plt.ylabel("Count")

    plt.xticks(
        [0, 1],
        ["Benign", "Malignant"]
    )

    plt.show()

    ######################################################
    # Correlation Heatmap
    ######################################################

    plt.figure(figsize=(14, 10))

    correlation = df.corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Feature Correlation Heatmap")

    plt.show()

    print("\nData Analysis completed")


##########################################################
#
#   Function name :     SplitData
#   Input :             Dataframe
#   Output :            X_train, X_test, Y_train, Y_test
#   Description :       Split dataset into training and
#                       testing datasets
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def SplitData(df):

    ######################################################
    # Separate input and output
    ######################################################

    X = df.drop(
        "CancerType",
        axis=1
    )

    Y = df["CancerType"]

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

    print("\nTraining Dataset:")
    print(X_train.shape)

    print("\nTesting Dataset:")
    print(X_test.shape)

    return X_train, X_test, Y_train, Y_test


##########################################################
#
#   Function name :     ScaleData
#   Input :             X_train, X_test
#   Output :            Scaled X_train, X_test
#   Description :       Performs Feature Scaling
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
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
#   Function name :     TrainModel
#   Input :             X_train, Y_train
#   Output :            Trained Model
#   Description :       Train Logistic Regression model
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def TrainModel(X_train, Y_train):

    model = LogisticRegression(
        max_iter=5000,
        random_state=42
    )

    model.fit(
        X_train,
        Y_train
    )

    print("\nModel training completed")

    return model


##########################################################
#
#   Function name :     EvaluateModel
#   Input :             Model, X_test, Y_test
#   Output :            None
#   Description :       Evaluate classification model
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def EvaluateModel(model, X_test, Y_test):

    ######################################################
    # Predict values
    ######################################################

    Y_pred = model.predict(
        X_test
    )

    ######################################################
    # Accuracy
    ######################################################

    accuracy = accuracy_score(
        Y_test,
        Y_pred
    )

    print("\n------------------------------------------")
    print("Model Evaluation")
    print("------------------------------------------")

    print("\nAccuracy :", accuracy)

    print(
        "Accuracy Percentage :",
        accuracy * 100
    )

    ######################################################
    # Confusion Matrix
    ######################################################

    cm = confusion_matrix(
        Y_test,
        Y_pred
    )

    print("\nConfusion Matrix:")
    print(cm)

    ######################################################
    # Classification Report
    ######################################################

    print("\nClassification Report:")

    print(
        classification_report(
            Y_test,
            Y_pred,
            target_names=[
                "Benign",
                "Malignant"
            ]
        )
    )

    ######################################################
    # Confusion Matrix Visualization
    ######################################################

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=[
            "Benign",
            "Malignant"
        ],
        yticklabels=[
            "Benign",
            "Malignant"
        ]
    )

    plt.title("Confusion Matrix")

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    plt.show()


##########################################################
#
#   Function name :     main
#   Input :             Command Line Arguments
#   Output :            None
#   Description :       Entry point of function
#   Date :              19/08/2026
#   Author :            Amit Sahebrao Kale
#
##########################################################

def main():

    ######################################################
    # Step 1 : Load Data
    ######################################################

    df = LoadData(
        "breast-cancer-wisconsin.csv"
    )

    ######################################################
    # Step 2 : Data Preprocessing
    ######################################################

    df = PreProcessed(
        df
    )

    ######################################################
    # Step 3 : Exploratory Data Analysis
    ######################################################

    ExploreData(
        df
    )

    ######################################################
    # Step 4 : Split Dataset
    ######################################################

    X_train, X_test, Y_train, Y_test = SplitData(
        df
    )

    ######################################################
    # Step 5 : Feature Scaling
    ######################################################

    X_train_scaled, X_test_scaled, scaler = ScaleData(
        X_train,
        X_test
    )

    ######################################################
    # Step 6 : Train Model
    ######################################################

    model = TrainModel(
        X_train_scaled,
        Y_train
    )

    ######################################################
    # Step 7 : Evaluate Model
    ######################################################

    EvaluateModel(
        model,
        X_test_scaled,
        Y_test
    )

    ######################################################
    # Step 8 : Save Model
    ######################################################

    joblib.dump(
        model,
        "BreastCancerModel.pkl"
    )

    joblib.dump(
        scaler,
        "BreastCancerScaler.pkl"
    )

    print("\nModel saved successfully")


##########################################################
#
#   Starter
#
##########################################################

if __name__ == "__main__":
    main()