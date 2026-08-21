#   Write a function is_palindrome(text) that returns True if the given string is a palindrome (ignoring case and spaces)

def is_palindrome(text:str):
    text = text.lower().replace(' ','')
    if text == text[::-1]:
        return True
    return False


print(is_palindrome('No pain no gain'))
print(is_palindrome('never Odd or even'))
print(is_palindrome('Race Car'))
