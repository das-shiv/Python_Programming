import time
num = int(input("Enter the number you want to count: "))
start = 1
while num >= start:
    print(start)
    time.sleep(1)
    start = start + 1
print("Counting is finished")

