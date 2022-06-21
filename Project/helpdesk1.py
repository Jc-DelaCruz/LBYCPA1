import shutil

def help_desk(select):
    columns = shutil.get_terminal_size().columns
    if select == "3":
        seperator1 = "="*30
        with open("FAQs.txt") as file:
                FaQs = file.read()
        print("Welcome to the CpE Help Desk!".center(columns))
        print(seperator1.center(columns))
        print("✯ ✯ FAQs ✯ ✯".center(columns))
        print(seperator1.center(columns))
        print(FaQs)
    return "✯ ✯ ✯ ✯ ✯".center(columns)
    
print(help_desk("3"))