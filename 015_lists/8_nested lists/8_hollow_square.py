#   print a matrix with the center elements replaced by *
matrix = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
rows = len(matrix)
cols = len(matrix[0])

for i in range(0, rows):
    for j in range(0, cols):
        if (i * j) % 3 != 0:
            print('*', end = ' ')
        else:
            print(matrix[i][j], end = ' ')
    print()