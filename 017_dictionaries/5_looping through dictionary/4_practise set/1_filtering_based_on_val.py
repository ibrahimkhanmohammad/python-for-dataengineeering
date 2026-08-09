#   filter the values and label it accordingly
def grade_filter(dct):
    result = {}
    for sub, mark in dct.items():
        if mark >= 80:
            result[sub] = "Excellent"
        elif mark >= 60:
            result[sub] = "Good"
        else:
            result[sub] = "Need Improvement"
    return result

marks = {'science': 40, 'maths': 80, 'physics': 65, 'chemistry': 50}
print(grade_filter(marks))
