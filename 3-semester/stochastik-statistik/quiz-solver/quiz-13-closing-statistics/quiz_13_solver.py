
####################################################################################################
# Quiz 13: Closing Statistics
####################################################################################################

# imports:


####################################################################################################
# Exercise 1: Trusting Intervall for expected value
####################################################################################################
print("\n\nExercise 1: Trusting Intervall for expected value")

# replace the following values with the values from the quiz

sample_size = 25 # n
arith_mean = 4 # x_bar
empiric_variance = 9 # s^2
confidence_level = 0.99 # Vertrauens-Intervall
# variance (True) or expected value (False)
calculate_variance = False


# Calculation:

if calculate_variance:
    print("Calculating the trusting intervall for the variance")
    free_degree = sample_size - 1 # f
    quantile_1 = (1 + confidence_level) / 2 # p_1
    quantile_2 = (1 - confidence_level) / 2 # p_2

    print("\bNow go to the table 3 'Quantile der Chi‐Quadrat‐Verteilung von «Pearson»'")
    print(f"and look for the value of the quantile p_1 = {quantile_1} and the free degree f = {free_degree}")
    print("and replace tha value of quantile_value_1 with the value from the table")
    print(f"\nand look for the value of the quantile p_2 = {quantile_2} and the free degree f = {free_degree}")
    print("and replace tha value of quantile_value_2 with the value from the table\n")

    quantile_value_1 = 29.82 # c REPLACE THIS VALUE
    quantile_value_2 = 3.57 # c REPLACE THIS VALUE

    lower_bound = (sample_size - 1) * empiric_variance / quantile_value_1
    upper_bound = (sample_size - 1) * empiric_variance / quantile_value_2

else:
    print("Calculating the trusting intervall for the expected value")
    # calculate the upper and lower bound of the trusting intervall for the expected value
    free_degree = sample_size - 1 # f
    quantile = (1 + confidence_level) / 2 # p

    print("\nNow go to the table 4 'Quantile der t‐Verteilung von «Student»'")
    print(f"and look for the value of the quantile p = {quantile} and the free degree f = {free_degree}")
    print("Then replace the value with the variable down below\n")

    quantile_value = 45.6 # c REPLACE THIS VALUE

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
values = [6, 4, 1, 6, 3]

# calculate the guessing value for the expected value
guessing_value = sum(values) / len(values)
print(f"Guessing value for the expected value: {guessing_value:.2f}")


####################################################################################################
# Exercise 3: Chi-Square Distribution
####################################################################################################
print("\n\nExercise 3: Chi-Square Distribution")

# replace the following values with the values from the quiz
number_freedom_degree = 6 # f
confidence_level = 0.95 # Vertrauens-Intervall

print("Now go to the table 3 'Quantile der Chi‐Quadrat‐Verteilung von «Pearson»'")
print("or the table 4 'Quantile der t‐Verteilung von «Student»' based on your quiz!")
print(f"and look for the value of the quantile p = {confidence_level} and the number of freedom degree f = {number_freedom_degree}")
print("I'm sorry, but I can't do this for you. You have to do it by yourself. :)")


####################################################################################################
# Exercise 4: Guess Value for variance
####################################################################################################
print("\n\nExercise 4: Guess Value for variance")

# replace the following values with the values from the quiz
values = [2, 1, 4, 1, 2]

# calculate the guessing value for the variance
guessing_value = sum([(x - sum(values) / len(values)) ** 2 for x in values]) / (len(values) - 1)

print(f"Guessing value for the variance: {guessing_value:.2f}")


print("\n For the multiple Choice: Have a look at the images. But be careful! The question can be slightly different!")