players = (("Messi", 55, 25), ("Neymar", 35, 30), ("Ronaldo", 40, 20))


#name = lambda names: names[0]
goal = lambda goals: goals[1]  
sorted_list = sorted(players,key=goal) # the sorted function is calling the goal lambda function to find the sorting key, sorted function is passing each item of the tuple to the lambda function and lambda function returns the 2nd item in each item. 

print(sorted_list)


'''
sorted(players, key = goal)
sorted function passes each item in players tuple to goal lambda function,
so it will pass ("Messi", 55,25) ("Neymar",35,30) and ("Ronaldo",40,20) to the lambda function

now in goal = lambda goals: goals[1]

here goals will be set to ("Messi", 55,25) , ("Neymar",35,30) and ("Ronaldo",40,20) as argument
and : goals[1] will find out each tuples index 1 value.

'''