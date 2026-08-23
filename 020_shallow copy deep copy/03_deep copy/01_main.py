# Deep copy: creates a new outer object and recursively creates new nested objects too
import copy

original = [1, 2, 3, [4, 5, 6], 98, 100]
deep = copy.deepcopy(original)

print(id(original)) # 1557483267008
print(id(deep)) # 1557485490432

deep[3][2] = 55
print(deep) # [1, 2, 3, [4, 5, 55], 98, 100]
print(original) # [1, 2, 3, [4, 5, 6], 98, 100]