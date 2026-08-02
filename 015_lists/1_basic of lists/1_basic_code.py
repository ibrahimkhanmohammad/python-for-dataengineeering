#   creating a list:

names = ['Ibrahim','Mohammad', 'Firdous', 99, 100.123, True]

print(names)
print(type(names)) #    to know the names variable datatype
print(len(names))

#   list operations: +, *:

marks = [1,2,3,4,5]
marks2 = [6,7,8,9,10]

#   + -> joins two lists and return new list
combined = marks + marks2
print(combined)
print(marks) #  the original list doesn't undergoes any affect

#   * -> repeats the list items by multiplier times, as multiplier should be in integer only
repeated = marks * 3
print(repeated)
print(marks) #  the original list doesn't undergoes any affect