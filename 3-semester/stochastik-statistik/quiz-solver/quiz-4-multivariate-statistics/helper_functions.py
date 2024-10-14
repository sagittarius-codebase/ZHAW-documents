from collections import defaultdict

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
    """
    Converts a list to a string without spaces.
    :param list lst: The list to convert.
    :return: string without spaces
    :rtype: str
    """
    return "[" + ",".join(map(str, lst)) + "]"

def get_ranking_list(coordinates):
    """
    Calculates the ranking list for a list of coordinates.

    :param list coordinates: A list of coordinates.
    :return: A list of the ranking of the coordinates.
    :rtype: list
    """
    sorted_coordinates = sorted(coordinates)
    rank_dict = defaultdict(list)

    # get the rank of each coordinate
    for i, x in enumerate(sorted_coordinates):
        rank_dict[x].append(i + 1)

    # calculate the average rank for each coordinate
    final_ranking = {}
    for key, ranks in rank_dict.items():
        if len(ranks) > 1:
            avg_rank = sum(ranks) / len(ranks)
            final_ranking[key] = avg_rank
        else:
            final_ranking[key] = ranks[0]

    # return the ranking list in the order of the original coordinates
    return [
        int(final_ranking[x]) if final_ranking[x] % 1 == 0 else final_ranking[x]
        for x in coordinates
    ]