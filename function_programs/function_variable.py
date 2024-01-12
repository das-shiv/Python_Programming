def hello():
    print("Hello")


hello() #This is calling the hello() function
print(hello) #This will print the memory location of hello()

hi = hello #assigning hello to hi variable
hi() # calling the hello() using the hi variable

print(hi) #printing the memory location of hi(), which is same as memory location of hello()