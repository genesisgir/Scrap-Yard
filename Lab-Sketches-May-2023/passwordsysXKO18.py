# PASSWORD SYSTEM
from typing import Type
import sys

PASSWORD = 'GenesisGir'
text_array = ['ACCESS GRANTED', 'ACCESS DENIED']

def password_sys() -> Type[str]:
    
    # exception handling
    try:
        while True:
            resp = input('Enter the password to the terminal to gain access >>>')

            # conditionals to gain access to system
            if resp.isalpha() and resp == PASSWORD:
                # display to user they gained access to terminal
                return print(text_array[0])
            
            elif resp.isdigit():
                print(resp)
                raise ValueError
            
            elif resp != PASSWORD:
                # display to user they gained access to terminal
                print(text_array[1], '\n')
                continue # re-iterate
            
            else:
                print('Please enter a valid password and try again')
                continue
    
    except:
        print('The password does not contain numbers try again. \n')

password_sys() # run method
sys.exit() # terminate program