color='red'
if color=='green':
    print("You have got 5 points\n")
elif color=='yellow':
    print("You have got 10 points\n")
else:
    print("You have got 15 points\n")

#5-7
favorite_fruits=['banana','apple','orange']
if 'banana' in favorite_fruits:
    print("You really like bananas!\n")

#5-7-1

request_toppings=[]

if request_toppings:
    for request_topping in request_toppings:
        if request_topping == 'green paper':
            print("Sorry,We are out of green papers right now.")
        else:
            print("Adding "+request_topping +".")
    print("\n Finished making your pizza!")

#test
avaliable_toppings=['mushroom','olives','green papers','pepperoni','pineapple','extra cheese']
request_toppings=['mushroom','french fries','extra cheese']
for request_topping in request_toppings:
    if request_topping in avaliable_toppings:
        print("Adding "+request_topping+".")
    else:
        print("Sorry,We don't have "+request_topping+".")
print("\nFinished making your pizza!\n")

#5-8
users=['admin','root','mike','loser','lily']
for user in users:
    if user=='admin':
        print("Hello "+user+" would you like to see a status report?\n")
    else:
        print("Hello "+user+" thank you for your logging in again!\n")

#5-9
users=[]
if users:
    for user in users:
        if user=='admin':
            users.pop()
            print("Hello "+user+" would you like to see a status report?\n")
        else:
            users.pop()
            print("Hello "+user+" thank you for your logging in again!\n")
else:
    print("We need to find some users\n")
    

#5-10
current_users=['Mike','John','Lucy','Lily','Jenny']
new_users=['Mike','Lucy','kite','lucy','phton']
for user in new_users:
    if user in current_users or user.upper() in current_users or user.lower() in current_users or user.title() in current_users:
        print("The user "+user+" has existed!You have to input another user")
    else:
        print("The user "+user+" has not used!")

#5-11
print("\n")
numbers=[val for val in range(1,10)]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")
print("\n")



    



























    
