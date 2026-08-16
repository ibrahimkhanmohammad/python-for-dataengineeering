def user_check(sett, user_name):
    if user_name in users:
        return(f'Access granted to Mr {user_name}')
    else:
        return(f'Access denied to Mr {user_name}')

users = {'Aizen', 'Ichigo', 'Yhwach'}
print(user_check(users,  'Aizen'))
print(user_check(users,  'Asta'))
