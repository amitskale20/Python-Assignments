# Simple Linear Regression Without ML Library

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

# Number of observations
n = len(X)

# Calculate mean
mean_x = sum(X) / n
mean_y = sum(Y) / n

# Calculate numerator and denominator
numerator = 0
denominator = 0

for i in range(n):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2

# Calculate slope
m = numerator / denominator

# Calculate intercept
c = mean_y - (m * mean_x)

# Regression equation
print("Mean of X =", mean_x)
print("Mean of Y =", mean_y)
print("Slope (m) =", m)
print("Intercept (c) =", c)

print("Regression Equation:")
print("Y =", m, "X +", c)

# Prediction for X = 6
x_value = 6
predicted_y = m * x_value + c

print("Predicted Y for X =", x_value, ":", predicted_y)