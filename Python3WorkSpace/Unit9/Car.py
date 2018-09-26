class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_description_name(self):
        long_name=str(self.year)+" "+self.make+" "+self.model
        return long_name.title()
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
    def read_odometer(self):
        print("The car has "+str(self.odometer_reading)+" miles on it.")
        
my_car=Car("audi",'a4',2016)
print(my_car.get_description_name())
my_car.read_odometer()
my_car.odometer_reading=23
my_car.read_odometer()
my_car.update_odometer(2005)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()
