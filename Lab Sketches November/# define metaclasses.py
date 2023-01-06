# define metaclasses
# custom dictionary class 📚
class member_table(dict):
    
    # define methods
    def __init__(self):
        self.member_names = []
        pass
        
    def __setitem__(self, key, value):
        # if the key is not already defined, add to the
        
        # list of keys.
        if key not in self:
            self.member_names.append(key)
            pass

        # Call superclass
        dict.__setitem__(self, key, value)
        pass

# metaclasses 💻
class Meta(type): # super Meta class
    
    # methods
    # prepare function
    def __prepare__(metacls, name, bases):
        return member_table()
        pass
    
    # The metaclass invocation/reference to/mention
    def __new__(cls, name, bases, classdict):
        # Note that we replace the classdict with a regular
        # dict before passing it to the superclass, so that we
        # don't continue to record member names after the class
        # has been created.
        
        result = type.__new__(cls, name, bases, dict(classdict))
        result.member_names = classdict.member_names
        return result
    pass

# inheritance classes/derived classes 💿
class TennisWaifus_Uber_Secret_Sugoi_Dekai_Metaclass(metaclass=Meta):
    pass

# subclasses 📀
class Sub_Class(TennisWaifus_Uber_Secret_Sugoi_Dekai_Metaclass):
    pass
