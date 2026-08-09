#   Define a dictionary with five subjects and their respective marks. Utilize the get() method to try accessing a subject that is not in the dictionary, ensuring it prints "Not Available" as a default.
def sub_marks(dct, sub):
    return dct.get(sub, "Not Available")


marks = {'c': 85, 'py': 95, 'cpp': 90, 'java': 80}
print(sub_marks(marks, 'cpp'))
print(sub_marks(marks, 'js'))