#   create a list that returns all prime items of  a list
def is_prime(num):
    factors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False

new_list = [i for i in range(2, 101) if is_prime(i)]
print(new_list)
