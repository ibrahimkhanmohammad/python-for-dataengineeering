#   print upper triangular matrix and it should print * in upper diagonal like [[1, *, *],[4, 5, *],[7, 8, 9]]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        if i >= j:
            print(matrix[i][j], end = ' ')
        else:
            print('*', end = ' ')
    print()