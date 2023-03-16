# automatic text reply system

# import modules
import sys

REPLIES = {'Agree': 'Yes, I agree. That sounds fine to me.',
        'Busy': 'Sorry, can we do this later this week or next week?',
        'No': 'No thank you. I am busy right now.'}

# make-shift Iphone userinterface prompt
print(''' 
    

Daniela: Hey Genesis can you make it right now?


Yes, I agree. That sounds fine to me. [1]

Sorry, can we do this later this week or next week? [2]

No thank you. I am busy right now. [3]


Choose a number to reply to the message. \n''')

# reply to the message
def reply():
  
  # reply function
  while True:
    
    # user input
    resp = input('>')
    
    # exception handling
    try:
      # condional
      if resp == '1':
        # accept the request
        print(REPLIES['Agree'])
        print('Your reply has been sent.')
        break

      elif resp == '2':
        # reject the request
        print(REPLIES['No'])
        print('Your reply has been sent.')
        break

      elif resp == '3':
        print(REPLIES['Busy'])
        print('Your reply has been sent.')
        break
      
      else:
        # raise an error
        raise ValueError
    
    except:
      print('Invalid input. Please try again. \n')
      continue

# call the reply function
reply()

print('End of program.')
sys.exit()