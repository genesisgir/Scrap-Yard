# Passing References

# import modules
import copy

def eggs(someParameter):
    
    someParameter.append('Hello')
    someParameter.append("Big booba")
    pass

# create variable
spam = [1, 2, 3]

# function call
eggs(spam)

# print out result!
print(spam)
