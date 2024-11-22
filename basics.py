import pandas as pd

# Example DataFrame
data = pd.DataFrame({
    "Age": [25, 30, 35, 40],
    "Salary": [3000, 4000, 5000, 6000],
    "Gender": ["Male", "Female", "Female", "Male"]
})

# Data Types
print("Data Types:\n", data.dtypes)

# Summary statistics
print("Summary Statistics:\n", data.describe(include='all'))
