"""
zaion python checklist
prompt user for their name
[1] if [x]
[1] elif
[1] else
[1] while loop [x]
[1] break [x]
[1] continue
[1] boolean value [x]
[1] for loop (print hello (5) times!) [1]
[1] range() with starting, stepping, and stopping integers [x]
[1] try and except 'exception handling' [x]
[1] lists [x]
[1] list nexus [x]
[1] list replication [x]
[1] import random
[1] shuffle a list
[1] return random value from within a list
[1] remove method [x]
[3] dictionary []
[1] keys()
[1] value()
[1] items()
[1] isPhoneNumber()
"""

# import module
import re

# regex for a phone number in the US

# united states regex
phoneNumRegex = re.compile(r'(\d\d\d){1,10}')

# match object
mo = phoneNumRegex.search('11')

# display group
print(mo.group())
