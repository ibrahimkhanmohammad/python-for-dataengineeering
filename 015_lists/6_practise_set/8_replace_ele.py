#   Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.

def replace_ele(lst):
    n = len(lst)
    for el in range(n):
        if lst[el] < 0:
            lst[el] = 0
    return lst

nums = [ -1, 2, 44, 20, 1, -5, -9, 5]
print(replace_ele(nums))