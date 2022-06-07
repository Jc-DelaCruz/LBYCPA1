def greet(name):
    """ Greets the <name>
    """
    if type(name) is not str:
        name = str(name)
    print("Greetings, " + name + "! " + "How are you today?")

def goodbye(name):
    """Says goodbye to <name>
    """
    if type(name) is not str:
        name = str(name)
    print("Goodbye " + name + ". Have a nice day ahead!")

def closing(name):
    if type(name) is not str:
        name = str(name)
    print("\n\n", name, "EQ1 - 12195758")
