ApplicantsDict = {'David': {'experience': 3,
                            'languages': ['Scala', 'Haskell', 'Perl'],
                            'ProjectSup': False
                            },
                  'Han': {'experience': 4,
                            'languages': ['Python', 'Golang', 'Ruby', 'Java'],
                            'ProjectSup': True
                            },
                  'Naomi': {'experience': 1,
                            'languages': ['Python', 'Java', 'Haskell'],
                            'ProjectSup': True
                            },
                  'Dan': {'experience': 5,
                            'languages': ['Ruby', 'Rust', 'Python', 'Java'],
                            'ProjectSup': False
                            },
                 }
MinExperience = 3
RequiredLanguages = ['Python', 'Java']
for name, cvDict in ApplicantsDict.items():
    if cvDict['experience'] >= MinExperience and (set(RequiredLanguages).issubset(set(cvDict['languages'])) or cvDict['ProjectSup']):
        print(f'{name} passes the screening.')