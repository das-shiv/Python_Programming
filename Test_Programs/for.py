# For loop iterates over a range of values

import time
start = int(input("Enter the starting number: "))
end = int(input("Enter the end number: "))

for i in range(start,end+1,2):
    print(i)
    time.sleep(0.5)

print("Counting finsihed")

