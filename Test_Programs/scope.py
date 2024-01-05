# scope of a variable is the part of the code in which the variable is accessible 

name = "Global name"  # Global variable is accessible from anywhere within the module

def local_variable():
    name = "Local variable" # Local variable defined with in the function is only accessible inside the function.
    print(name)  # Local variable will be printed, if it is not present then the global variable will be used.

print(name) # Global variable will be printed.
local_variable() # Local variable will be printed, if it is absent then global variable will be printed.


'''
Precedence order of variable:
Local, Enclosed , Global, Built-in (LEGB)
'''
