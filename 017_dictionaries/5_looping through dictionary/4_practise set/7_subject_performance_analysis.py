#   Given a dictionary of marks for different subjects, loop over its values () to calculate and print the total marks and the average mark obtained.
def total_avg(dct):
    total = 0
    for val in dct.values():
        total += val
        average = total / len(dct)
    return total, average

marks = {'sci': 85, 'mat': 78, 'phy': 65, 'chem': 35}
print(total_avg(marks))
