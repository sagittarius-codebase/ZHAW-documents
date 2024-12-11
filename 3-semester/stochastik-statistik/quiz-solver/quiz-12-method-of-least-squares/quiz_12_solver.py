
####################################################################################################
# Quiz 12: Method of Least-Squares (KQM)
####################################################################################################

# Imports:
import numpy as np
import matplotlib.pyplot as plt

####################################################################################################
# Exercise 1: linear regression based on data points
####################################################################################################
print("Exercise 1: linear regression based on data points")

# replace the following values with the given data points:
x_i = np.array([[-1], [0], [2]])
y_i = np.array([[-2], [-3], [1]])

# based on the equation: g(x) = β_0 + β_1 * x
factor_on_beta_0 = 1

factor_vector = np.array([[factor_on_beta_0], [factor_on_beta_0], [factor_on_beta_0]])

print("The Matrix based on the two vectors: ")
print(x_i)
print("and")
print(y_i)
print("is:")

print(np.hstack((factor_vector, x_i)))

print("and the vector:")
print(y_i)

####################################################################################################
# Exercise 2: linear regression, residual variance and correlation coefficient, etc. based on bivariate data
####################################################################################################
print("\n\nExercise 2: linear regression, residual variance and correlation coefficient, etc. based on bivariate data")

# replace the following values with the given data points:
data = [[-3, 4],
        [-4, 4],
        [2, -1],
        [-1, -3]]





# visualize the data with matplotlib points to check for correctness:
data = np.array(data)
plt.scatter(data[:, 0], data[:, 1], s=100, c='red', marker='*')
plt.title("Data points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()



