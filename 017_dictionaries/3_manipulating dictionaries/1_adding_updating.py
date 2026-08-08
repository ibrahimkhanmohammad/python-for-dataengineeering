student = {'name': 'ibrahim','age': 19,'city': 'bvrm'}

#   adding key-value pairs
student['phn'] = 123
print(student)

#   updating existing value by using key
student['age'] = 20
print(student)

#   better approach by using .update() method we can actually pass multiple key-value pairs all at once without writing again and again each time
student.update({'gender': 'male', 'phn': 789})
print(student)