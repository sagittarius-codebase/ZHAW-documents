import helper_functions as hf


def power_set_of_set(my_set):
    """
    This function returns the power set of a given set.
    String my_set should be in the form of "{x, y, z}".
    Example: [1, 2, 3] -> [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

    :param string my_set: set of elements
    :return: power set of the given set
    :rtype: string
    """

    # remove curly braces and split
    my_set = my_set[1:-1].split(",")
    my_set = [element.strip() for element in my_set]

    power_set = [[]]
    for element in my_set:
        for subset in power_set:
            power_set = power_set + [list(subset) + [element]]

    power_set_string = hf.convert_to_string(power_set)

    return power_set_string