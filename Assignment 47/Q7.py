from sklearn.linear_model import LinearRegression

# Dataset
X = [[1], [2], [3], [4], [5]]
Y = [50, 55, 60, 65, 70]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Display coefficient
print("Coefficient:", model.coef_[0])

# Display intercept
print("Intercept:", model.intercept_)

