black_list = ['samuel', 'josh', 'joe', 'amy', 'ivy']
num_students = int(input('Enter the number students: '))
students_list = []
white_list = []

for student in range(num_students):
    prompt = input('Enter the first name of the student: ')
    while prompt == '':
        prompt = input('Pls enter a valid input command(first name of the student): ')
    students_list.append(prompt)
for student in students_list:
    if student not in black_list:
        white_list.append(student)

if len(white_list) == 0:
    print("No student is allowed to graduate.")
elif len(white_list) == 1:
    print(f"Only {white_list[0]} is allowed to graduate.")
else:
    print(f'These {len(white_list)} student(s) are allowed to graduate:')
    print(*sorted(white_list), sep=' ')
