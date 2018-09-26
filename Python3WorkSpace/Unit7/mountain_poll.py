responses={}
polling_active=True
while polling_active:
    name=input("Please input your name:\n")
    response=input("Which mountain would you like to climb someday?\n")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(Yes/No)\n")
    if repeat == 'No':
        polling_active=False
print("\n--Poll result")
for name,response in responses.items():
    print(name.title()+"would like to climb "+response)
