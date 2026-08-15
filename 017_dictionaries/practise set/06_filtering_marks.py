#   Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to generate a new dictionary that prints only the subjects where the student scored 40 or more (i.e., passed)

def result(dct):
    return{sub: mark for sub, mark in dct.items() if mark >= 40}

marks = {
    'mat': 95,
    'sci': 80,
    'soc': 65,
    'chem': 35,
    'comp': 40,
}

print(result(marks))