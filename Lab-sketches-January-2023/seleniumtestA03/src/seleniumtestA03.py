# import modules
import requests

# request
r = requests.get('https://i0.wp.com/loucosporgeek.com.br/wp-content/uploads/2022/02/Sono-Bisque-Doll-wa-Koi-wo-Suru-Episodio-06-1.jpg?resize=390%2C220&ssl=1') # HTML/HTTL requests

# save image from byte object to images repo in seleniumA03 folder
with open(r'Scrap-Yard\Lab-sketches-January-2023\seleniumtestA03\images\wtf.png', 'wb') as f:
    
    # read bytes from response object
    f.write(r.content) # write bytes from response
    f.close() # close
    pass # null , nill , nothing