# exception handling

# global variable for age
age = " "

# flow control
while True:

    try: # check for exceptions!

        age = int(input("whats your age? >"))

        if age >= 1:
            
            break
            pass
        
        pass

    except ValueError: # notify user of Value Error!


        print("You cant have letters or special characters in your age! \n")

        continue # re-iterate
        pass # do nothing

print("You are", str(age), "years old!", sep=" ") # end result