from restaurant import *
class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['sweet','spicy','acid']
    def display_flavors(self):
        print("The flavors of the IceCream:\n")
        for flavor in self.flavors:
            print(flavor)

iceCream=IceCreamStand("重庆鸡公煲","肉食类")
iceCream.display_flavors()
