# break stops the execution of a loop , while continue skips the iteration and goes to next iteration
import time
start = int(input("Enter the starting number: "))
end = int(input("Enter the end number: "))
skip = int(input("Enter the number you want to skip: "))
stop = int(input("Enter the break number:" ))

for i in range(start,end+1):
    if i == skip:
        continue
    elif i == stop:
        break
    else:
        print(i)
        time.sleep(0.5)
        i = i+1

print("Counting finished....")
