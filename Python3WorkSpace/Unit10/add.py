msg="please input two words:(Enter 'q' to exit)"
while True:
    print(msg)
    try:
        first=input("please input your first number?\n")
        if first =='q':
            break
        first=int(first)
        second=input("please input your second number?\n")
        if second =='q':
            break
        second=int(second)
    except ValueError:
        print("Your input was wrong!")       
    else:
        print("The total result is:"+str(first+second))
