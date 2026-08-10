#   without dict comprehension using for loop
squares = {}
for val in range(1, 6):
    squares[val] = val ** 2
print(squares)

#   with dict comprehension
squares = {val: val**2 for val in range(1, 6)}
print(squares)