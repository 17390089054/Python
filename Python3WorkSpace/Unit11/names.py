from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first=input("\nPlease give me a first name:\n")
    if first =='q':
        break
    second=input("Please give me a last name:\n")
    if second=='q':
        break
    formatted_name=get_formatted_name(first,second)
    print("\tNeatly formatted name: "+formatted_name+" .")
    
