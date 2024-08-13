# 1. Declare and assign the variables here:
shuttle = "Determination"
mph = 17500
distMars = 225000000
distMoon = 384400
mpk = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(shuttle))
print(type(mph))
print(type(distMars))
print(type(distMoon))
print(type(mpk))

# Code your solution to exercises 3 and 4 here:
mtma = 0.0
mtma = distMars * mpk

htma = 0.0
htma = mtma / mph

dtma = 0
dtma = htma / 24

dtma = str(dtma)
print(shuttle + " will take " + dtma + " days to reach Mars.")

# Code your solution to exercise 5 here

mtmo = 0.0
mtmo = distMoon * mpk

htmo = 0.0
htmo = mtmo / mph

dtmo = 0
dtmo = htmo / 24

dtmo = str(dtmo)
print(shuttle + " will take " + dtmo + " days to reach the moon.")