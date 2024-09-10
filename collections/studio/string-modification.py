my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

mynew_string = my_string[0:3]
mynew_string = my_string[3:] + mynew_string

# Use a template literal to print the original and modified string in a descriptive phrase.

print("Original string was {0}, new string is {1}.".format(my_string, mynew_string))

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

letter_request = input("How many letters would you like to move to the end?\n")
letter_request = int(letter_request)
errortype = "none"
if letter_request > len(my_string):
    print("Error. Letter request too large. Exceeds string index.")
    errortype = "'exceeds index'"
    mynew_string = my_string[0:3]
    mynew_string = my_string[3:] + mynew_string
    print("Result is {0} due to error {1}. Defaulted to 3.".format(mynew_string, errortype))
else:
    mynew_string = my_string[0:letter_request]
    mynew_string = my_string[letter_request:] + mynew_string
    print(mynew_string)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
