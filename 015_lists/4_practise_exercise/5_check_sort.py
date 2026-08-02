def check_sort(lst):
    n = len(lst)
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            return False
    return True


nums  = [10, 20, 30, 40, 50]
nums2 = [90, 20, 30, 40, 50]

print(check_sort(nums))
print(check_sort(nums2))