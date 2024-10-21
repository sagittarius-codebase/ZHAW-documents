from math import comb

def number_of_arrangements_of_sequence(sequence):
    """
    This function returns the number of ways you can arrange the numbers in a given sequence.
    same numbers are not being counted as different numbers.
    :param list sequence: sequence of numerals
    :return: number of ways you can arrange the numbers in the sequence
    :rtype: int
    """

    sequence_dict = {}
    for number in sequence:
        if number in sequence_dict:
            sequence_dict[number] += 1
        else:
            sequence_dict[number] = 1

    number_of_arrangements = 1
    sequence_length = len(sequence)

    for number in sequence_dict:
        number_of_arrangements *= comb(sequence_length, sequence_dict[number])
        sequence_length -= sequence_dict[number]

    return number_of_arrangements