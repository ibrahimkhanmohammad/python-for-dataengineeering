#   print min and max elements of a list without using min() and max() built-in functions

#   approach - 1
def smallest_greatest(lst):
    s = sorted(lst)
    return s[0], s[-1]


nums = [10, 40, -5, 20]
print (smallest_greatest(nums))


#   approach - 2
def smallest_greatest(lst):
    mini, maxi = float('inf'), float('-inf')
    for el in lst:
        if el < mini:
            mini = el
        if el > maxi:
            maxi = el
    return mini, maxi


nums = [10, 40, -5, 20]
print (smallest_greatest(nums))
