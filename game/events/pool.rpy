init:
    if persistent.mod_disable_original_events == False:
        $ event("pool1", "act == 'pool' and inhibition > 80", event.choose_one('pool'))
        $ event("pool2", "act == 'pool' and inhibition > 80", event.choose_one('pool'))
        $ event("pool3", "act == 'pool' and behavior > 20", event.choose_one('pool'))
        $ event("pool4", "act == 'pool' and behavior < 20", event.choose_one('pool'))
        $ event("pool5", "act == 'pool' and athletics > 25", event.choose_one('pool'))
        $ event("pool6", "act == 'pool' and morale > 20", event.choose_one('pool'))
        $ event("pool7", "act == 'pool' and athletics > 25", event.choose_one('pool'))
        $ event("pool8", "act == 'pool' and morale > 25 and inhibition < 90", event.choose_one('pool'))
        $ event("pool9", "act == 'pool' and inhibition < 90 and inhibition > 50", event.choose_one('pool'))
        $ event("pool10", "act == 'pool' and inhibition > 90", event.choose_one('pool'))
        $ event("pool11", "act == 'pool' and inhibition < 70", event.choose_one('pool'))
        $ event("pool12", "act == 'pool'", event.choose_one('pool'))
        $ event("pool13", "act == 'pool' and behavior < 50 and deviance > 5", event.choose_one('pool'))
        $ event("pool14", "act == 'pool' and inhibition < 90", event.choose_one('pool'))
        $ event("pool15", "act == 'pool' and morale > 35 and inhibition < 95", event.choose_one('pool'))
        $ event("pool16", "act == 'pool' and athletics > 30", event.choose_one('pool'))
        $ event("pool17", "act == 'pool'", event.choose_one('pool'))
        $ event("pool18", "act == 'pool' and inhibition < 95 and athletics > 30", event.choose_one('pool'))
        $ event("pool19", "act == 'pool' and inhibition < 85 and deviance > 20", event.choose_one('pool'))
        $ event("pool20", "act == 'pool' and inhibition > 70", event.choose_one('pool'))
        $ event("pool21", "act == 'pool' and athletics > 25 and athletics < 65", event.choose_one('pool'))
        $ event("pool22", "act == 'pool' and inhibition < 90", event.choose_one('pool'))
        $ event("pool23", "act == 'pool' and inhibition < 95 and inhibition > 60", event.choose_one('pool'))
        $ event("pool24", "act == 'pool' and inhibition < 85 and deviance > 20", event.once(), event.choose_one('pool', 3))     #WD: Stop Dup Events# priority=20)
        $ event("pool25", "act == 'pool' and inhibition < 85 and deviance > 20", event.choose_one('pool'))                      #Ash: I promise...
        $ event("pool26", "act == 'pool' and deviance < 10", event.choose_one('pool'))
        $ event("pool27", "act == 'pool' and behavior < 45", event.choose_one('pool'))
        $ event("pool28", "act == 'pool' and behavior < 55 and inhibition < 100", event.choose_one('pool'))
        $ event("pool29", "act == 'pool' and athletics < 45", event.choose_one('pool'))
        $ event("pool30", "act == 'pool' and (uniform == 'nude_uniform' or inhibition < 70)", event.choose_one('pool'))
        $ event("pool31", "act == 'pool' and morale > 40 and athletics > 50", event.choose_one('pool'))
        $ event("pool32", "act == 'pool' and behavior < 50 and deviance > 10", event.choose_one('pool'))
        $ event("pool33", "act == 'pool' and inhibition < 85", event.choose_one('pool'))
        $ event("pool34", "act == 'pool' and inhibition > 45 and inhibition < 95", event.choose_one('pool'))
        $ event("pool35", "act == 'pool' and inhibition > 45 and inhibition < 95", event.choose_one('pool'))
        
        $ event("pool36", "act == 'pool' and inhibition > 45 and inhibition < 95", event.choose_one('pool'))
        
        $ event("pool37", "act == 'pool' and inhibition > 50 and deviance > 15 and evil_points > 0", event.choose_one('pool'))


label pool1:
    
    scene pool1a with fade
    if deviance < 35:
        pov "You're not allowed to eat ice cream during class!"
        return
    else:
        menu:
            "You're not allowed to eat ice cream during class!":
                $ behavior += 1
                return

            "Do you want something else to put in your mouth?":
                scene pool1b
                $ morale -= 1
                girl "..."
                return

label pool2:
    
    scene pool2 with fade
    "Seems like she's getting ready for class."
    return

label pool3:
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("pool3_"+randImg)
    with fade
    "A team of good girls are cleaning the pool."
    pov "Keep up the good work girls!"
    $ behavior += 1
    return


label pool4:
    
    scene pool4 with fade
    "A group of girls is cheering each other on before swimming class."
    $ athletics += 1
    return
    

label pool5:
    
    scene pool5 with fade
    "A girl beat her own personal record! Pushing your body to the limit really pays off."
    $ athletics += 1
    return


label pool6:
    
    scene pool6 with fade
    "After training hard, a girl just wants to have fun."
    $ morale += 1
    return


label pool7:
    
    scene pool7 with fade
    "The water is really nice, but eventually you gotta get up and wrap that wet body in a soft towel."
    $ athletics += 1
    return
    
    
label pool8:
    
    scene pool8 with fade
    "You walk by the pool and two sweet girls wave and smile at you. What a nice day!"
    $ inhibition -= 1
    return
    
    
label pool9:
    
    scene pool9 with fade
    "As you inspect the pool area you come across a shy girl, doing her best not to get noticed while putting on her swim suit. She flinches as she sees you."
    menu:
        "Leave her alone.":
            "You turn around and walk to the other side of the pool."

        "Wave at her.":
            $ morale -= 1
            "You give her a little waive, and walk right past her."

        "Peek-a-boo." if new_game_plus == True:
            $ inhibition += 1
            "You put your hands in front of your face, and then spread your fingers. You laugh at your own move. The girl tries to cover her body and respond with a somewhat embarrassed smile."
    return
            
            
label pool10:
    
    scene pool10 with fade
    "When a teacher shows up, some get nervous. Don't worry girls, just checking that everything's fine."
    $ inhibition += 1
    return
    
    
label pool11:
    
    scene pool11 with fade
    pov "Having a pool sure brings out the best in the students!"
    $ morale += 1
    return


label pool12:
    if renpy.random.randint(1,2) == 1:
        scene pool12-1 with fade
    else:
        scene pool12-2 with fade
    "You catch a good glimpse of a cute girl just as she gets out of the pool."
    return


label pool13:
    
    if inhibition > 90:
        scene pool13-1 with fade
    else:
        scene pool13-2 with fade
    "One of the older students makes fun of a younger one's bust size. Don't be like that, all sizes are fine!"
    $ behavior -= 1
    $ morale -= 1
    return


label pool14:
    
    scene pool14-1 with fade
    "It's nice to see the students start to spend more of their spare time in the pool."
    $ inhibition -= 1
    return


label pool15:
    
    scene pool15 with fade
    "When you're young, it's hard to get everything in place. School, friends, boys - *sigh*"
    $ morale -= 1
    return
    
    
label pool16:
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("pool16_"+randImg)
    with fade
    
    if renpy.random.randint(1,2) == 1:
        "If you're gonna make the swim team, better work on those strokes."
    else:
        "Some of these girls really are like dolphins.\nCute, wet and taste like fish."
    $ athletics += 1
    return
    

label pool17:
    
    scene pool17 with fade
    "Those modern bathing suits keep moving upward. Better take time to pull and release."
    python:
        if renpy.random.randint(1,3) == 1:
            inhibition += 1
        else:
            athletics += 1
    return
    
    
label pool18:
    
    scene pool18 with fade
    "Experimenting with your bathing suit can earn you valuable seconds!"
    python:
        if renpy.random.randint(1,3) == 1:
            inhibition += 1
        else:
            athletics += 1
    return
    

label pool19:
    
    if renpy.random.randint(1,2) == 1:
        scene pool19-1 with fade
    else:
        scene pool19-2 with fade
    if renpy.random.randint(1,2) == 1:
        "When they see you closing in, they freeze. Those foolish kids!"
    else:
        "Seems like some students rather play around in the pool rather than use it for exercise."
    $ deviance += 1
    return


label pool20:
    
    scene pool20 with fade
    "Wet girls are good girls."
    $ inhibition -= 1
    return
    
    
label pool21:
    
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("pool21_"+randImg)
    with fade
    "One of the girls got a mouthful of water. Are you alright?"
    $ morale -= 1
    return
    
    
label pool22:
    
    scene pool22 with fade
    "You meet the eyes of a girl trying to get some sun after a nice dip in the pool. Such beautiful... eyes..."
    $ inhibition -= 1
    return


label pool23:
    
    scene pool23 with fade
    "HEY! Girls only!"
    python:
        if renpy.random.randint(1,3) == 1:
            reputation -= 1
        else:
            morale -= 1
    return


label pool24:
    
    "It's getting late, perhaps a dip in the pool before going home?"
    scene pool24-1 with fade
    girl "Oh, hello there [povTitle] [povLastName]."
    "Apparently, this young girl was in the same mindset."
    girl "Nice evening, don't ya think?"
    pov "Yeah, it's nice. What are you doing here this late?"
    girl "I know everybody's probably on their way home, but I wanted to have some quality time just by myself."
    pov "Can't say I blame you."
    girl "Funny to run into you here [povTitle] [povLastName], were you thinking the same as me?"
    pov "You got me kid."
    girl "* giggle * That's what my daddy use to say."
    pov "Is that so?"
    menu:
        "I bet I can show you a few tricks that daddy doesn't know about.":
            girl "..."
            pov "I mean..."
            "She gets up from the water and walks away."
            pov "Oh daddy..."

        "Sounds like a good man":
            girl "He's the best! Say, wanna race to the other side?"
            pov "Sure, I'll go easy on you."
            girl "HA!"
            "You race her and of course, you win. As you celebrate in the shower you accidentally rub against her butt..."
            girl "Oh!"
            pov "Sorry, I got carried away there for a while."
            girl "It's ok, you are the winner after all. * giggle *"
            scene pool24-2
            "In the spur of the moment, you pull her back to you and grab her tits. She seems a bit shocked, but doesn't really fight it."
            girl "Ah, you have to be gentle, you... aaah!" 
            pov "Hush now and let the winner collect his reward."
            scene pool24-3
            "With a swift grip you maneuver her against the shower and at the same time pull her pants to the side."
            girl "Hey! This wasn't part of the plan!"
            pov "I can tell you're not much of a planner, are you?"
            "She lets you have your way, maybe she's afraid of what you'd do if she refused. The thought only makes you more aroused, and you come deep inside her."
            girl "No..."
            pov "Yes!"
            "A nice evening indeed."
            $ deviance += 1
    $ morale -= 1
    $ inhibition += 1
    return


label pool25:
    
    scene pool25 with fade
    "When you've got a body built to gather attention, don't be surprised if an extra pair of hands suddenly shows up."
    $ deviance += 1
    return


label pool26:
    
    scene pool26 with fade
    "Be sure to get out of the water before you get all wrinkled!"
    return


label pool27:
    
    scene pool27 with fade
    "Try to leave that competitive feeling behind once practice is over."
    $ behavior -= 1
    return


label pool28:
    
    scene pool28 with fade
    pov "Nothing compares to being compared, right girls?"
    girls "..."
    $ inhibition -= 1
    $ morale -= 1
    return


label pool29:
    
    scene pool29 with fade
    "It's important to be well equipped!"
    $ athletics -= 1
    return


label pool30:
    
    scene pool30 with fade
    "Hey, why use a towel when you can let the sun dry your body."
    $ inhibition -= 1
    return


label pool31:
    
    scene pool31 with fade
    "It's important to give your body a treat after a hard days training. Poolside massage, anyone?"
    if renpy.random.randint(1,2) == 1:
        $ inhibition -= 1
    else:
        $ morale += 1
    return


label pool32:
    
    scene pool32:
        pos (0.0, 0.0)
        linear 10.0 pos (0.0, -1.5)
        linear 10.0 pos (0.0, -0.0)
    with fade
    "The girls can be pretty rough if you don't follow the gangs code of conduct. I wonder what she did?"
    $ behavior -= 1
    $ morale -= 1
    return


label pool33:
    
    scene pool33 with fade
    "When you thought you couldn't get any wetter..."
    pov "Don't forget to wet yourself on the inside as well."
    girl "..."
    $ inhibition -= 1
    return


label pool34:
    
    scene pool34 with fade
    if renpy.random.randint(1,2) == 1:
        "A good swim can really take it's toll on you."
    else:
        "Training hard and staying fit. Some students really take it to the next level."
    return


label pool35:
    
    scene pool35 with fade
    if renpy.random.randint(1,2) == 1:
        "Sometimes you just need to relax and take a break."
    else:
        "Her flirtatious eyes and great body sure is easy on the eyes."
    return


# NOTE: 
label pool36:
    scene pool with fade
    "While taking a strut around the pool you find a particularly attractive girl and decide to talk to her."
    if (inhibition - renpy.random.randint(1,10 ) ) > 80:
        show brunette_bikini:
            pos (0.35, 0.0)
            zoom 0.3
            pause 0.1
            linear 10.0 zoom 1.0 pos (0.2, -0.2)
        "As you walk towards her you can see how she starts to blush."
        menu:
            "Talk to her":
                pov "Hello there miss!"
                girl "Hello [povTitle] [povLastName]!"
                pov "How's everything?"
                girl "Umm, it's good I guess."
                "I better leave before this get awkward."
                
            "Inspect her assets":
                show brunette_bikini:
                    linear 5.0 zoom 1.0 pos (0.2, -0.5)
                "Looks good indeed."
                girl "Umm... [povLastName]?"
                menu:
                    "Take a closer look":
                        show brunette_bikini:
                            linear 5.0 zoom 1.25 pos (0.15, -0.75)
                        "Wow, these are godsend..."
                        girl "Eh... Ummm... [povTitle] [povLastName]?"
                        "I wonder if they are real..?"
                        girl "Hello? Is something wrong?"
                        menu:
                            "Touch them":
                                girl "AH!"
                                "Hmm, feels real alright... Guess they just grow up faster these days..."
                                $ inhibition += 1
                                $ morale -= 1

                            "Maybe not":
                                pov "Oh, sorry, did you say something?"
                                girl "Umm..."
                                pov "I like your bikini!"
                                girl "Yeah... I kinda noticed..."
                                pov "Anyway, keep up the good work!"
                                $ inhibition += 1
    else:
        show swimsuit:
            pos (0.35, 0.0)
            zoom 0.4
            pause 0.1
            linear 10.0 zoom 1.0 pos (0.2, -0.2)
        "As you walk towards her you can see how she starts to blush with a wry smile."
        menu:
            "Talk to her":
                pov "Hello there miss!"
                girl "Oh, good day [povTitle] [povLastName]!"
                pov "How's everything?"
                girl "It's much better with you here."
                pov "Oh, thank you."
                
            "Inspect her assets":
                show swimsuit:
                    linear 5.0 zoom 1.0 pos (0.2, -0.5)
                "Looks good indeed."
                girl "*giggle* [povTitle] [povLastName]?"
                menu:
                    "Take a closer look":
                        show swimsuit:
                            linear 5.0 zoom 1.25 pos (0.15, -0.75)
                        "Wow, that cleavage..."
                        girl "Are they really that good [povLastName]?"
                        "I wonder if they are real..?"
                        girl "*giggle* Is anybody home?"
                        menu:
                            "Touch them":
                                girl "Ah... Geeze... Grow up already!"
                                "Hmm, feels real alright... Guess they just grow up faster these days..."
                                $ inhibition -= 1
                                $ morale -= 1

                            "Maybe not":
                                show swimsuit:
                                    linear 2.5 zoom 1.25 pos (0.15, -0.3)
                                pov "Oh, sorry, did you say something?"
                                girl "*giggle* A lot on your mind today?"
                                pov "Yeah... It's hard work being principal."
                                girl "Yeah *giggle* I can see that."
                                pov "Anyway, have a good day."
                                $ inhibition -= 1
    return


label pool37:
    "As you enter the changing rooms you see lone busty girl and you decide to sneak up on her."
    scene pool37-1 with fade
    girl "Ah!"
    pov "Shh, little mouse, don't make a squeak."
    scene pool37-2
    girl "Umm.... W-what are you doing?"
    pov "Don't you worry, I'm just inspecting your assets."
    girl "Ah, do-don't touch me like that!"
    pov "Shh, just pretend I'm your boyfriend and enjoy this."
    girl "... B-but I don't have... Mhm, a-a boyfriend..."
    scene pool37-3
    girl "Mhmm, WAAH! Don't rip it off like that!"
    pov "You're sure blessed with a fine body."
    girl "Ehmm, Mhmm... Th-thank you... Ah, ahh... \nAh, my-my nipples... Mhmm."
    scene pool37-4
    girl "Mhmm, th-this... Ah, not so-Mhmm... bad..."
    pov "Then you'll like this."
    scene pool37-5
    girl "AH! Mhmm, s-slow... Mhmm! Ah! *pant* P-please... Mhmm..."
    pov "Are you getting wet and slippry down there?"
    girl "*blush* Eh.... Mhmm... N-no... AH! Ahhh..."
    pov "Be honest little mouse I am sure you're plenty wet and slippery right now. Let's take a look shall we?"
    scene pool37-6
    girl "N-no!! AH! Mhmm... Y-yea--Ah!"
    pov "I told you so. Wet and slippery. Getting horny by being a harassed by a stranger?"
    girl "Mhmm.. N-no... Ah! Th-thats-AH! Hmm.. No-not-AH-AH! Mhmm..."
    pov "It feels like a little mouse is cumming."
    girl "*pant* Ah, Mhmm, AH! AHHH!"
    scene pool37-7
    pov "My work here is done little mouse. Now take a shower and clean yourself up. And remember, don't look back."
    girl "*pant* *pant* Mhmm...."
    return

    