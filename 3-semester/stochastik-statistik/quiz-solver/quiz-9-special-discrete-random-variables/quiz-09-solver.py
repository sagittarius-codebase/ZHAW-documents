
####################################################################################################
# Quiz 9: Special Discrete Random Variables
####################################################################################################

# Imports:
from scipy.stats import poisson


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


