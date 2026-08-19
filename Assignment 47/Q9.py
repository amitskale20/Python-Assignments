from sklearn.linear_model import LinearRegression

# Dataset
X = [
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
]

Y = [50, 55, 60, 65, 70]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Display coefficients
print("Coefficient of StudyHours:", model.coef_[0])
print("Coefficient of SleepHours:", model.coef_[1])

# Display intercept
print("Intercept:", model.intercept_)