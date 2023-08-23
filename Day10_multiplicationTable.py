table_row = ''
for i in range(1, 11):
    for j in range(1, 11):
        table_row += (f'{str(i)} x {str(j)} = {str(i * j)} \n')
        print(table_row)
        table_row = ''