# global constant
CAT = "cat"


def kitty(): # overwite global variable CAT
    # local constant
    global CAT
    global WAIFU
    
    CAT = "Super Kitty!"
    WAIFU = "GenesisGir"
    
    pass

kitty()

print(CAT)