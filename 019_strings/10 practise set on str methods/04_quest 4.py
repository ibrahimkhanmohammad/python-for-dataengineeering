#   Take a list of names as input (comma separated). Split them, sort them alphabetically, and join them back with " | " as separator.

def fruit(fruits:str):
    fruit_list = sorted(fruits.split(', '))
    fruit_list = ' | '.join(fruit_list)
    return fruit_list

fruits = 'Apple, Cherry, Strawberry, Banana, Amla'
print(fruit(fruits))