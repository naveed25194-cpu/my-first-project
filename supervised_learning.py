# Supervised Learning Example (Linear Regression)

from sklearn.linear_model import LinearRegression
import numpy as np

# Input (hours studied)
X = np.array([[1], [2], [3], [4], [5]])

# Output (marks)
y = np.array([40, 50, 60, 70, 80])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict
predicted = model.predict([[6]])

print("Predicted marks for 6 hours:", predicted[0])