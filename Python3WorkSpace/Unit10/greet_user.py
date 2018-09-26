import json

filename="username.txt"
with open(filename) as file:
    username=json.load(file)
    print("Welcome back, "+username+"!")

