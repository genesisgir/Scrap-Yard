# string-interpolation-component.py

# var
WIFE = 'mrsgenesis'
AGE = 19
TALENT = 'Coding'

# output  I'm Dating my wife mrsgenesis and she is 19.
print(f'I\'m Dating my wife %s she is good at {TALENT} and she is %s!' %(WIFE,AGE))

# var
HUSBAND = 'Genesisgir' # string interpolation
SKILL = 'Coding' # string interpolation
WALLPAPER = 'Waifu' # f-string

# output  I'm Dating my husband Genesisgir and he is good at Coding and he has waifu wallpaper's .
print(f'I\'m Dating my husband %s and he is very good at %s, he also likes to use {WALLPAPER} wallpapers.' %(HUSBAND,SKILL))