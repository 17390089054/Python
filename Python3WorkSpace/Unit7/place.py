responses={}
polling_active=True
while polling_active:
    name=input("please input your name\n")
    response=input("If you can visit one place,where would you like to go?\n")
    responses[name]=response
    repeat=input("Would you like to invite another people to join?(yes/no)\n")
    if repeat == 'no':
        polling_active=False

print("Here are the result for polling:")
for name,response in responses.items():
    print(name.title()+"Would like to go to "+response)
