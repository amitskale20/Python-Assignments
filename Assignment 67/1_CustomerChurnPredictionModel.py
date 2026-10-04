##########################################################
#
#    Customer Churn Prediction Model
#
##########################################################

import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def main():

    # Define input features
    # Age, Monthly Charges, Tenure, Complaints, Support Calls

    X = np.array([
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 1500, 5, 6, 10],
        [28, 600, 18, 1, 1],
        [35, 800, 30, 0, 0],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7]
    ])

    # Target labels
    # 0 = Customer will stay
    # 1 = Customer will leave

    y = np.array([
        0, 0, 1, 1, 0,
        0, 1, 1, 0, 1
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

    # New customer
    new_customer = np.array([
        [46, 1450, 5, 6, 9]
    ])

    # Scale new customer
    new_customer_scaled = scaler.transform(new_customer)

    # Predict
    prediction_probability = model.predict(
        new_customer_scaled,
        verbose=0
    )[0][0]

    prediction = 1 if prediction_probability >= 0.5 else 0

    # Display result
    print("Test Input :", new_customer.tolist())

    print(
        "Model Training Accuracy :",
        f"{accuracy * 100:.2f}%"
    )

    print(
        "Prediction Probability :",
        f"{prediction_probability:.4f}"
    )

    if prediction == 1:
        print("Prediction : Customer may leave")
    else:
        print("Prediction : Customer will stay")


if __name__ == "__main__":
    main()