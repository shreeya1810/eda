from load_data import load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = load_data()

# Prepare features (X) and target (y)
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]  # Features
y = data['species']  # Target

# Convert target labels to numeric values
y = y.astype('category').cat.codes

# Split data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Model Accuracy
rf_accuracy = rf.score(X_test, y_test)
print("Random Forest Accuracy:", rf_accuracy)
