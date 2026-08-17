#   enumerate is less useful in set as it is helpful in other data types, but we can still perform operation on sets
fruits = {'apple', 'banana', 'cherry', 'kiwi'}

for index, fruit in enumerate(fruits, start = 1):
    print(f'{index}. {fruit}')