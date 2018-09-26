status=True
while status:
    name=input("Please input your name(Enter 'q' to exit the program):\n")
    if name =='q':
        status=False
    else:
        print("Hello ,"+name.title())
        with open('guests.txt','a') as file:
            file.write("Hello,"+name.title()+"!\n")

    
