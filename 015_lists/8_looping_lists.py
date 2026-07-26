marks = [13, 24, 21, 20, 95, 87, 67]
print(marks)

for num in marks:
    print(num, end=' ')

print()

i = 0
while i < len(marks):
    print(marks[i], end=' ')
    i += 1

print()

for num in marks[::-1]:
    print(num, end=' ')

print()

count = 0
for num in marks:
    if num % 2 == 0:
        count += 1
print(count)



i , count = 0, 0
while i < len(marks):
    if marks[i] % 2 == 0:
        count += 1
    i+=1
print(count)

total = 0
for num in marks:
    total += num
print(total)

print(sum(marks))