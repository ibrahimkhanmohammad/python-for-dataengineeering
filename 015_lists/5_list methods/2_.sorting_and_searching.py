nums = [10, 50, 40, 65, 85, 20, 40]

#   sorting and reversing -> .sort() , .sort(reverse = True) , .reverse()

#   .sort()     sort in ascending order in place, it doesn't return or create new list unlike sorted built in function
nums.sort()
print(nums)

#   .sort(reverse = True)    sort in descending order in place
nums.sort(reverse=True)
print(nums)

#   .reverse()    reverse the original list but not perform asc or desc operation
nums.reverse()
print(nums)

#   searching and counting -> .index() , .count()

#   .index()    it finds the element index of the list, if not present throws an error, and also it returns so we can directly use inside print
print(nums.index(50))

#   .count()    it counts the element occurrence in a list, if  not 0, and also it returns so we can directly use inside print
print(nums.count(50))
print(nums.count(40))
print(nums.count(60))