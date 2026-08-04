#   create a list of [1, 2, 3....9, 20]

#   approach - 1 (traditional way)
new_list = []
for el in range(1, 11):
    new_list.append(el)
print(new_list)

#   approach - 2 (by using list comprehension (lc))
new_list = [el for el in range(1, 11)]
print(new_list)

result = [el for el in range(10, 0, -1)]
print(result)