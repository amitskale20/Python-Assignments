##########################################################
#
#    Loan Approval Prediction Model
#
##########################################################

import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def main():

    # Define input dataset
    # Income, Credit Score, Loan Amount, Existing EMI, Employment Status

    X = np.array([
        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 10000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 15000, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ])

    # Target labels
    # 0 = Loan rejected
    # 1 = Loan approved

    y = np.array([
        0, 1, 1, 0, 1,
        1, 0, 1, 0, 1
    ])

    # Clean dataset
    X = np.nan_to_num(X)

    # Apply StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Create FNN model
    model = Sequential([
        Dense(8, activation='relu', input_shape=(5,)),
        Dense(4, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    # Compile model
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    # Train model
    model.fit(
        X_scaled,
        y,
        epochs=100,
        batch_size=2,
        verbose=0
    )

    # Evaluate model
    loss, accuracy = model.evaluate(
        X_scaled,
        y,
        verbose=0
    )

    # New applicant
    new_applicant = np.array([
        [55000, 720, 400000, 10000, 1]
    ])

    # Scale new applicant
    new_applicant_scaled = scaler.transform(new_applicant)

    # Predict
    prediction_probability = model.predict(
        new_applicant_scaled,
        verbose=0
    )[0][0]

    prediction = 1 if prediction_probability >= 0.5 else 0

    # Display results
    print("Test Input :", new_applicant.tolist())

    print(
        "Model Training Accuracy :",
        f"{accuracy * 100:.2f}%"
    )

    print(
        "Prediction Probability :",
        f"{prediction_probability:.4f}"
    )

    if prediction == 1:
        print("Prediction : Loan Approved")
    else:
        print("Prediction : Loan Rejected")


if __name__ == "__main__":
    main()