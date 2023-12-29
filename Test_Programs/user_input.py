# User input in python is taken using input() function
name = input("Enter your name: ")
age = int(input("How old are you: "))
print(f"Hello {name}, \nIt's nice to meet you")

if age >= 18:
    print("You are eligible to cast a vote in the election")
else:
    print("You are not old enough to cast a vote in the election")

