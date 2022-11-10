# return statements and functions!

"""
████████╗███████╗███╗░░██╗███╗░░██╗██╗░██████╗░██╗░░░░░░░██╗░█████╗░██╗███████╗██╗░░░██╗
╚══██╔══╝██╔════╝████╗░██║████╗░██║██║██╔════╝░██║░░██╗░░██║██╔══██╗██║██╔════╝██║░░░██║
░░░██║░░░█████╗░░██╔██╗██║██╔██╗██║██║╚█████╗░░╚██╗████╗██╔╝███████║██║█████╗░░██║░░░██║
░░░██║░░░██╔══╝░░██║╚████║██║╚████║██║░╚═══██╗░░████╔═████║░██╔══██║██║██╔══╝░░██║░░░██║
░░░██║░░░███████╗██║░╚███║██║░╚███║██║██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║██║░░░░░╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═╝░░░░░░╚═════╝░

Once the program execution hits a return statement within a function it evaluates to what ever it's next to!
this can be super helpful when functions begin to get really complex with intricate pathways. The function terminates
once a return statement is reached.

                        ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
                        ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
                        ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
                        ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄ EVALUATE PLEASE!
                        ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
                        ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤    RETURN STATEMENTS RULE!
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
                        ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄         RETURN AWESOMENESS!
                        ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
                        ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
                        ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
                        ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
                        ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
                        ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
                        
"""

# creating a function that handles parameters (hello function)
def hello(person: str, parameter_amount: int):
    
    # flow controls
    if person == "TennisWaifu":
        
        return print(f"Hello {person} you have created {parameter_amount} function!")
        pass
    
    elif person == "GenesisGir":
        
        return print(f"Hello {person} you have created {parameter_amount} function!")
        pass
    
    print("Go fuck yourself")
    
    pass # pass this line of code/do nothing! 

# creating another function that handles parameters (goodbye function)
def goodbye(username: str, parameter_int: int):
    
    # flow controls
    if username == "TennisWaifu":
        
        return print(f"Hello {username} you have created {parameter_int} function!")
        pass
    
    elif username == "GenesisGir":
        
        return print(f"Hello {username} you have created {parameter_int} function!")
        pass
    
    print("Return statements suck I dont need them lol")
    
    
    pass
    
    

hello("TennisWaifu", str(1))
goodbye("GenesisGir", str(1))
