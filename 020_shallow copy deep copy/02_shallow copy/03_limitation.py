# As shallow copy creates a new outer object, but nested objects are still shared and affect with original

import copy

original = [[1, 2, 3], 98, 99, 100]
shallow = copy.copy(original)

print(id(shallow))
print(id(original))

# for outer object
shallow[3] = 999
print(shallow)  # [[1, 2, 3], 98, 99, 999]
print(original) # [[1, 2, 3], 98, 99, 100]

# for nested object
shallow[0][2] = 99
print(shallow) # [[1, 2, 99], 98, 99, 999]
print(original) # [[1, 2, 99], 98, 99, 999]
