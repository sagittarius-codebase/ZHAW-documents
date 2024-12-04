
####################################################################################################
# Quiz 11: Normal Distribution ZGS
####################################################################################################

# imports:
import scipy.stats as stats
import scipy.integrate as integrate

####################################################################################################
# Exercise 1: random generator generates numbers
print("Exercise 1: random generator generates numbers")
####################################################################################################

# Replace the following with the values of your quiz:

# range:
lower_bound = 26
upper_bound = 38
# lower_bound ≤ z ≤ upper_bound

amount = 153
value = 4785
# variations of the exercise:

# at maximum or at minimum:
at_maximum = True

# sum or arithmetic mean:
is_sum = True

# Calculations:
expected_val = (lower_bound + upper_bound) / 2
print(f"Expected value: {expected_val}")

variation = ((upper_bound - lower_bound) * (upper_bound - lower_bound + 2)) / 12
print(f"Variation: {variation}")

summed_expected_val = amount * expected_val
summed_variation = amount * variation
standard_deviation = summed_variation ** 0.5

mean_expected_val = expected_val
mean_variation = variation
mean_standard_deviation = mean_variation ** 0.5


if is_sum:
    z = (value - summed_expected_val) / standard_deviation
else:
    z = (value - mean_expected_val) / mean_standard_deviation

p = stats.norm.cdf(z) if at_maximum else 1 - stats.norm.cdf(z)

comparison = "≤" if at_maximum else ">"
output_type = "X" if is_sum else "X̄"

print(f"Either you got to your STS table and search for the value z = {abs(z):.4f}, maybe you need interpolation.")
print(f"Or you just use this result: P({output_type} {comparison} {value:.2f}) = {p:.4f} (not recommended)")


####################################################################################################
# Exercise 2: expected value and variance based on the given values
print("\nExercise 2: expected value and variance based on the given values")
################################################################################################

# Replace the following with the values of your quiz:
number_of_variables = 5
expected_value = 15
variance = 2

# differentiate between sum and mean:
is_sum = True

# Calculations:
summed_expected_val = number_of_variables * expected_value
summed_variance = number_of_variables * variance

mean_expected_val = expected_value
mean_variance = variance / number_of_variables

if is_sum:
    print(f"Expected value of the sum: {summed_expected_val}")
    print(f"Variance of the sum: {summed_variance}")
else:
    print(f"Expected value of the mean: {mean_expected_val}")
    print(f"Variance of the mean: {mean_variance}")


####################################################################################################
# Exercise 3: binomial distribution approximation via normal distribution
print("\nExercise 3: binomial distribution approximation via normal distribution")
####################################################################################################

# Replace the following with the values of your quiz:

# in B(n, p)
number_of_repetitions = 90 # n
probability = 0.7 # p

# probability P (X ≤/< x ≤/< Y)
lower_bound = 12
upper_bound = 42

# bigger than or equal-bigger than (False = bigger than (<) and not equal-bigger than (≤))
bigger_than_lower_bound = True
bigger_than_upper_bound = False

# Calculations:
lower_bound_correction = 0.5 if bigger_than_lower_bound else -0.5
upper_bound_correction = -0.5 if bigger_than_upper_bound else 0.5

approx_lower_bound = lower_bound + lower_bound_correction
approx_upper_bound = upper_bound + upper_bound_correction

print("P (" + str(lower_bound) + " ≤/< X ≤/< " + str(upper_bound) + ") ~ P (" + str(approx_lower_bound) + " < X ≤ " + str(approx_upper_bound) + ")")

expected_value = number_of_repetitions * probability
variance = number_of_repetitions * probability * (1 - probability)

print(f"Expected value: {expected_value:.2f}")
print(f"Variance: {variance:.2f}")

####################################################################################################
# Exercise 4: number of datapoints below a function curve in a Unit square
print("\nExercise 4: number of datapoints below a function curve in a Unit square")
####################################################################################################

# Replace the following with the values of your quiz:
number_of_datapoints = 36

# for example: E(1/20 X) and V(1/20 X)
fraction_of_datapoints = 1 / 36

# function:
function = lambda x: (1 * (1 - x) * (x + 1/3)) / 1

# Calculations:
function_integral = integrate.quad(function, 0, 1)[0]
# the area can be used as the probability

expected_value = number_of_datapoints * function_integral
variance = number_of_datapoints * function_integral * (1 - function_integral)

fraction_expected_value = expected_value * fraction_of_datapoints
fraction_variance = variance * (fraction_of_datapoints ** 2)

print(f"E(1/{number_of_datapoints} X) = {fraction_expected_value:.3f}")
print(f"V(1/{number_of_datapoints} X) = {fraction_variance:.3f}")





