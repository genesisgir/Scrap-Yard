# PASSWORD PROMPT
PASSWORD = 'genesis'

while True: # reprompt, unsure that the password is correct if it is login

    # prompt user
    response = input('Enter password >')

    # flow
    if response == PASSWORD: # user entered correct credentials
    
        # user has logged in
        print('ACCESS GRANTED')
        break
        pass # null, nill

    else: # user entered incorrect credentials

        # user has logged in
        print('ACCESS DENIED')
        continue
        pass