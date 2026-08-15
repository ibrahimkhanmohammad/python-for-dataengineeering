# zip() pairs corresponding elements of two lists.
# It returns a zip object, and each pair is a tuple.

subjects = ['Math', 'Science', 'English']
marks = [95, 80, 75]

res = (zip(subjects, marks))
print(list(res))
# print(dict(res))

print(type(res))