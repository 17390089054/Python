import json

# 如果以前存储了用户名,就加载它
# 否则,就提示用户输入用户名并存储它
# 查询是否存在用户名
def get_sorted_username():
    filename="username.json"
    try:
        with open(filename) as file:
            username=json.load(file)
    except FileNotFoundError:
        return None
    else:
      return username
#没有用户名则创建它
def get_new_username():
    username=input("What is your name?\n")
    filename="username.json"
    with open(filename,'w') as file:
        json.dump(username,file)
    return username        
         


def greet_user():
    username=get_sorted_username()
    if username:
        print("Welcome back,"+username+"!")
    else:
        username=get_new_username()
        print("We will remember you when you come back, "+username+"!")

greet_user()


    
        

    
