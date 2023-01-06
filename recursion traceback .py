# function
def recursor(): # recursive behavior!
    
    # display message to stdout/stream
    print("I AM RECURSED!")
    
    # return flow conrtols
    return recursor()
    pass

# function call
recursor()