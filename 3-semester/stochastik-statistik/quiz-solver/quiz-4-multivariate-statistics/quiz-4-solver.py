
import helper_functions as hf

# replace with your data from your quiz!
bivariate_data = [[6, 5] , [4, -2] , [8, -5] , [-3, 6] , [-7, -13] , [-4, 0] , [-4, 3] , [-12, 4] , [-4, 12]]


hf.plot_data(bivariate_data)

# The following Characteristics are calculated:

# 1: x-Coordinates:

x_coordinates = [data[0] for data in bivariate_data]

# Convert the list to a string with no spaces so you can just copy it to your quiz.
x_coordinates_str = "[" + ",".join(map(str, x_coordinates)) + "]"

print('(1) x-Coordinates:', x_coordinates_str)


