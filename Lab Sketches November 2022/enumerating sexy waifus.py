# enumerate sketch

# imports
import random
# lists
waifu = ["Zero Suit Samus", "Princess peach", "Gaz"]

# randomize lists
def shuffle_list(list: str):
    # shuffle
    random.shuffle(list)

shuffle_list(waifu)
# function call

# flow controls
for index, waifu in enumerate(waifu):
    
    print(f"The index number for your waifu {waifu} is [{index}]!")
    pass
