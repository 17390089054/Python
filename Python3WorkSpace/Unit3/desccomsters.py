customers=['grandpa','grandma','cousin','sister']
customers.insert(0,"ant")
customers.insert(2,"prince")
customers.append("wife")
print("I'am so sorry! The table can not be sent timely,So I have to only invite two people to join the party!")
c1=customers.pop()
print("I'am so sorry,"+c1+" You have to go now!")
c2=customers.pop()
print("I'am so sorry,"+c2+" You have to go now!")
c3=customers.pop()
print("I'am so sorry,"+c3+" You have to go now!")
c4=customers.pop()
print("I'am so sorry,"+c4+" You have to go now!")
c5=customers.pop()
print("I'am so sorry,"+c5+" You have to go now!")
print("Congratulations,"+customers[0]+" You are still invited!")
print("Congratulations,"+customers[1]+" You are still invited!")
del customers[1]
del customers[0]
print(customers)


