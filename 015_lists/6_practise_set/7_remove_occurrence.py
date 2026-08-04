#   Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurrences of that integer from the list.

#   approach - 1 with new list
def remove_dup(lst, target):
    if target not in lst:
        print("Please enter again, the element does not exist.")
        return lst

    new_lst = []

    for el in lst:
        if el != target:
            new_lst.append(el)

    return new_lst


nums = [1, 5, 4, 6, 5, 4, 5, 6, 2, 3]
print(remove_dup(nums, 5))


#   approach - 2 in original list
def remove_occurrence(lst, target):
    while target in lst:
        lst.remove(target)
    return lst

nums = [1, 5, 4, 6, 5, 4, 5, 6, 2, 3]
print(remove_occurrence(nums, 5))