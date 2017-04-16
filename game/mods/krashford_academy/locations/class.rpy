image krashford class1 = "mods/krashford_academy/locations/class/class1.jpg"
image krashford class2 = "mods/krashford_academy/locations/class/class2.jpg"


init:
    if mod_trigger_krashford == True:
        $ event("krashford_class1", "act == 'class' and deviance < 20", event.choose_one('class'), priority=200)
        $ event("krashford_class2", "act == 'class' and behavior < 50", event.choose_one('class'), priority=200)

label krashford_class1:
    
    scene krashford class1 with fade
    if renpy.random.randint(1,2) == 1:
        "You better learn to handle that gun, it might give you another day to live."
    else:
        "I'm lucky standing next to her and not in front."
    #TODO: gun training +
    return


label krashford_class2:
    
    scene krashford class2 with fade
    if renpy.random.randint(1,2) == 1:
        "Run, gun and kill those bastards!"
    else:
        "Rage against the "
    #TODO: gun training +
    return

