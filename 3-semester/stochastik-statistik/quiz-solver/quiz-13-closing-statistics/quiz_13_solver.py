
####################################################################################################
# Quiz 13: Closing Statistics
####################################################################################################

# imports:


####################################################################################################
# Exercise 1: Trusting Intervall for expected value
####################################################################################################
print("\n\nExercise 1: Trusting Intervall for expected value")

# replace the following values with the values from the quiz

sample_size = 9 # n
arith_mean = -4 # x_bar
empiric_variance = 4 # s^2
confidence_level = 0.99 # Vertrauens-Intervall

# calculate the upper and lower bound of the trusting intervall for the expected value
free_degree = sample_size - 1 # f
quantile = (1 + confidence_level) / 2 # p

print("Now go to the table 4 'Quantile der t‐Verteilung von «Student»'")
print(f"and look for the value of the quantile p = {quantile} and the free degree f = {free_degree}")
print("Then replace the value with the variable down below")

quantile_value = 3.355 # c REPLACE THIS VALUE

barrier_e = quantile_value * (empiric_variance ** 0.5 / sample_size ** 0.5)

lower_bound = arith_mean - barrier_e
upper_bound = arith_mean + barrier_e

print(f"Lower bound: {lower_bound:.2f}")
print(f"Upper bound: {upper_bound:.2f}")


####################################################################################################
# Exercise 2: Guess Value for the expected value (aka arithmetical mean)
####################################################################################################
print("\n\nExercise 2: Guess Value for the expected value (aka arithmetical mean)")

# replace the following values with the values from the quiz
values = [4, 5, 4, 2, 5]

# calculate the guessing value for the expected value
guessing_value = sum(values) / len(values)
print(f"Guessing value for the expected value: {guessing_value:.2f}")


####################################################################################################
# Exercise 3: Chi-Square Distribution
####################################################################################################
print("\n\nExercise 3: Chi-Square Distribution")

# replace the following values with the values from the quiz
number_freedom_degree = 2 # f
confidence_level = 0.995 # Vertrauens-Intervall

print("Now go to the table 3 'Quantile der Chi‐Quadrat‐Verteilung von «Pearson»'")
print(f"and look for the value of the quantile p = {confidence_level} and the number of freedom degree f = {number_freedom_degree}")
print("I'm sorry, but I can't do this for you. You have to do it by yourself. :)")


####################################################################################################
# Exercise 4: Guess Value for variance
####################################################################################################
print("\n\nExercise 4: Guess Value for variance")

# replace the following values with the values from the quiz
values = [4, 3, 1, 1, 1]

# calculate the guessing value for the variance
guessing_value = sum([(x - sum(values) / len(values)) ** 2 for x in values]) / (len(values) - 1)

print(f"Guessing value for the variance: {guessing_value:.2f}")