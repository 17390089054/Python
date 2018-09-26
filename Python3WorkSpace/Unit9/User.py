class User():
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
    def describe_user(self):
        full_name=self.first_name+" "+self.last_name
        print("The full_name is:"+full_name)
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
    def greet_user(self):
        print("Hello,"+self.first_name+" "+self.last_name)
user=User("Harry","Potter")
user.describe_user()
user.greet_user()
user.increment_login_attempts()
print("User login_attempts:"+str(user.login_attempts))
user.increment_login_attempts()
print("User login_attempts:"+str(user.login_attempts))
user.increment_login_attempts()
print("User login_attempts:"+str(user.login_attempts))
user.reset_login_attempts()
print("User login_attempts:"+str(user.login_attempts))



