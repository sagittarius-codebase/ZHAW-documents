import power_set as ps
import number_of_arrangements as noa

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
print("Number of elements in the power set of a set with", number_of_elements_in_set, "elements is:", number_of_elements_in_power_set)


####################################################################################################
# Exercise: In how many ways can you arrange the numbers in the sequence
####################################################################################################

# Replace the following with the sequence of your quiz:
sequence = [3, -2, 0, 3, -1, -2, 2, 3, 3, -2]
number_of_arrangements = noa.number_of_arrangements_of_sequence(sequence)
print("Number of ways you can arrange the numbers in the sequence", sequence, "is:", number_of_arrangements)