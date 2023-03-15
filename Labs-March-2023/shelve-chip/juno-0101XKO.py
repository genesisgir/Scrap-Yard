# import modules
import sys, os, pathlib, shelve
import pyinputplus as pyip

# directory path
dir_path = 'C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\shelve-chip'

# change cwd
os.chdir(dir_path)

# create shelve obj
shelf_password_file = shelve.open(filename='password-data')

# password creation 
def create_password():
    """
    Create a password for user.
    """
    
    # password creation prompt
    while True:

        # user creates password
        password = pyip.inputPassword('Create a password \n')
        
        # write password data to shelve object
        shelf_password_file['password'] = password
        
        #  save &close the shelve file
        shelf_password_file.sync()
        shelf_password_file.close()
        
        print() # blank line
        print('Password %s has been created and saved' %(password))
        break # escape loop

# login w/password
def login_prompt():
    """
    Login with shelved password in db.
    """
    
    # globals
    global shelf_password_file
    
    # re-open shelve file
    shelf_password_file = shelve.open(filename='password-data')
    
    # login prompt
    while True:
        
        # prompt user for password
        r = pyip.inputPassword('Login with the password \n')

        # condtionals
        if r == shelf_password_file['password']:

            # print login success to screen/stream!
            print('access granted!')
            
            # close shelve file
            shelf_password_file.close()
            sys.exit() # exit program

        elif r != shelf_password_file['password']:

            # print denied login to screen/stream!
            print('access denied!')
            continue
        
        else: 
            continue # re-iter

# password prompt logic
def password_prompt():
    """ # password_prompt()
    Gives the user the choice to create a password or login into the system.
    """
    
    while True:
        
        # ask user if they would like to create a password or login
        r = pyip.inputMenu(prompt='What would you like to do? \n', 
                        choices=['Create a password', 'Login into the system'], 
                            numbered=True)
        
        print() # blank line
        
        # user option conditions
        if r == 'Create a password':
            # user creates password and saves that into a shelve file
            create_password()
        
        elif r == 'Login into the system':
            # user enters the login prompt
            login_prompt()
        
        else:
            continue# re-iter
            pass
        
# program starts
password_prompt()