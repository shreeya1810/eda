import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = [10, 12, 12, 13, 14, 20, 22, 30, 50]

# Histogram
plt.hist(data, bins=8, alpha=0.7, color='blue', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# Density Plot
pd.Series(data).plot(kind='kde', color='red', title="Density Plot")
plt.show()
