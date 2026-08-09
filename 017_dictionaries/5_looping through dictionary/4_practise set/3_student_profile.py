#   Create a dictionary for a student, including keys like name, age, city, and marks (as a list of scores). Print each piece of information using its key.
def details(dct):
    result = []
    for keys in dct.keys():
        result.append((keys, dct[keys]))
    return result

student = {'name': 'abc', 'age': 99, 'city': 'saturn', 'marks': [40, 52, 36, 98, 75]}
print(details(student))