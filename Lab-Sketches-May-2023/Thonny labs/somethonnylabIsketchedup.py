# consts
THONNY = 'Thonny dude'
GENESISGIR = 'GenesisGir'

# start here

# GenesisGir dialogue
print('Hello thonny how are you?')
input('press [enter]')

# Thonny dialogue
print('%s: I\'m doing okay and you %s?' %(THONNY, GENESISGIR)) # str interpolation to insert the 'Thonny name into the string'


# conversation logic
while True:
    
    # users input to thonny
    reply = input('Eneter your reply to the fucking Thonny guy >>>')
    print()



    # condtionals
    if reply = 'Good':
        
        
        # Thonny dialogue
        print('%s: Thats nice to hear! catch you later!' %(THONNY)) # str interpolation to insert the 'Thonny name into the string'
        
        
    elif reply == 'bad':
        
        # Thonny dialogue
        print('%s: Sorry to hear that goodbye!' %(THONNY)) # str interpolation to insert the 'Thonny name into the string'
        
    else:
        continue # re-iterate
        pass













