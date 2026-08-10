marks = {'mat' : 85, 'sci' : 92, 'eng' : 60, 'soc' : 45}

#   keep only marks which are > 80
top_marks = {sub : mark for sub, mark in marks.items() if mark > 80}
print(top_marks)

#   transform into or double the marks
doubled_marks = {sub : mark*2 for sub, mark in marks.items()}
print(doubled_marks)