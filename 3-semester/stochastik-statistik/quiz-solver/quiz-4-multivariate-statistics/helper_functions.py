import matplotlib.pyplot as plt

def plot_data(data):
    """
    Plots the data in a scatter plot with the same look as in the quiz.

    :param list data: A list of lists with the data points. Each sub-list should contain two values.
    :return: None
    """
    # plot the data
    for data in data:
        plt.scatter(data[0], data[1], color='red', edgecolor='red', facecolors='none')
    # Dashed lines for x and y axes
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.xlabel('x-Achse')
    plt.ylabel('y-Achse')
    plt.title('Bivariate Data')
    plt.show()

def list_to_no_space_string(lst):
    return "[" + ",".join(map(str, lst)) + "]"