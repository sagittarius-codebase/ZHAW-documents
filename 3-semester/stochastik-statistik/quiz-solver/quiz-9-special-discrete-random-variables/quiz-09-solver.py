
####################################################################################################
# Quiz 9: Special Discrete Random Variables
####################################################################################################

# Imports:
from scipy.stats import poisson
from math import log, ceil, comb


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

# Replace the following with the values of your quiz:
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


####################################################################################################
# Exercise 3: Lottery with luck-tickets
####################################################################################################

# Replace the following with the values of your quiz:
number_of_tickets = 16 # N
number_of_luck_tickets = 8 # M
number_purchased_tickets = 7 # n
maximum_of_received_luck_tickets = 1 # if text sais: less than 2, then 1!
minimum_of_received_luck_tickets = 0
# based on your text set either maximum_of_received_luck_tickets or minimum_of_received_luck_tickets
# the other one should be set to 0

# Calculate the probability of getting at most the MAXIMUM of defined luck-tickets:
if minimum_of_received_luck_tickets == 0:
    probability = 0
    for i in range(maximum_of_received_luck_tickets + 1):
        probability += comb(number_of_luck_tickets, i) * comb(number_of_tickets - number_of_luck_tickets, number_purchased_tickets - i) / comb(number_of_tickets, number_purchased_tickets)
    print("The probability of getting at most the MAXIMUM of defined luck-tickets is:", round(probability, 3), "\n")
else:
    probability = 0
    for i in range(minimum_of_received_luck_tickets, number_purchased_tickets + 1):
        probability += comb(number_of_luck_tickets, i) * comb(number_of_tickets - number_of_luck_tickets, number_purchased_tickets - i) / comb(number_of_tickets, number_purchased_tickets)
    probability = 1 - probability
    print("The probability of getting at least the MINIMUM of defined luck-tickets is:", round(probability, 3), "\n")


####################################################################################################
# Exercise 4: Number is binomial distributed
####################################################################################################

# Replace the following with the values of your quiz:
number_of_trials = 6 # n
probability_of_success = 0.4 # p
number_of_successes = 3 # x

P = comb(number_of_trials, number_of_successes) * probability_of_success**number_of_successes * (1 - probability_of_success)**(number_of_trials - number_of_successes)

print("The probability of getting", number_of_successes, "successes in", number_of_trials, "trials is:", round(P, 3), "\n")

