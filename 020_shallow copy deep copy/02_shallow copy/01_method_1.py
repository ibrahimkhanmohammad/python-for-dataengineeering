# method - 1

original = [1, 2, 3]
shallow = original.copy()

print(id(original))
print(id(shallow))

shallow.append(5)
print(shallow)
print(original)