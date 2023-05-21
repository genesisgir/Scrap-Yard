responses = ['5','10','25','50']

while True:
    # creating response variable
    resp = input('Would you like to skipcount by, 5, 10, 25, or 50?')
    
    # conditionals
    if resp == responses[0]:
        
        for n in range(1, 101, 5):
            print(n)
        break
    
    elif resp == responses[1]:
        for n in range(0,101,10):
            print(n)

    
    elif resp == responses[2]:
        for n in range (0,100,25):
            print(n)
            break

    
    elif resp == responses[3]:
        for n in range (0,100,50):
            print(n)
            break
    
    else:
        continue
    pass

print('You have successfully skip counted by ' , resp , '\n')