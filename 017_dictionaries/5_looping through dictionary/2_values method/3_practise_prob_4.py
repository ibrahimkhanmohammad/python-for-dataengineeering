#   find the total marks of a student by using values method
def marks(dct):
    total = 0
    for val in dct.values():
        total += val
    return total

student = {'science': 40, 'maths': 80, 'physics': 65, 'chemistry': 50}
print(marks(student))