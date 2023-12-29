import time
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("What symbol you want to print?")


print("About to start printing your symbols......")
time.sleep(1)

for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
        time.sleep(0.5)      
    print()
