#   always sorted function return in the form of lists irrespective of any data type, so to convert it into a tuple we have tuple() constructor
nums = (40, -5, 60, 91, 33)
sorted_tup = (sorted(nums))
print(sorted_tup)
print(sorted(nums, reverse=True))
#   it does not affect the original tuple by the way
print(nums)

#   use tuple() constructor when we want to change the sorted function answer into a tuple way rather than in list
sorted_tup = tuple(sorted_tup)
print(sorted_tup)