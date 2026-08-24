def calculate(a: int, b: int) -> int:
    return a + b


x = calculate(5, 5)
print(x)


# if we do not return something then use -> None or just leave like that
def calculation(a: int, b: int) -> None:
    print(a + b)


calculation(10, 20)
