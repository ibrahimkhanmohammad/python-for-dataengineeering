# Type Conversion
my_set = {5, 5, 2, 4, 5, 5, 6, 5, 'xyz', 'abc', 99.99, 5}
print(list(my_set)) #   the duplicates removed because set does not hold any duplicate values it contains only unique values

my_list = [54, 65, 43, 32, 32, 3, 43, 43, 43, 43]
print(list(set(my_list)))