#Set is a collection of unordered, unindexed and unique items.

animals = {"tiger", "lions", "dog"}
birds = {"crow", "parrot", "falcon"}

for i in animals:  #Set is unordered so every time the items will be printed in different order
    print(i)  


#Some methods of set

animals.add("cat")
print(animals)
animals.pop()
print(animals)
#animals.remove("cat")
print(animals.difference(birds)) #shows what is in animals but not in birds

zoo = animals.union(birds)
print(zoo)
