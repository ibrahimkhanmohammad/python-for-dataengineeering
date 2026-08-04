#    Create a list containing the squares of numbers from 1 to 10 (i.e., [1, 4, 9, ... , 100]).

#   approach - 1
result = []
for el in range(1, 11):
    result.append(el ** 2)

print(result)


#   approach - 2
def square_lst(lst):
    new_lst = []
    for el in lst:
        new_lst.append(el ** 2)
    return new_lst


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(square_lst(nums))

#   these two approaches are not good way to write code, so further we can optimize and learn concepts called list comprehension in future