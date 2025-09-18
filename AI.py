from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load sample data
data = load_iris()
X, y = data.data, data.target

# Train AI model
model = DecisionTreeClassifier()
model.fit(X, y)

# Make a prediction
print(model.predict([[5.1, 3.5, 1.4, 0.2]]))  # Example input
