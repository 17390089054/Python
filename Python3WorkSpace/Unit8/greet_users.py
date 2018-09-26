def greet_users(names):
    for name in names:
        msg="Hello, "+name.title()+"!"
        print(msg)
usernames=['hanaha','ty','margot']
greet_users(usernames)
