import os

location = input("Enter the full path you want to check: ")

if os.path.exists(location):
    print("The location exists")
    if os.path.isfile(location):
        print("This is a file")
    elif os.path.isdir(location):
        print("This is a directory")
        
else:
    print("This location does not exists.")