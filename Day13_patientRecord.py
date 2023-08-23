def PrintQueue(*aList, **aDict):
    for person in aList:
        for patient, info in aDict.items():
            if person == patient:
                print(f'{person}:')
                for key, value in info.items():
                    print(f'{key}: {value}')
                print('...........')


QueueList = ['Stiffany', 'Nelson', 'Xavier', 'Francis', 'Mercy', 'Obedience', 'Judah']
PatientDict = {'Nelson': {'age': 30, 'Weight': 65},
               'Xavier': {'age': 25, 'Weight': 61},
               'Stiffany': {'age': 35, 'Weight': 50},
               'Mercy': {'age': 26, 'Weight': 45}
              }

print('The following people are on queue')
PrintQueue(*QueueList, **PatientDict)