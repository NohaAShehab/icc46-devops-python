
# mys = {True, 34, 'new element', 'Information Technology Institute', 'noha',
#        'Ali', ('test', 10), 23.32, 'Ahmed'}
# print(mys)


def myfun():
    pass

def askForName():
    name = input("please enter your name : ")
    if name.isspace():
        print("--- name must be spaces")
        return False

    return name.upper()

username=  askForName()
print(username)


###########################






# temp= "My name is {0}, I works at {1}, {anyvar}"
# print(temp.format())


print(34,14234,123, sep="-", end="$")
print("hello")






