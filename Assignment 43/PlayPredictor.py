import pandas as pd
 
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
Border = "=" * 50
# ==================================================
# STEP 1: GET DATA
# ==================================================
print(Border)
print("PART 1 - GET DATA")
print(Border)

df = pd.read_csv(
    "MarvellousInfosystems_PlayPredictor.csv"
)
 
Border = "=" * 50
print("PLAY PREDICTOR")
print(Border)
 
print("\nOriginal Dataset:")
print(df)
 
 
# ==================================================
# STEP 2: CLEAN / PREPARE / MANIPULATE DATA
# ==================================================
 
# Remove unnecessary index column

print(Border)
print("STEP 2: CLEAN / PREPARE / MANIPULATE DATA")
print(Border)

df = df.drop(
    "Unnamed: 0",
    axis=1
)
 
 
# Create encoders
 
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()
play_encoder = LabelEncoder()
 
 
# Encode categorical columns
 
df["Wether"] = weather_encoder.fit_transform(
    df["Wether"]
)
 
df["Temperature"] = temperature_encoder.fit_transform(
    df["Temperature"]
)
 
df["Play"] = play_encoder.fit_transform(
    df["Play"]
)
 
 
print("\nEncoded Dataset:")
print(df)
 
 
# ==================================================
# DISPLAY ENCODING
# ==================================================
 
print("\nWeather Mapping:")
 
for i, value in enumerate(
    weather_encoder.classes_
):
    print(value, "=", i)
 
 
print("\nTemperature Mapping:")
 
for i, value in enumerate(
    temperature_encoder.classes_
):
    print(value, "=", i)
 
 
print("\nPlay Mapping:")
 
for i, value in enumerate(
    play_encoder.classes_
):
    print(value, "=", i)
 
 
# ==================================================
# SEPARATE FEATURES AND TARGET
# ==================================================
 
X = df[
    ["Wether", "Temperature"]
]
 
y = df["Play"]
 
 
# ==================================================
# STEP 3: TRAIN DATA
# ==================================================
 
# Assignment specifies K = 3

print(Border)
print("STEP 3: TRAIN DATA")
print(Border)

model = KNeighborsClassifier(
    n_neighbors=3
)
 
# Train using whole dataset
 
model.fit(
    X,
    y
)
 
print("\nModel Training Completed")
 
 
# ==================================================
# STEP 4: TEST DATA
# ==================================================

print(Border)
print("STEP 4: TEST DATA")
print(Border)

weather = input(
    "\nEnter Weather (Sunny/Overcast/Rainy): "
)
 
temperature = input(
    "Enter Temperature (Hot/Cool/Mild): "
)
 
 
# Convert user input using existing encoders
 
weather_encoded = weather_encoder.transform(
    [weather]
)[0]
 
temperature_encoded = temperature_encoder.transform(
    [temperature]
)[0]
 
 
# Create input
 
new_data = [[
    weather_encoded,
    temperature_encoded
]]
 
 
# Predict
 
prediction = model.predict(
    new_data
)
 
 
# Convert encoded prediction to original label
 
result = play_encoder.inverse_transform(
    prediction
)
 
 
print(
    "\nPredicted Result:",
    result[0]
)
 
 
# ==================================================
# STEP 5: CALCULATE ACCURACY
# ==================================================

print(Border)
print("STEP 5: CALCULATE ACCURACY")
print(Border)

def CheckAccuracy(X, y, K):
 
    # Divide dataset into equal parts
 
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.5,
        random_state=42
    )
 
    # Create KNN
 
    model = KNeighborsClassifier(
        n_neighbors=K
    )
 
    # Train
 
    model.fit(
        X_train,
        y_train
    )
 
    # Test
 
    y_pred = model.predict(
        X_test
    )
 
    # Calculate accuracy
 
    accuracy = accuracy_score(
        y_test,
        y_pred
    )
 
    return accuracy
 
 
# ==================================================
# ACCURACY FOR DIFFERENT K VALUES
# ==================================================
 
print("\n" + "=" * 50)
print("ACCURACY")
print("=" * 50)
 
for K in [1, 3, 5, 7]:
 
    accuracy = CheckAccuracy(
        X,
        y,
        K
    )
 
    print(
        "K =",
        K,
        "Accuracy =",
        round(accuracy * 100, 2),
        "%"
    )
 