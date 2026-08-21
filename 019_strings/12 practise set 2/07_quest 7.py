#    Take a string as input. Check if it is a valid Indian PAN card number. Format: 5 uppercase letters + 4 digits + 1 uppercase letter (Total 10 characters). Example: ABCDE1234F

def validity_pan(pan_id:str):
    if (len(pan_id) == 10
        and pan_id[:5].isupper()
        and pan_id[:5].isalpha()
        and pan_id[5:9].isdigit()
        and pan_id[9].isupper()
        and pan_id[9].isalpha()):
        return 'Valid'
    else:
        return 'Invalid'
pan_id = input("Enter PAN ID: ")
print(validity_pan(pan_id))
