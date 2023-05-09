# escape characters example
#print(r'My name is Molly and I have ten cat\'s and six\' dogs I\'m very keen on having pets and shit \'\'\'')

# multi-line strings
#print(''' 
#    
#    HELLOOOOOO
#    THIS IS A MULTILINE STRING 
#    PRETTY COOL RIGHT?
#    ''')

# multi-line comments
#'''
#THIS IS A MULTILINE COMMENT 
#THIS IS FUCKING COOL 
#:D'''

# TODO multi line select (ctrl + alt + shft + arrow up or down)

# indexing and slicin#
#string = 'Vanilla'
#
#print(string[0:])

# The in and not in Operators with Strings

# conditions
#if 'hello' in 'HeLlo im Mrsgenesis':
#    print('hello')
#
#elif 'hello' not in 'tomato':
#
#    print('bye bye.')
#
#else:
#    pass





# exception handling 


#try : # testing/checking out code for errors/exception
#    
#    if 'hello' in 'hello im Mrsgenesis':
#        raise ValueError
#        print('hello \n')
#    
#    elif 'hello' not in 'tomato':
#        
#        print('bye bye. \n')
#    
#    else:
#        pass
#
#except: # where we write code that will fix they exceptions!
#
#    print('Fixed code! \n') 
#
#finally:
#    
#    print('Finalization checks passed! \n')
#
#
#print('reached the global scope!')

# exceptions with arrays

# list array
#list_a = ['hello', 'hello im Mrsgenesis', 'tomato']

# tuple array
#list_b = ('hello', 'hello im Mrsgenesis', 'tomato')

# dict array
#list_b = {'a': 'hello', 'b': 'hello im Mrsgenesis', 'c': 'tomato'}

# exceptions handling
#try : # testing/checking out code for errors/exception
#    
#    if list_a[0] in list_a[1]:
#        raise ValueError
#        print('hello \n')
#    
#    elif list_a[0] not in list_a[2]:
#        
#        print('bye bye. \n')
#    
#    else:
#        pass
#
#except: # where we write code that will fix they exceptions!
#
#    print('Fixed code! \n') 
#
#finally:
#    
#    print('Finalization checks passed! \n')
#
#
#print('reached the global scope!')




# string interpolation

#interpolation_a = ['hello', 'hello im Mrsgenesis', 'tomato']

#print('%s i am a %s i like candy %s ' %(interpolation_a[0] ,interpolation_a[2], interpolation_a[1]))


# upper(), lower(), isupper(), and islower() Methods

#print('hello \n'.upper()) # converts string to uppercase
#print('HELLO \n'.lower()) # converts string to lowercase
#
#print('HELLO \n'.isupper()) # checks if string is uppercase
#print('hello \n'.islower()) # checks if string is lowercase


# isX String Methods
'''
isalpha() Returns True if the string consists only of letters and isn’t blank

isalnum() Returns True if the string consists only of letters and numbers and is not blank

isdecimal() Returns True if the string consists only of numeric characters and is not blank

isspace() Returns True if the string consists only of spaces, tabs, and newlines and is not blank

istitle() Returns True if the string consists only of words that begin with an uppercase
'''

# examples
#print('hello'.isalpha()) # True
#print('hello123'.isalnum()) # True
#print('123'.isdecimal()) # True
#print(' '.isspace()) # True
#print('This Is Title Case 123'.istitle()) # True



# startswith() and endswith() Methods

#print('hello'.startswith('g')) # True
#print('hello'.endswith('o')) # True


#  join() and split() Methods

#array_a = ['hello', 'hello im Mrsgenesis', 'tomato']

#print(' '.join(array_a))
#print(' '.join(array_a).split())

# partition() method

#print('Happy'.partition('p'))


'''

>>> 'Hello'.rjust(10)

'     Hello' # output

>>> 'Hello'.rjust(20)

'              Hello' # output

>>> 'Hello, World'.rjust(20)

'         Hello, World' # output

>>> 'Hello'.ljust(10)

'Hello     ' # output

'''

# removing whitespace with strip(), rstrip(), and lstrip()

#spam = '    Hello World     '
#
#spam.strip() # removes whitespace from both sides
#spam.rstrip() # removes whitespace from right side
#spam.lstrip() # removes whitespace from left side



# numeric values of characters with ord() and chr()

#ord() # converts character to unicode number
#chr() # converts unicode number to character

# example
#print(ord('A')) # 65
#print(chr(77)) # M

'''
These functions are useful when you need to do an ordering or mathematical operation on characters
'''

#import pyperclip
#
#pyperclip.copy('Hello world!') # copies string to clipboard
#print(pyperclip.paste()) # 'Hello world!'



















