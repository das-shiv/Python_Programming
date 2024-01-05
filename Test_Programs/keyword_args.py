# Keyword arguments = Allow us to pass arguments in any order while calling a function.

def user(name, age, msg):
    print(f"Hello {name} , you are {age} year old,\nyour message is: {msg}")


user(msg="hello", name= "raju", age=20)

