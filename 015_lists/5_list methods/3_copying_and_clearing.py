nums = [10, 20, 30]

#   .copy()     creates a shallow copy of original list, if we not want to do changes in an original list, we can learn further in future
updated_nums = nums.copy()
updated_nums.append(100)
print(nums)     # [10, 20, 30]
print(updated_nums)     # [10, 20, 30, 100]

#   .clear()    clears the entire list by removing every element, but it does not delete the list, instead do an empty list
nums.clear()
print(nums)