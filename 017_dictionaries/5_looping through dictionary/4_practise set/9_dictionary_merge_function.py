#   Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries (d1 and d2) as arguments and returns a new dictionary formed by merging them using the update() method. Ensure d1 remains unchanged.
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

d1 = {'a': 1, 'b': 2}
d2 = {'b': 9, 'c': 3,'d': 5}
print(merge_dicts(d1,d2))