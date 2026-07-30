#   find maximum in alist without using built-in max() function

nums = [10, -2, 15, 8, -7, 6]
maxi = float('-inf')

for num in nums:
    if num > maxi:
        maxi = num

print(f'Maximum number is {maxi}')