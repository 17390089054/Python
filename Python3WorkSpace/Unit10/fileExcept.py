dog="dog.txt"
cat="cat.txt"
try:
    with open(dog,"r") as file:
        print("Welcome to visit dog :")
        lines=file.readlines()
        print(lines)
except FileNotFoundError:
    print("File "+dog+" not found!")
try:
    with open(cat,"r") as file:
        print("Welcome to visit cat :")
        lines=file.readlines()
        print(lines)
except FileNotFoundError:
    print("File "+cat+" not found!")

    

