# import modules
import requests


# payload
payload = {'key1': 'science', 'key2':'artifical'}

# request/response object constructors
r = requests.get(url='https://httpbin.org/get', params=payload)

# exception handling
try: # check for HTTP download exceptions
    
    # raise HTTP exception if one has occured
    r.raise_for_status()
    pass

except Exception as exc:
    print('There was a problem: %s' % (exc))
    pass

print(r.url)