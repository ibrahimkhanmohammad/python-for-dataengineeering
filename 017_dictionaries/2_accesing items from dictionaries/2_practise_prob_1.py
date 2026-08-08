#   from a dict called marks, return sub value if exists, if not then sub not found
def sub_marks(dct, sub):
    return dct.get(sub, 'not found')

marks = {
        'c': 85,
        'py': 95,
        'cpp': 95,
        'java':80
        }

print(sub_marks(marks, 'py'))
print(sub_marks(marks, 'js'))