alien={"x_position":0,"y_position":25,"speed":"medium"}
#向右移动外星人
print("Original x-position:"+ str(alien['x_position']))

#根据移动速度决定其移动多远
if alien['speed'] == 'slow':
    x_increment=1
elif alien['speed'] == 'medium':
    x_increment=2
else:
    x_increment=3

print("x_position:"+str(alien['x_position']+x_increment))


#6-1
person={"first_name":"July","last_name":"Herb","age":18,"city":"Mexio"}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
print("\n")

#6-3
game={"July":1,"Mike":4,"John":18,"Smith":45,"Lucy":6}
print("July "+str(game["July"]))
print("Mike "+str(game['Mike']))
print("John "+str(game['John']))
print("Smith "+str(game['Smith']))
print("Lucy "+str(game['Lucy']))

#6-4
game={"July":1,"Mike":4,"John":18,"Smith":45,"Lucy":6}
for name,value in game.items():
    print(name+" "+str(value))

print("\n")
#6-5
river={"nile":"egypt","Amaza River":"Amaza","Yangtze River":"China"}
for name,value in river.items():
    print("The "+name.title()+" runs through "+value.title())
    print(name.title())
    print(value.title())
print("\n") 
#6-6
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
list=['sarah','phil']
for name, language in favorite_languages.items():
    if name in list:
        print(name.title()+",thank you for joining us!")
    else:
        print(name.title()+",We are waitting for you to join!")
print("\n")














