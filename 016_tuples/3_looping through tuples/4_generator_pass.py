nums = (10, 20, 30, 40, 50)
#   iterating over a generator
for el in (x for x in nums):
    print(el, end=' ')