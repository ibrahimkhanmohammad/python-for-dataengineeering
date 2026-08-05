#   just like upper triangular matrix, we have to print * in place of lower diagonal
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if i > j:
            print('*', end = ' ')
        else:
            print(matrix[i][j], end = ' ')
    print()