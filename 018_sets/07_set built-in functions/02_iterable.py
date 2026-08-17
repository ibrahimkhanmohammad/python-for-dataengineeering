#   sets also converts into an iterable functions like tuple and list and vice versa
list_nums = [10, 50, 30, 28, 28, 50]

set_nums = set(list_nums)
print(set_nums)
tuple_nums = tuple(set_nums)
print(tuple_nums)