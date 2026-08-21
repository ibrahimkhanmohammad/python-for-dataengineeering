#   strip methods are of 3 types and it removes extera white space in a text which helpful for data cleaning, they are of:
#   strip(), lstrip(), rstrip()

#   strip() - remove leading and trailing white spaces from a string
greet = '    Hello World     '
clean = greet.strip()
print(clean)
print(len(clean))

#   lstrip() - removes leading white spaces from a string
greet = '    Hello World     '
clean = greet.lstrip()
print(clean)
print(len(clean))

#   rstrip() - remove trailing white spaces from a string
greet = '    Hello World     '
clean = greet.rstrip()
print(clean)
print(len(clean))