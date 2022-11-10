
"""
████████╗███████╗███╗░░██╗███╗░░██╗██╗░██████╗░██╗░░░░░░░██╗░█████╗░██╗███████╗██╗░░░██╗
╚══██╔══╝██╔════╝████╗░██║████╗░██║██║██╔════╝░██║░░██╗░░██║██╔══██╗██║██╔════╝██║░░░██║
░░░██║░░░█████╗░░██╔██╗██║██╔██╗██║██║╚█████╗░░╚██╗████╗██╔╝███████║██║█████╗░░██║░░░██║
░░░██║░░░██╔══╝░░██║╚████║██║╚████║██║░╚═══██╗░░████╔═████║░██╔══██║██║██╔══╝░░██║░░░██║
░░░██║░░░███████╗██║░╚███║██║░╚███║██║██████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║██║░░░░░╚██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═╝░░░░░░╚═════╝░

Working with for loops and while loops and making Equivalent for loops with while loops as well and testing out
the capabilities with how the 'in' keyword works as well as the range() function. 

                        ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
                        ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
                        ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
                        ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄ 'tennis' in 'tenniscourt'   
                        ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰  True
                        ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤    
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗  '1' in 'There was 1 magical blade in my hand.'
                        ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄   True   
                        ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
                        ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄   'loser' in 'waifu'
                        ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄    False
                        ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
                        ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
                        ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
                        ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿


"""
""" 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 🆃🅴🅽🅽🅸🆂 """

# list for loop, in keyword, range() sketch 

# variable containing a list value with 3 items! 
relic = ["Old TV", "Shiny Stone", "Pearl"]

# flow control
#for index in range(len(relic)):
    
#    print(str(index) + " is the index for the item " + relic[index])
#    pass

#i = None

# flow control
#for i in range(1, 4):
    
#    print("testing")
#    pass

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - -  - - - - - - - - - - - - - - 

# creating an Equivalent for loop with a while loop!

# import module
#import time

# variable that contains an integer!
#i = 0

#while i < 10: # Equivalent for loop!
    
#    print("I wish to be a for loop!")
    
#    time.sleep(1) # delay program execution
    
#    i += 1
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - -  - - - - - - - - - - - - - - 

# Health system using a Equivalent for loop with a while loop !

# import module
#import time

# variable that contains an integer!
#health = 10

#while health >  0: # Equivalent for loop!
    
#    print("You took some uber damage and lost 1 health!")
    
#    time.sleep(1) # delay program execution
    
#    health -= 1
    
#print("You have died!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - -  - - - - - - - - - - - - - - 

# hunger system using a Equivalent for loop with a while loop !

# import module
import time
import sys

# variable that contains an integer!
damage = 0
hunger = 100


while hunger > 0: # Equivalent for loop!
    
    # define functions
    def Hunger_loss(x: int): # damages users hunger in real-time!
        
        # reference variables from global scopes!
        global damage 
        global hunger 
        
        # deduct hunger and track damage int!
        damage = damage + 1
        hunger -= x
        pass
    
    def Hunger_replenish(x: int): # damages users hunger in real-time!
        
        # deduct hunger and track damage int!
        hunger = 100
        pass
    
    def notice():
        # Notify user of damage!
        print("Some seem to be getting hungry! -1 hunger!")
        pass
    
    
    
    # tell user about how much damage they took!
    notice()
    time.sleep(0.1) # delay program execution
    
    # deduct hunger!
    Hunger_loss(1)
    
    
    
    # flow control!
    if hunger == 50: # user hunger reaching dangrous levels!
        
        print("You are beginning to starve! Get some food or you will die!")
        
        pass
    
    elif hunger == 20: # when user hits 20 hunger level!
        
        print(f"You feel yourself about to pass out your at your hunger level {hunger}")
        
        pass
    
    elif hunger == 1: # hunger recover prompt!
        # prompting user to eat bread!
        resp = input("You are about to die would you like to eat bread? y/n > ")
        print()
        
        # flow control
        if resp == "y": # user chooses to eat!
            
            #recover user hunger to defeault to 100!
            Hunger_replenish
    
            print("You chew into the fluffy piece of bread and your hunger is recovered! \n")
            
            time.sleep(1)
            
            print("You walk back home to your wife and children. . \n")
            
            input("Press enter")
            
            sys.exit()
            pass
        
        elif resp == "n": # user decides to die!
            
            print("You decide to die a noble hungry man! Bread isn't your thing. \n")
            
            time.sleep(1)
            
            print("Your eyes closes softly. . \n")
            
            time.sleep(1)
            
            print("You have died!")
            
            input("Press Enter!")
            
            sys.exit() # program terminates
            pass
        
        
        pass
    
