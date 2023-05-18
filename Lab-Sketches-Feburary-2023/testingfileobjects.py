with open(file= r"Lessons\DarkCloud\resources\STORYSCRIPTS\FairyKingEncounterScript.txt", mode='r') as f:

    # collect file object data
    content = f.readlines() 
    # display contents with list comprehension
    [print(line) for line in content[0:3]]

    # display contents without list comprehension
    for line in content[0:3]:
        print(line) 
