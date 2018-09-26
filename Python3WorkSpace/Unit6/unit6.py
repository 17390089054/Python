#6-7
print("6-7")
user0={"name":"hello","age":15,"sex":"男"}
user1={"name":"nuli","age":18,"sex":"女"}
user2={"name":"meizu","age":21,"sex":"男"}
people=[user0,user1,user2]
for user in people:
    print(user['name'])
    print(user['age'])
    print(user['sex'])
print("\n")

#6-8
print("6-8")
cat={"type":"cat","owner":"John"}
dog={"type":"dog","owner":"Lily"}
snake={"type":"snake","owner":"mike"}
wolf={"type":"wolf","owner":"lucy"}
turtle={"type":"turtle","owner":"shelly"}
pets=[cat,dog,snake,wolf,turtle]
for pet in pets:
    print("type:"+pet['type']+" owner:"+pet['owner'])
print("\n")

#6-9
print("6-9")
favorite_places={"lucy":"Beijing","John":"TianJin","Mike":"Wuhan"}
for name,place in favorite_places.items():
    print(name+"'s favorite place is "+place)   
print("\n")

#6-10
print("6-10")
person={
        "lucy":{2,5,9,4},
        "mike":{4,9,7,8},
        "lily":{1,4,6,2}
        }
for name,numbers in person.items():
    print(name.title()+"'s favarite number is:")
    for number in numbers:
        print(number)
print("\n")

#6-11
print("\n")
cities={
"Beijing":{"country":"China","population":"1.4billion","fact":"the capital of China"},
"NewYork":{"country":"USA","population":"35million","fact":"the capital of USA"},
"London":{"country":"UN","population":"15million","fact":"the capital of UN"}
}
for city,info in cities.items():
    print(city+":\n"+"\tcountry:"+info["country"]+"\n\tpopulation:"+info['population']+"\n\tfact:"+info['fact'])
print("\n")






