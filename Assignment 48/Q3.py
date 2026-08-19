from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
X = [[1], [2], [3], [4], [5]]
Y = [20000, 25000, 30000, 35000, 40000]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Print coefficient
print("Coefficient:", model.coef_[0])

# Print intercept
print("Intercept:", model.intercept_)

# Predict salary for 6 years
prediction = model.predict([[6]])

print("Predicted Salary for 6 Years Experience: ₹",
      prediction[0])

# Predict values for regression line
predicted_Y = model.predict(X)

# Plot data points
plt.scatter(X, Y, label="Actual Data")

# Plot regression line
plt.plot(X, predicted_Y, label="Regression Line")

plt.xlabel("Experience (Years)")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.legend()
plt.show()