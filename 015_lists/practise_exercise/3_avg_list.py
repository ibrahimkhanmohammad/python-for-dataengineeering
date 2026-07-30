#   calculate avg using len() and without sum()

def calc_avg(nums):
    total = 0
    for num in nums:
        total+=num
    avg = total / len(nums)
    return avg

nums = [10, -8, 5, 6, -7, -1, 4]

ans = calc_avg(nums)
print(f'Average is {ans:.3f}')