# global constant
CAT = "cat"


def kitty(): # overwite global variable CAT
    # local constant
    global CAT
    global WAIFU
    
    CAT = "Super Kitty!"
    WAIFU = "Moore Kitsune"
    
    pass

kitty()

print(CAT)