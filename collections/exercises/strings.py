# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.

print(text[0:12])


# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!

print(text[-12:])


# 3. Print a slice of the middle 12 characters from 'text'.

print(text[int(len(text)/2-6):int(len(text)/2+6)])


# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
x = 0
for x in range(len(word)):
    print(word[x])
    x = x+1



# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
x = 0
drow = ""
for x in range(len(word)-1, -1, -1):
    drow += word[x]
print(drow)


# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
x = 0
droword = ""
while x != "end":
    if x >= 0:
        for x in range(len(word)):
            droword += word[x]
            x += 1
        x = -1
    elif x <= 0:
        droword = droword + " | "
        for x in range(len(word)-1, -1, -1):
            droword += word[x]
        print(droword)
        str(x)
        x = "end"

# Or I could've done this
print(word + " | " + drow)