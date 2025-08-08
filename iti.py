
# print("----------- welcome to ITI module -----------------")
track = 'DEVOPS'

def askForName(message="Please enter name: "):
    while True:
        name = input(message)
        if name.isalpha():
            return  name
        print("please enter valid name ")


# username = askForName()



# I need to write some code --> for default call, testing ??
# every .py file has its main ? __name__='__main__'
"""
I need to add some lines ?? called only when I run this file ??
"""
if __name__ == '__main__':
    "when the file calling entry point is this file "
    print("---- running ITI module")
    print('track')
    print(track)