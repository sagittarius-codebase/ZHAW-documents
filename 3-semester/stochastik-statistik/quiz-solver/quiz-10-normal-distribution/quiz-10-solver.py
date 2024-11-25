
####################################################################################################
# Quiz 10: Normal Distribution
####################################################################################################

# Imports:

####################################################################################################
# Exercise 1: Normal Distribution Intervall
####################################################################################################

# Replace the following with the values of your quiz:
expected_value = 70 # μ
standard_deviation = 2 # σ


# determine the intervall that contains 99.7% of the values:
lower_bound = expected_value - 3 * standard_deviation
upper_bound = expected_value + 3 * standard_deviation

print("The intervall that contains 99.7% of the values is:", lower_bound, "to", upper_bound, "\n")


####################################################################################################
# Exercise 2: Standard Normal Distribution
####################################################################################################

# Replace the following with the values of your quiz:
value = 0.97 # value x in: P(X <= x)

print("Search in your table for the value and determine the probability that the value is less or equal to.")
print("value = ", value, "\n")

####################################################################################################
# Exercise 3: Normal Distribution with custom expected value and standard deviation
####################################################################################################

# Replace the following with the values of your quiz:
expected_value = 60 # μ
standard_deviation = 20 # σ
value = 118

# determine the probability that the value is less or equal to 63:
z = (value - expected_value) / standard_deviation

print("Search in your table for the value of z and determine the probability that the value is less or equal to ", value)
print("z = ", z, "\n")

####################################################################################################
# Exercise 4: Standard Normal Distribution with higher than rather than less or equal
####################################################################################################

# Replace the following with the values of your quiz:
value = 1.28 # value x in: P(X > x)

print("Search in your table for the value and determine the probability that the value is higher than.")
print("value = ", value)
print("An then subtract the value from 1 to get the probability that the value is higher than. -> P(X > x) = 1 - P(X <= x)\n")

####################################################################################################
# Exercise 5: general standardization of a normal distribution
####################################################################################################

# Replace the following with the values of your quiz:
expected_value = -4 # μ
standard_deviation = 5 # σ

# How to calculate U out of X generally?

print("U = (X - μ) / σ, so here:")
if expected_value < 0:
    print("U = ( X +", abs(expected_value), ") /", standard_deviation)
else:
    print("U = ( X -", expected_value, ") /", standard_deviation)


