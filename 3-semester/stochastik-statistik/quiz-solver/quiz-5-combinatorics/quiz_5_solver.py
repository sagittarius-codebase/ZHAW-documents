import power_set as ps
import number_of_arrangements as noa
import number_of_tests as nots
import number_of_positive_integers as nopi

####################################################################################################
# Exercise: Power set of a set

# Exercise: Number of elements in the power set of a set
####################################################################################################

# Replace the following with the set of your quiz:
set_for_power_set = "{4, {0}, c}"
power_set = ps.power_set_of_set(set_for_power_set)
print("Power set of", set_for_power_set, "is: ", power_set, "\n")

# Replace the following with the set of your quiz:
number_of_elements_in_set = 3
number_of_elements_in_power_set = 2 ** number_of_elements_in_set
print("Number of elements in the power set of a set with", number_of_elements_in_set, "elements is:", number_of_elements_in_power_set, "\n")


####################################################################################################
# Exercise: In how many ways can you arrange the numbers in the sequence
####################################################################################################

# Replace the following with the sequence of your quiz:
sequence = [3, -2, 0, 3, -1, -2, 2, 3, 3, -2]
number_of_arrangements = noa.number_of_arrangements_of_sequence(sequence)
print("Number of ways you can arrange the numbers in the sequence", sequence, "is:", number_of_arrangements, "\n")


####################################################################################################
# Exercise: Number of tests to run for given input-vectors and values they can become and percentage of test-coverage
################################################################################################

# Replace the following with the possible values of the input vectors of your quiz:
# Form: x1:[x, y, z],x2:[x, y, z],x3:[x, y, z]
pos_val_input_vectors = "x1:[0, 1, 2, 3, 4],x2:[0, 1, 2, 3, 4],x3:[0, 1, 2, 3],x4:[0, 1, 2]"
test_coverage = 80

number_of_tests = nots.number_of_tests_to_run(pos_val_input_vectors, test_coverage)
print("Number of tests to run for given input-vectors and values they can become and percentage of test-coverage is:", number_of_tests, "\n")


####################################################################################################
# Exercise: Number of positive integers with at least a certain digit in it
####################################################################################################

# Replace the following with the digit and the number of digits of your quiz:
digit = 4
number_of_digits = 10

number_of_positive_integers = nopi.number_of_positive_integers_with_digit(digit, number_of_digits)
print("Number of positive integers with at least the digit", digit, "in it is:", number_of_positive_integers, "\n")