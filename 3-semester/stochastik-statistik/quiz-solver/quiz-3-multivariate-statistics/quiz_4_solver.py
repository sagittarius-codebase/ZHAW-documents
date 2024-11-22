import helper_functions as hf
from math import sqrt

# replace with your data from your quiz!
# bivariate_data = [[6, 5], [4, -2], [8, -5], [-3, 6], [-7, -13], [-4, 0], [-4, 3], [-12, 4], [-4, 12]]
bivariate_data = [[1,-7],[-5,3],[0,0],[-9,1],[2,4],[-4,-9],[-13,13],[2,3],[0,2],[-4,1],[-14,-9]]

# Change according to the instructions in the quiz:
number_of_decimal_places = 2

hf.plot_data(bivariate_data)

# The following Characteristics are calculated:

# 1: x-Coordinates:
x_coordinates = [data[0] for data in bivariate_data]
x_coordinates_str = hf.list_to_no_space_string(x_coordinates)
print('(1) x-Coordinates:', x_coordinates_str)

# 2: sorted x-Coordinates:
sorted_x_coordinates = sorted(x_coordinates)
sorted_x_coordinates_str = hf.list_to_no_space_string(sorted_x_coordinates)
print('(2) sorted x-Coordinates:', sorted_x_coordinates_str)

# 3: ranking list of x-Coordinates:
ranking_list_x = hf.get_ranking_list(x_coordinates)
ranking_list_x_str = hf.list_to_no_space_string(ranking_list_x)
print('(3) ranking list of x-Coordinates:', ranking_list_x_str)

# 4: y-Coordinates:
y_coordinates = [data[1] for data in bivariate_data]
y_coordinates_str = hf.list_to_no_space_string(y_coordinates)
print('(4) y-Coordinates:', y_coordinates_str)

# 5: sorted y-Coordinates:
sorted_y_coordinates = sorted(y_coordinates)
sorted_y_coordinates_str = hf.list_to_no_space_string(sorted_y_coordinates)
print('(5) sorted y-Coordinates:', sorted_y_coordinates_str)

# 6: ranking list of y-Coordinates:
ranking_list_y = hf.get_ranking_list(y_coordinates)
ranking_list_y_str = hf.list_to_no_space_string(ranking_list_y)
print('(6) ranking list of y-Coordinates:', ranking_list_y_str)

# 7: Covariance (not corrected):
mean_x = sum(x_coordinates) / len(x_coordinates)
mean_y = sum(y_coordinates) / len(y_coordinates)

covariance = sum([(x - mean_x) * (y - mean_y) for x, y in bivariate_data]) / len(bivariate_data)

print('(7) Covariance (not corrected):', round(covariance, number_of_decimal_places))

# 8: Pearson's correlation coefficient:
variance_x = sum([(x - mean_x) ** 2 for x in x_coordinates]) / len(x_coordinates)
variance_y = sum([(y - mean_y) ** 2 for y in y_coordinates]) / len(y_coordinates)

pearsons_correlation_coefficient = covariance / sqrt(variance_x * variance_y)

print('(8) Pearson\'s correlation coefficient:', round(pearsons_correlation_coefficient, number_of_decimal_places))

# 9: Covariance of the ranking lists (not corrected):

mean_ranking_x = sum(ranking_list_x) / len(ranking_list_x)
mean_ranking_y = sum(ranking_list_y) / len(ranking_list_y)
covariance_ranking_lists = sum(
    [(x - mean_ranking_x) * (y - mean_ranking_y) for x, y in zip(ranking_list_x, ranking_list_y)]) / len(ranking_list_x)

print('(9) Covariance of the ranking lists (not corrected):', round(covariance_ranking_lists, number_of_decimal_places))

# 10: Spearman's correlation coefficient

# Variance of the ranking lists (standard deviation squared)
variance_ranking_x = sum([(x - mean_ranking_x) ** 2 for x in ranking_list_x]) / len(ranking_list_x)
variance_ranking_y = sum([(y - mean_ranking_y) ** 2 for y in ranking_list_y]) / len(ranking_list_y)

# Standard deviation is the square root of the variance
std_dev_ranking_x = sqrt(variance_ranking_x)
std_dev_ranking_y = sqrt(variance_ranking_y)

# Spearman's correlation coefficient (r_s)
spearman_correlation_coefficient = covariance_ranking_lists / (std_dev_ranking_x * std_dev_ranking_y)

print('(10) Spearman\'s correlation coefficient:', round(spearman_correlation_coefficient, number_of_decimal_places))
