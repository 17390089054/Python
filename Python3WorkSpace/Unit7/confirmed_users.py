unconfirmed_users=['Mike','Alice','Shelly','Python']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("\nVerifying user: "+ current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users are have benn confirmed:\n")
for confirmed_user in confirmed_users:
    print(confirmed_user)
    
    
