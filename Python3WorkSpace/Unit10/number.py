import json

# 存储数字
def save_number(filename):
    number=input("Please input your favorite number ?\n")
    try:
        with open(filename,'w') as file:
            number=int(number)
            json.dump(number,file)
    except TypeError:
        print("类型转换错误!")
    except FileNotFoundError:
        print("文件未找到")

#读取数字
def get_number(filename):
    try:
        with open(filename,'r') as file:
            number=json.load(file)
    except FileNotFoundError:
        print("文件尚未找到!")
        return None
    else:
        return number

# 验证程序
def make_program():
    filename="favorite_number.json"
    number=get_number(filename)
    if number:
        print("I know your favorite number!It's "+str(number))
    else:
        save_number(filename)
make_program()






    
