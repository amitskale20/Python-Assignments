from sklearn.linear_model import LinearRegression

print("----------------------------------------")
print("Linear Regression Assignment")
print("----------------------------------------")

# Q7 Dataset
X = [[1], [2], [3], [4], [5]]
Y = [50, 55, 60, 65, 70]

# Create model
model = LinearRegression()

# Train model
model.fit(X, Y)

# Display coefficient
print("Coefficient:", model.coef_[0])

# Display intercept
print("Intercept:", model.intercept_)

# Q8 Prediction
prediction = model.predict([[6]])

print("Predicted Marks for 6 Study Hours:",
      prediction[0])

print("----------------------------------------")

# Q9 Multiple Linear Regression

X_multi = [
    [1, 7],
    [2, 6],
    [3, 7],
    [4, 6],
    [5, 8]
]

Y_multi = [50, 55, 60, 65, 70]

# Create model
model_multi = LinearRegression()

# Train model
model_multi.fit(X_multi, Y_multi)

# Display coefficients
print("Coefficient of StudyHours:",
      model_multi.coef_[0])

print("Coefficient of SleepHours:",
      model_multi.coef_[1])

# Display intercept
print("Intercept:",
      model_multi.intercept_)

print("----------------------------------------")