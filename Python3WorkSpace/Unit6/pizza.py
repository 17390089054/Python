#存储所点pizza的信息
pizza={"crust":"thick","toppings":['mushrooms','extra cheese']}

#概述所点pizza
print("Your ordered a "+pizza['crust']+"-crust pizza "+"with the following toppings:")
for topping in pizza['toppings']:
    print("\t"+topping)
