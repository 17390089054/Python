fileName='C:\\Users\\knight\\Desktop\\Unit10\\data1.txt'
try:
    with open(fileName) as file_object:
        contents=file_object.read()
        print(contents.strip())
except FileNotFoundError:
        print("Sorry,"+fileName.title()+" not found!")

print("read in line\n")
with open(fileName) as file:
    for line in file:
        print(line.strip())#默认有换行的空白

