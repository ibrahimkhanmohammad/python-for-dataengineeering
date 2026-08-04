#   Separate a list of integersi into two distinct lists: one containing all the even numbers and the other containing all the odd numbers.
def even_odd(lst):
    even_lst = []
    odd_lst = []
    for el in lst:
        if el%2 == 0:
            even_lst.append(el)
        else:
            odd_lst.append(el)

    print(f"Even List: {even_lst}")
    print(f"Odd List: {odd_lst}")


nums = [1, 2, 4, 6, 7, 17, 9, 10]
even_odd(nums)