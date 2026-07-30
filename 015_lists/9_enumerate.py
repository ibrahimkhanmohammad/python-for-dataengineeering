fruits = ['apple', 'banana', 'orange', 'strawberry']

for index, value in enumerate(fruits):
    print(f'{index}.{value}')

print()

#   enumerate() with custom starting index

for index, value in enumerate(fruits, start=1):
    print(f'{index}.{value}')

print()


#   to print only indexes with values where the values are even

marks = [24, 40, 39, 85, 48, 24]

for index, values in enumerate(marks, start=1):
    if values % 2 == 0:
        print(f'{index}.{values}')