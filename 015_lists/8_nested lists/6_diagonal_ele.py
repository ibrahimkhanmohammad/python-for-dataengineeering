#   print only diagonal elements of a matrix, and remaining as *'s
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i == j:
            print(matrix[i][j], end = ' ')
        else:
            print('*', end = ' ')
    print()