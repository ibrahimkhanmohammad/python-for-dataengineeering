#   find the total marks of a student by using items method
def marks(dct):
    total = 0
    for sub, mark in dct.items():
        total += mark
    return total

student = {'science': 40, 'maths': 80, 'physics': 65, 'chemistry': 50}
print(marks(student))