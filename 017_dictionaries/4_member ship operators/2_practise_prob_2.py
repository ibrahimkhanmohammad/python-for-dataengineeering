#   using membership operators return if sub exist ina dict if not then return sub not found
def sub_marks(dct, sub):
    if sub in dct:
        return dct[sub]
    else:
        return 'sub not found'

marks = {
        'c': 85,
        'py': 100,
        'cpp': 95,
        'java': 80
    }

print(sub_marks(marks, 'js'))
print(sub_marks(marks, 'py'))