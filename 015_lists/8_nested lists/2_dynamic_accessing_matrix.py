#   to access every item more dynamically irrespective of any order of matrix
from email.contentmanager import raw_data_manager

matrix = [[8, 5, 6, -2],
          [-4, 5, 9, 1],
          [5, 2, 3, 6]]

rows = len(matrix)  #   as rows indicate total len of matrix
cols = len(matrix[0])   #   as cols indicate len of cols so basically we can use len(matrix[0]) or len(matrix[1]) or and so on because of same order

#   to access items of the matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end = ' ')
    print()