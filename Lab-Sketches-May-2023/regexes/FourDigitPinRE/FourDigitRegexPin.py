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
                                
more regex practice sketches, the last sketch I was trying to figure out a way to intake multiple regexes infinitely but failed due to not 
wanting to rework it right than and there this should be a reminder to take slow careful steps with production and not to rush things.
production is a marathon not a sprint.

🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 🅶🅴🅽🅴🆂🅸🆂 
"""
# define pin method
def pin():

    """
    # pin() method
    A function that reads pin data from text files and if one is not found user may create heir own pin with the system
    """
    
    # module imports
    import re, time, random
    
    # read pin data from file
    with open(file=r'C:\Users\daint\Documents\GitHub\Scrap-Yard\Lab-Sketches-May-2023\regexes\FourDigitPinRE\pin.txt', mode='r') as f:

        # read data from file and store it
        pin = f.read()
        pass

    # regex patterns
    four_digit_pin_regex = re.compile(r'^(\d{4})$')

    # search the match object from data
    match_object = four_digit_pin_regex.search(pin)

    # some exception handling
    try:
        # set False the pin found in file not user crteated
        user_created_pin = False
        
        # display text
        print('A regex pattern was localized! [pin:%s] make sure to goto the file path in case you forget the pin!' %(match_object.group()))
        print(r'file location: C:\Users\daint\Documents\GitHub\Scrap-Yard\Lab-Sketches-May-2023\regexes\FourDigitPinRE\pin.txt')
        print('now closing program!...')
        time.sleep(random.randint(a=1,b=2))

    except:
        
        # pin not found on file exception 
        print('WARNING!: A valid pin was not found in the file! \n')
        
        # pin prompt logic
        while True:
            # retrieve user input
            resp = input('Would you like to create your own pin? [Y/n] >')
            print()
            
            # condtions
            if resp == 'Y':
                
                # set True due to user created pin
                user_created_pin = True
                
                # user creates pin
                while True:
                    
                    # U/I
                    resp = input('Enter a four digit pin >') # user enters a pin response
                    print()

                    if len(resp) == 4 and resp.isdecimal:

                        # create user generated pin
                        pin = resp
                        break # escape loop
                    
                    else:
                        print('Enter a valid four digit pin and use only numbers not letters! \n\n' )
                        continue # re-iterate

    finally:
        
        if user_created_pin == True:
            
            # display final pin information to user
            print('Success the pin you have created is (%s)! Write this down to not forget it. \n' %(pin))
        
        elif user_created_pin == False:
            pass
        
        else:
            pass

# call func
pin()
