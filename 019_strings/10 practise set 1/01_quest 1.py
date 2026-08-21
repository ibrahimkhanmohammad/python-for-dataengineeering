#   Take an email as input. Validate that it contains exactly one @ and at least one .. Print "Valid" or "Invalid"
def check_mail(email:str):
    if email.count('@') == 1 and email.count('.') >= 1:
        return 'Valid'
    return 'Invalid'

email = 'abc.def@gmail.com'
print(check_mail(email))