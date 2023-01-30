# doc string example!

# import modules
import sys

# be aware of global and local scopes!
# define functions
def x():
    # doc str 
    """returns GenesisGir's name using a return statement"""    
    return "GenesisGir"
    pass

def xy():
    # doc str 
    """Terminates and closes program with the sys.exit() function!"""
    
    return sys.exit()
    pass

def init():
    # doc str 
    """initiate program with this function to start it idk."""
    # shows the docmentaion of the functions created
    help_me()

    # store function within the y variable!
    y = x
    
    return print(x), xy()
    pass

def help_me():
    # doc str 
    """ help() on documentaion on functions"""
    
    # globals
    global x
    global y
    
    # variables
    x = print(help(x))
    y = print(help(xy))
    
    
    return x, y
    pass

# program begins
init()
