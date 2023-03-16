"""

            ░██████╗███████╗███╗░░██╗██████╗░██████╗░████████╗██████╗░░█████╗░░██████╗██╗░░██╗░░██╗██╗░░
            ██╔════╝██╔════╝████╗░██║██╔══██╗╚════██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║░░██║░██╔╝╚██╗░
            ╚█████╗░█████╗░░██╔██╗██║██║░░██║░░███╔═╝░░░██║░░░██████╔╝███████║╚█████╗░███████║██╔╝░░╚██╗
            ░╚═══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░░░░██║░░░██╔══██╗██╔══██║░╚═══██╗██╔══██║╚██╗░░██╔╝
            ██████╔╝███████╗██║░╚███║██████╔╝███████╗░░░██║░░░██║░░██║██║░░██║██████╔╝██║░░██║░╚██╗██╔╝░
            ╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░╚═╝╚═╝░░


Using send2trash is much safer than Python’s regular delete functions, because it will send folders and files to your computer’s trash 
or recycle bin instead of permanently deleting them. If a bug in your program deletes something with send2trash you didn’t intend to delete,
you can later restore it from the recycle bin.
"""

# import modules
import send2trash, os, sys, pathlib, random, subprocess
import pyinputplus as pyip
import cProfile, time

# change cwd
os.chdir('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\send2trash')

# trash creator method
def create_trash(trash_name: str = 'trash', message_contents: str ='I am trash, woe is me...'):
    
    # create some text file trash logic
    with open(file='%s.txt' %(trash_name), mode='w') as f:
        f.write('%s' %(message_contents))

# garbage collector method
def garbage_collector(trash_path: str = ''):
    """ # garbage_collector()
    asks user to create trash, recycle it, open recycle bin or exit.
    """
    
    # garbage collector option iterator
    while True:
        # garbage collector options
        option = ['Create txt file trash', 'Recycle some trash', 'Open recycle bin', 'Exit garbage collector']
        
        # user input
        response = pyip.inputMenu(prompt='Garbage Collector v1.0.0 \n', choices=[option[0], option[1], option[2], option[3]], numbered=True)
        print()
        
        # logic condtionals
        if response == option[0]: # create trash
            
            # trash file name
            trash_filename = input('What would you like to name the trash? \n')
            print()
            
            # trash message contents
            trash_contents = input('What should the trash message contain, not like it matters anyway right? \n')
            print()
            
            #  generate some trash
            create_trash(trash_name=trash_filename, message_contents=trash_contents)
            continue
            pass
        
        elif response == option[1]: # recycle trash
            
            # trash path prompt
            
            trash_path = input('Enter the absoloute path of the trash you wish to obliterate. \n')
            print()
            
            # recyle message array
            recycled_messages = (
                '%s has been sent to the recycling bin to be burned, exploded and tortured for all etern-..no?' %(trash_filename),
                '%s has been sent to the recycling bin.' %(trash_filename),
                '%s has been recycle bin and await\'s your choice to be deleted forever. ' %(trash_filename))
            
            # display user a random recycle message
            print(random.choice(recycled_messages), '\n')
            
            # send trash to local machine recycle bin
            send2trash.send2trash(trash_path)
            
            continue
            pass
        
        elif response == option[2]:
            
            # set admin privilages to file
            os.chmod(path='C:\$Recycle.Bin', mode=0o777)
            
            #subprocess.Popen('C:\\Windows\\System32\\example.exe') works for normal executables
            subprocess.run(["explorer.exe", "shell:RecycleBinFolder"]) # normal/special executables
            continue
        
        elif response == option[3]: # exit garbage collector v1.0.0
            break # exit garbage collector
        
        else:
            print()
            continue # iterate
    
    print('Thank you for using garbage collector v1.0.0! \n')
    
    # display
    print(cProfile.run('create_trash()'))
    return sys.exit() 

# garbage collector v1.0.0
garbage_collector()

