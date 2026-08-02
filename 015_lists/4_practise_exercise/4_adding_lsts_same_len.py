def add_lsts(lst1, lst2):
    new_lst = []
    n = len(lst1)
    for i in range(n):
        total = lst1[i] + lst2[i]
        new_lst.append(total)
    return new_lst


nums1 = [10, 5, -4, -9, 1]
nums2 = [-4, 5 , 6 ,-3, 4]
print(add_lsts(nums1, nums2))