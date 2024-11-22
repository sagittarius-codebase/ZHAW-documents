
####################################################################################################
# Quiz 9: Special Discrete Random Variables
####################################################################################################

# Imports:
from scipy.stats import poisson
from math import log, ceil


####################################################################################################
# Exercise 1: Server - requests per minute
####################################################################################################

# Replace the following with the values of your quiz:
requests_per_minute = 8697 / 100
number_of_minutes = 30
maximum_of_requests = 2629

# Calculate the probability of the MAXIMUM of requests in 30 minutes:
P = poisson.cdf(maximum_of_requests, requests_per_minute * number_of_minutes)
print("The probability of the maximum of requests in", number_of_minutes, "minutes is:", round(P, 3), "\n")


####################################################################################################
# Exercise 2: probabilistic program
####################################################################################################

correct_result_prob = 0.28
minimum_prob_for_correct_result = 0.93

# Calculate the minimum number of repetitions needed to reach the minimum probability for a correct result:
# Actual equation: (0.28 = p, 0.93 = P, n = number of repetitions)
# P( X >= 1 ) ≥ 0.93
# 1 - P( X < 1 ) ≥ 0.93
# 1 - P( X = 0 ) ≥ 0.93
# 1 - 0.93 ≥ P( X = 0 ) = nCr( n, 0 ) * 0.28^0 * (1 - 0.28)^(n-0)
# 0.07 ≥ 0.72^n
# n = log(0.07) / log(0.72)

n = ceil(log(1 - minimum_prob_for_correct_result) / log(1 - correct_result_prob))

print("The minimum number of repetitions needed to reach the minimum probability for a correct result is:", n, "\n")

