def checkInput(string):
    if not(type(string) is str and len(string) == 8):
        raise TypeError("Input not a valid string")
    for char in string:
        if not (char == "0" or char == "1"):
            raise ValueError("Strings must contain a '0' or '1' characters only")

# This function performs the logical bitwise NOT on an 8-character string
def bitwise_NOT(string):
    checkInput(string)

    result = str()
    for char in string:
        if char == '1':
            result += '0'
        else:
            result += '1'

    return result

# This function performs the logical bitwise OR on two 8-character strings
def bitwise_OR(string1, string2):
    checkInput(string1)
    checkInput(string2)

    result = str()
    for ch1, ch2 in zip(string1, string2):
            if ch1 == '1' or ch2 == '1':
                result += '1'
            else:
                result += '0'
    return result

# This function performs the logical bitwise AND on two 8-character strings
def bitwise_AND(string1, string2):
    checkInput(string1)
    checkInput(string2)

    result = str()
    for ch1, ch2 in zip(string1, string2):
            if ch1 == '1' and ch2 == '1':
                result += '1'
            else:
                result += '0'

    return result
