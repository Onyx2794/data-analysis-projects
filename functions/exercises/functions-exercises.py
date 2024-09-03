# Part 1 A -- Make a Line
def makeline (size):
    line = ""
    for i in range(size):
        line = line + "#"
    return line

print(makeline(5))

# Part 1 B -- Make a Square
# create a function using your make_line function to code a square

def makesquare (size):
    square = ""
    for i in range(size):
        square = square + "\n"
        square = square + makeline(size)
    return square

print(makesquare(5))

# Part 1 C -- Make a Rectangle

def makerectangle (length, height):
    rectangle = ""
    for i in range(height):
        rectangle = rectangle + "\n"
        rectangle = rectangle + makeline(length)
    return rectangle

print(makerectangle(5, 3))





# Part 2 A -- Make a Stairs

def makedownstair (height):
    stairs = ""
    for i in range(height):
        stairs = stairs + "\n"
        stairs = stairs + makeline(i+1)
    return stairs

print(makedownstair(5))

# Part 2 B -- Make Space-Line 

def makespaceline (space, line):
    spaceline = ""
    for i in range(space):
        spaceline = spaceline + " "
    spaceline = spaceline + makeline(line)
    for i in range(space):
        spaceline = spaceline + " "
    return spaceline

print(makespaceline(3, 5))
        


# Part 2 C -- Make Isosceles Triangle

def makeisosceles (height):
    triangle = ""
    for i in range(height):
        triangle = triangle + "\n"
        triangle = triangle + makespaceline((height - i - 1), (2 * i) - 1)
    return triangle
print (makeisosceles(5))

print("\n")


# Part 3 -- Make a Diamond

def makediamond (height):
    diamond = ""
    halfdiamond = makeisosceles(height)
    diamond = halfdiamond + "\n"
    for i in range(len(halfdiamond) -1, -1, -1):
        diamond = diamond + halfdiamond[i]
    return diamond
print (makediamond(5))




