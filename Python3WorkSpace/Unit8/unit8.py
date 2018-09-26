#8-1 调用函数
def display_message():
    print("We are learning functions")
print("\n")

#8-2 传递实参
def favorite_book(title):
    print("One of my favorite books is "+title.title())

#8-3 位置参数 关键字参数
def describe_pet(animal_type,pet_name):
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

#8-3 位置参数 关键字参数
def describe_pet(pet_name,animal_type='dog'):
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

#8-4 关键字实参 默认实参
def make_shirt(size,font):
    print("The T-shirt's size is "+size+" and the font is "+font)

def make_shirt(size,font='I love Python'):
    print("I want to make a "+size+" T-shirt and the font is "+font)

def make_shirt(font,size='Medium'):
    print("I want to make a "+size+" T-shirt and the font is "+font)

#8-5 城市
def describe_city(ciy,country='China'):
    print(city.title()+" is in "+country.title())

#返回字典
def build_person(first_name,last_name):
	person={'first':first_name,"last":last_name}
	return person
#选择参数输出 
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

#拓展参数
def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person

#8-6
def city_country(city,country):
    full_name=city.title()+","+country.title()
    return full_name

#8-8
def get_albums():
    print("input q for exitting:\n")
    status=True
    while status:
        singer=input("Please input the singer's name:\n")
        if singer=='q':
            break
        album=input("Please input the singer's album:\n")
        if album=='q':
            break
        albums=make_album(singer,album)
        print(albums)
#8-7
def make_album(singer,album):
    albums={"singer":singer,"album":album}
    return albums












































    
    
    

    
