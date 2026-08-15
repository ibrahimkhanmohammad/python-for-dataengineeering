# zip() is a built-in Python function that combines two or more iterables element-wise and returns a zip object containing tuples of corresponding elements
# It returns a zip object, and each pair is a tuple.

subjects = ['Math', 'Science', 'English']
marks = [95, 80, 75]

res = (zip(subjects, marks))
print(list(res))
# print(dict(res))

print(type(res))