location = input("Enter the location of the file: ")
text = input("Enter the text you want to add to the file: ")
with open (location, 'a') as file:
    file.write(text + "\n")

file.closed

'''
file modes
r = read  (default mode)
w = write (will replace text)
a = append (will append the text)
'''