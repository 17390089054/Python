import json

filename='number.json'
with open(filename,"r") as file:
    numbers=json.load(file)
print(numbers)
