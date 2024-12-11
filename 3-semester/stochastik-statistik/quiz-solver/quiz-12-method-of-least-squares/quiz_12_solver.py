
####################################################################################################
# Quiz 12: Method of Least-Squares (KQM)
####################################################################################################

# Imports:
import numpy as np
import matplotlib.pyplot as plt
import math

####################################################################################################
# Exercise 1: linear regression based on data points
####################################################################################################
print("Exercise 1: linear regression based on data points")

# replace the following values with the given data points:

x_i = np.array([[-1], [2], [3]])
y_i = np.array([[-3], [7], [4]])

# based on the equation: g(x) = β_0 + β_1 * x
factor_on_beta_0 = 1

factor_vector = np.array([[factor_on_beta_0], [factor_on_beta_0], [factor_on_beta_0]])

print("The Matrix based on the two vectors: ")
print(x_i)
print("and")
print(y_i)
print("is:\n")

print(np.hstack((factor_vector, x_i)))

print("and the vector:")
print(y_i)

####################################################################################################
# Exercise 2: linear regression, residual variance and correlation coefficient, etc. based on bivariate data
####################################################################################################
print("\n\nExercise 2: linear regression, residual variance and correlation coefficient, etc. based on bivariate data")

# replace the following values with the given data points:
data = [[2, 4],
        [-2, -1],
        [3, -4],
        [-1, -2],
        [1, 2],
        [2, -3]]

# min and max values for graph:
x_min = -2
x_max = 3
y_min = -4
y_max = 4


x_avg = np.mean([x[0] for x in data])
y_avg = np.mean([x[1] for x in data])

variance_x = np.var([x[0] for x in data])
variance_y = np.var([x[1] for x in data])
covariance = np.cov([x[0] for x in data], [x[1] for x in data], bias=True)[0][1]

print("x_avg:", x_avg)
print("y_avg:", y_avg)
print("variance_x:", variance_x)
print("variance_y:", variance_y)
print("covariance:", covariance)


# (1) regression line (to y): -> y(x) = m * x + d
m_y = covariance / variance_x
d_y = y_avg - m_y * x_avg
print(f"\n(1) The regression line is: y(x) = {m_y:.2f} * x + {d_y:.2f}")
print(f"So: m = {m_y:.2f} and d = {d_y:.2f}")

# (2) residual variance:
residual_variance = variance_y - (covariance ** 2) / variance_x
print(f"\n(2) The residual variance is: {residual_variance:.2f}")

# (3) explained variance:
explained_variance = covariance ** 2 / variance_x
print(f"\n(3) The explained variance is: {explained_variance:.4f}")

# (4) total variance:
total_variance = residual_variance + explained_variance
print(f"\n(4) The total variance is: {total_variance:.2f}")

# (5) Determinacy measure:
determinacy_measure = explained_variance / total_variance
print(f"\n(5) The determinacy measure is: {determinacy_measure:.4f}")

# (6) Pearson correlation coefficient:
correlation_coefficient = math.sqrt(determinacy_measure)
correlation_coefficient = -correlation_coefficient if m_y < 0 else correlation_coefficient
print(f"\n(6) The Pearson correlation coefficient is: {correlation_coefficient:.2f}")

# (7) regression line (to x): -> x(y) = m' * y + d'
m_x = covariance / variance_y
d_x = x_avg - m_x * y_avg
print(f"\n(7) The regression line is: x(y) = {m_x:.2f} * y + {d_x:.2f}")
print(f"So: m' = {m_x:.2f} and d' = {d_x:.2f}")

# visualize the data and function with matplotlib points to check for correctness:
data = np.array(data)
x = np.linspace(-10, 10, 100)
func_y = lambda x: m_y * x + d_y
func_x = lambda y: m_x * y + d_x
plt.scatter(data[:, 0], data[:, 1], s=300, c='red', marker='*')
plt.plot(x, func_y(x), label=f"y(x) = {m_y:.2f} * x + {d_y:.2f}", c='blue')
plt.plot(func_x(x), x, label=f"x(y) = {m_x:.2f} * y + {d_x:.2f}", c='green')
plt.title("Data points")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.ylim(y_min, y_max)
plt.xlim(x_min, x_max)
plt.legend()
plt.tick_params(axis='both', which='both', direction='in', length=6, width=1, colors='black', grid_color='black', grid_alpha=0.5, top = True, right = True)
plt.show()
