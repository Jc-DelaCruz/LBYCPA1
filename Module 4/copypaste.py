def string_rotations(str1, str2):
    # This function checks if the given two strings are rotations of each other
    # Hint: You can use the 'in' operator and string concatenation

    if not (type(str1) is str and type(str2) is str):
        raise TypeError("Inputs are not a valid strings!")

    # YOUR CODE HERE
    if str2 in str1 + str1:
        evaluation = True
    else:
        evaluation = False

    return evaluation # Make sure to assign the result to the evaluation variable

str1 = (input("Input a series of letters and/or numbers: "))
str2 = (input("Input 2nd Letter/Number: "))

evaluation = string_rotations(str1, str2)

print("Rotation: ", evaluation)
