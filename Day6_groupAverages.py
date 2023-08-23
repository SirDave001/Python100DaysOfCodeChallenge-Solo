def get_average(a_list):
    total = 0
    for mark in a_list:
        total += mark
    average = total/len(a_list)
    return average

def get_max(a_list):
    max_value = 0
    for mark in a_list:
        if mark > max_value:
            max_value = mark
    return max_value

mark_list = [[23, 45, 4, 23, 12, 6, 7, 8, 98, 78],
             [12, 34, 56, 78, 65, 43, 35],
             [21, 32, 43, 54, 65, 76, 87, 98]]

average_list = []
for group_list in mark_list:
    average_value = get_average(group_list)
    average_list.append(average_value)
max_average = get_max(average_list)

print(f'The school with the highest average score of {max_average} is school {average_list.index(max_average)}')