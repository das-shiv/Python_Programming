# **kwargs = allow to pass arguments in key order format and stores in a dictionary, ** is compulsory.

def greet(**kwargs):
    print(kwargs) # prints the kwargs dictionary
    print("Hello ",end=" ")
    for key,value in kwargs.items():  #iterates over a kwargs dictionary
        print(value,end=" ")


greet(title="Mr." ,first="Guido",middle = "van", last = "Russom")