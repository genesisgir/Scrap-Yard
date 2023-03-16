"""

                █▀█ █▀▀ ▄▀█ █▀▄ █ █▄░█ █▀▀   ▄▀█ █▄░█ █▀▄   █░█░█ █▀█ █ ▀█▀ █ █▄░█ █▀▀   █▀▀ █ █░░ █▀▀ █▀
                █▀▄ ██▄ █▀█ █▄▀ █ █░▀█ █▄█   █▀█ █░▀█ █▄▀   ▀▄▀▄▀ █▀▄ █ ░█░ █ █░▀█ █▄█   █▀░ █ █▄▄ ██▄ ▄█


reading and writing capabilites within python


"""

# import modules
from pathlib import Path
import os

#print(type(str(Path('genesis','images','waifus')))) # create a path object

#print(type(Path('genesis','images','waifus'))) # create a path object



# TODO append to end of folder
# filename array
#files = ['genesis.txt','thicc-Jiggly-Waifu.png','waifus.mp4']
#
#for filename in files:
#    print(Path(r'C:\User\Genesis', filename))
#    pass

# TODO joining paths with / operator
# TODO you can use the / operator to join paths or use the joinpath() method
#print(Path('hello') / 'world')
#print(Path('hello') / 'world' / 'images' / 'waifus')
#print(Path('hello').joinpath('Genesis'))
#print(Path('hello').joinpath('Genesis').joinpath('images').joinpath('waifus'))
## both work equally the same
"""
GenesisGir answer
output should look like this:
32 - hello\world
33 - hello\world\images\waifu
34 - hello\genesis
35 - hello\genesis\images\waifus

windows paths use the '\' slash and linux uses the '/'.
"""

# TODO cwd() & os.chdir() methods
#print(Path().cwd()) # current working directory
#os.chdir(path=r'C:\Users\daint\Documents\Github\Scrap-Yard\Lab-sketches-January-2023\typescript sketches') # change cwd
#print(Path().cwd())  # display current working dir
#os.chdir(path=r'C:\Users\daint\Documents\Github') # revert back to orginal cwd
#print(Path().cwd())

# TODO The Home() method
#print(Path().home())

""" <- home() tips
return the path object of the home dir of this PC/local machine.
"""

""" <- Absolute vs Relative Paths


There are two ways to specify a file path:

An absolute path, which always begins with the root folder
A relative path, which is relative to the program’s current working directory
"""

# TODO how to create directories/repos w/os.makedirs
#os.makedirs(name='C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Lab-sketches-January-2023\\typescript sketches\\waifus', exist_ok=True)
#print(Path().cwd())

# TODO create new directory
#Path('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\reading-and-writing-files-scraps\\newdir').mkdir()

# TODO verifying if a path is absolute or relative
#print(Path().cwd()) # current working directory

# abosolute path
#print(Path().cwd().is_absolute()) # check if cwd is absolute

# relative
#print(Path('\genesis\images\waifus').is_absolute()) # check if path is absolute

# TODO check path type
#path = r'Scrap-Yard\Labs-March-2023\functionmetaldevice.py'
#
#print(os.path.abspath(path))
#print(os.path.isabs(path))
#print(os.path.isdir(path))
#print(os.path.isfile(path))
#print(os.path.islink(path))
#print(os.path.ismount(path))

# TODO relative paths and the relpath() method 
#print(os.path.relpath(
#    path=r'C:\Users\daint\Documents\Github\Scrap-Yard\Lab-sketches-January-2023\typescript sketches\waifus', 
#    start=r'C:\Users\daint\Documents\Github\Scrap-Yard\Lab-sketches-January-2023\typescript sketches'))

# TODO retrieving certain parts of a path with .anchor, .drive, .root, .parent, .name, .stem, .suffix
path = Path('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\reading-and-writing-files-scraps\\newdir')

# components of a path (abs/rel)
#print(path.anchor) # returns the drive letter
#print(path.drive) # returns the drive letter
#print(path.root) # returns the root dir
#print(path.parent) # returns the parent dir
#print(path.name) # returns the name of the file
#print(path.stem) # returns the name of the file without the suffix
#print(path.suffix) # returns the suffix of the file

# TODO how to get  certain parts of a path with path indexes
#print(Path.cwd()) # current working directory
#print(Path.cwd().parents[0]) 
#print(Path.cwd().parents[1]) 
#print(Path.cwd().parents[2])
#print(Path.cwd().parents[3])

# TODO os.path.basename() returns the last part of a path
#file_path = 'C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\reading-and-writing-files-scraps\\read-writeXKO06532.py'
#print(os.path.basename(file_path))
#print()
#print(os.path.dirname(file_path))

# TODO os.path.getsize() 
#print(os.path.getsize(r'Scrap-Yard\Labs-March-2023\PyinputplusScarps\Fake-IP-Addresses.txt'), 'bytes') # returns the size of a file in bytes
#print(os.listdir('Scrap-Yard\Labs-March-2023\PyinputplusScarps')) # list all files in a dir
#
## path byte size
#path_total_size = 0
#
#for filename in os.listdir('Scrap-Yard\Labs-March-2023\PyinputplusScarps'):
#    path_total_size += os.path.getsize(os.path.join('Scrap-Yard\Labs-March-2023\PyinputplusScarps', filename))
#
#print(path_total_size, 'bytes')

# TODO glob.glob() returns a list of strings of all the files in the cwd that match the pattern
#path = Path('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\PyinputplusScarps')
#print(path.glob('*')) # returns a generator object 
#print(list(path.glob(pattern='*.py'))) # returns a list of all files in the dir

# TODO Checking Path Validity
#path_1 = Path('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\reading-and-writing-files-scraps\\newdir')
#path_2 = Path('C:\\Users\\daint\\Documents\\Github\\Scrap-Yard\\Labs-March-2023\\reading-and-writing-files-scraps\\read-writeXKO06532.py')
#print(path_1.is_absolute())
#print(path_1.is_dir())
#print(path_2.is_file())

# TODO check to see whether a flash drive is connect to PC
#flash_drive = Path('D:\\')
#print("Flash Drive connected status: %s" %(flash_drive.exists()))

# TODO reading and writing to files
# TODO shelve(), pathlib() - read_text(), write_text()

# change cwd to save txt file
#os.chdir(path=r'Scrap-Yard\Labs-March-2023\reading-and-writing-files-scraps')
#
## naming the txt file
#p = Path('Spam.txt')
#
## write to the path object Spam.txt
#p.write_text(data='Hello GenesisGir, This is the first time you using the write_text() method in Python!')
#
## print text
#print(p.read_text())

# TODO shelve practice

## import module
#import shelve

## shelve file var
#shelve_file = shelve.open(filename=r'Scrap-Yard\Labs-March-2023\reading-and-writing-files-scraps\shelve')

## store list values in shelve file
#print(shelve_file['programmers'])

## close shelve file
#shelve_file.close()