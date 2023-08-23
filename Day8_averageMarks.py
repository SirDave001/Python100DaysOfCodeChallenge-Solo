students = [['Vic', 85, 76, 56],
            ['Obi', 78, 87, 98],
            ['Viv', 98, 89, 87],
            ]
each_test_total = []
num_tests = len(students[0]) - 1
num_students = len(students)
for test_index in range(num_tests):
    each_test_total.append(0)
for student_index in range(num_students):
    for test_index in range(num_tests):
        each_test_total[test_index] += students[student_index][test_index + 1]
each_test_average = []
for test_index in range(num_tests):
    each_test_average.append(each_test_total[test_index] / len(students))
for test_index in range(num_tests):
    print(f'The average for test {test_index + 1} is {each_test_average[test_index]}')
    
print(f'The highest average is {max(each_test_average)} and is in test {each_test_average.index(max(each_test_average)) + 1}.')