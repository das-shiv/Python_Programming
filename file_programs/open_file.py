location = input("Enter the full path to the file :")

try:

    with open(location, 'r') as file:
        print(file.read())
except Exception as e:
    print(e)

#print(file.closed)
