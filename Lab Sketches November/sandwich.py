

class loops: # my iterator
    
    # methods
    
    # iterate process
    def __iter__(self):
        
        # instants/variables
        self.integer = 1
        return self
        pass
    
    # traverse process
    def __next__(self):
        
        if self.integer <= 100:
            
            # class instants/variable
            x = self.integer = 0
            
            # increase integer!
            self.integer += 1
            return x
            
            pass
        
        else:
            raise StopIteration
        
        pass
    pass

# object instances
myclass = loops()
iterator = myclass

# import modules
import time

# flow controls
for i in iterator:
    
    print("Big boobies")
    time.sleep(0.1)
    pass