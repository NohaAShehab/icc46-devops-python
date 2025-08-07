


name = "Ahmed" # variable with global scope ?
# can be accessed any where in the script

print(name)

name = name.upper()
print(name)


def printName():
    print(f"name = {name}")

printName()





##############################3


def printTrack():
    track = "Devops"  # available in memory while executed function
    # local variable can be accessed only inside the function
    print(f"track name is {track}")

printTrack()
print('--------')
# print(track)

################################################

"modify the global variable from inside the function ??"

name = 'noha'

def modifyname():
    global  name # please dont' create new variable use the global one
    name = "Noha updated"  # I need to use the global one
    print(name)


# modifyname()


######################## function inside a function




# def outerfun():
#     track = 'devops'
#     print(f"track= {track}")
#
#     def innerfun():
#         # inner function can access outer function variables ?
#         print(f"form inner track = {track}")
#     innerfun()
#
# outerfun()


### modify local variable from inside inner the function

def outerfun():
    track = 'devops'
    print(f"track= {track}")

    def innerfun():
        track = "DEVOPS TRack"  # new local variable for the inner
        # inner function can access outer function variables ?
        print(f"form inner track = {track}")
    innerfun()
    print(f"track= {track}")

outerfun()

print("-------------------------------------------------")
def outerfun2():
    track = 'devops'
    print(f"track= {track}")

    def innerfun():
        # use the variable of the parent ?
        nonlocal track  # plz don't create new local one , use the one in the parent
        track = "DEVOPS TRack"
        # inner function can access outer function variables ?
        print(f"form inner track = {track}")
    innerfun()
    print(f"track= {track}")

outerfun2()












