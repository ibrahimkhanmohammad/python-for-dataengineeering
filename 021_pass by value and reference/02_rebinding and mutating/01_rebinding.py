# Rebinding is the process of changing a variable or parameter so that it refers to a different object

def rebinding(x):
    x = [20]
    print(id(x))
    print(f'inside function: {x}')


num = [10]
print(id(num))
rebinding(num)
print(f'outside function: {num}')
