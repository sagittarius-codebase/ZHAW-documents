import power_set as ps

####################################################################################################
# Exercise: Power set of a set

# Exercise: Number of elements in the power set of a set
####################################################################################################

# Replace the following with the set of your quiz:
set_for_power_set = "{1, 2, 3}"
power_set = ps.power_set_of_set(set_for_power_set)
print("Power set of", set_for_power_set, "is: ", power_set, "\n")

# Replace the following with the set of your quiz:
number_of_elements_in_set = 3
number_of_elements_in_power_set = 2 ** number_of_elements_in_set
print("Number of elements in the power set of a set with", number_of_elements_in_set, "elements is:", number_of_elements_in_power_set)