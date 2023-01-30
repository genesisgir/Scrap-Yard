import requests

# ask the server for a response object
# import modules
import requests

# request/response object constructors
r = requests.get('https://steamcommunity.com/profiles/76561198086758434/myworkshopfiles/')

# exception handling
try: # check for HTTP download exceptions
    
    # raise HTTP exception if one has occured
    r.raise_for_status()
    pass

except Exception as exc:
    print('There was a problem: %s' % (exc))
    pass


print(r.text.encode().decode('utf-8').encode())