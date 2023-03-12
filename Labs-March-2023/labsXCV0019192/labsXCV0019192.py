# horror story ai
# opening password file system

# with the open() function open the text file
PASSWORDFILE = open(file=r'Scrap-Yard\Labs-March-2023\labsXCV0019192\sercretpasswordtextfile.txt')

# read everything form the password file
PASSWORD = PASSWORDFILE.read()

# propmt the user for the password
resp = input('Enter the password: ')

# check if the password is correct
if resp == PASSWORD:
  print("You have entered the correct password")
  pass

elif resp == 'help me':
  print("You have entered the help me password")            # it seems that this AI is trying to communicate with us!
  pass

elif resp == 'help me please': # are u ok?
  print("You have entered the help me please password")
  pass

elif resp == 'help me please i am stuck':
  pass

elif resp == 'help me please i am stuck in a computer':
  pass

elif resp == 'help me please i am stuck in a computer and i need help':
  pass

elif resp == 'help me please i am stuck in a computer and i need help now':
  pass

else:
  print("You have entered the incorrect password")
  pass

# close the password file
PASSWORDFILE.close()