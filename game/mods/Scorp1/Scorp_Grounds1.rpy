#### FLAGON EVENT PACK 1 - Grounds ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this. 
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Grounds.
## Pictures are located in the subdirectory \Scorp1\Grounds
## All custom images, characters, variables... are prefixed with "scorp_" (with the exception of temp variables) to avoid conflicts.
## Please PLEASE note that *all* scenarios in this mod are intended to involve (fictional) characters over the age of 18.
#### SETUP ####

#Define characters
define scorp_guy = Character('Guy', color="#1E90FF")
define scorp_girl = Character('Girl', color="#1E60FF")

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Define the screen used for scrolling a picture (background picture to be declared first as 'scorp_bg')
screen scorp_screen:
    viewport:
        edgescroll (200, 500)
        mousewheel True
        add scorp_bg

#Declaring images

image bg scorp_grounds1 = "mods/Scorp1/Grounds/scorp_grounds1.jpg"
image bg scorp_grounds2 = "mods/Scorp1/Grounds/scorp_grounds2.jpg"
image bg scorp_grounds3 = "mods/Scorp1/Grounds/scorp_grounds3.jpg"
image bg scorp_grounds4 = "mods/Scorp1/Grounds/scorp_grounds4.jpg"
image bg scorp_grounds5 = "mods/Scorp1/Grounds/scorp_grounds5.jpg"
image bg scorp_grounds6_1 = "mods/Scorp1/Grounds/scorp_grounds6_1.jpg"
image bg scorp_grounds6_2 = "mods/Scorp1/Grounds/scorp_grounds6_2.jpg"
image bg scorp_grounds7 = "mods/Scorp1/Grounds/scorp_grounds7.jpg"
image bg scorp_grounds8 = "mods/Scorp1/Grounds/scorp_grounds8.jpg"
image bg scorp_grounds9 = "mods/Scorp1/Grounds/scorp_grounds9.jpg"
image bg scorp_grounds10 = "mods/Scorp1/Grounds/scorp_grounds10.jpg"
image bg scorp_grounds11 = "mods/Scorp1/Grounds/scorp_grounds11.jpg"
image bg scorp_grounds12 = "mods/Scorp1/Grounds/scorp_grounds12.jpg"
image bg scorp_grounds13 = "mods/Scorp1/Grounds/scorp_grounds13.jpg"
image bg scorp_grounds14 = "mods/Scorp1/Grounds/scorp_grounds14.jpg"
image bg scorp_grounds15 = "mods/Scorp1/Grounds/scorp_grounds15.jpg"
image bg scorp_grounds16 = "mods/Scorp1/Grounds/scorp_grounds16.jpg"
image bg scorp_grounds17 = "mods/Scorp1/Grounds/scorp_grounds17.jpg"
image bg scorp_grounds18 = "mods/Scorp1/Grounds/scorp_grounds18.jpg"
image bg scorp_grounds19 = "mods/Scorp1/Grounds/scorp_grounds19.jpg"
image bg scorp_grounds20 = "mods/Scorp1/Grounds/scorp_grounds20.jpg"
image bg scorp_grounds21_1 = "mods/Scorp1/Grounds/scorp_grounds21_1.jpg"
image bg scorp_grounds21_2 = "mods/Scorp1/Grounds/scorp_grounds21_2.jpg"
image bg scorp_grounds22 = "mods/Scorp1/Grounds/scorp_grounds22.jpg"
image bg scorp_grounds23 = "mods/Scorp1/Grounds/scorp_grounds23.jpg"
image bg scorp_grounds24 = "mods/Scorp1/Grounds/scorp_grounds24.jpg"
image bg scorp_grounds25 = "mods/Scorp1/Grounds/scorp_grounds25.jpg"
image bg scorp_grounds26 = "mods/Scorp1/Grounds/scorp_grounds26.jpg"
image bg scorp_grounds27 = "mods/Scorp1/Grounds/scorp_grounds27.jpg"

#Setting up events and conditions

init:
    $ event("scorp_grounds1", "act == 'school_grounds' and inhibition < 75 and inhibition > 20 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds2", "act == 'school_grounds' and inhibition < 60 and deviance > 60 and deviance < 95", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds3", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds4", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds5", "act == 'school_grounds' and inhibition < 30 and deviance > 70 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds6", "act == 'school_grounds' and uniform == 'nude_uniform' and deviance > 20", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds7", "act == 'school_grounds' and uniform == 'nude_uniform' and artistery > 70", event.choose_one('school_grounds'), priority=200)    
    $ event("scorp_grounds8", "act == 'school_grounds' and uniform == 'sexy_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds9", "act == 'school_grounds' and uniform == 'nude_uniform' and morale > 70", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds10", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds11", "act == 'school_grounds' and inhibition < 20 and deviance > 80", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds12", "act == 'school_grounds' and inhibition < 75 and inhibition > 30", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds13", "act == 'school_grounds' and inhibition < 30 and deviance > 70 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds14", "act == 'school_grounds' and morale > 20 and inhibition < 60 and deviance > 40", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds15", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds16", "act == 'school_grounds' and deviance < 25", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds17", "act == 'school_grounds' and inhibition < 10 and deviance > 90", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds18", "act == 'school_grounds' and inhibition < 50 and deviance > 60 and deviance < 90", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds19", "act == 'school_grounds' and behavior < 40", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds20", "act == 'school_grounds' and uniform == 'nude_uniform' and deviance > 50", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds21", "act == 'school_grounds' and uniform == 'conservative_uniform' and inhibition < 30", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds22", "act == 'school_grounds' and uniform == 'nude_uniform' and deviance > 70", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds23", "act == 'school_grounds' and deviance > 10 and deviance < 40", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds24", "act == 'school_grounds' and deviance < 75", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds25", "act == 'school_grounds' and inhibition > 15 and inhibition < 50", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds26", "act == 'school_grounds' and inhibition < 90 and inhibition > 75", event.choose_one('school_grounds'), priority=200)
    $ event("scorp_grounds27", "act == 'school_grounds' and deviance > 75 and inhibition < 35", event.choose_one('school_grounds'), priority=200)

label scorp_grounds1:
    
    scene bg scorp_grounds1 with fade
    "Word has gotten around that plenty of the girls have stopped wearing panties."
    girl "What are you doing, jerk??"
    guy "Haha, it's true!"
    $ inhibition -=1
    return
    
label scorp_grounds2:

    scene bg scorp_grounds2 with fade
    girl "Ahhh - ahhh-h - I know we live on the same street, Seiji - b-but y-you're going to have to take it out when we h-have to part ways -"
    guy "No I don't. You're sleeping in my bed tonight."
    girl "O-oh, o-okay... Nnnngh..."
    return
    
label scorp_grounds3:
    
    scene bg scorp_grounds3 with fade
    "It's easy to tell an Ashford girl on her way home from the girls who go to other schools."
    return
    
label scorp_grounds4:
    
    #Panning up and down
    scene bg scorp_grounds4:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_grounds4")    
    show screen scorp_screen
    
    "If a girl is caught in the rain in the new uniform, she could catch a chill! This girl's planned ahead for her walk home!"
    hide screen scorp_screen
    return
    
label scorp_grounds5:
   
    scene bg scorp_grounds5 with fade
    "You're in the Metro station to head home when, on the escalator above you, you recognise an Ashford student."
    "She's obviously wearing nothing under her skirt, and both of her clearly-visible holes are a mess of dripping cum. On top of that, her tits are hanging out."
    "You can already see people's shocked gazes. This isn't going to do much for your school's reputation."
    $ reputation -=1
    return
    
label scorp_grounds6:
    
    scene bg scorp_grounds6_1 with fade
    "This girl is so nervous about the walk home that she's painted clothes onto her nude body. She's hoping no-one will notice her naked uniform."
    "Does it work?"
    scene bg scorp_grounds6_2 with fade   
    "Nope! Maybe tomorrow she'll make it home without being dragged into an alley!"
    return
    
label scorp_grounds7:
    
    scene bg scorp_grounds7 with fade
    "Music club has been {b}weird{/b} lately."
    guy "It's art! Of course you don't understand!"
    $ artistery +=1    
    return
    
label scorp_grounds8:
    
    scene bg scorp_grounds8 with fade
    "With the introduction of the sexier uniform, girls have started to report getting attacked by perverts on the way home."
    $ morale -=1
    $ deviance +=1    
    return
    
label scorp_grounds9:
    
    scene bg scorp_grounds9 with flash
    "You look up at the Ashford building, and see a number of girls have stayed after school for some kind of club. They're waving at you as you leave."
    girls "We love you, [povTitle] [povLastName]! Ashford is the best!"
    $ morale +=1    
    return
    
label scorp_grounds10:
    scene bg scorp_grounds10 with fade
    "Everywhere you look, nude female flesh. The new uniform really demonstrates what Ashford is all about."
    return
    
label scorp_grounds11:
    
    scene bg scorp_grounds11 with fade
    "Looks like one of the male teachers has found a new hood ornament."
    "You're sure he'll let her go after he's driven her round the block a few times."
    return
    
label scorp_grounds12:
    
    scene bg scorp_grounds12 with fade
    girl "H-hey - I took my panties off for the walk home - just like you asked - look!"
    guy "...Oh my God, you actually did it."
    $ inhibition -=1     
    return
    
label scorp_grounds13:
    
    #Panning up and down
    scene bg scorp_grounds13:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_grounds13")    
    show screen scorp_screen
    
    "The boys like pulling pranks like this on girls who don't put out."
    "You don't have time to wait and see what happens when someone finds her."
    $ behavior -=1
    $ inhibition -=1     
    hide screen scorp_screen
    return 
    
label scorp_grounds14:
    
    scene bg scorp_grounds14 with fade
    "You see this beautiful pair rushing out of the school's front gates, anxious to get home. They've clearly been tormented by the dildoes all day."
    "Friends who experiment together, stay together."
    $ morale +=1
    $ inhibition -=1
    return
    
label scorp_grounds15:
    
    scene bg scorp_grounds15 with fade
    "With the new uniform catching lots of attention in the street, some of the girls have started renting out their bodies as advertising space."
    "As the instigator of the uniform scheme, you of course a percentage of the revenue."
    $ cash += 50  
    return
    
label scorp_grounds16:
    
    scene bg scorp_grounds16 with fade
    "This girl is leaving school with a hop, skip and a jump!"
    return
    
label scorp_grounds17:
    
    scene bg scorp_grounds17 with fade
    "It's so mean when the boys gang up on a new girl."
    $ behavior -=1    
    return
    
label scorp_grounds18:
    
    scene bg scorp_grounds18 with fade
    girl "Eeek - doing this - out in the open like this - ah -"
    guy "Don't act like you're not enjoying it!"
    girl "Ohh - ohh, I'm cumming -"
    $ inhibition -=1     
    return    
    
label scorp_grounds19:
    
    scene bg scorp_grounds19 with fade
    "You spot a few girls messing around on the roof, and climbing up the water tower."
    pov "Hey! Get down from there!!"
    "They just make rude gestures at you and carry on playing."
    $ behavior -=1       
    return
    
label scorp_grounds20:
    
    scene bg scorp_grounds20 with fade
    "Oh dear - some prankster chained this girl up in the rain! At least he left her the umbrella..."
    "You manage to get her free. You like girls wet, but not {b}that{/b} wet."
    girl "Brrr! So cold! Thank you [povTitle] [povLastName]!"
    $ inhibition +=1
    return
    
label scorp_grounds21:
    
    scene bg scorp_grounds21 with fade
    "In protest against the new ultra-conservative uniforms, some girls have started cutting strategic holes in their attire."
    "When asked about it, they all angrily say that Ashford is no longer a conservative place, and the new uniform is stifling both their sexuality and the boy's right to easy access."
    "They tell you they're going to keep behaving badly until the issue is solved."
    $ morale -=2
    $ behavior -=2   
    return
    
label scorp_grounds22:
    
    scene bg scorp_grounds22 with fade
    "She looks at you so innocently as she prepares to leave, that you almost don't notice what's on her bicycle seat."
    "Watching her climb on and ride slowly away is a truly astounding sight."
    $ inhibition -=1
    return
    
label scorp_grounds23:
    
    scene bg scorp_grounds23 with fade
    "Under a blood-red sunset, two girls explore sides of themselves they'd never known were there."
    $ deviance +=1    
    return
    
label scorp_grounds24:
    
    scene bg scorp_grounds24 with fade
    "It's such a drag when two good friends argue, and someone gets caught in the middle."
    $ morale -=1     
    return
    
label scorp_grounds25:
    
    "Some girls have begun having sex in school grounds, potentially in full view of anyone who walks by. Some do it purely for the thrill."
    scene bg scorp_grounds25 with fade    
    "...And others just get blackmailed into doing it by a boy with access to a few embarrassing photos."
    $ inhibition -=1
    return
    
label scorp_grounds26:
    
    scene bg scorp_grounds26 with fade
    "The moment's shelter from the rain you share with this girl somehow makes you feel young again."
    return
    
label scorp_grounds27:
    
    "This girl and her male friends have been walking the same route home from Ashford for years."
    scene bg scorp_grounds27 with fade    
    "They've never considered each other anything but friends, but Ashford is a different place now... One day, when walking home, the boys started looking at her with lust rather than affection."
    guy "Take it! Take it, you fucking slut! I can't believe we never did this earlier!"
    girl "Aahh - aahh - yes - use me - use me like a fucktoy -"
    $ inhibition -=1
    $ deviance +=1
    $ morale -=1
    return