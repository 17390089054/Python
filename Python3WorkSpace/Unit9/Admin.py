from User import *

class Privileges():
    def __init__(self):
         self.privileges=['can add post','can delete post','can ban user']

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privilege=Privileges()
        
    def show_privileges(self):
        for privilge in self.privilege.privileges:
            print(privilge)

admin=Admin("Harry","Potter")
admin.show_privileges()
