import random, webbrowser, time, sys

# functions
def ELOC(x: int): # create multiple eloc's with this cloner
    
    # flow controls for loops
    for i in range(0, x): # conditions
    
        print()
        pass
    
    pass

def login(): # displays log-in!
    
    # user credential constants
    USER_NAME = "tenniswaifu"
    PASSWORD = "waifu123"
    
    print("Welcome to the Waifu network database! \n")
    time.sleep(1) # delay program execution by one seconds
    print("Login to your account! \n")
    time.sleep(1) # freeze exe
    
    # username and password prompts
    while True: # Looping statement!
        
        # username prompt
        login_credientials_username = input("What is your user name? > ")
        
        if login_credientials_username != USER_NAME:
            
            print("Incorrect data!") # wrong data! ⚠
            
        else:
            pass
        
        ELOC(1)
        
        # password prompt
        login_credientials_password = input("What is your password? > ")

        if login_credientials_password != PASSWORD:
            
            print("Incorrect data!") # let user know their input was incorrect! ⚠
        
        else:
            pass
        
        ELOC(1)
        
        # flow controls
        if login_credientials_username == USER_NAME and login_credientials_password == PASSWORD:

            print(f"{USER_NAME} has logged in!") # display to user they have logged in!

            sys.exit() # close program at will!
            pass
        
        else:
            
            print("Wrong Data try again") # user input wrong username or password!
            
            ELOC(1)
            
            continue # re-iterate!
            pass



login()