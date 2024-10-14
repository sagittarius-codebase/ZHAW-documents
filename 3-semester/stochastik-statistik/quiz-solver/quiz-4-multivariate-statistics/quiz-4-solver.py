
import helper_functions as hf

# replace with your data from your quiz!
bivariate_data = [[6, 5] , [4, -2] , [8, -5] , [-3, 6] , [-7, -13] , [-4, 0] , [-4, 3] , [-12, 4] , [-4, 12]]


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

# Create a dictionary to store the average ranks for duplicates
rank_dict = defaultdict(list)

# Populate the dictionary with indices for each value
for i, x in enumerate(sorted_x_coordinates):
    rank_dict[x].append(i + 1)

# Compute the middle rank for each value
final_ranking = {}
for key, ranks in rank_dict.items():
    # If there are multiple occurrences, find the middle rank
    if len(ranks) > 1:
        avg_rank = sum(ranks) / len(ranks)
        final_ranking[key] = avg_rank
    else:
        final_ranking[key] = ranks[0]

# Create the ranking list based on the original x_coordinates
ranking_list = [
    int(final_ranking[x]) if final_ranking[x] % 1 == 0 else final_ranking[x]
    for x in x_coordinates
]

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


