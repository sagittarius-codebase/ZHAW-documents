import re

def number_of_tests_to_run(pos_val_input_vectors, test_coverage):
    """
    Calculate number of tests to run for given input-vectors and values they can become,
    and percentage of test-coverage

    :param str pos_val_input_vectors:
    :param int test_coverage:
    :return: number of tests to run
    :rtype: int
    """

    number_of_tests = 1

    pos_results = re.findall(r'\[([0-9, ]+)]', pos_val_input_vectors)
    pos_results_lists = [list(map(int, match.split(', '))) for match in pos_results]


    for sub_list in pos_results_lists:
        number_of_tests *= len(sub_list)

    return int(number_of_tests * test_coverage / 100)