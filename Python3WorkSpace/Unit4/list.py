print("4.3:")
for value in range (1,21):
    print(value)
print("\n")
print("4.4:")
lists=[val for val in  range(1,1000001)]
print(min(lists))
print(max(lists))
print(sum(lists))
print("\n")
#print("4.5:")
#for value in range(1,1000001):
#    print(value)
# print("\n")
print("4.6:")
lists=[value for value in range(1,21,2)]
for val in lists:
    print(val)
print("\n")
print("4.7:")
lists=[val for val in range(3,30,3)]
for value in lists:
    print(value)
print("\n")
print("4.8:")
lists=[value**3 for value in range(1,11)]
for value in lists:
    print(value)
print("\n")
print("4.9:")
lists=[val**3 for val in range(1,11)]
print(lists)


