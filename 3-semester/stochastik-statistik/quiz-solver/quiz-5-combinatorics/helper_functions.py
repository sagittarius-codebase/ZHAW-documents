
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

