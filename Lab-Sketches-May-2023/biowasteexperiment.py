''' <- doc

                                    █▄▄ █ █▀█ █░█░█ ▄▀█ █▀ ▀█▀ █▀▀   █▀ █▀▀ █▀█ ▄▀█ █▀█
                                    █▄█ █ █▄█ ▀▄▀▄▀ █▀█ ▄█ ░█░ ██▄   ▄█ █▄▄ █▀▄ █▀█ █▀▀
                                    
                                                            __    _                                   
                                                    _wr""        "-q__                             
                                                _dP                 9m_     
                                                _#P                     9#_                         
                                                d#@                       9#m                        
                                                d##                         ###                       
                                                J###                         ###L                      
                                                {###K                       J###K                      
                                                ]####K      ___aaa___      J####F                      
                                            __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
                                        _g##############mZ_         __g##############m_               
                                    _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_             
                                    a###""          ,Z"#####@" '######"\g          ""M##m            
                                     J#@"             0L  "*##     ##@"  J#              *#K           
                                    #"               `#    "_gmwgm_~    dF               `#_          
                                    7F                 "#_   ]#####F   _dK                 JE          
                                    ]                    *m__ ##### __g@"                   F          
                                                            "PJ#####LP"                                 
                                    `                       0######_                      '           
                                                            _0########_                                   
                                        .               _d#####^#####m__              ,              
                                            "*w_________am#####P"   ~9#####mw_________w*"         labcrop, chemicals, disaster!         
                                                ""9@#####@M""           ""P@#####@M""    
                                                

Implementing the range() function for a daily scrap yard module, makes the use of the range function to iterate through a array of containers that are
a biowaste material.
'''
# imports
from dataclasses import dataclass
from typing import Type

# dataclasses
@dataclass
class Containers:
    
    # container array
    global biocontainer_storage
    biocontainer_storage = [
        # lab container items
        'Container-46B',
            'Container-47B',
                'Container-48B',
                    'Container-49B',
                        'Container-50B',
                        'Container-51B']
    
    # fields/properties
    name: str
    id: str
    type: str = 'Biowaste'
    
    # class methods
    @staticmethod
    def __storage__() -> Type[str]:
        ''' # __containers__() class method
        Displays a list of containers from a labcorp that are substances to biowaste for experimentation
        '''
        
        # display all the containers in range and iterate them
        print('The biowaste containers in storage are the following:')
        for  int, c in enumerate(biocontainer_storage):
            print('[%s] %s' %(int, c))

# object constructors/initializers
Container_46B = Containers(name = biocontainer_storage[0], id = '46B', type='BioWaste')
Container_47B = Containers(name = biocontainer_storage[1], id = '47B', type='BioWaste')
Container_48B = Containers(name = biocontainer_storage[2], id = '48B', type='BioWaste')
Container_49B = Containers(name = biocontainer_storage[3], id = '49B', type='BioWaste')
Container_50B = Containers(name = biocontainer_storage[4], id = '50B', type='BioWaste')
Container_51B = Containers(name = biocontainer_storage[5], id = '51B', type='BioWaste')

# display items in storage
Containers.__storage__()