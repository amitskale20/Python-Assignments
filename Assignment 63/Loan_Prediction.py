####################################################################
# Assignment 63 : Loan Default Prediction using MLP
# Author : Amit Sahebrao Kale
# Date : 13/09/2026
####################################################################

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import ConfusionMatrixDisplay


####################################################################
# Function Name : LoadData
# Description : Load loan default dataset
####################################################################

def LoadData(filename):

    print("Loading Dataset...")
    print("========================================")

    df = pd.read_csv(filename)

    print("Dataset Loaded Successfully")

    return df


####################################################################
# Function Name : DisplayInformation
# Description : Display basic information
####################################################################

def DisplayInformation(df):

    print("\nDataset Shape : ", df.shape)

    print("\nColumn Names :")
    print(df.columns.tolist())

    print("\nFirst Five Records :")
    print(df.head())

    print("\nDataset Information :")
    print(df.info())


####################################################################
# Function Name : ExploreData
# Description : Perform exploratory analysis
####################################################################

def ExploreData(df):

    print("\nStatistical Information :")
    print(df.describe(include="all"))

    print("\nUnique Values :")

    for column in df.columns:

        print(
            column,
            " : ",
            df[column].unique()
        )


####################################################################
# Function Name : CheckMissingValues
# Description : Check missing values
####################################################################

def CheckMissingValues(df):

    print("\nMissing Values :")
    print(df.isnull().sum())


####################################################################
# Function Name : CheckClassBalance
# Description : Check target class distribution
####################################################################

def CheckClassBalance(df):

    print("\nTarget Class Distribution :")
    print(df["Default"].value_counts())

    print("\nTarget Class Percentage :")
    print(
        df["Default"].value_counts(normalize=True) * 100
    )

    df["Default"].value_counts().plot(
        kind="bar"
    )

    plt.xlabel("Default")
    plt.ylabel("Number of Applicants")
    plt.title("Loan Default Class Distribution")

    plt.show()


####################################################################
# Function Name : PreProcessed
# Description : Encode categorical variables
####################################################################

def PreProcessed(df):

    print("\nPreprocessing Dataset...")
    print("========================================")

    df["PreviousDefault"] = df["PreviousDefault"].map({
        "Yes": 1,
        "No": 0
    })

    df = pd.get_dummies(
        df,
        columns=["HomeOwnership"],
        dtype=int
    )

    print("\nAfter Encoding :")
    print(df.head())

    return df


####################################################################
# Function Name : SplitData
# Description : Separate X and y
####################################################################

def SplitData(df):

    X = df.drop(
        "Default",
        axis=1
    )

    y = df["Default"]

    print("\nInput Shape  : ", X.shape)
    print("Output Shape : ", y.shape)

    return X, y


####################################################################
# Function Name : TrainTestSplit
# Description : Split dataset
####################################################################

def TrainTestSplit(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nTraining Data : ", X_train.shape)
    print("Testing Data  : ", X_test.shape)

    return X_train, X_test, y_train, y_test


####################################################################
# Function Name : FeatureScaling
# Description : Scale features
####################################################################

def FeatureScaling(X_train, X_test):

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)

    print("\nFeature Scaling Completed")

    return X_train, X_test, scaler


####################################################################
# Function Name : CreateModel
# Description : Create MLPClassifier
####################################################################

def CreateModel(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    learning_rate_init=0.001
):

    model = MLPClassifier(
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        solver="adam",
        learning_rate_init=learning_rate_init,
        max_iter=1000,
        random_state=42
    )

    return model


####################################################################
# Function Name : TrainModel
# Description : Train MLP model
####################################################################

def TrainModel(model, X_train, y_train):

    print("\nTraining Model...")
    print("========================================")

    model.fit(
        X_train,
        y_train
    )

    print("Training Completed")

    return model


####################################################################
# Function Name : EvaluateModel
# Description : Calculate evaluation metrics
####################################################################

def EvaluateModel(
    model,
    X_train,
    X_test,
    y_train,
    y_test
):

    y_train_pred = model.predict(X_train)

    y_test_pred = model.predict(X_test)

    train_accuracy = accuracy_score(
        y_train,
        y_train_pred
    )

    test_accuracy = accuracy_score(
        y_test,
        y_test_pred
    )

    precision = precision_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_test,
        y_test_pred,
        zero_division=0
    )

    print("\nTraining Accuracy : {:.2f}%".format(
        train_accuracy * 100
    ))

    print("Testing Accuracy  : {:.2f}%".format(
        test_accuracy * 100
    ))

    print("Precision          : {:.2f}".format(
        precision
    ))

    print("Recall             : {:.2f}".format(
        recall
    ))

    print("F1-Score           : {:.2f}".format(
        f1
    ))

    print("\nNumber of Iterations : ", model.n_iter_)

    return y_test_pred


####################################################################
# Function Name : DisplayConfusionMatrix
# Description : Display confusion matrix
####################################################################

def DisplayConfusionMatrix(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(X_test)

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    print("\nConfusion Matrix :")
    print(cm)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=[
            "Low Risk",
            "High Risk"
        ]
    )

    display.plot()

    plt.title(
        "Loan Default Confusion Matrix"
    )

    plt.show()


####################################################################
# Function Name : DisplayClassificationReport
# Description : Display classification report
####################################################################

def DisplayClassificationReport(
    model,
    X_test,
    y_test
):

    y_pred = model.predict(X_test)

    print("\nClassification Report :")

    print(
        classification_report(
            y_test,
            y_pred,
            target_names=[
                "Low Risk",
                "High Risk"
            ],
            zero_division=0
        )
    )


####################################################################
# Function Name : PlotLossCurve
# Description : Plot training loss
####################################################################

def PlotLossCurve(model):

    plt.figure(
        figsize=(10, 6)
    )

    plt.plot(
        model.loss_curve_
    )

    plt.xlabel(
        "Iterations"
    )

    plt.ylabel(
        "Loss"
    )

    plt.title(
        "MLP Training Loss"
    )

    plt.grid()

    plt.show()


####################################################################
# Function Name : PredictNewApplicants
# Description : Predict new loan applicants
####################################################################

def PredictNewApplicants(
    employee_data,
    model,
    scaler,
    feature_columns
):

    employee_data = pd.DataFrame(
        employee_data,
        columns=feature_columns
    )

    employee_data = scaler.transform(
        employee_data
    )

    prediction = model.predict(
        employee_data
    )

    probability = model.predict_proba(
        employee_data
    )

    print("\nNew Applicant Predictions")
    print("========================================")

    for i in range(len(prediction)):

        if prediction[i] == 0:

            result = "Low Default Risk"

        else:

            result = "High Default Risk"

        print(
            "Applicant {} : {}".format(
                i + 1,
                result
            )
        )

        print(
            "Default Probability : {:.2f}%".format(
                probability[i][1] * 100
            )
        )

        print("----------------------------------------")


####################################################################
# Function Name : ActivationExperiment
# Description : Compare activation functions
####################################################################

def ActivationExperiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    activations = [
        "identity",
        "logistic",
        "tanh",
        "relu"
    ]

    print("\nActivation Function Experiment")
    print("========================================")

    for activation in activations:

        model = CreateModel(
            hidden_layer_sizes=(32, 16),
            activation=activation,
            learning_rate_init=0.001
        )

        model.fit(
            X_train,
            y_train
        )

        accuracy = accuracy_score(
            y_test,
            model.predict(X_test)
        )

        print(
            "{} : {:.2f}%".format(
                activation,
                accuracy * 100
            )
        )


####################################################################
# Function Name : HiddenLayerExperiment
# Description : Compare hidden layer architectures
####################################################################

def HiddenLayerExperiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    architectures = [
        (10,),
        (20, 10),
        (50, 25),
        (100, 50, 25)
    ]

    print("\nHidden Layer Experiment")
    print("========================================")

    for architecture in architectures:

        model = CreateModel(
            hidden_layer_sizes=architecture,
            activation="relu",
            learning_rate_init=0.001
        )

        model.fit(
            X_train,
            y_train
        )

        accuracy = accuracy_score(
            y_test,
            model.predict(X_test)
        )

        print(
            "{} : {:.2f}%".format(
                architecture,
                accuracy * 100
            )
        )


####################################################################
# Function Name : LearningRateExperiment
# Description : Compare learning rates
####################################################################

def LearningRateExperiment(
    X_train,
    X_test,
    y_train,
    y_test
):

    learning_rates = [
        0.0001,
        0.001,
        0.01
    ]

    print("\nLearning Rate Experiment")
    print("========================================")

    for learning_rate in learning_rates:

        model = CreateModel(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            learning_rate_init=learning_rate
        )

        model.fit(
            X_train,
            y_train
        )

        accuracy = accuracy_score(
            y_test,
            model.predict(X_test)
        )

        print(
            "{} : {:.2f}%".format(
                learning_rate,
                accuracy * 100
            )
        )


####################################################################
# Function Name : main
####################################################################

def main():

    ################################################################
    # Step 1 : Load Dataset
    ################################################################

    print("\nStep 1 : Load Dataset")
    print("========================================")

    df = LoadData(
        "Loan_Default.csv"
    )


    ################################################################
    # Step 2 : Understand Dataset
    ################################################################

    print("\nStep 2 : Understand Dataset")
    print("========================================")

    DisplayInformation(df)


    ################################################################
    # Step 3 : Exploratory Analysis
    ################################################################

    print("\nStep 3 : Exploratory Data Analysis")
    print("========================================")

    ExploreData(df)


    ################################################################
    # Step 4 : Missing Values
    ################################################################

    print("\nStep 4 : Missing Values")
    print("========================================")

    CheckMissingValues(df)


    ################################################################
    # Step 5 : Target Class Balance
    ################################################################

    print("\nStep 5 : Target Class Balance")
    print("========================================")

    CheckClassBalance(df)


    ################################################################
    # Step 6 : Encoding
    ################################################################

    print("\nStep 6 : Encode Categorical Variables")
    print("========================================")

    df = PreProcessed(df)


    ################################################################
    # Step 7 : Separate X and y
    ################################################################

    print("\nStep 7 : Separate X and y")
    print("========================================")

    X, y = SplitData(df)


    ################################################################
    # Step 8 : Train Test Split
    ################################################################

    print("\nStep 8 : Train Test Split")
    print("========================================")

    X_train, X_test, y_train, y_test = TrainTestSplit(
        X,
        y
    )


    ################################################################
    # Step 9 : Feature Scaling
    ################################################################

    print("\nStep 9 : Feature Scaling")
    print("========================================")

    X_train, X_test, scaler = FeatureScaling(
        X_train,
        X_test
    )


    ################################################################
    # Step 10 : Create MLP Model
    ################################################################

    print("\nStep 10 : Create MLPClassifier")
    print("========================================")

    model = CreateModel()

    print(model)


    ################################################################
    # Step 11 : Train Model
    ################################################################

    print("\nStep 11 : Train Model")
    print("========================================")

    model = TrainModel(
        model,
        X_train,
        y_train
    )


    ################################################################
    # Step 12-15 : Evaluation
    ################################################################

    print("\nStep 12-15 : Model Evaluation")
    print("========================================")

    EvaluateModel(
        model,
        X_train,
        X_test,
        y_train,
        y_test
    )


    ################################################################
    # Step 13 : Confusion Matrix
    ################################################################

    print("\nStep 13 : Confusion Matrix")
    print("========================================")

    DisplayConfusionMatrix(
        model,
        X_test,
        y_test
    )


    ################################################################
    # Step 14 : Classification Report
    ################################################################

    print("\nStep 14 : Classification Report")
    print("========================================")

    DisplayClassificationReport(
        model,
        X_test,
        y_test
    )


    ################################################################
    # Step 16 : Training Loss
    ################################################################

    print("\nStep 16 : Training Loss")
    print("========================================")

    PlotLossCurve(model)


    ################################################################
    # Step 17 : New Applicants
    ################################################################

    print("\nStep 17 : Test New Loan Applicants")
    print("========================================")

    feature_columns = X.columns.tolist()

    print(
        "Model Features : ",
        feature_columns
    )


    ################################################################
    # Hyperparameter Experiment
    ################################################################

    ActivationExperiment(
        X_train,
        X_test,
        y_train,
        y_test
    )

    HiddenLayerExperiment(
        X_train,
        X_test,
        y_train,
        y_test
    )

    LearningRateExperiment(
        X_train,
        X_test,
        y_train,
        y_test
    )


####################################################################
# Starter
####################################################################

if __name__ == "__main__":

    main()