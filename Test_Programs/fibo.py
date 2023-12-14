#FIBONACCI SERIES

def fibo(num):

    n1,n2,count = 0,1,1 # 1st and 2nd number of fibo series is 0,1 count is set to 1
    if num <= 0: # Check the length of the series, negative length is not possible
        print("Enter a positive number")
    
    elif num==1: # Fibo series of length 1 is 0
        print(n1)

    else:
        print(n1, end=" ") #Print the 1st number of series i.e 0
        print(n2, end=" ") # Print the 2nd nu of the series, now the series is 0 1
        while (count<num): # We need to print the series starting from 1 till the entered value num
            next = n1+n2 # Calculate the next value in series, which is sum of previous two
            print(next, end=" ") # We print the next value in series , now the series looks like 0 1 next (for 1st iteration)
            n1 = n2 # we move one step next in the series and now n1 value becomes n2
            n2 = next # next value is now the value of n2
            count = count+1 # we increase the count value by 1
        
        print()
        print(f"The fibonacci of {no} is {next}")
        


while True:

    no = int(input("Enter the length of the fibonacci series: "))

    fibo(no)
