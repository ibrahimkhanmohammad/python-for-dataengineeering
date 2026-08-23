original = [1, 2, 3]
copy = original
copy.append(100)
print(copy)
print(original)

#   they both are same because '=' does not work with mutable objects, and it is called reference copy because it copies address

#   for proof - as addresses same we can say that it just update no matter what we do because it is mutable objects
print(id(copy))
print(id(original))

print(original is copy) # it gives boolean value if addresses are same
print(original == copy) # it gives boolean value if values are same (as addresses are same then values are also same)

a = [4, 5, 6]
b = [4, 5, 6]

print(a is b)
print(a == b)