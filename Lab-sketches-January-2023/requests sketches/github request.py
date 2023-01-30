# import modules
import requests

# request/response object constructors
r = requests.get('https://www.behance.net/gallery/154627447/Sometimes')

# exception handling
try: # check for HTTP download exceptions
    
    # raise HTTP exception if one has occured
    r.raise_for_status()
    pass

except Exception as exc:
    print('There was a problem: %s' % (exc))
    pass

# save byte image to disk
print(r.text)