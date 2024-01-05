# Exceptions = Any event that prevents the normal execution of a program.
try:
    num = float(input("Enter the numerator: "))
    den = float(input("Enter the denominator: "))
    result = num/den
    print(result)

except ZeroDivisionError as e:
    print(e)
    print("Can not divide a number by zero")
except Exception as e:
    print(e)
    print("Please only enter non zero numbers.")

finally:
    print("This message from finally block will run always")






    