# *args = It is used to pass any number of arguments to a function, it creates a tuple of the arguments passed.
# We can name it anything other *args, * is mandatory , e.g. *items, *values, *numbers etc.

def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i

    return sum 


print(addition(1,2,3,4,34,5.45))