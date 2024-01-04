# Functions =  A block of code that gets executed when it is called.
# return = It returns a value/object to the caller
'''
def greetings():
    name = input("Enter your name: ")
    print(f"Hello {name}, the Greetings function has answered to your summons")


greetings()
'''

def add(name, a, b):
    s = a+b
    print(f"Hello {name}, the sum of {a} and {b} is: {s}")



add("shiv",5,6)
 
 
 
def multi(a,b):
   return a*b

multiplication = multi(5,4)
print(multiplication)
