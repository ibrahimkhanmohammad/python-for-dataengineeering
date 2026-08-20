sentence = 'python is powerful and python is crazy language'

#   count() - it counts the total sub str within a str
print(sentence.count('python'))
print(sentence.count('cpp'))

#   find() - it find the least index inside a str where sub str exists, returns -1 if does not exist instead of error
print(sentence.find('is'))
print(sentence.find('python'))
print(sentence.find('cpp'))

#   index() - it is just like find() but return value error if sub str does not exist
print(sentence.index('is'))
# print(sentence.index('cpp'))  returns Value Error

#   replace() - it replaces old sub str with new sub str
print(sentence.replace('python','cpp'))
#   if we want to change only first occurrence or count then mention 1 if both then 2 and so on
print(sentence.replace('python','cpp',1))