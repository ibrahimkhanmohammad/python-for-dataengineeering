# Pass by value means a copy of the value is passed to the function. Changes made to the parameter inside the function do not affect the original variable outside the function

#  for immutable objects -> Changes/reassignment inside don't affect outside

def add(x):
    x += 1
    print(id(x))
    print(f'inside function: {x}')


num = 10
print(id(num))
add(num)
print(f'outside function: {num}')
