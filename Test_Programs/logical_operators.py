#It checks if two or more conditional statements are true.

temp = float(input("What is the temperature outisde? "))

if temp > 35:
    print("The weather is really hot outside, carry an umbrella")

elif temp >= 15 and temp <= 35:
    print("The weather is nice, enjoy the weather ")
elif temp <= 15 and temp > 0:
    print("It's really cold outisde, don't forget to wear your jacket")
elif temp == 0 or temp < 0:
    print("The temperature is freezing, better stay inside")
else:
    print("Enter a valid temperature")
