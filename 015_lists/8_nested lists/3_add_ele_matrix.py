#   adding each and every item of a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

total = 0
for i in range(3):
    for j in range(3):
        total += matrix[i][j]

print(total)