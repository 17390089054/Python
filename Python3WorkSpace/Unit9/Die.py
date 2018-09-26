from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        x=randint(1,self.sides)
        return x

print("6 sides Die follows(10 times):\n")
die=Die()
for i in range(1,11):
    x=die.roll_die()    
    print(x)

print("10 sides Die follows(10 times):\n")
die=Die(10)
for i in range(1,11):
    x=die.roll_die()    
    print(x)

print("20 sides Die follows(10 times):\n")
die=Die(20)
for i in range(1,11):
    x=die.roll_die()    
    print(x)
    
