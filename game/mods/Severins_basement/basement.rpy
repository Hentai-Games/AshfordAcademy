image bg black = "mods/Severins_basement/basement/black.jpg"
image adventurer = "mods/Severins_basement/basement/adventurer.jpg"
image adventurer2 = "mods/Severins_basement/basement/adventurer2.jpg"
image basement23 = "mods/Severins_basement/basement/awhile.jpg"
image basement6 = "mods/Severins_basement/basement/basement 1.jpg"
image basement7 = "mods/Severins_basement/basement/basement 2.jpg"
image basement8 = "mods/Severins_basement/basement/basement 3.jpg"
image basement9 = "mods/Severins_basement/basement/basement 4.jpg"
image basement10 = "mods/Severins_basement/basement/basement 5.jpg"
image basement11 = "mods/Severins_basement/basement/basement 6.jpg"
image basement12 = "mods/Severins_basement/basement/basement 7.jpg"
image basement13 = "mods/Severins_basement/basement/basement 8.jpg"
image basement26 = "mods/Severins_basement/basement/basement 9.jpg"
image basement14 = "mods/Severins_basement/basement/Bondage.jpeg"
image basement15 = "mods/Severins_basement/basement/Bondage 2.jpg"
image basement21 = "mods/Severins_basement/basement/Broken.jpg"
image broken2 = "mods/Severins_basement/basement/broken2.jpg"
image bulge1 = "mods/Severins_basement/basement/bulge1.jpg"
image bulge2 = "mods/Severins_basement/basement/bulge2.jpg"
image cutpanty = "mods/Severins_basement/basement/cutpanty.jpeg"
image data = "mods/Severins_basement/basement/data.png"
image doublefellatio = "mods/Severins_basement/basement/doublefellatio.jpg"
image drug = "mods/Severins_basement/basement/drug.jpg"
image finfound = "mods/Severins_basement/basement/finally found.jpg"
image flooded = "mods/Severins_basement/basement/flooded.jpg"
image basement16 = "mods/Severins_basement/basement/Group.jpg"
image group2 = "mods/Severins_basement/basement/group2.jpg"
image helpless = "mods/Severins_basement/basement/helpless.jpg"
image mio1 = "mods/Severins_basement/basement/mio1.png"
image mio2 = "mods/Severins_basement/basement/mio2.png"
image mio3 = "mods/Severins_basement/basement/mio3.png"
image mio4 = "mods/Severins_basement/basement/mio4.png"
image mummy = "mods/Severins_basement/basement/mummy.jpeg"
image new1 = "mods/Severins_basement/basement/new1.jpg"
image new2 = "mods/Severins_basement/basement/new2.jpg"
image new3 = "mods/Severins_basement/basement/new3.jpg"
image new4 = "mods/Severins_basement/basement/new4.jpg"
image new5 = "mods/Severins_basement/basement/new5.jpg"
image orgy = "mods/Severins_basement/basement/orgy.jpg"
image basement17 = "mods/Severins_basement/basement/Pimp.jpg"
image pokemon1 = "mods/Severins_basement/basement/pokemon1.jpg"
image pokemon2 = "mods/Severins_basement/basement/pokemon2.jpg"
image pokemon3 = "mods/Severins_basement/basement/pokemon3.jpg"
image basement22 = "mods/Severins_basement/basement/PoorChoice.jpg"
image basement19 = "mods/Severins_basement/basement/Punish.jpeg"
image basement18 = "mods/Severins_basement/basement/punishment.jpg"
image basement20 = "mods/Severins_basement/basement/Restrained.jpg"
image basement1 = "mods/Severins_basement/basement/safe 1.jpg"
image basement2 = "mods/Severins_basement/basement/safe 2.jpg"
image basement3 = "mods/Severins_basement/basement/safe 3.jpg"
image basement4 = "mods/Severins_basement/basement/safe 4.jpg"
image basement5 = "mods/Severins_basement/basement/safe 5.jpg"
image basement24 = "mods/Severins_basement/basement/safe 6.jpg"
image basement25 = "mods/Severins_basement/basement/safe 7.jpg"
image asleep = "mods/Severins_basement/basement/sleeping.jpg"
image smoker = "mods/Severins_basement/basement/smoker.png"
image threesome = "mods/Severins_basement/basement/threesome.jpeg"
image tornclothes = "mods/Severins_basement/basement/tornclothes.png"
image basementtraining = "mods/Severins_basement/basement/training.jpeg"
image basetrifellatio = "mods/Severins_basement/basement/trifellatio.jpeg"
image vulnerable = "mods/Severins_basement/basement/vulnerable.jpg"
image waybig = "mods/Severins_basement/basement/waybig.jpg"

define building_basement = 0
define basement_detention = 0

init 900:
    
    
    
    python:
        buildings.append({"name": "basement",       "cost" : [100, 200, 300, 400, 500, 0],         "requirement": "1 == 1",        "image": "mods/Severins_basement/buildings/basement.jpg",    "description": "Opens up the labyrinth below the campus. \n\nEach purchase opens up more and more of the labyrinth and cleans it up.  \n\nIt costs {b}[building_cost]{/b} to buy and {b}100{/b} per month."})
        buyables.append({"name": "basement_detention",              "requirement": "basement_detention == 0 and building_basement > 0",                           "cost": [0,0,0,0,0,40,0],       "image": "mods/Severins_basement/buildings/basement_detention.jpg",        "description": "Send the naughty female students into the basement, and hire some 'Minotaurs' to patrol the corridors.\nUnlocks Basement detention."})
        policy_choices.append({"label":"pda_rules","text":"Basement Detention - To the Labyrinth.","requirement":"basement_detention > 0","action":"[SetVariable('pda_rules', 'pda_basement'), SetVariable('pda_rule_level', 6)]"})
        
        def basementPlannerChoices():
            if (building_basement > 0):
                dp_choice("Basement", "basement","Afternoon")
        
        modDayPlannerFunctions.append(basementPlannerChoices)
    
    $ event("basement1", "act == 'basement' and building_basement < 3", event.choose_one('basement'), priority=200)
    $ event("basement2", "act == 'basement' and building_basement > 2", event.choose_one('basement'), priority=200)
    $ event("basement3", "act == 'basement' and building_basement > 2", event.choose_one('basement'), priority=200)
    $ event("basement4", "act == 'basement' and building_basement > 3", event.choose_one('basement'), priority=200)
    $ event("basement5", "act == 'basement' and building_basement > 2", event.choose_one('basement'), priority=200)
    $ event("basement6", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement7", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement8", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement9", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement10", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement11", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement12", "act == 'basement' and building_basement > 2 and deviance >20 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement13", "act == 'basement' and building_basement > 3 and deviance > 30 and behavior < 50", event.choose_one('basement'), priority=200)
    $ event("basement14", "act == 'basement' and building_basement > 3 and deviance > 30 and behavior < 50 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement15", "act == 'basement' and building_basement > 2 and deviance > 5 and inhibition < 70 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement16", "act == 'basement' and building_basement > 3 and deviance > 30 and behavior < 50 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement17", "act == 'basement' and building_basement > 3 and deviance > 30 and behavior < 50 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement18", "act == 'basement' and building_basement > 3 and deviance > 30", event.choose_one('basement'), priority=200)
    $ event("basement19", "act == 'basement' and building_basement > 3 and deviance > 40 and behavior < 75 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement20", "act == 'basement' and building_basement > 3 and deviance > 25 and behavior < 60 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement21", "act == 'basement' and building_basement > 3 and deviance > 30 and behavior < 40 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement22", "act == 'basement'", event.choose_one('basement'), priority=200)
    $ event("basement23", "act == 'basement' and building_basement > 2", event.choose_one('basement'), priority=200)
    $ event("basement24", "act == 'basement' and building_basement > 3 and deviance > 50 and behavior < 50 and basement_detention > 0", event.choose_one('basement'), priority=200)
    $ event("basement25", "act == 'basement' and building_basement > 2", event.choose_one('basement'), priority=200)
    
    
label basement1:
    
    scene bg black with fade
    show basement1 at center
    "The basement is filled with clutter."
    return
    
label basement2:
    
    scene bg black with fade
    $ basement = renpy.random.choice(['basement2', 'basement25'])
    $ renpy.show(basement, at_list=[center])
    "It seems as if someone is starting their own private library down here."
    $ academics += 2
    $ academics += 5
    $ behavior -= 1
    return

label basement3:
    
    scene bg black with fade
    show basement3 at center
    "A student has decided to take advantage of an empty room to study."
    $ academics += 1
    $ academics += 5
    return
    
label basement4:
    
    scene bg black with fade
    show basement4 at center
    "A student has managed to set up a functional recording studio down here."
    $ artistery += 2
    $ artistery += 5
    return
    
label basement5:
    
    scene bg black with fade
    $ basement = renpy.random.choice(['basement5', 'basement24'])
    $ renpy.show(basement, at_list=[center])
    "It seems like this student is ready to live down here."
    $ behavior -= 1
    $ morale += 1
    return
    
label basement6:
    
    scene bg black with fade
    $ basement = renpy.random.choice(['basement6', 'new1', 'new2', 'new3', 'new4', 'new5', 'basement9', 'helpless'])
    $ renpy.show(basement, at_list=[center])
    "Some of the female students don't get very far in the labyrinth before they're fucked."
    $ morale -= 2
    $ deviance += 5
    return
    
label basement7:
    
    scene bg black with fade
    $ basement = renpy.random.choice(["basement7", 'basement8', 'flooded'])
    $ renpy.show(basement, at_list=[center])
    "Poor girl.  She probably didn't see it cumming."
    $ deviance += 5
    $ morale -= 1
    $ deviance += 1
    return
    
label basement8:
    
    scene bg black with fade
    show basement9 at center
    "It looks like she really enjoyed it."
    $ deviance += 5
    $ deviance += 3
    return
    
label basement9:
    
    scene bg black with fade
    show basement10 at center
    "This girl has found her true self."
    $ deviance += 5
    $ deviance += 3
    return
    
label basement10:
    
    scene bg black with fade
    $ basement = renpy.random.choice(["basement11", 'basement16', 'basement12'])
    $ renpy.show(basement, at_list=[center])
    "This girl seems like she is enjoying herself."
    $ deviance += 5
    $ deviance += 2
    $ inhibition -= 3
    $ morale += 2
    return
    
label basement11:
    
    scene bg black with fade
    $ basement = renpy.random.choice(["basement13", 'basement22'])
    $ renpy.show(basement, at_list=[center])
    "This cheerleader chose the wrong guys to piss off."
    $ deviance += 5
    $ morale -= 2
    $ behavior -= 1
    $ deviance += 2
    return
    
label basement12:
    
    scene bg black with fade
    $ basement = renpy.random.choice(["basement14", 'basement18', 'basement19', 'basement20', 'basement15'])
    $ renpy.show(basement, at_list=[center])
    "This girl is recieving a full course punishment."
    $ morale -= 2
    $ behavior += 3
    $ deviance += 5
    $ deviance += 2
    return
    
label basement13:
    
    scene bg black with fade
    show basement17 at truecenter
    "Some students like the basement so much, that they start new lives in the labyrinth."
    $ behavior -= 2
    $ morale += 2
    $ deviance += 5
    $ deviance += 2
    $ reputation -= 1
    return

label basement14:
    
    scene bg black with fade
    $ basement = renpy.random.choice(["basement21", 'basement23', 'finfound', 'broken2'])
    $ renpy.show(basement, at_list=[truecenter])
    "It appears these girls have been down here for a while."
    $ behavior += 1
    $ morale += 1
    $ deviance += 5
    $ deviance += 1
    return
    
label basement15:
    
    scene bg black with fade
    $ adventure = renpy.random.choice(["adventurer", 'adventurer2', 'cutpanty'])
    $ renpy.show(adventure, at_list=[truecenter])
    "Rule#5 of Dungeon-Crawling: Never lower your guard in a labyrinth."
    $ behavior -= 2
    $ morale -= 1
    $ deviance += 1
    $ inhibition -= 2
    return
    
label basement16:
    
    scene bg black with fade
    $ caught = renpy.random.choice(["helpless", 'drug', 'tornclothes', 'threesome'])
    $ renpy.show(caught, at_list=[truecenter])
    "Poor girl.  She managed to escape once, but it doesn;t look like its going to happen again."
    $ behavior += 2
    $ morale -= 2
    $ deviance == 2
    return
    
label basement17:
    
    scene bg black with fade
    $ bigger = renpy.random.choice(["waybig", 'bulge1', 'bulge2', 'new4', 'new3'])
    $ renpy.show(bigger, at_list=[truecenter])
    if renpy.random.random() > .5:
        "Girls that are sent to the basement learn very quickly how much can fit in their pussies."
    else:
        "This girl found out she can fit alot more in her pussy than she ever thought possible."
    $ deviance += 2
    $ morale -= 3
    $ behavior += 1
    return
    
label basement18:
    
    scene bg black with fade
    show data at truecenter
    "Looks like this girl is being used as a test subject for some aphrodasiacs."
    $ deviance += 2
    $ behavior -= 1
    return
    
label basement19:
    
    scene bg black with fade
    show doublefellatio at truecenter
    "These two girls no longer have any qualms with sucking someone off."
    $ deviance += 3
    $ inhibition -= 2
    return
    

label basement20:
    
    scene bg black with fade
    $ enjoyment = renpy.random.choice(["group2", 'orgy', 'basementtraining'])
    $ renpy.show(enjoyment, at_list=[truecenter])
    "After enough training, even the most virtuous girls begin to enjoy sex."
    $ behavior += 3
    $ deviance += 2
    $ inhibition -= 3
    return
    
label basement21:
    
    scene bg black with fade
    show pokemon1 at truecenter
    "Since this girl has resisted her training thus far, her captors are resorting to more intense methods."
    hide pokemon1
    show pokemon2 at truecenter
    "They're going to marinate her entire body in semen, until she can't live without it."
    hide pokemon2
    show pokemon3 at truecenter
    "It doesn't look like she'll last very long."
    $ behavior += 2
    $ deviance += 2
    return
    
label basement22:
    
    scene bg black with fade
    show smoker at truecenter
    "It looks like this girl snuck off into the basement for a private smoke.  Do you..."
    menu:
        "Reprimand her":
            "You decide to reprimand her, sending her back to class with an ashamed look on her face."
            if renpy.random.random() > .5:
                "You doubt that it really did anything, but it was worth a shot trying to stop her."
                $ behavior += 2
                $ morale -= 2
                $ reputation += 2
            else:
                "You feel like she has learned her lesson."
                $ behavior += 3
                $ reputation += 2
                $ morale -= 2
        "Let it go":
            "You decide to let her have her smokes."
            $ behavior -= 3
            $ reputation -= 1
            if renpy.random.random() > .5:
                if deviance < 20:
                    "As you leave, she sees you and gives you a grateful nod of the head."
                    $ inhibition -= 2
                else:
                    "As you leave, she sees you and gives you a sultry smile and winks."
                    $ deviance += 1
            else:
                "You leave without her seeing you."
        "Encourage it":
            "You walk over to her and congratulate her on finding a scluded spot to enjoy her smokes."
            "She looks a t you confused, and you tell her she should try smoking around school more often."
            "You leave with her trying to figure out why you would say that."
            $ behavior -= 2
            $ reputation -= 2
        "Ask for one" if new_game_plus == True:
            "You go up to her and ask if you may partake in a smoke as well."
            $ reputation -= 1
            $ morale += 2
            $ behavior -= 2
            $ inhibition -= 3
            if deviance > 20:
                "She doesn't have a problem with you asking for a smoke and offers the one in her mouth."
                "You thank her and take a nice long draw on the cigarette."
                "You hand it back and thank her again.  As you leave, you see her stick the cigarette back in her mouth and smile."
                $ deviance += 3
            else:
                "Looking surprised, she quickly pulls out a fresh cigarette and hand it to you."
                "You thank her and  pull out your own lighter."
                "After you take a few long draws, you hand the cigarette back to her and thank her again."
                $ deviance += 2
                $ inhibition -= 1
        "ALCOHOL!" if start_day_with_gin == True:
            "Running up to her, you yell about how cigarettes are unhealthy."
            girl "I'm sorry Mr. [povLastName]!  I'm sorry!  It's just that... I'm... addicted."
            pov "As long as you understand the harmful effects of cigarettes.  As for your addiction, I got something to help."
            girl "What is it Mr. [povLastName]?  Can it help me?"
            pov "It's a bottle of gin!  It will cure any other addictions you may have!"
            girl "Gin sir?  Are you sure."
            pov "Absolutely!  Nothing is better."
            girl "If you say so... I'll try it."
            pov "Atta girl.  Here you go."
            "The girl takes a sip and immediately begins to flush.  At your encouragement, she quickly drains half the bottle."
            $ behavior -= 2
            $ reputation -= 2
            $ morale += 3
            if deviance > 30:
                pov "Now how are you feeling?"
                girl "I feel... so... HOT!  Please fuck me now Mr. [povLastName]!"
                pov "Whatever you say!"
                $ mio = renpy.random.choice(["mio1", 'mio2', 'mio3', 'mio4'])
                $ renpy.show(mio, at_list=[truecenter])
                "You fuck the girl for the rest of the hour, filling her to the brim with alcohol and cum."
                $ deviance += 3
                $ inhibition -= 1
            else:
                "The two of you spend the rest of the school day drinking."
                $ inhibition -= 3
                $ deviance += 1
    return

label basement23:
    
    scene bg black with fade
    show vulnerable at truecenter
    if deviance < 20:
        "This girl seems to have made herself at home in the basement."
        $ morale += 3
    elif deviance < 50:
        "This girl is apparently not aware of the dangers of turning her back to the door."
        $ inhibition -= 3
        $ deviance += 1
    else:
        "Looks like this girl is just waiting to be fucked."
        menu:
            "Oblige her":
                "You fuck the unwary girl until late, never letting her see your face."
                if renpy.random.random() > .4:
                    "She really seemed to enjoy it, even begging you to cum inside at the end."
                    $ morale += 2
                    $ deviance += 2
                    $ inhibition -= 3
                    $ deviance += 10
                else:
                    "She seems to not have been ready and fought the entire time until you came deep inside her womb."
                    $ morale -= 3
                    $ deviance += 2
                    $ deviance += 5
            "Leave her be":
                "You leave her for someone else to find."
                $ inhibition -= 3
                $ deviance += 2
    return
    
label basement24:
    
    scene bg black with fade
    show basetrifellatio at truecenter
    "One of the main slavers was moving out of town and gifted you with three of his best slaves."
    "They don't resistagainst your orders."
    $ deviance += 3
    $ inhibition -= 2
    $ behavior += 1
    return
    
label basement25:
    
    scene bg black with fade
    show mummy at truecenter
    "Looks like this girl is practicing her mummy role in the latest play."
    $ artistery += 5
    $ morale += 2
    if inhibition < 70:
        "Looks like she went for the authentic look... no panties."
        $ inhibition -= 2
    return
    
    
    
    
    