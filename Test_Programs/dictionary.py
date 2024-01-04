# Dictionary is a unordered key value pair data structure

capitals = {"India":"New Delhi",
            "USA":"Washington DC",
            "Spain":"Madrid",
            "France":"Paris"}

"""
print(capitals)
print(capitals["India"])
print(capitals.get("Germany"))
print(capitals.pop("France"))
capitals.update({"Germany":"Berlin"})
print(capitals)
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.clear()
"""

for key,values in capitals.items():
    print(key,values)
