#   Accept a string as input. Print its reverse using string slicing.

def reverse_name(naam):
    return naam[::-1]

name = input('username: ')
print(reverse_name(name))