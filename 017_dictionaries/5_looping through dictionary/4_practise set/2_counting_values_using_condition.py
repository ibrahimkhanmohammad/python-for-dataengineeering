#   using values method iterate through each value and return the number of passed subjects
def passed_subjects(dct):
    sub_pass = 0
    for val in dct.values():
        if val >= 40:
            sub_pass += 1
    return f'no. of subjects passed {sub_pass}'

marks = {'science': 35, 'maths': 80, 'physics': 65, 'chemistry': 50}
print(passed_subjects(marks))