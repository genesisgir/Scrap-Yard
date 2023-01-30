# import modules
import requests

# response model obj
resp = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# exception handling
try: # check for HTTP download exceptions
    
    # raise HTTP exception if one has occured
    resp.raise_for_status()
    pass

except Exception as exc:
    print('There was a problem: %s' % (exc))
    pass

# save file to local hard drive
file = open('Romeo and Juliet.txt', 'wb')

# check chunk of file
for chunk in resp.iter_content(chunk_size=100000, decode_unicode=False):
    print(file.write(chunk))
    pass

# close the file
file.close()