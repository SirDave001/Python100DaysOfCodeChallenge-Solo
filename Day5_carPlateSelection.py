car_plates = ['AB1234', 'CD5678', 'EF901', 'GH234', 'IJ567', 'KL8901']
odd_days = ['MON', 'WED', 'FRI']
even_days = ['TUE', 'THU','SAT']
pass_list = []
day = input('Enter day of the week (SUNday to SATurday): ')
for plate in car_plates:
    last_digit = int(plate[-1])
    if day in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)
    elif day in even_days and last_digit % 2 == 0:
        pass_list.append(plate)
    elif day == 'SUN':
        pass_list.append(plate)
        
print(pass_list)
    