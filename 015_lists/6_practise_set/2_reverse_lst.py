#   reverse the list without using .reverse() and list slicing [::-1]
def reverse_list(lst):
    n = len(lst)
    new_list = []
    for el in range(n - 1, -1, -1):
        new_list.append(lst[el])

    return new_list


nums = [10, 40, -5, 20]
ans = reverse_list(nums)
print(ans)