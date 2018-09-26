class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("The restaurant_name is "+self.restaurant_name+" and the cuisine_type is "+self.cuisine_type)
    def open_restaurant(self):
        print("The restaurant is openning!")
    def set_number_served(self,number):
        self.number_served=number
        print("The number of restaurant is "+str(self.number_served))
    def increment_number_served(self,increment):
        self.number_served+=increment
        
restaurant=Restaurant("聚源小炒","餐饮")
#print("The restaurant's name is "+restaurant.restaurant_name +" and the type of it is "+restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("The people served "+str(restaurant.number_served)+"\n")
restaurant.number_served=10
print("The people served "+str(restaurant.number_served)+"\n")
restaurant.set_number_served(20)
restaurant.increment_number_served(10);
print("The people served "+str(restaurant.number_served)+"\n")

