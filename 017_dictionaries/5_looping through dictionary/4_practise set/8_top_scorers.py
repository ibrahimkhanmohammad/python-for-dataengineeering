#   Populate a dictionary with six student names and their corresponding marks. Loop through it and print the names of all students who achieved a score above 75
def stud_names(dct):
    for name, score in dct.items():
        if score > 75:
            print(name)

students = {'abc': 45, 'def': 84, 'fgh': 86, 'ijk': 78, 'lmn': 96, 'opq': 87}
stud_names(students)

