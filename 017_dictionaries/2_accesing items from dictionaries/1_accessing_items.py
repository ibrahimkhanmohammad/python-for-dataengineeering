marks =  { 'name': 'ibrahim',
          'python': 98,
          'java': 85,
          'cpp': 95,
          'c': 90 }
print(marks)

#   to access items in dicts we use keys unlike indexes
print(marks['python'])
print(marks['c'])
# print(marks['js'])  #   it throws an error as KeyError as key 'js' does not exist

#   so we can use get method instead of printing by  using key like
print(marks.get('cpp'))
print(marks.get('java'))
print(marks.get('ruby'))  #   it will return None as default if key does not exist, we can change default None to 0 or -1  like
print(marks.get('swift', -1))