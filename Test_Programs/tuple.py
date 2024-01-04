# Collection of ordered elements, immutable

emp = ("josh", 1223, 25)
print(emp)

for i in emp:
    print(i)

print(emp.count(25))  #Counts occurence of 25
print(emp.index(1223)) # Display the index of 1223

if "josh" in emp:
    print("josh is here")
else:
    print("josh is not here")
