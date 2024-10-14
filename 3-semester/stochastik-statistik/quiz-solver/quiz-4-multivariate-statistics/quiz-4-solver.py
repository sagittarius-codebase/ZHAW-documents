
import helper_functions as hf
from collections import defaultdict

# replace with your data from your quiz!
bivariate_data = [[6, 5] , [4, -2] , [8, -5] , [-3, 6] , [-7, -13] , [-4, 0] , [-4, 3] , [-12, 4] , [-4, 12]]

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
ranking_list = hf.get_ranking_list(x_coordinates)
ranking_list_str = hf.list_to_no_space_string(ranking_list)
print('(3) ranking list of x-Coordinates:', ranking_list_str)


# 4: y-Coordinates:
y_coordinates = [data[1] for data in bivariate_data]
y_coordinates_str = hf.list_to_no_space_string(y_coordinates)
print('(4) y-Coordinates:', y_coordinates_str)

# 5: sorted y-Coordinates:
sorted_y_coordinates = sorted(y_coordinates)
sorted_y_coordinates_str = hf.list_to_no_space_string(sorted_y_coordinates)
print('(5) sorted y-Coordinates:', sorted_y_coordinates_str)

# 6: ranking list of y-Coordinates:
ranking_list = hf.get_ranking_list(y_coordinates)
ranking_list_str = hf.list_to_no_space_string(ranking_list)
print('(6) ranking list of y-Coordinates:', ranking_list_str)

# 7: Covariance (not corrected):
mean_x = sum(x_coordinates) / len(x_coordinates)
mean_y = sum(y_coordinates) / len(y_coordinates)

covariance = sum([(x - mean_x) * (y - mean_y) for x, y in bivariate_data]) / len(bivariate_data)

print('(7) Covariance (not corrected):', round(covariance, number_of_decimal_places))



