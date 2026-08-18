user_input = input("Type 'yes' or 'no': ")  #   user may type 'YEs', 'YES', or nothing

if user_input.lower() == 'yes':
    print('Confirmed')
elif user_input.lower() == 'no':
    print('Cancelled')
else:
    print('Invalid input')