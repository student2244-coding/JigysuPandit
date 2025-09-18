import numpy as np

# Training data (Hours studied)
X = np.array([1, 2, 3, 4, 5])
# Target data (Exam scores)
y = np.array([2, 4, 6, 8, 10])

# Calculate mean
mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculate slope (m) and intercept (b)
numerator = np.sum((X - mean_x) * (y - mean_y))
denominator = np.sum((X - mean_x)**2)

m = numerator / denominator
b = mean_y - m * mean_x

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict for 6 hours of study
x_input = 6
y_pred = m * x_input + b

print(f"Predicted score for {x_input} hours of study: {y_pred}")
