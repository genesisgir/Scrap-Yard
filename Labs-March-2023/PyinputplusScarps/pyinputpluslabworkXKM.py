"""



                ██████╗░██╗░░░██╗██╗███╗░░██╗██████╗░██╗░░░██╗████████╗██████╗░██╗░░░░░██╗░░░██╗░██████╗
                ██╔══██╗╚██╗░██╔╝██║████╗░██║██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗██║░░░░░██║░░░██║██╔════╝
                ██████╔╝░╚████╔╝░██║██╔██╗██║██████╔╝██║░░░██║░░░██║░░░██████╔╝██║░░░░░██║░░░██║╚█████╗░
                ██╔═══╝░░░╚██╔╝░░██║██║╚████║██╔═══╝░██║░░░██║░░░██║░░░██╔═══╝░██║░░░░░██║░░░██║░╚═══██╗
                ██║░░░░░░░░██║░░░██║██║░╚███║██║░░░░░╚██████╔╝░░░██║░░░██║░░░░░███████╗╚██████╔╝██████╔╝
                ╚═╝░░░░░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚══════╝░╚═════╝░╚═════╝░
                                            ⼕ㄖᗪ🝗 ⻏丫 Ꮆ🝗𝓝🝗丂讠丂Ꮆ讠尺
                                            
pyinputplus is a 3rd party module that was created by al sweigart to take different forms of inputs than the standard library built-in one
as we all know and love 'input()', It comes with tons of user input types ranging from password input types that hide the password as you type 
it, boolean inputs, choicemenu inputs, address inputs, email inputs and more.


"""

# TODO add more input types

# imports
import pyinputplus

# methods
def password_prompt():
  
  ## password constant
  PASSWORD = 'lave123'
  
  # password prompt
  while True:
    resp = pyinputplus.inputPassword('Enter your password >')

    # password conditional
    if resp == PASSWORD:

      print('access granted!')
      break

    elif resp != PASSWORD:

      print('access denied!')
      continue

    else:
      continue

def input_bool():
  
  # inputbool prompt
  while True:
    resp = pyinputplus.inputBool(prompt='Are you hungry? >')

    # bool conditional
    if resp == True:

      print('You are hungry and you get fed!')
      break

    elif resp == False:

      print('You are not hungry')
      break

    else:
      continue

# pyinputplus inputchoice
def choices():
  
  type = ['waifu programmer', 'normal programmer']
  
  while True:
    
    # user input choice
    resp = pyinputplus.inputChoice(prompt='What type of programmer are you?', choices=[type[0], type[1]])
    
    # display choice to stdout
    print(resp)

# pyinputplus inputmenu
def choice_menu():
    
    # programmer list
    programmer = ['waifu programmer', 'normal programmer']
    
    while True:

      # user input choice menu
      resp = pyinputplus.inputMenu(prompt='What type of programmer are you? \n ', numbered=True, choices=[programmer[0], programmer[1]])

      if resp == programmer[0]:
        
        print("You like waifu's I see?")
        break # escape the loop
      
      elif resp == programmer[1]:
        print("Just an average programmer I see.")
        break
      
      else:
        pass # do nothing

# pyinputplus email input
def email_input():
  
  while True:
    # user email input
    resp = pyinputplus.inputEmail(prompt='Enter a valid email address \n')

    # user's email var
    email = resp

    # email condtionals
    if email == 'genesisexample@gmail.com':

      print("The email was genesisexample@gmail.com! \n" )
      break # escape loop

    else:
      print('Input the correct email, Invalid entry. \n')
      continue # re-iterate

# pyinputplus date input
def date_input():
  
  # iterator
  while True:
    
    # date input
    resp = pyinputplus.inputDate(prompt='Set the date \n')
    
    # set date
    current_date = resp
    
    # display to user the current date they have set
    message = print("Today's date is %s" %(current_date))
    break
  
  return message

# pytinputplus ip address input
def ip_input():
  """ # ip_input()
  stores fake ip address's that user inputs into a text file
  """
  
  # iterator loop
  while True:
    
    # store IP logic
    while True:
      # user ip input
      resp = pyinputplus.inputIP(prompt='Enter a IPv4 or IPv6 address to store into the text file. \n')
      print() # blank line

      # store IP address into const
      IP = resp

      # write IP addresses to file
      with open(file=r'Scrap-Yard\Labs-March-2023\PyinputplusScarps\Fake-IP-Addresses.txt', mode='a', encoding='utf-8', newline='\n') as f:

        # store IP address to IP address file
        f.write(IP + '\n')
        f.close()

      # IP successfully stored message!
      print('IP stored into text file! \n')
      
      # prompt user to store more IP's
      resp = pyinputplus.inputMenu(
        prompt="Store more IP's? \n", 
        choices=['Enter IPv4/IPv6 address to store.', 'Continue'],
        numbered=True)
      
      print()
      
      # IP store re-prompt condtional
      if resp == 'Enter IPv4/IPv6 address to store.':
        continue # re-iterate
      
      elif resp == 'Continue':
        break # escape
      
      else:
        pass
    
    # condtionals
    resp = pyinputplus.inputMenu(
      prompt="Would you like to display all the IP address's? \n", 
      choices=['Yes', 'No'], 
      numbered=True)
    
    print() # blank line of code
    
    # display ip conditional
    if resp == 'Yes':
      
      with open(file= r'Scrap-Yard\Labs-March-2023\PyinputplusScarps\Fake-IP-Addresses.txt') as f:
        # store IP data
        IP_DATA = f.read()
        pass
      
      message = print("%s"  %(IP_DATA))
      return message
    
    elif resp == 'No':
      break # break loop
    
    else:
      pass # do nothing just pass through

# function calls (uncomment one of them to test)
#password_prompt()
#input_bool()
#choices()
#choice_menu()
#email_input()
#date_input()
#ip_input()