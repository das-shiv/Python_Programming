import random

num_int = random.randint(1,6)
print(num_int)

num_float = random.random()
print(num_float)


cards = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","ACE"]
random.shuffle(cards)
print(cards)
