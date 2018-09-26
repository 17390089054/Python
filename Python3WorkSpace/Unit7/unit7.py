#7-4
prompt="Please input pizza ingredient\n"
prompt+="(Enter quit if you want to stop)\n"
while True:
    message=input(prompt)
    if message == 'quit':
        break
    else:
        print("Adding "+message.title()+" into the pizza \n")
#7-5
prompt="please input your age:\n"
while True:
    age=input(prompt)
    age=int(age)
    if age<0:
        break
    elif  age <3:
        fee=0
        print("The fee is "+str(fee))
    elif age <=12:
        fee=10
        print("The fee is "+str(fee))
    elif age >12:
        fee=15
        print("The fee is "+str(fee))
print("\n")



