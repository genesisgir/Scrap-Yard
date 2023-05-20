# creating the password variable
password = '12345'

# defining the enter_pass function
def enter_pass():
    
    # conditionals
    while True:
        
        # response variable
        resp = input('enter your password')
        
        if resp == password:
            print('Access granted\n')
            print('You know have access to confidential documents!\n')
            
            break
        
        elif resp != password:
            print('This password is incorrect please try again')
            input('press enter to try again')
    
        elif resp =='123456':
            print('Almost there!')
            pass
        
        else:
            continue    
# function call
enter_pass()