from load_data import load_data
import matplotlib.pyplot as plt

# Data
labels = ['Category A', 'Category B', 'Category C']
sizes = [15, 30, 55]

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.show()
