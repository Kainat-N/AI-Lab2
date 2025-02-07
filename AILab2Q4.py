import matplotlib.pyplot as plt
from sklearn.datasets import load_iris  
import numpy as np  
# Load the Iris dataset  
iris = load_iris()  
# Accessing the features (data) using NumPy array  
X = np.array(iris.data) # (Features (sepal length, sepal width, petal length, petal width) #Accessing the target labels (species)   
Y = np.array(iris.target) # Target variable (species: 0 for setosa, 1 for versicolor, 2 for  virginica)


# ------------I have Uplaoded this Code on Colab and it was working all fine so submitting This here in py file rest of questions were done in VS Code.----------------


feature_names = iris.feature_names  # Feature names


mean_values = np.mean(X, axis=0)
median_values = np.median(X, axis=0)
std_dev_values = np.std(X, axis=0)


min_values = np.min(X, axis=0)
max_values = np.max(X, axis=0)

# Extracting above mentioned values from table
sepal_data = X[:, :2]  

# Printing each calculated value
for i, name in enumerate(feature_names):
    print(f"{name.capitalize()}:")
    print(f"  Mean: {mean_values[i]:.2f}")
    print(f"  Median: {median_values[i]:.2f}")
    print(f"  Std Dev: {std_dev_values[i]:.2f}")
    print(f"  Min: {min_values[i]:.2f}")
    print(f"  Max: {max_values[i]:.2f}\n")




# Scatter Plot Sepal Length vs Sepal Width
plt.figure(figsize=(10, 4))
plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap='viridis', edgecolors='k')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')

# Histogram
plt.subplot(1, 3, 2)
plt.hist(X[:, 0], bins=15, color='blue', alpha=0.7)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.title('Distribution of Sepal Length')

# Line Plot
plt.subplot(1, 3, 3)
plt.plot(X[:, 2], X[:, 3], 'r-o')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Petal Width')

plt.tight_layout()
plt.show()
