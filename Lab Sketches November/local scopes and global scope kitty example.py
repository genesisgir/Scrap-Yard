# global constant
CAT = "cat"


def kitty(): # overwite global variable CAT
    # local constant
    global CAT
    global WAIFU
    
    CAT = "Super Kitty!"
    WAIFU = "TennisWaifu"
    
    pass

kitty()

print(CAT)