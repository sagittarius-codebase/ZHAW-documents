
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

    power_set_string = convert_to_string(power_set)

    return power_set_string


def convert_to_string(power_set):
    """
    This function converts a power set to a string.
    Form: "{{},{x},{y},{z},{x,y},{x,z},{y,z},{x,y,z}}"

    :param list power_set: power set to be converted to string
    :return: power set in correct form
    :rtype: string
    """

    result = "{"
    for subset in power_set:
        subset_str = "{" + ",".join(map(str, subset)) + "}"
        result += subset_str + ","
    result = result[:-1] + "}"  # Remove the last comma and space, then close the outer braces
    return result