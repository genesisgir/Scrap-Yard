"""
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 

                        █▀█ █▀▀ █▀▀ █░█ █░░ ▄▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀ █ █▀█ █▄░█ █▀
                        █▀▄ ██▄ █▄█ █▄█ █▄▄ █▀█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█ █ █▄█ █░▀█ ▄█

                                                four digit pin regex
                                    
                                    ⣿⣿⣿⣿⣿⣿⠟⠋⠁⣀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿
                                    ⣿⣿⣿⣿⠋⠁⠀⠀⠺⠿⢿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿
                                    ⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣤⣤⠀⠀⠀⠀⠀⣤⣦⣄⠀⠀
                                    ⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⠏⣿⣿⣿⣿⣿⣁⠀⠀⠀⠛⠙⠛⠋⠀⠀
                                    ⡿⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣰⣿⣿⣿⣿⡄⠘⣿⣿⣿⣿⣷⠄⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⡇⠀⠀⠀⠀⠀⠀⠀⠸⠇⣼⣿⣿⣿⣿⣿⣷⣄⠘⢿⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠁⠀⠀⠀⣴⣿⠀⣐⣣⣸⣿⣿⣿⣿⣿⠟⠛⠛⠀⠌⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⣶⣮⣽⣰⣿⡿⢿⣿⣿⣿⣿⣿⡀⢿⣤⠄⢠⣄⢹⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⣿⣿⣿⣿⣿⡘⣿⣿⣿⣿⣿⣿⠿⣶⣶⣾⣿⣿⡆⢻⣿⣿⠃⢠⠖⠛⣛⣷⠀
                                    ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣮⣝⡻⠿⠿⢃⣄⣭⡟⢀⡎⣰⡶⣪⣿⠀
                                    ⠀⠀⠘⣿⣿⣿⠟⣛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⡿⢁⣾⣿⢿⣿⣿⠏⠀
                                    ⠀⠀⠀⣻⣿⡟⠘⠿⠿⠎⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣵⣿⣿⠧⣷⠟⠁⠀⠀
                                    ⡇⠀⠀⢹⣿⡧⠀⡀⠀⣀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢰⣿⠀⠀⠀⠀
                                    ⡇⠀⠀⠀⢻⢰⣿⣶⣿⡿⠿⢂⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⡏⠀⠀⠁⠀⠀⠀⠀
                                    ⣷⠀⠀⠀⠀⠈⠿⠟⣁⣴⣾⣿⣿⠿⠿⣛⣋⣥⣶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡀

                                    丂ㄖㄩ尺⼕🝗 ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺
                                
Creating a mobile phone number regex and expanding the knowledge on regexes with simple logic to check to see if a mobile number exists,
if not registering a brand new mobile number in a company!

collaborators: MrsgenesisGir
🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
"""

# import module
import re, sys  
# create regular expression
MOBILE_NUMBER_REGEX = re.compile(r'^(\d{3})-(\d{3}-\d{4})$')

# define function
def mobile():
    
    # global
    global mo
    
    
    # open text file and retrive data!
    with open(file=r'Scrap-Yard/Lab-Sketches-May-2023/regexes/MobileNumberregex/mobile.txt', mode='r') as file:
        
        # read the contents of the file and store them in a variable
        mobile_number = file.read()
        file.close

    # search for patterns within string
    mo = MOBILE_NUMBER_REGEX.search(mobile_number)
    
    # exception handling
    try: # check and scan for exceptions
        
        # display number values
        print('The number found was %s' %(mo.group()))
        print('The area code is (%s)' %(mo.group(1)))
        print('The body of the mobile number (%s)' %(mo.group(2)))
        
    
    except: # fix , build code to handle exception

        # create a function to create a mobile number for company
        def create_mobile_number():
            
            # global
            ''' refer to the global var within the global scope'''
            global mo
            global MOBILE_NUMBER_REGEX
            
            # phone logic
            while True:
                
                # prompt user if they would like to create a number
                resp = input('Would you like to create a mobile number? [Y/n] >')
                print()

                # conditionals
                if resp == 'Y':
                    
                    while True:
                        
                        # TODO make a more restricted way to accept a user mobile input.
                        # mobile number creation
                        resp = input('Enter a valid phone number ex.(xxx-xxx-xxxx) must contain two hyphens and no letters. >')
                        print(resp) # ELOC

                        # phone number conditions
                        # must contain numbers, hyphens, 12 characters
                        if len(resp) == 12:

                            # new created user generated mobile number
                            user_created_mobile_number = resp
                            
                            # search for patterns within string
                            mo = MOBILE_NUMBER_REGEX.search(user_created_mobile_number)
                            break # escape the loop
                            
                        else:
                            
                            # display invalid mobile number input
                            print('Whoops try again! enter a valid mobile number it must contain 10 digits, two hyphens ex.(xxx-xxx-xxxx)')
                            continue
                        
                    break
                
                elif resp == 'n':
                    # terminate program
                    print('You chose to not create a mobile number, closing program...')
                    sys.exit()
                
                else: # invalid entry
                    continue
                
        
        # warn user that a number was not found on the file
        print('WARNING: A mobile number was not found in the text file. \n')
        
        # prompt user to create mobile number
        create_mobile_number()

    finally: # output code when all code fixed!
        
        # display number values
        print('The number found was %s' %(mo.group()))
        print('The area code is (%s)' %(mo.group(1)))
        print('The body of the mobile number (%s)' %(mo.group(2)))

# call
mobile()































