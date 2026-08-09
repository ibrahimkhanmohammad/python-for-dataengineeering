#   find the total marks of a student by using keys method
def marks(dct):
    total = 0
    for sub in dct.keys():
        total += dct[sub]
    return total

student = {'science': 40, 'maths': 80, 'physics': 65, 'chemistry': 50}
print(marks(student))