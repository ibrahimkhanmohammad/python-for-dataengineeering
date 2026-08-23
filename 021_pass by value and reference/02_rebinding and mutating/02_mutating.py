# Mutation is the process of changing the contents or state of an existing mutable object without making the variable refer to a different object

def mutate(x):
    x[0] = 5
    print(id(x))
    print(f'inside function: {x}')


num = [10, 20]
print(id(num))
mutate(num)
print(f'outside function: {num}')
