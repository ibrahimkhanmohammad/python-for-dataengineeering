age = input('enter age: ')
if age.isdigit():
    age = int(age)
    if age >= 18:
        print(f'since you are {age} you can vote')
    else:
        print(f'since you are {age} you cannot vote')
else:
    print(f'{age} is invalid age')