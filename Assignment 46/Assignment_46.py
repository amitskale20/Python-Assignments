import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ==================================================
# STEP 1: GET DATA
# ==================================================

print("=" * 60)
print("STEP 1: GET DATA")
print("=" * 60)

df = pd.read_csv(
    "Advertising.csv"
)

print("\nDataset:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())


# ==================================================
# STEP 2: CLEAN / PREPARE DATA
# ==================================================

print("\n" + "=" * 60)
print("STEP 2: PREPARE DATA")
print("=" * 60)


# Check missing values

print("\nMissing Values:")
print(df.isnull().sum())


# Input features

X = df[
    [
        "TV",
        "radio",
        "newspaper"
    ]
]


# Target

y = df["sales"]


# ==================================================
# STEP 3: TRAIN DATA
# ==================================================

print("\n" + "=" * 60)
print("STEP 3: TRAIN DATA")
print("=" * 60)


# 50% Training
# 50% Testing

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.5,
    random_state=42
)

print(
    "Training Records:",
    X_train.shape[0]
)

print(
    "Testing Records:",
    X_test.shape[0]
)

# Create model
model = LinearRegression()

# Train model

model.fit(
    X_train,
    y_train
)

print("\nLinear Regression Model Trained")

# ==================================================
# STEP 4: TEST DATA
# ==================================================

print("\n" + "=" * 60)
print("STEP 4: TEST DATA")
print("=" * 60)

y_pred = model.predict(
    X_test
)


# ==================================================
# STEP 5: EXPECTED VS PREDICTED
# ==================================================

print("\n" + "=" * 60)
print("STEP 5: EXPECTED VS PREDICTED VALUES")
print("=" * 60)


result = pd.DataFrame({
    "Expected Sales": y_test.values,
    "Predicted Sales": y_pred
})


print(
    result.to_string(index=False)
)


# ==================================================
# PERFORMANCE
# ==================================================

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)


mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

r2 = r2_score(
    y_test,
    y_pred
)


print(
    "Mean Absolute Error:",
    round(mae, 2)
)

print(
    "Mean Squared Error:",
    round(mse, 2)
)

print(
    "R2 Score:",
    round(r2, 4)
)