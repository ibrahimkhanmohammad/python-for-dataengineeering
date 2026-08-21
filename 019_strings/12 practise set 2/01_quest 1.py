#   Take a username as input. Strip any spaces from both sides and check if the cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid"

def username_check(username:str):
    clean_name = username.strip()
    if clean_name[0].isdigit():
        return 'Invalid'
    return 'Valid'

username = input('enter username: ')
print(username_check(username))