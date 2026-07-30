#   return true if target exist in the list, if not then return false

def target_val(lst, target):
    for num in lst:
        if num == target:
            return True
    return False

nums = [10, 9, -5, 7, -3, 6]
print(target_val(nums, 10))
print(target_val(nums, -1))
