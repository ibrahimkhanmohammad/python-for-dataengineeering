#   in a list, remove all duplicate elements while preserving the original order of unique elements
def remove_duplicates(lst):
    result = []
    for el in lst:
        if el not in result:
            result.append(el)
    return result

nums = [1, 5, 4, 4, 6, 4, 8, 1, 0, 5]
print(remove_duplicates(nums))