#### FLAGON EVENT PACK 1 - Classroom ####

## This event pack contains events for all original locations in the game, as well as new events for the monthly actions.
## This File is for the Classrom.
## Pictures are located in the subdirectory \Flagon1\Classroom
## All custom images, characters, variables... are prefixed with "fla_" (with the exception of temp variables) to avoid conflicts.
## Formatting shamelessly stolen from Goldo. All your Code are belong to us!
#### SETUP ####

#Define characters
#Characters go here if needed

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Declaring images

image bg fla_classroom1 = "mods/Flagon1/Classroom/fla_classroom1.jpg"
image bg fla_classroom2 = "mods/Flagon1/Classroom/fla_classroom2.jpg"
image bg fla_classroom3 = "mods/Flagon1/Classroom/fla_classroom3.jpg"
image bg fla_classroom4 = "mods/Flagon1/Classroom/fla_classroom4.jpg"
image bg fla_classroom5 = "mods/Flagon1/Classroom/fla_classroom5.jpg"
image bg fla_classroom6 = "mods/Flagon1/Classroom/fla_classroom6.jpg"
image bg fla_classroom7 = "mods/Flagon1/Classroom/fla_classroom7.jpg"
image bg fla_classroom8 = "mods/Flagon1/Classroom/fla_classroom8.jpg"
image bg fla_classroom9 = "mods/Flagon1/Classroom/fla_classroom9.jpg"
image bg fla_classroom12 = "mods/Flagon1/Classroom/fla_classroom12.jpg"
image bg fla_classroom13 = "mods/Flagon1/Classroom/fla_classroom13.jpg"
image bg fla_classroom15 = "mods/Flagon1/Classroom/fla_classroom15.jpg"
image bg fla_classroom17 = "mods/Flagon1/Classroom/fla_classroom17.jpg"
image bg fla_classroom18 = "mods/Flagon1/Classroom/fla_classroom18.jpg"
image bg fla_classroom19 = "mods/Flagon1/Classroom/fla_classroom19.jpg"
image bg fla_classroom20 = "mods/Flagon1/Classroom/fla_classroom20.jpg"
image bg fla_classroom21 = "mods/Flagon1/Classroom/fla_classroom21.jpg"
image bg fla_classroom22 = "mods/Flagon1/Classroom/fla_classroom22.jpg"
image bg fla_classroom23 = "mods/Flagon1/Classroom/fla_classroom23.jpg"
image bg fla_classroom25 = "mods/Flagon1/Classroom/fla_classroom25.jpg"
image bg fla_classroom26 = "mods/Flagon1/Classroom/fla_classroom26.jpg"
image bg fla_classroom28 = "mods/Flagon1/Classroom/fla_classroom28.jpg"
image bg fla_classroom30 = "mods/Flagon1/Classroom/fla_classroom30.jpg"
image bg fla_classroom31 = "mods/Flagon1/Classroom/fla_classroom31.jpg"
image bg fla_classroom33 = "mods/Flagon1/Classroom/fla_classroom33.jpg"
image bg fla_classroom34 = "mods/Flagon1/Classroom/fla_classroom34.jpg"
image bg fla_classroom36 = "mods/Flagon1/Classroom/fla_classroom36.jpg"
image bg fla_classroom37 = "mods/Flagon1/Classroom/fla_classroom37.jpg"
image bg fla_classroom38 = "mods/Flagon1/Classroom/fla_classroom38.jpg"
image bg fla_classroom39 = "mods/Flagon1/Classroom/fla_classroom39.jpg"
image bg fla_classroom41 = "mods/Flagon1/Classroom/fla_classroom41.jpg"
image bg fla_classroom42 = "mods/Flagon1/Classroom/fla_classroom42.jpg"
image bg fla_classroom44 = "mods/Flagon1/Classroom/fla_classroom44.jpg"

#Setting up events and conditions

init:
    $ event("fla_classroom1", "act == 'class' and deviance > 5", event.choose_one('class'), priority=200)
    $ event("fla_classroom2", "act == 'class' and deviance > 5", event.choose_one('class'), priority=200)
    $ event("fla_classroom3", "act == 'class' and morale > 20", event.choose_one('class'), priority=200)
    $ event("fla_classroom4", "act == 'class' and athletics < 25", event.choose_one('class'), priority=200)
    $ event("fla_classroom5", "act == 'class' and inhibition < 85", event.choose_one('class'), priority=200)
    $ event("fla_classroom6", "act == 'class' and academics > 15", event.choose_one('class'), priority=200)
    $ event("fla_classroom7", "act == 'class' and inhibition < 100", event.choose_one('class'), priority=200)
    $ event("fla_classroom8", "act == 'class' and behavior < 10", event.choose_one('class'), priority=200)
    $ event("fla_classroom9", "act == 'class' and academics > 10", event.choose_one('class'), priority=200)
    $ event("fla_classroom10", "act == 'class' and deviance > 50 and inhibition < 49 and academics > 50 ", event.choose_one('class'), priority=200)
    $ event("fla_classroom11", "act == 'class' and deviance > 50 and inhibition < 49 and learning_materials == 1.3", event.choose_one('class'), priority=200)
    $ event("fla_classroom12", "act == 'class' and deviance > 50 and academics > 65", event.choose_one('class'), priority=200)
    $ event("fla_classroom13", "act == 'class' and deviance > 20 and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("fla_classroom14", "act == 'class' and deviance > 75 and inhibition < 24", event.choose_one('class'), priority=200)
    $ event("fla_classroom15", "act == 'class' and deviance > 40 and inhibition < 74", event.choose_one('class'), priority=200)
    $ event("fla_classroom16", "act == 'class' and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("fla_classroom17", "act == 'class' and deviance > 40 and inhibition < 60", event.choose_one('class'), priority=200)
    $ event("fla_classroom18", "act == 'class' and deviance > 75 and inhibition < 24", event.choose_one('class'), priority=200)
    $ event("fla_classroom19", "act == 'class' and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("fla_classroom20", "act == 'class' and deviance > 10", event.choose_one('class'), priority=200)
    $ event("fla_classroom21", "act == 'class' and deviance > 15 and inhibition < 60", event.choose_one('class'), priority=200)
    $ event("fla_classroom22", "act == 'class' and deviance > 45 and inhibition and uniform != 'nude_uniform' < 55", event.choose_one('class'), priority=200)
    $ event("fla_classroom23", "act == 'class' and inhibition < 74", event.choose_one('class'), priority=200)
    $ event("fla_classroom24", "act == 'class' and inhibition < 65", event.choose_one('class'), priority=200)
    $ event("fla_classroom25", "act == 'class' and deviance > 30 and inhibition < 60", event.choose_one('class'), priority=200)
    $ event("fla_classroom26", "act == 'class' and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("fla_classroom27", "act == 'class' and deviance > 65 and inhibition < 35", event.choose_one('class'), priority=200)
    $ event("fla_classroom28", "act == 'class' and inhibition < 70", event.choose_one('class'), priority=200)
    $ event("fla_classroom29", "act == 'class' and inhibition < 85", event.choose_one('class'), priority=200)
    $ event("fla_classroom30", "act == 'class' and deviance > 25", event.choose_one('class'), priority=200)
    $ event("fla_classroom31", "act == 'class' and deviance > 20 and inhibition < 70", event.choose_one('class'), priority=200)
    $ event("fla_classroom32", "act == 'class' and deviance > 75 and inhibition < 24", event.choose_one('class'), priority=200)
    $ event("fla_classroom33", "act == 'class' and deviance > 10 and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("fla_classroom34", "act == 'class' and deviance > 75 and inhibition < 24 and athletics < 75", event.choose_one('class'), priority=200)
    $ event("fla_classroom35", "act == 'class' and deviance > 50 and inhibition < 49", event.choose_one('class'), priority=200)
    $ event("fla_classroom36", "act == 'class' and deviance > 30 and inhibition < 70", event.choose_one('class'), priority=200)
    $ event("fla_classroom37", "act == 'class' and uniform == 'nude_uniform' and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("fla_classroom38", "act == 'class' and uniform == 'nude_uniform' and inhibition > 60", event.choose_one('class'), priority=200)
    $ event("fla_classroom39", "act == 'class' and uniform == 'nude_uniform' and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("fla_classroom40", "act == 'class' and deviance > 75 and inhibition < 24", event.choose_one('class'), priority=200)
    $ event("fla_classroom41", "act == 'class' and deviance > 50 and inhibition < 49", event.choose_one('class'), priority=200)
    $ event("fla_classroom42", "act == 'class' and deviance > 50 and inhibition < 49", event.choose_one('class'), priority=200)
    $ event("fla_classroom43", "act == 'class' and deviance > 50 and inhibition < 49", event.choose_one('class'), priority=200)
    $ event("fla_classroom44", "act == 'class' and deviance > 50 and inhibition < 49", event.choose_one('class'), priority=200)
    $ event("fla_classroom45", "act == 'class' and deviance > 30 and inhibition < 65", event.choose_one('class'), priority=200)
    
label fla_classroom1:
    
    scene bg fla_classroom1 with fade
    "The lack of boys in your school means that girl/girl relationships are becoming more and more common."
    return
    
label fla_classroom2:
    
    scene bg fla_classroom2 with fade
    "You spot a couple of girls sharing a brief kiss."
    return
    
label fla_classroom3:
    
    scene bg fla_classroom3 with fade
    "It's always good to see student's enjoying thier lunch."
    return
    
label fla_classroom4:
    
    scene bg fla_classroom4 with fade
    "Looks like PE class wiped this poor girl out. Maybe you should spend some more time whipping your students into shape?"
    return
    
label fla_classroom5:
    
    scene bg fla_classroom5 with fade
    "You enter the room just in time to see a student twirl around, which causes her skirt to flutter upward."
    menu:
        "Enjoy the show":
            "While the girl doesn't seem to mind your stare, your not quite sure the other students in the room share the sentiment."
            $ inhibition -=1
            if renpy.random.randint(1, 3) == 1:
                $ deviance += 5
                $ reputation -=1
        "Avert your eyes":
            "You quickly turn your head, pretending to be fascinated by something on the blackboard."
            $ inhibition +=1
            if renpy.random.randint(1, 3) == 1:
                $ reputation += 1
    return
    
label fla_classroom6:
    
    scene bg fla_classroom6 with fade
    "Looks like english class is going well. You spend a few minutes listening to the student reading from the book and try not to laugh when she stutters on 'counterquasiproantiunredemidisestablishmentarianism'"
    return
    
label fla_classroom7:
    
    scene bg fla_classroom7 with fade
    "The custodial staff just waxed the floors last night. This poor young man slips and ends up giving a nearby girl quite the kiss."
    return
    
label fla_classroom8:
    
    scene bg fla_classroom8 with fade
    "Some of your students are getting fed up with thier rowdier classmates."
    return
    
label fla_classroom9:
    
    scene bg fla_classroom9 with fade
    "A nice conversation between classes can help clear the mind."
    return
    
label fla_classroom10:
    
    $ r=renpy.random.randint(1, 3)
    image bg fla_classroom10 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom10_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom10_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom10_3.jpg")
    
    scene bg fla_classroom10 with fade
    "Looks like today's biology class is focusing on the female reproductive system today. It's great to see the female students helping out!"
    return
    
label fla_classroom11:
    
    $ r=renpy.random.randint(1, 2)
    image bg fla_classroom11 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom11_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom11_2.jpg")
    
    scene bg fla_classroom11 with fade
    "Your brand new textbooks are paying off, as students follow the step by step instructions and helpful diagrams!"
    return

label fla_classroom12:
    
    scene bg fla_classroom12 with fade
    "Your students know that proper motivation is key to any endevour. So this student agreed to have sex with anyone who got a perfect score on the last test."
    return

label fla_classroom13:
    
    scene bg fla_classroom13 with fade
    "You wander into an empty classroom just in time to see a student trying to clean herself up using her tie. She freezes and begins to turn red when she spots you."
    menu:
        "Hand her some tissues":
            "She mumbles a thank you but it's clear from the way she avoids looking at you and deeply blushes that shes mortified to be seen like this."
            $ morale -=1
            $ deviance +=1
        "Scold her and send her off to detention":
            pov "This kind of behaviour is simply not acceptable. Clean yourself up and report for detention after class."
            "The girl is clearly ashamed, but you must maintain order at your school."
            $ behavior +=1
            $ morale -=1
        "Pretend not to have seen her":
            pov "Wait... this isn't my office. Blast! I hate not being able to see without my glasses."
            "Your not sure the girl believes your words, but she at least seems grateful you made the attempt."
            $ morale +=1
            $ behavior -=1
    return
    
label fla_classroom14:

    $ r=renpy.random.randint(1, 4)
    image bg fla_classroom14 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom14_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom14_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom14_3.jpg","r==4","mods/Flagon1/Classroom/fla_classroom14_4.jpg")
    
    scene bg fla_classroom14 with fade
    "When you first started at Ashford you worried that the lack of men at the school would be a problem. However, as almost all sense of shame has fled your students they have no problem sharing a cock in their relentless search for pleasure."
    return
    
label fla_classroom15:
    
    scene bg fla_classroom15 with fade
    "Teachers are no more immune to the rising tide of lust than your students. Fortunatly they do tend to be discreet."
    return
    
label fla_classroom16:

    $ r=renpy.random.randint(1, 2)
    image bg fla_classroom16 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom16_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom16_2.jpg")
    
    scene bg fla_classroom16 with fade
    "It seems that boobjobs are becoming popular among the bustier students."
    return
    
label fla_classroom17:
    
    scene bg fla_classroom17 with fade
    "Looks like a couple of braver (or at least hornier) students have started having sex right in the middle of a classroom between lessons."
    "From the looks of things most of the other students are scandalized, but turned on. However, letting them continue would be probably be bad for discipline, and could ruin the schools reputation."
    menu:
        "They need to learn this stuff. Enjoy the show":
            "You watch on with a benevolent smile as the cries of pleasure reach a fevor pitch. Soon cum is pouring into the girls pussy as she shudders with orgasm"
            if renpy.random.randint(1, 2) == 1:
                "As the sated lovers leave to get clean the class burst into amazed gossip. It takes forever to get them focused on the next lesson."
                $ behavior -=5
                $ inhibition -=3
                $ deviance +=3
            else:
                "As the two lovers leave to get clean you can see quite a few students trying to hide the signs of thier arousal. However you also spot more than one clearly disgusted student."
                $ behavior -=5
                $ inhibition -=3
                $ deviance +=3
                $ reputation -=2
                $ deviance += 5
        "This must be stopped":
            "As much as it pains you to stop such a lovely show, if this gets out the PTA will crucify you. Possibly literally."
            pov "WHAT THE IN THE HELLS DO YOU THINK YOUR DOING!?"
            boy "We where just..."
            girl "I thought it would be okay to..."
            pov "NO EXCUSES! My office NOW! You two have detention until the Sun burns out!"
            "As you march the young lovers out of the classroom you can tell your reaction has had a chilling effect on the students. But you know this was for the best."
            $ behavior +=5
            $ inhibition +=3
            $ deviance -=3
            if renpy.random.randint(1, 2) == 1:
                $ reputation +=2
    return
    
label fla_classroom18:
    
    scene bg fla_classroom18 with fade
    "These days it's not to uncommon for you to enter a room and find an orgy going on."
    return
    
label fla_classroom19:
    
    scene bg fla_classroom19 with fade
    "The students always know which classrooms will be unused and available for other uses."
    return
    
label fla_classroom20:
    
    scene bg fla_classroom20 with fade
    "A scrapping noise prompts you to peek into a classroom that should be empty this time of day. You see faintly blushing girl lying near nude atop some desks. Looks like someone is a budding exhibitionist!"
    return
    
label fla_classroom21:
    
    scene bg fla_classroom21 with fade
    "This exhibionist considers it her job to loosen up the more restrained students. While most of the class barely notices her antics anymore these boys can't take thier eyes of her moist pussy."
    return
    
label fla_classroom22:
    
    scene bg fla_classroom22 with fade
    "This girl got caught coming to class without any panties on. As punishment, she has to masturbate while the boy sitting next to her watches closely."
    return
    
label fla_classroom23:
    
    scene bg fla_classroom23 with fade
    "Class can be quite boring. Some students have found ways to quietly amuse themselves at those times."
    return
    
label fla_classroom24:

    $ r=renpy.random.randint(1, 4)
    image bg fla_classroom24 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom24_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom24_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom24_3.jpg","r==4","mods/Flagon1/Classroom/fla_classroom24_4.jpg")
    
    scene bg fla_classroom24 with fade
    "Quiet sounds of feminine moaning lead you to peek into an unused classroom. Looks like no boys allowed to you."
    return
    
label fla_classroom25:
    
    scene bg fla_classroom25 with fade
    "Huh, that redhead student and that boy had both been after the same girl for weeks. Looks like they decided teaming up was the best way to catch her."
    return
    
label fla_classroom26:
    
    scene bg fla_classroom26 with fade
    "A careful peak into this classroom nets a a great view of a silver haired beauty masturbating before going home."
    return
    
label fla_classroom27:
    
    $ r=renpy.random.randint(1, 4)
    image bg fla_classroom27 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom27_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom27_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom27_3.jpg","r==4","mods/Flagon1/Classroom/fla_classroom27_4.jpg")
    
    scene bg fla_classroom27 with fade
    teacher "It is important to maintain your concentration even in the most stressful situation. This will be essential to passing your exams! Understood?"
    girl "Ahhh... ye... yes teacher!"
    return
    
label fla_classroom28:
    
    scene bg fla_classroom28 with fade
    "As you reach under a desk to retrieve a dropped pen you get quite the eyeful of this pantyless student. She notices your gaze and simply smirks at you."
    menu:
        "Give an appreciative smile back":
            "You take a good second look before straightning up and handing her pen back."
            $ inhibition -=1
        "Give detention":
            "As you return the pen to her, you lean forward and whisper detention into her ear. That wipes the smirk of her face quickly."
            $ behavior +=1
    return
    
label fla_classroom29:
    
    $ r=renpy.random.randint(1, 2)
    image bg fla_classroom29 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom29_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom29_2.jpg")
    
    scene bg fla_classroom29 with fade
    "It's not that uncommon for you to peek into a classroom at the end of the day and spot someone using thier desk to take the edge off."
    return
    
label fla_classroom30:
    
    scene bg fla_classroom30 with fade
    "Some girls can't be satisfied by just one boy."
    return
    
label fla_classroom31:
    
    scene bg fla_classroom31 with fade
    "Some of your students are getting bored with simple handjobs and like to try something a little more difficult."
    return
    
label fla_classroom32:
    
    $ r=renpy.random.randint(1, 2)
    image bg fla_classroom32 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom32_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom32_2.jpg")
    
    scene bg fla_classroom32 with fade
    if uniform == 'nude_uniform':
        "For safety reasons during Home Ec students are allowed to put on an apron. However, this just seems to make these girls even hornier than complete nudity does."
    else:
        "Looks like Home Ec class has turned into another lesbian orgy. This might not happen if they wore something more than just aprons, but somehow you can't bring yourself to scold them."
    return
    
label fla_classroom33:
    
    scene bg fla_classroom33 with fade
    "Funny, the heat doesn't seem that bad to you, but these girls are so desperate to cool down that thier baring thier underwear right in front of you."
    return
    
label fla_classroom34:
    
    scene bg fla_classroom34 with fade
    "Your athletics program has payed off big time. This boy has managed to fuck every girl in his class multiple times without a break. You can't help but be impressed."
    return
    
label fla_classroom35:
    
    $ r=renpy.random.randint(1, 3)
    image bg fla_classroom35 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom35_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom35_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom35_3.jpg")
    
    scene bg fla_classroom35 with fade
    "Looks like Sex Ed classes have gotten to masturbation. Your glad to see your students diligently learning important skills!"
    return
    
label fla_classroom36:
    
    scene bg fla_classroom36 with fade
    "These two sisters just transfered into your school. A few of thier classmates convinced them this was a tradition of the class."
    return
    
label fla_classroom37:
    
    scene bg fla_classroom37 with fade
    pov "So what do you girls think of the new uniform policy?"
    girl1 "I wasn't to sure at first, but after a little while it didn't bother me at all!"
    girl2 "Yeah, thiers something empowering about just baring everything!"
    pov "Glad to hear it."
    return
    
label fla_classroom38:
    
    scene bg fla_classroom38 with fade
    "Hmm, maybe you where a bit hasty implementing the Nude Uniform policy. Most of the class seems hideously embarrased."
    $ morale -=1
    return
    
label fla_classroom39:
    
    scene bg fla_classroom39 with fade
    "Looks like the nude uniform is a great hit. This class enjoys it's lunch without the slightest hint of shame."
    $ morale +=1
    return
    
label fla_classroom40:
    
    $ r=renpy.random.randint(1, 3)
    image bg fla_classroom40 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom40_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom40_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom40_3.jpg")
    
    scene bg fla_classroom40 with fade
    "It wasn't easy finding enough boys to go around for the Gangbang portion of Sex Ed, but you feel it's important for the girls to know how to deal with multiple partners."
    return
    
label fla_classroom41:
    
    scene bg fla_classroom41 with fade
    "This girl volunteered to help the other students learn to finger a girl in Sex Ed class."
    return
    
label fla_classroom42:
    
    scene bg fla_classroom42 with fade
    "Looks like the remedial lesson on Masturbation is going quite well. Your sure these girls will pass the make up test with little problem."
    return
    
label fla_classroom43:
    
    $ r=renpy.random.randint(1, 3)
    image bg fla_classroom43 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom43_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom43_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom43_3.jpg")
    
    scene bg fla_classroom43 with fade
    teacher "It's important that you know how to relieve sexual stress on your own. The use of vibrators can aid in that!"
    girls "Yes teacher!"
    "Sex Ed is one of your favorite classes"
    girl1 "Cumming! CUMMING! YESSSSSSSSSS!"
    "Best class ever."
    return
    
label fla_classroom44:
    
    scene bg fla_classroom44 with fade
    "Hmm, looks like you walked into the class during a cunnilingus test. Some of the girls blush as you watch carefully, but judging by the way thier pussies get even wetter it's just making them more excited."
    return
    
label fla_classroom45:
    
    $ r=renpy.random.randint(1, 4)
    image bg fla_classroom45 = ConditionSwitch("r==1","mods/Flagon1/Classroom/fla_classroom45_1.jpg","r==2","mods/Flagon1/Classroom/fla_classroom45_2.jpg","r==3","mods/Flagon1/Classroom/fla_classroom45_3.jpg","r==4","mods/Flagon1/Classroom/fla_classroom45_4.jpg")
    
    scene bg fla_classroom45 with fade
    "It seems the increased sexual activity at Ashford has started affecting the teaching staff. You've spotted more than one teacher using a discrete vibrator while teaching. And some of them aren't all that discrete."
    return