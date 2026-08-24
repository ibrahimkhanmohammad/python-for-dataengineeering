def max_marks(marks: list[int]) -> int:
    return max(marks)


print(max([10, 20, 50]))

#  if we want items with both str and int then:
def print_lst(lst: list[int | str]):
    print(lst)


print_lst([10, 20, 'asta'])