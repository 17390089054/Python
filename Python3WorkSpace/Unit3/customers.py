customers=['grandpa','grandma','cousin','sister']
message=" to the party"
print("invite "+customers[0]+message)
print("invite "+customers[1]+message)
print("invite "+customers[2]+message)
print("invite "+customers[3]+message)

print(customers[1]+" can not join the party!")
customers[1]='uncle'
print("The members of the party is:")
print(customers[0])
print(customers[1])
print(customers[2])
print(customers[3])
