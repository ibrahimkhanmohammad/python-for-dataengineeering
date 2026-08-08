student = {'name': 'ibrahim','age': 19,'city': 'bvrm'}

#   pop() method removes particular val by using key and return, if not exists then return KeyError
age = student.pop('age')
print(f'popped val is {age}')
print(student)
# student.pop('marks')  #   return error called KeyError
# print(student)

#   so to avoid error we can pass default value like key not exist
marks = student.pop('marks', 'key not exist')
print(marks)
print(student)

#   del method removes particular value and not return and also if mention del variable then it deletes entire variable with values
del student['city']
print(student)
# del student   #   removes entire dictionary as we using del
# print(student)

#   clear() method help to clear every key-value pair and return None and when we print the variable it prints {} empty dictionary
print(student.clear())
print(student)