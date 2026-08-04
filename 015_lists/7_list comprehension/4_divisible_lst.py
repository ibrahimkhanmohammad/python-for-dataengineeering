#   create a list which is divisible by both 3 and 5
divisible_lst = [el for el in range(1, 31) if el % 3 == 0 and el % 5 == 0]
print(divisible_lst)

divisible_lst = [el for el in range(1, 31) if el % 3 == 0 or el % 5 == 0]
print(divisible_lst)
