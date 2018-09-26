print("Give me two numbers,and I will divide them.\n")
print("Enter 'q' to quit!\n")
while True:
    first_number=input("First number:\n")
    if first_number == 'q':
        break
    second_number=input("Seconf number:\n")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by 0!")
           
