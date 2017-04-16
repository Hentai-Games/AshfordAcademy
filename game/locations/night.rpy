init:
    
    $ event("normal_night", "act == 'night' and planning_day != 0", priority=90)
    $ event("planning_night", "act == 'night' and planning_day == 0", event.only(), priority=1)


label normal_night:
    
    scene bg home with fade
    if renpy.random.randint(1,20) == 1:
        if povGender == "Female":
            "You decide to take a shower and {i}comfort yourself{/i} before going to bed."
        else:
            "You decide to shower and shave before going to bed."
    else:
        "It's getting late, so you decide to go to sleep."
    return


label planning_night:
    
    scene bg home with fade
    python:
        if povGender == "Male":
            drink = renpy.random.choice(["Jack Daniels", "Glenfiddich", "Bagpiper", "Captain Morgan", "Red label", "Ole Smoky", "Laphroaig", "Yamazaki", "Black Label", "Teerenpeli"])
            drink += renpy.random.choice([" on the rocks", ""])
        elif povGender == "Female":
            drink = renpy.random.choice(["Chateau d'Yquem", "Musella", "Bourgogne Chardonnay", "Abraxas", "Hidden Rock"])
        else:
            drink = "Error, a unusually fine drink with a taste of ^Parsing the script failed"
    "After a long day of planning you decide to pour yourself a glass of [drink]."
    return
