#FACTORIAL GENERATOR

def factorial(num):
    fact = 1 # Initial value of factorial is set to 1 as fact of 0 and 1 is 1
    if num < 0: # If entered no is negative factorial is not possible
        print("Please enter a positive number")
    elif num == 0 and num == 1: # fact of 0 and 1 is always 1
        return 1
    else:
        for i in range(1,num+1): #  Looping over the range from 1 to the entered number(num+1)
            fact = fact*i # For each iteration we multiply the next number with value of factorial
        print(f"Factorial of {num} is {fact} ") 
        

no = int(input("Enter a number: "))
factorial(no)

