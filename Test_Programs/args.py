# THE sys module has different methods like the argv method which is used to pass command line argument while running a program
import sys

#print(f"The name of the program is {sys.argv[0]}")
#print(f"The argument list is {list(sys.argv)}")
prog = sys.argv[0]
name = sys.argv[1]
id = int(sys.argv[2])

print("The name of the program is: ", prog)
print(" Name of the author is :", name, f"Author id is {id}")
