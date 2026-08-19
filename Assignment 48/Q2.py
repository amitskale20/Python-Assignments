# Model Performance

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Regression equation
m = 0.4
c = 2.4

# Predict Y values
predicted_Y = []

for x in X:
    prediction = m * x + c
    predicted_Y.append(prediction)

print("Actual Y      Predicted Y")

for i in range(len(Y)):
    print(Y[i], "           ", predicted_Y[i])

# Calculate MSE
squared_error_sum = 0

for i in range(len(Y)):
    error = Y[i] - predicted_Y[i]
    squared_error_sum += error ** 2

mse = squared_error_sum / len(Y)

print("\nMSE =", mse)

# Calculate R2
mean_y = sum(Y) / len(Y)

sst = 0

for value in Y:
    sst += (value - mean_y) ** 2

r2 = 1 - (squared_error_sum / sst)

print("R2 Score =", r2)