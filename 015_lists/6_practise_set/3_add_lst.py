#   add tow lists without modifying original lists

#   approach - 1
def add_lists(lst1, lst2):
    return lst1 + lst2

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]

print(add_lists(nums1, nums2))


#   approach - 2
def add_lists(lst1, lst2):
    new_lst = []
    for el in lst1:
        new_lst.append(el)
    for el in lst2:
        new_lst.append(el)
    return new_lst

nums1 = [11, 22, 33]
nums2 = [44, 55, 66]

print(add_lists(nums1, nums2))