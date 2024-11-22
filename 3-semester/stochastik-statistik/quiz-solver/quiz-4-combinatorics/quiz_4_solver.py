import power_set as ps
import number_of_arrangements as noa
import number_of_tests as nots
import number_of_positive_integers as nopi
import number_of_distribution_to_server as nodts

####################################################################################################
# Exercise: Power set of a set

# Exercise: Number of elements in the power set of a set
####################################################################################################

# Replace the following with the set of your quiz:
set_for_power_set = "{10,d,{g}}"
power_set = ps.power_set_of_set(set_for_power_set)
print("Power set of", set_for_power_set, "is: ", power_set, "\n")

# Replace the following with the set of your quiz:
number_of_elements_in_set = 5
number_of_elements_in_power_set = 2 ** number_of_elements_in_set
print("Number of elements in the power set of a set with", number_of_elements_in_set, "elements is:", number_of_elements_in_power_set, "\n")


####################################################################################################
# Exercise: In how many ways can you arrange the numbers in the sequence
####################################################################################################

# Replace the following with the sequence of your quiz:
sequence = [-1,2,0,-2,-2,-1]
number_of_arrangements = noa.number_of_arrangements_of_sequence(sequence)
print("Number of ways you can arrange the numbers in the sequence", sequence, "is:", number_of_arrangements, "\n")


####################################################################################################
# Exercise: Number of tests to run for given input-vectors and values they can become and percentage of test-coverage
################################################################################################

# Replace the following with the possible values of the input vectors of your quiz:
# Form: x1:[x, y, z],x2:[x, y, z],x3:[x, y, z]
pos_val_input_vectors = "x1:[-2, -1, 0, 1, 2],x2:[-3, -2, -1, 0, 1, 2],x3:[-1, 0, 1, 2],x4:[-1, 0, 1, 2]"
test_coverage = 70

number_of_tests = nots.number_of_tests_to_run(pos_val_input_vectors, test_coverage)
print("Number of tests to run for given input-vectors and values they can become and percentage of test-coverage is:", number_of_tests, "\n")


####################################################################################################
# Exercise: Number of positive integers with at least a certain digit in it
####################################################################################################

# Replace the following with the digit and the number of digits of your quiz:
digit = 6
number_of_digits = 6

number_of_positive_integers = nopi.number_of_positive_integers_with_digit(digit, number_of_digits)
print("Number of positive integers with at least the digit", digit, "in it is:", number_of_positive_integers, "\n")


####################################################################################################
# Exercise: n copies of a backup are distributed to x servers. How many ways can the copies be distributed?
# (also possible to have no or all copy on a server)
#
# Part 2: Now m copies are distributed to x servers. How many ways can the copies be distributed if at least one copy is on each server?
####################################################################################################

# Replace the following with the number of copies and the number of servers of your quiz:
number_of_servers = 8
number_of_copies_part_1 = 5
number_of_copies_part_2 = 14

# Part 1:
number_of_distribution_part_1 = nodts.number_of_distribution_to_server(number_of_servers, number_of_copies_part_1)
print("Number of ways you can distribute", number_of_copies_part_1, "copies to", number_of_servers, "servers is:", number_of_distribution_part_1)

# Part 2:
effective_number_of_copies_part_2 = number_of_copies_part_2 - number_of_servers
number_of_distribution_part_2 = nodts.number_of_distribution_to_server(number_of_servers, effective_number_of_copies_part_2)
print("Number of ways you can distribute", number_of_copies_part_2, "copies to", number_of_servers, "servers is, if at least one copy is on each server:", number_of_distribution_part_2, "\n")

