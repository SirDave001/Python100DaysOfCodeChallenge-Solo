import random

def get_char(char_list, number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list

while True:
    pwd_char = int(input('Enter your preferred number of characters in the password: '))
    pwd_upper = int(input('At least how many uppercase letters: '))
    pwd_lower = int(input('At least how many lowercase letters: '))
    pwd_digits = int(input('At least how many digits: '))
    pwd_symbols = int(input('At least how many symbols: '))
    if pwd_char < pwd_upper + pwd_lower + pwd_digits + pwd_symbols:
        print('Characters numbers do not match. Try again.')
    else:
        break
    
upper_list = [chr(i) for i in range(65, 91)]
upper_char = get_char(upper_list, pwd_upper)
lower_list = [chr(i) for i in range(97, 123)]
lower_char = get_char(lower_list, pwd_lower)
digit_list = [chr(i) for i in range(0, 10)]
digit_char = get_char(digit_list, pwd_digits)
symbol_list = [chr(i) for i in range(33, 48)]
symbol_list += [chr(i) for i in range(58, 65)]
symbol_list += [chr(i) for i in range(91, 97)]
symbol_list += [chr(i) for i in range(123, 127)]
symbol_char = get_char(symbol_list, pwd_symbols)

pwd_unfilled_chars = pwd_char - pwd_upper - pwd_lower - pwd_digits - pwd_symbols
pwd_whole_list = upper_list + lower_list + digit_list + symbol_list
rem_char = get_char(pwd_whole_list, pwd_unfilled_chars)

pwd = upper_char + lower_char + digit_char + symbol_char + rem_char
random.shuffle(pwd)
pwd = ''.join(pwd)
print(f'Your password is: {pwd}')
regenerate = input('Do you want to regenerate the password? ')
if regenerate == 'y':
    pwd = get_char(pwd_whole_list, pwd_unfilled_chars)
    random.shuffle(pwd)
    pwd = ''.join(pwd)
    print(f'Your password is: {pwd}')
else:
    print('Thank you for playing.')
