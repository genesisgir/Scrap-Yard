# a test .py to see if try and except clauses have their own local scopes

""" 𝖙𝖊𝖓𝖓𝖎𝖘𝖜𝖆𝖎𝖋𝖚 𝖈𝖗𝖚𝖈𝖎𝖆𝖑 𝖒𝖔𝖉𝖚𝖑𝖊𝖘 𝖎𝖒𝖕𝖔𝖗𝖙 𝖕𝖗𝖊𝖘𝖊𝖙 """
import sys # Access system-specific parameters and functions
import time # Time access and conversions



# exception handling
try: # check for abnormalites
    
    name = int(input("Whats your age? > "))
    
    if name != str.isalnum():
        raise ValueError
        pass
        
    else:
        pass 
    
    pass
    

    

except ValueError as x: # resolve abnormalites
    
    x.add_note("it wont work idk")
    x.add_note("you must have broke something!")
    pass


