def user():
    username = input('What is your username?\n')
    password = input('What is your password?\n')
    password_length = len(password)
    password_protected = '*' * password_length

    if len(password) >= 10:
        print(f'{username}, your password {password_protected} is great!')
    elif len(password) == 8:
        print(f'{username}, your password {password_protected} is just the exact characters')
    else:
        print(f'Sorry {username}, your password {password_protected} is not enough')


user()
user()