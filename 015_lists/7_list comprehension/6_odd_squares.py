#   create a list of returning the squares of odd elements of a list
def odd_squares(lst):
    return [el ** 2 for el in lst if el % 2 != 0]

# nums = list(range(1, 11))
nums = [el for el in range(1, 11)]
print(odd_squares(nums))