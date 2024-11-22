import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Group1', 'Group2', 'Group3']
values1 = [4, 7, 6]
values2 = [5, 8, 7]

# Bar positions
x = np.arange(len(categories))
width = 0.4

# Plot
plt.bar(x - width/2, values1, width, label='Category 1')
plt.bar(x + width/2, values2, width, label='Category 2')
plt.xticks(x, categories)
plt.legend()
plt.title("Grouped Bar Chart")
plt.show()
