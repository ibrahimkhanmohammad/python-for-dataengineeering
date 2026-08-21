#   Clean Phone Number Take a phone number as input in the format +91-98765-43210. Remove all dashes and the country code. Print the cleaned 10-digit number.
def phone(number:str):
    clean_number = number.replace('-','').replace('+91','')
    return clean_number

number = '+91-98765-43210'
print(phone(number))