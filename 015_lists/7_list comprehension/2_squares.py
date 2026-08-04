#   traditional approach
squares = []
for el in range(1, 6):
    squares.append(el ** 2)
print(squares)

#   by using list comprehension (lc)
squares = [el ** 2 for el in range(1, 6)]
print(squares)