#   creation of 2d list which is 3 x 3 matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print(type(matrix))

#   accessing elements of 2d lists
print(matrix[0])
print(matrix[2])
print(matrix[1][0])
print(matrix[2][1])
print(matrix[0][2])

#   to access everything
for i in range(3):
    for j in range(3):
        print(matrix[i][j], end = ' ')
    print()

