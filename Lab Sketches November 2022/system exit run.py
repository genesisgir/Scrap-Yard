# exception names

import sys

try:
    
    raise sys.exit()

except SystemExit:
    
    print("An error has caused the program to act erractic, would you like to close the program?")

    resp = input("y/n >")
    
    if resp =="y": # user decides to close application early.
        
        sys.exit()
        pass
    
    elif resp == "n": # user decides to let program fix issues!
        
        pass