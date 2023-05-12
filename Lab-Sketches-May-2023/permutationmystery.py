from itertools import permutations 
from typing import Type
'''
                                        █░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█   █▀█ ▄▀█ █▄░█ █▄▀
                                        █▀█ █▀█ █▄▄ █░█ ██▄ █▀▄   █▀▄ █▀█ █░▀█ █░█

            Lets learn about list comprenensions. You are riven three integers . y and y reoresenung the olmensions of
            a cubold along with an integer n.
'''

# invalid arrays [0, 0 ,0]   [0, 1, 1]   [1, 0, 1]   [1, 1, 0]   [1, 1, 1]

# valid arrays established
[i, j, k] = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

# perms for dimensions
i_perms = permutations(i)
j_perms = permutations(j)
k_perms = permutations(k)

# define methods
def dimensions() -> Type[None]:
    ''' # dimensions() method
    returns the dimensions of i, j, k
    '''

    # display permutations for the var i
    print('The permutations of i are:')
    for perm in i_perms:
        
        print(perm)  
    print()
    
    
    # display permutations for the var j
    print('The permutations of j are:')
    for perm in j_perms:
        print(perm)
    print()
    
    
    # display permutations for the var k
    print('The permutations of k are:')
    for perm in k_perms:
        print(perm)
    print()

    return None

# display dimensions
dimensions()

# TODO use list comprehension on line '26'
if __name__ == '__main__':
    x = int(input('What are the dimensions of i? >'))
    y = int(input('What are the dimensions of j? >'))
    z = int(input('What are the dimensions of k? >'))
    n = int(input('What is the sum'))