prompt="\nTell me something ,and I will repeat it back to you:"
prompt+="\nEnter quit to exit the program.\n"
message=""
while message!='quit':
    message=input(prompt)
    if message !='quit':
        print(message)


#method 2
prompt="\nTell me something ,and I will repeat it back to you:"
prompt+="\nEnter quit to exit the program.\n"
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

