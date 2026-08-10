marks = {'math' : 45, 'sci' : 46, 'chem' : 42, 'py' : 49}

#   it sorts alphabetically
print(dict(sorted(marks.items(), key=lambda x:x[0])))
#   now it sorts base on the marks of students
print(dict(sorted(marks.items(), key=lambda x:x[1])))

