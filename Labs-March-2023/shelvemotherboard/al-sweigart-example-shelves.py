"""
█▀ █░█ █▀▀ █░░ █░█ █▀▀ ▄▀ ▀▄
▄█ █▀█ ██▄ █▄▄ ▀▄▀ ██▄ ▀▄ ▄▀

al sweigart example shelves - 2021-03-23
"""



# Import modules
import shelve, os, pathlib

os.chdir(r'Scrap-Yard\Labs-March-2023\shelvemotherboard')

# Create a shelve object
shelfFile = shelve.open('mydata')

# List of cats
cats = ['Zophie', 'Pooka', 'Simon']

# Write to the shelve object
shelfFile['cats'] = cats

# Close the shelve object
shelfFile.close()

# Open the shelve object
shelfFile = shelve.open('mydata')

# Read from the shelve object
type(shelfFile)
type(shelfFile['cats'])
shelfFile['cats']
shelfFile.close()












