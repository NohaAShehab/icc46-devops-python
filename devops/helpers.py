

def askForInt(message="please enter integer"):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num
        print("-- please enter valid number ")