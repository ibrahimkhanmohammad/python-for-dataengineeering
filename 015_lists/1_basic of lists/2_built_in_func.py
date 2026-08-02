marks = [41, 24, 85, 96, 36, 75]
print(marks)

#   len() - to find the length of the list
size = len(marks)
print(size)

#   sum() - to find the sum of the elements in a list
total = sum(marks)
print(total)

#   min() - to find minimum element in a list
mini = min(marks)
print(mini)

#   max() - to find maximum element in a list
maxi = max(marks)
print(maxi)

#   sorted() - returns the new list, but does not affect the original list, i.e; original list remains unchanged, by sorting it in ascending order
asc_sorted = sorted(marks)
print(asc_sorted)
print(marks)

#   for descending sorted order list
desc_sorted = sorted(marks, reverse=True)
print(desc_sorted)
print(marks)

#   practical usage of builtin func

#   to calculate average marks

average = sum(marks) / len(marks)
print(f'average: {average:.2f}')