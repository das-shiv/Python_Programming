# slice = var[start:stop:step]

name = "lionel messi"

first_name = name[0:6]
print(first_name)
last_name = name[7:]
print(last_name)
funny_name = name[0:12:2]
print(funny_name)

reversed_name = name[::-1]
print(reversed_name)

# Using the slice function, slice = slice(start,stop,step)

website = "http://www.google.com"
website2 = "http;//www.wikipedia.com"
slice = slice(11,-4)
print(website[slice])
print(website2[slice])
