filename='pi_digits.txt'

with open (filename) as file:
    lines =file.readlines()
print(lines)
pi_string=''
for line in lines:
    pi_string+=line.strip()

birth=input("Please input your birthday:\n")
if birth in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
    
print(pi_string[:20]+"...")
print(len(pi_string))
