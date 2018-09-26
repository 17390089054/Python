prompt="\nPlease enter the name of a city you have visited:\n"
prompt+="(Enter quit when you finished!)\n"
while True:
    message=input(prompt)
    if message=='quit':
        break
    else:
        print("I'd like to go to "+message+"!")

