import json

#判断用户名是否存在
def is_user_exists(username):
    filename="username.json"
    try:
        with open(filename,'r') as file:
            lines=file.readlines()
        if lines:
            for line in lines:
                if username==line.rstrip():
                    return True                
            return False
    except FileNotFoundError:
        print("The file is not found!")

#数据存入文件
def get_new_username(username):
    filename="username.json"
    try:
        with open(filename,"a") as file:
            file.write(username+"\n")
    except Exception:
        print("File not found!")

#问候用户
def greet_user():
    username=input("Please input your name:\n")
    if is_user_exists(username):
        print("Hello,"+username)
    else:
        get_new_username(username)
        print("We will wait you come back,"+username.title())

greet_user();

