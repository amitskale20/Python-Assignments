from sklearn.linear_model import LinearRegression

# Dataset
X = [[1], [2], [3], [4], [5]]
Y = [50, 55, 60, 65, 70]

# Create and train model
model = LinearRegression()
model.fit(X, Y)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])