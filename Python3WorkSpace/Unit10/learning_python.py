fileName="learning_python.txt"
with open(fileName) as file:
    print(file)
    lines =file.readlines()
    print(lines)

str=''
for line in lines:
    str+=line
print(str)
