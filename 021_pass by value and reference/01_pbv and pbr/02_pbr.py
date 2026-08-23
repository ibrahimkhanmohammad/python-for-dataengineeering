# Pass by reference means a reference/address of the original variable is passed to the function. Therefore, changes made through the parameter can affect the original variable outside the function

#  for mutable objects -> Mutations inside can affect outside

'''
def add(x):
    x.append(20)
    print(id(x))
    print(f'inside function: {x}')

num = [10]
print(id(num))
add(num)
print(f'outside function: {num}')
'''

# to avoid this we can use deep copy

import copy


def add(x):
    x = copy.deepcopy(x)
    x.append(20)
    print(id(x))
    print(f'inside function: {x}')


num = [10]
print(id(num))
add(num)
print(f'outside function: {num}')
