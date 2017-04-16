#### FLAGON EVENT PACK 1 - Grounds ####

## This event pack contains events for all original locations in the game, as well as new events for the monthly actions.
## This Files is for the School grounds, or more properly Around the Town.
## Pictures are located in the subdirectory \Flagon1\Grounds."
## All custom images, characters, variables... are prefixed with "fla_" (with the exception of temp variables) to avoid conflicts.
## Formatting shamelessly stolen from Goldo. All your Code are belong to us!
#### SETUP ####

#Define characters
define fla_guy = Character('Guy', color="#1E90FF")
define fla_girl = Character('Girl', color="#1E60FF")

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Declaring images

image bg fla_grounds1 = "mods/Flagon1/Grounds/fla_grounds1.jpg"
image bg fla_grounds2 = "mods/Flagon1/Grounds/fla_grounds2.jpg"
image bg fla_grounds3 = "mods/Flagon1/Grounds/fla_grounds3.jpg"
image bg fla_grounds4 = "mods/Flagon1/Grounds/fla_grounds4.jpg"
image bg fla_grounds6 = "mods/Flagon1/Grounds/fla_grounds6.jpg"
image bg fla_grounds8 = "mods/Flagon1/Grounds/fla_grounds8.jpg"
image bg fla_grounds9 = "mods/Flagon1/Grounds/fla_grounds9.jpg"
image bg fla_grounds10 = "mods/Flagon1/Grounds/fla_grounds10.jpg"
image bg fla_grounds11 = "mods/Flagon1/Grounds/fla_grounds11.jpg"
image bg fla_grounds12 = "mods/Flagon1/Grounds/fla_grounds12.jpg"
image bg fla_grounds13 = "mods/Flagon1/Grounds/fla_grounds13.jpg"
image bg fla_grounds14 = "mods/Flagon1/Grounds/fla_grounds14.jpg"
image bg fla_grounds15 = "mods/Flagon1/Grounds/fla_grounds15.jpg"
image bg fla_grounds16 = "mods/Flagon1/Grounds/fla_grounds16.jpg"
image bg fla_grounds17 = "mods/Flagon1/Grounds/fla_grounds17.jpg"
image bg fla_grounds18 = "mods/Flagon1/Grounds/fla_grounds18.jpg"
image bg fla_grounds19 = "mods/Flagon1/Grounds/fla_grounds19.jpg"
image bg fla_grounds20 = "mods/Flagon1/Grounds/fla_grounds20.jpg"
image bg fla_grounds21_1 = "mods/Flagon1/Grounds/fla_grounds21_1.jpg"
image bg fla_grounds21_2 = "mods/Flagon1/Grounds/fla_grounds21_2.jpg"
image bg fla_grounds22 = "mods/Flagon1/Grounds/fla_grounds22.jpg"
image bg fla_grounds23 = "mods/Flagon1/Grounds/fla_grounds23.jpg"
image bg fla_grounds24 = "mods/Flagon1/Grounds/fla_grounds24.jpg"
image bg fla_grounds25 = "mods/Flagon1/Grounds/fla_grounds25.jpg"
image bg fla_grounds26 = "mods/Flagon1/Grounds/fla_grounds26.jpg"
image bg fla_grounds27 = "mods/Flagon1/Grounds/fla_grounds27.jpg"
image bg fla_grounds29 = "mods/Flagon1/Grounds/fla_grounds29.jpg"
image bg fla_grounds30 = "mods/Flagon1/Grounds/fla_grounds30.jpg"
image bg fla_grounds31 = "mods/Flagon1/Grounds/fla_grounds31.jpg"
image bg fla_grounds32 = "mods/Flagon1/Grounds/fla_grounds32.jpg"
image bg fla_grounds33 = "mods/Flagon1/Grounds/fla_grounds33.jpg"
image bg fla_grounds34_1 = "mods/Flagon1/Grounds/fla_grounds34_1.jpg"
image bg fla_grounds34_2 = "mods/Flagon1/Grounds/fla_grounds34_2.jpg"
image bg fla_grounds35 = "mods/Flagon1/Grounds/fla_grounds35.jpg"
image bg fla_grounds36 = "mods/Flagon1/Grounds/fla_grounds36.jpg"
image bg fla_grounds37 = "mods/Flagon1/Grounds/fla_grounds37.jpg"
image bg fla_grounds38 = "mods/Flagon1/Grounds/fla_grounds38.jpg"
image bg fla_grounds39 = "mods/Flagon1/Grounds/fla_grounds39.jpg"
image bg fla_grounds40 = "mods/Flagon1/Grounds/fla_grounds40.jpg"
image bg fla_grounds41 = "mods/Flagon1/Grounds/fla_grounds41.jpg"

#Setting up events and conditions

init:
    $ event("fla_grounds1", "act == 'school_grounds' and inhibition < 90", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds2", "act == 'school_grounds' and inhibition < 90 and athletics > 20", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds3", "act == 'school_grounds' and inhibition < 100 and behavior <15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds4", "act == 'school_grounds' and morale > 50", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds5", "act == 'school_grounds' and morale > 75", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds6", "act == 'school_grounds' and morale > 50", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds8", "act == 'school_grounds' and inhibition < 80", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds9", "act == 'school_grounds' and inhibition < 80 and deviance > 5 ", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds10", "act == 'school_grounds' and inhibition < 100", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds11", "act == 'school_grounds' and morale > 10", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds12", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds13", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds14", "act == 'school_grounds' and morale > 20", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds15", "act == 'school_grounds' and inhibition < 100", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds16", "act == 'school_grounds' and behavior < 15 and deviance > 5", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds17", "act == 'school_grounds' and morale > 25", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds18", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds19", "act == 'school_grounds' and behavior > 20", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds20", "act == 'school_grounds' and uniform == 'sexy_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds21", "act == 'school_grounds' and inhibition < 100", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds22", "act == 'school_grounds' and inhibition < 90", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds23", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds24", "act == 'school_grounds' and morale > 20 and deviance < 5", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds25", "act == 'school_grounds' and morale < 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds26", "act == 'school_grounds' and morale < 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds27", "act == 'school_grounds' and inhibition < 25 and deviance > 75", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds28", "act == 'school_grounds' and inhibition < 80 and deviance > 10", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds29", "act == 'school_grounds' and inhibition < 90 and athletics > 30", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds30", "act == 'school_grounds' and inhibition < 80", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds31", "act == 'school_grounds' and inhibition < 50 and deviance > 50", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds32", "act == 'school_grounds' and inhibition < 50 and deviance > 30", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds33", "act == 'school_grounds' and inhibition < 30 and deviance > 50", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds34", "act == 'school_grounds' and inhibition < 75 and deviance > 15", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds35", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds36", "act == 'school_grounds' and uniform == 'nude_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds37", "act == 'school_grounds' and inhibition < 60 and deviance > 20", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds38", "act == 'school_grounds' and inhibition < 75 and deviance > 10", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds39", "act == 'school_grounds' and inhibition < 70 and uniform == 'sexy_uniform'", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds40", "act == 'school_grounds' and inhibition < 75", event.choose_one('school_grounds'), priority=200)
    $ event("fla_grounds41", "act == 'school_grounds' and deviance > 15 and athletics > 20 and academics > 30", event.choose_one('school_grounds'), priority=200)
    
##Low Sex Events

label fla_grounds1:
    
    scene bg fla_grounds1 with fade
    "The setting sun and blossoming cherry trees perfectly complement this girls beauty. The wind gently lifting her skirt doesn't hurt though."
    $ inhibition -=1
    return
    
label fla_grounds2:

    scene bg fla_grounds2 with fade
    "Riding a bike is an excellent way to stay in shape."
    $ athletics +=1
    return
    
label fla_grounds3:
    
    scene bg fla_grounds3 with fade
    "Several boys are taking pictures of the girls. They seem less than pleased about this."
    $ morale -=1
    $ behavior -=1
    return
    
label fla_grounds4:
    
    scene bg fla_grounds4 with fade
    "It warms your heart to know that your students are actually happy to come to classes."
    $ morale +=1
    return
    
label fla_grounds5:
    
    $ r=renpy.random.randint(1,2)
    image bg fla_grounds5 = ConditionSwitch("r==1","mods/Flagon1/Grounds/fla_grounds5_1.jpg","r==2","mods/Flagon1/Grounds/fla_grounds5_2.jpg")
    
    scene bg fla_grounds5 with fade
    "You see a group of students taking advantage of the nice weather to have thier lunch outdoors."
    $ morale+=1
    return
    
label fla_grounds6:
    
    scene bg fla_grounds6 with fade
    girl "Yeah, this school is way better than my last!"
    $ morale +=1
    return
    
label fla_grounds8:
    
    scene bg fla_grounds8 with fade
    "The heats been pretty nasty lately, but your students don't let it get them down!"
    $ morale +=1
    $ inhibition -=1
    return
    
label fla_grounds9:
    
    scene bg fla_grounds9 with fade
    "The heat is so bad that students will do almost anything to cool down, even to the point of removing layers of clothing."
    $ inhibition -=1
    $ deviance +=1
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5
    return
    
label fla_grounds10:
    
    scene bg fla_grounds10 with flash
    pov "OOOOF! Careful there young lady!"
    "Heh Heh Heh... kitty!"
    return
    
label fla_grounds11:
    scene bg fla_grounds11 with fade
    "On your way home you spot a couple of kids playing around."
    return
    
label fla_grounds12:
    
    scene bg fla_grounds12 with fade
    "Due to your school having more girls than boys, some girls have had to learn the value of sharing."
    return
    
label fla_grounds13:
    
    scene bg fla_grounds13 with fade
    "They say the way to a mans heart is through his stomach. But you bet the short skirt doesn't hurt."
    return
    
label fla_grounds14:
    
    scene bg fla_grounds14 with fade
    "You spot a happy looking couple on their way to lunch."
    $ morale +=1
    return
    
label fla_grounds15:
    
    scene bg fla_grounds15 with fade
    "While your students seem depressed by the rain, you think it might just have some benefits."
    $ morale -=1
    $ inhibition -=1
    return
    
label fla_grounds16:
    
    scene bg fla_grounds16 with fade
    girl "KYAAAAAH!"
    "An embarassed cry catches your attention, and you spot a young boy running off, having just flipped this girls skirt up."
    $ behavior -=1
    $ inhibition +=1
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5
    return
    
label fla_grounds17:
    
    scene bg fla_grounds17 with fade
    "When you stop at the mall to pick up a few things, you spot a couple of your students out on a date. Looks like the poor guy is being used as a baggage horse."
    return
    
label fla_grounds18:
    
    scene bg fla_grounds18 with fade
    "Two students race home, laughing. Looks like they had a good day at school."
    $ morale +=1
    return
    
label fla_grounds19:
    
    scene bg fla_grounds19 with fade
    "This girl slipped in the rain and twisted her ankle. Fortunatly, your students are always willing to help eachother."
    $ behavior +=1
    return
    
label fla_grounds20:
    
    scene bg fla_grounds20 with fade
    "Sexy Uniforms plus Rainy Weather equals Good Times!"
    $ inhibition -=1
    return
    
label fla_grounds21:
    
    scene bg fla_grounds21_1 with fade
    "The roof is a popular place for love confessions"
    scene bg fla_grounds21_2
    "And this one seems to be going very well!"
    $ morale +=1
    return
    
label fla_grounds22:
    
    scene bg fla_grounds22 with fade
    "One of your students interupts your cloud watching. Still, given the view you can't complain."
    $ inhibition -=1
    return
    
label fla_grounds23:
    
    scene bg fla_grounds23 with fade
    "You spot a student sitting alone on the swing set. She looks kind of lonely."
    $ morale -=1
    return
    
label fla_grounds24:
    
    scene bg fla_grounds24 with fade
    girl "Say AHHHH."
    $ deviance +=1
    return
    
label fla_grounds25:
    
    scene bg fla_grounds25 with fade
    "These girls just started dating recently."
    $ inhibition -=1
    return
    
label fla_grounds26:
    
    scene bg fla_grounds26 with fade
    "The shortage of boys in your school means that sometimes conflicts can erupt."
    $ behavior -=1
    return
    
## High Sex Events

label fla_grounds27:
    
    scene bg fla_grounds27 with fade
    guy "Vote for me in the school council election and I promise that no one will go without sex again!"
    $ inhibition -=1
    $ deviance +=1
    $ morale +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return
    
label fla_grounds28:
    
    $ r=renpy.random.randint(1,3)
    image bg fla_grounds28 = ConditionSwitch("r==1","mods/Flagon1/Grounds/fla_grounds28_1.jpg","r==2","mods/Flagon1/Grounds/fla_grounds28_2.jpg","r==3","mods/Flagon1/Grounds/fla_grounds28_3.jpg")
    
    scene bg fla_grounds28 with fade
    "As girls get more and more horny, discrete sex toys are becoming more popular."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds29:
    
    scene bg fla_grounds29 with fade
    "Riding a bike to school is a great way to stay in shape. But make sure to take care of your equipment."
    $ inhibition -=1
    $ athletics +=1
    return
    
label fla_grounds30:
    
    scene bg fla_grounds30 with fade
    "Some girls have started going around without panties. It's seems to give them quite the thrill."
    $ inhibition -=1
    return
    
label fla_grounds31:
    
    scene bg fla_grounds31 with fade
    "The sound of moans echoing through the nearby forest drew you to this scene. Looks like one of your teachers let herself be overwhelmend by her lust."
    "Unfortunatly it seems your not the only person who noticed the noise."
    $ deviance +=2
    $ reputation -=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5
    return
    
label fla_grounds32:
    
    scene bg fla_grounds32 with fade
    "These two students couldn't wait to find a good spot and have begun giving eachother handjobs right in the hallway."
    $ behavior -=1
    $ deviance +=1
    $ inhibition -=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return
    
label fla_grounds33:
    
    scene bg fla_grounds33 with fade
    "Your students love of exhibitionism has gotten to the point where looking in any random window is likely to get you a good show."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds34:
    
    scene bg fla_grounds34_1 with fade
    "The familiar sounds of sex have led you to the schools rooftop, where a couple of students are going at it."
    menu:
        "Stop them":
            pov "Alright, that's quite enough of that! Get dressed and meet me in my office!"
            $ deviance -=1
            $ morale -=1
        "Let them continue":
            scene bg fla_grounds34_2
            "Unfortunatly other people are quickly attracted by the sounds. To your suprise this isn't enough to stop the couple, who continue to climax before leaving"
            girl "I can't believe they did that in public!"
            guy "So indecent!"
            girl2 "So bold!"
            $ deviance +=2
            $ inhibition -=2
            $ reputation -=1
    return
    
label fla_grounds35:
    
    scene bg fla_grounds35 with fade
    "You spot a couple of your teachers carpooling. They must be in a hurry, thier still in uniform."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds36:
    
    scene bg fla_grounds36 with fade
    "Your students seem to have grown used to the Naked Uniform rule. Best idea you ever had. EVER."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds37:
    
    scene bg fla_grounds37 with fade
    "Some of the girls are getting quite agressive. This girls has practically pinned her boyfriend to the ground in her rush to relieve herself."
    $ deviance +=1
    $ inhibition -=1
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5
    return
    
label fla_grounds38:
    
    scene bg fla_grounds38 with fade
    "Looks like these girls didn't notice you taking a nap on the roof. You make sure to stay well hidden and enjoy the show as the two girls expertly finger eachothers pussys."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds39:
    
    scene bg fla_grounds39 with fade
    "This girl has embraced the Sexy Uniforms whole heartedly."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds40:
    
    scene bg fla_grounds40 with fade
    "Once you found out how many girls are going without panties these days you made sure that the floors were polished to a mirror sheen."
    pov "So... beautiful."
    $ deviance +=1
    $ inhibition -=1
    return
    
label fla_grounds41:
    
    scene bg fla_grounds41 with fade
    "Riding a bike to school is a great way to stay in shape. And with a few simple add-ons can be alot of fun as well!"
    $ deviance +=1
    $ academics +=1
    $ athletics +=1
    return