import numpy as np
import matplotlib.pyplot as plt

def plot_cdf(pmf_values, x_values):
    """
    This function plots the Cumulative Distribution Function (CDF) of a discrete random variable.

    :param list pmf_values: list of probabilities of the random variable
    :param list x_values: list of values of the random variable
    :return: None
    """
    cdf_values = np.cumsum(pmf_values)
    # Plot the horizontal plateau lines for each segment
    for i in range(len(x_values)):
        # Draw horizontal lines representing the CDF plateaus
        plt.hlines(cdf_values[i], x_values[i], x_values[i + 1] if i + 1 < len(x_values) else 10, color='b', linewidth=2)
    # Draw the line from (0, 0) to the first x value
    plt.hlines(0, 0, x_values[0], color='b', linewidth=2)
    # Draw the final horizontal line at the last plateau extending to the end
    plt.hlines(1, x_values[-1], 10, color='b', linewidth=2)
    # Setting plot limits and labels
    plt.ylim(-0.01, 1.1)
    plt.xlim(0, 10)
    plt.xlabel("X values")
    plt.ylabel("CDF")
    plt.title("Cumulative Distribution Function")
    plt.grid(True)
    # Display the plot
    plt.show()