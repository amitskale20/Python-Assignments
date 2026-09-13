####################################################################
# Assignment 62 : Employee Attrition Prediction
# Author : Amit Sahebrao Kale
# Date : 11/09/2026
####################################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay


####################################################################
# Function Name : LoadData
# Description : Load Employee Attrition dataset
####################################################################

def LoadData(filename):

    print("Loading Dataset...")
    print("========================================")

    df = pd.read_csv(filename)

    print("Dataset Loaded Successfully")
    print("========================================")

    return df


####################################################################
# Function Name : DisplayInformation
# Description : Display dataset information
####################################################################

def DisplayInformation(df):

    print("Dataset Shape : ", df.shape)

    print("\nColumn Names :")
    print(df.columns)

    print("\nFirst Five Records :")
    print(df.head())


####################################################################
# Function Name : CheckMissingValues
# Description : Check missing values
####################################################################

def CheckMissingValues(df):

    print("\nMissing Values :")
    print(df.isnull().sum())


####################################################################
# Function Name : PreProcessed
# Description : Convert categorical values into numerical values
####################################################################

def PreProcessed(df):

    print("\nPreprocessing Dataset...")
    print("========================================")

    df["OverTime"] = df["OverTime"].map({
        "Yes" : 1,
        "No" : 0
    })

    df["Attrition"] = df["Attrition"].map({
        "Yes" : 1,
        "No" : 0
    })

    print("Categorical Data Converted Successfully")

    return df


####################################################################
# Function Name : SplitData
# Description : Separate input and output
####################################################################

def SplitData(df):

    X = df.drop("Attrition", axis=1)

    Y = df["Attrition"]

    return X, Y


####################################################################
# Function Name : TrainTestSplit
# Description : Split dataset into training and testing data
####################################################################

def TrainTestSplit(X, Y):

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.20,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Data Shape : ", X_train.shape)
    print("Testing Data Shape  : ", X_test.shape)

    return X_train, X_test, Y_train, Y_test


####################################################################
# Function Name : FeatureScaling
# Description : Standardize input features
####################################################################

def FeatureScaling(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)

    return X_train, X_test, scaler


####################################################################
# Function Name : CreateModel
# Description : Create Multilayer Perceptron model
####################################################################

def CreateModel():

    model = MLPClassifier(
        hidden_layer_sizes=(16, 8),
        activation="relu",
        solver="adam",
        learning_rate_init=0.001,
        max_iter=500,
        random_state=42
    )

    return model


####################################################################
# Function Name : TrainModel
# Description : Train Neural Network
####################################################################

def TrainModel(model, X_train, Y_train):

    print("\nTraining MLP Neural Network...")
    print("========================================")

    model.fit(X_train, Y_train)

    print("Training Completed")

    return model


####################################################################
# Function Name : DisplayIterations
# Description : Display number of iterations
####################################################################

def DisplayIterations(model):

    print("\nNumber of Iterations : ", model.n_iter_)


####################################################################
# Function Name : TrainingAccuracy
# Description : Calculate training accuracy
####################################################################

def TrainingAccuracy(model, X_train, Y_train):

    Y_pred = model.predict(X_train)

    Accuracy = accuracy_score(Y_train, Y_pred)

    print("\nTraining Accuracy : {:.2f}%".format(
        Accuracy * 100
    ))


####################################################################
# Function Name : TestingAccuracy
# Description : Calculate testing accuracy
####################################################################

def TestingAccuracy(model, X_test, Y_test):

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Testing Accuracy : {:.2f}%".format(
        Accuracy * 100
    ))

    print("\nClassification Report :")
    print(classification_report(
        Y_test,
        Y_pred,
        target_names=["Stay", "Leave"]
    ))


####################################################################
# Function Name : DisplayConfusionMatrix
# Description : Display confusion matrix
####################################################################

def DisplayConfusionMatrix(model, X_test, Y_test):

    Y_pred = model.predict(X_test)

    CM = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix :")
    print(CM)

    Display = ConfusionMatrixDisplay(
        confusion_matrix=CM,
        display_labels=["Stay", "Leave"]
    )

    Display.plot()

    plt.title("Employee Attrition Confusion Matrix")

    plt.show()


####################################################################
# Function Name : PlotLossCurve
# Description : Display loss curve
####################################################################

def PlotLossCurve(model):

    plt.figure(figsize=(10, 6))

    plt.plot(
        model.loss_curve_,
        label="Training Loss"
    )

    plt.xlabel("Iterations")
    plt.ylabel("Loss")

    plt.title("MLP Training Loss Curve")

    plt.legend()

    plt.grid()

    plt.show()


####################################################################
# Function Name : PredictAttrition
# Description : Predict attrition for new employee
####################################################################

def PredictAttrition(employee_data, model, scaler):

    employee_data = scaler.transform(employee_data)

    prediction = model.predict(employee_data)

    probability = model.predict_proba(employee_data)

    for i in range(len(prediction)):

        if prediction[i] == 1:

            print(
                "Employee {} : Leave".format(i + 1)
            )

        else:

            print(
                "Employee {} : Stay".format(i + 1)
            )

        print(
            "Leave Probability : {:.2f}%".format(
                probability[i][1] * 100
            )
        )

        print("----------------------------------------")


####################################################################
# Function Name : main
####################################################################

def main():

    ################################################################
    # Step 1 : Load Dataset
    ################################################################

    print("Step 1 : Load Dataset")
    print("========================================")

    df = LoadData("Employee_Attrition.csv")


    ################################################################
    # Step 2 : Display Dataset Information
    ################################################################

    print("\nStep 2 : Dataset Information")
    print("========================================")

    DisplayInformation(df)


    ################################################################
    # Step 3 : Check Missing Values
    ################################################################

    print("\nStep 3 : Missing Values")
    print("========================================")

    CheckMissingValues(df)


    ################################################################
    # Step 4 : Preprocessing
    ################################################################

    print("\nStep 4 : Data Preprocessing")
    print("========================================")

    df = PreProcessed(df)


    ################################################################
    # Step 5 : Separate Input and Output
    ################################################################

    print("\nStep 5 : Separate Input and Output")
    print("========================================")

    X, Y = SplitData(df)

    print("Input Shape  : ", X.shape)
    print("Output Shape : ", Y.shape)


    ################################################################
    # Step 6 : Train Test Split
    ################################################################

    print("\nStep 6 : Train Test Split")
    print("========================================")

    X_train, X_test, Y_train, Y_test = TrainTestSplit(
        X,
        Y
    )


    ################################################################
    # Step 7 : Feature Scaling
    ################################################################

    print("\nStep 7 : Feature Scaling")
    print("========================================")

    X_train, X_test, scaler = FeatureScaling(
        X_train,
        X_test
    )

    print("Feature Scaling Completed")


    ################################################################
    # Step 8 : Create MLP Model
    ################################################################

    print("\nStep 8 : Create MLP Model")
    print("========================================")

    model = CreateModel()

    print(model)


    ################################################################
    # Step 9 : Train Model
    ################################################################

    print("\nStep 9 : Train Model")
    print("========================================")

    model = TrainModel(
        model,
        X_train,
        Y_train
    )


    ################################################################
    # Step 10 : Display Number of Iterations
    ################################################################

    print("\nStep 10 : Number of Iterations")
    print("========================================")

    DisplayIterations(model)


    ################################################################
    # Step 11 : Training Accuracy
    ################################################################

    print("\nStep 11 : Training Accuracy")
    print("========================================")

    TrainingAccuracy(
        model,
        X_train,
        Y_train
    )


    ################################################################
    # Step 12 : Testing Accuracy
    ################################################################

    print("\nStep 12 : Testing Accuracy")
    print("========================================")

    TestingAccuracy(
        model,
        X_test,
        Y_test
    )


    ################################################################
    # Step 13 : Confusion Matrix
    ################################################################

    print("\nStep 13 : Confusion Matrix")
    print("========================================")

    DisplayConfusionMatrix(
        model,
        X_test,
        Y_test
    )


    ################################################################
    # Step 14 : Loss Curve
    ################################################################

    print("\nStep 14 : Loss Curve")
    print("========================================")

    PlotLossCurve(model)


    ################################################################
    # Step 15 : Predict New Employees
    ################################################################

    print("\nStep 15 : Predict New Employees")
    print("========================================")

    employee_data = pd.DataFrame([
        [25, 3000, 2, 4, 5, 3, 3, 1, 1, 2],
        [40, 8000, 10, 15, 3, 4, 3, 0, 2, 3],
        [30, 4500, 5, 7, 10, 2, 2, 1, 3, 2],
        [50, 10000, 20, 25, 2, 4, 4, 0, 1, 4],
        [28, 3500, 3, 5, 15, 3, 2, 1, 2, 1]
    ], columns=[
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ])

    PredictAttrition(
        employee_data,
        model,
        scaler
    )


####################################################################
# Starter
####################################################################

if __name__ == "__main__":

    main()