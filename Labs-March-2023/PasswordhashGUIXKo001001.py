# import modules
import bcrypt
import PySimpleGUI  as sg

GENESIS_PASSWORD = 'Test'
password_bytes = GENESIS_PASSWORD.encode('utf-8')

ArrayOfPassword = []

print(ArrayOfPassword)

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

ArrayOfPassword.append(hashed)

layout = [
    [sg.Text('Enter a password to hash')],
    [sg.Text('Enter Password'), sg.InputText(key='password')],
    [sg.Button('Ok'), sg.Button('Cancel')],
    [sg.Multiline(ArrayOfPassword, key='hashed_passwords', size=(60, 10), disabled=True)]
]

# create the GUI window
sg.theme('DarkAmber')
window = sg.Window('Password Hasher', layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    password = values['password']
    if not password:
        continue
    password_bytes = password.encode('utf-8')
    # check if password already exists in the list of hashed passwords
    for p in ArrayOfPassword:
        if bcrypt.checkpw(password_bytes, p):
            sg.popup('Password already exists!')
            break
    else:  # password not found in list of hashed passwords
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        ArrayOfPassword.append(hashed_password)
        window['hashed_passwords'].update(ArrayOfPassword)
        # check if password matches any hashed password in the list
        for p in ArrayOfPassword[:-1]:
            if bcrypt.checkpw(password_bytes, p):
                sg.popup('Password matches a hashed password!')
                break
        else:
            sg.popup('Password hashed successfully!')

# close the GUI window
window.close()

# while True:
#   print(ArrayOfPassword)


#   def create_password(password):
#       salt = bcrypt.gensalt()
#       hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#       ArrayOfPassword.append(hashed_password)
#       return hashed_password

#   def check_password(password):
#       for p in ArrayOfPassword:
#           if bcrypt.checkpw(password.encode('utf-8'), p):
#               return True
#       hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
#       ArrayOfPassword.append(hashed_password)
#       return False

#   def login():
#       pw = input("Enter Password:")
#       if check_password(pw):
#           print("Password Matches")
#           return True
#       else:
#           print("Wrong Password")
#           create_password(pw)
#           return False

#   login()