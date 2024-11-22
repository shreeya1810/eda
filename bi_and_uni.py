import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 3D Scatter
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['sepal_length'], data['sepal_width'], data['petal_length'], c='r', marker='o')
ax.set_xlabel('Sepal Length')
ax.set_ylabel('Sepal Width')
ax.set_zlabel('Petal Length')
plt.show()
