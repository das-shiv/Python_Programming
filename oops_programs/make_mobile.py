from mobile import Mobile

mobile1 = Mobile("Motorola", "G73", "Black", 2023)

print(mobile1.mobile_type) # Accessing a class variable
mobile1.specs()
mobile1.calling()
mobile1.messages()
mobile1.email()
mobile1.gaming()


mobile2 = Mobile("iphone", "iphone 15", "white", 2023)
print("-----------------------------------------------")

mobile2.mobile_type = "keypad"

mobile2.specs()
mobile2.calling()
mobile2.messages()
mobile2.email()
mobile2.gaming()
