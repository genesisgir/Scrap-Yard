# in and not in operators

# import modules
import sys

# define function
def waifu_checker(in_name: str, not_in_name: str):
    
    waifus = ["yumi", "lexxi", "mary"]

    # flow control with in and not in!
    # in flow control result
    if in_name in waifus:
        # dialog message to display to user
        print(f"hello {in_name}! \n")
        pass
    else:
        pass
    
    # not in flow control result!
    if not_in_name not in waifus:
        # dialog message to display to user
        print(f"I wish {not_in_name} was here.. \n")
        
        pass
    else:
        pass
    
    # not in flow control result!
    if "mary" in waifus:
        # dialog message to display to user
        print(f"Hello {waifus[2]}! \n")
        sys.exit()# force program to close prematurely (early) 
        pass

    else: # any other outcome
        pass

# function call for waifu checker!
waifu_checker("lexxi", "ishowspeed")