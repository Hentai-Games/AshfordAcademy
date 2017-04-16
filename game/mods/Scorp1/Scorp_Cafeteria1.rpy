#### SCORP EVENT PACK 1 - Cafeteria ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this. 
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Cafeteria.
## Pictures are located in the subdirectory \Scorp1\Cafeteria
## All custom images, characters, variables... are prefixed with "scorp_" (with the exception of temp variables) to avoid conflicts.
## Please PLEASE note that *all* scenarios in this mod are intended to involve (fictional) characters over the age of 18.
#### SETUP ####

#Define characters
#Characters go here if needed

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

image bg scorp_cafeteria1 = "mods/Scorp1/Cafeteria/scorp_cafeteria1.jpg"
image bg scorp_cafeteria2 = "mods/Scorp1/Cafeteria/scorp_cafeteria2.jpg"
image bg scorp_cafeteria3 = "mods/Scorp1/Cafeteria/scorp_cafeteria3.jpg"
image bg scorp_cafeteria4 = "mods/Scorp1/Cafeteria/scorp_cafeteria4.jpg"
image bg scorp_cafeteria5 = "mods/Scorp1/Cafeteria/scorp_cafeteria5.jpg"
image bg scorp_cafeteria6 = "mods/Scorp1/Cafeteria/scorp_cafeteria6.jpg"
image bg scorp_cafeteria7 = "mods/Scorp1/Cafeteria/scorp_cafeteria7.jpg"
image bg scorp_cafeteria8 = "mods/Scorp1/Cafeteria/scorp_cafeteria8.jpg"
image bg scorp_cafeteria9 = "mods/Scorp1/Cafeteria/scorp_cafeteria9.jpg"
image bg scorp_cafeteria10 = "mods/Scorp1/Cafeteria/scorp_cafeteria10.jpg"
image bg scorp_cafeteria11 = "mods/Scorp1/Cafeteria/scorp_cafeteria11.jpg"
image bg scorp_cafeteria12 = "mods/Scorp1/Cafeteria/scorp_cafeteria12.jpg"
image bg scorp_cafeteria13_1 = "mods/Scorp1/Cafeteria/scorp_cafeteria13_1.jpg"
image bg scorp_cafeteria13_2 = "mods/Scorp1/Cafeteria/scorp_cafeteria13_2.jpg"
image bg scorp_cafeteria14 = "mods/Scorp1/Cafeteria/scorp_cafeteria14.jpg"
image bg scorp_cafeteria15 = "mods/Scorp1/Cafeteria/scorp_cafeteria15.jpg"
image bg scorp_cafeteria16_1 = "mods/Scorp1/Cafeteria/scorp_cafeteria16_1.jpg"
image bg scorp_cafeteria16_2 = "mods/Scorp1/Cafeteria/scorp_cafeteria16_2.jpg"
image bg scorp_cafeteria17 = "mods/Scorp1/Cafeteria/scorp_cafeteria17.jpg"
image bg scorp_cafeteria18 = "mods/Scorp1/Cafeteria/scorp_cafeteria18.jpg"
image bg scorp_cafeteria19 = "mods/Scorp1/Cafeteria/scorp_cafeteria19.jpg"
image bg scorp_cafeteria20 = "mods/Scorp1/Cafeteria/scorp_cafeteria20.jpg"
image bg scorp_cafeteria21 = "mods/Scorp1/Cafeteria/scorp_cafeteria21.jpg"
image bg scorp_cafeteria22 = "mods/Scorp1/Cafeteria/scorp_cafeteria22.jpg"
image bg scorp_cafeteria23_1 = "mods/Scorp1/Cafeteria/scorp_cafeteria23_1.jpg"
image bg scorp_cafeteria23_2 = "mods/Scorp1/Cafeteria/scorp_cafeteria23_2.jpg"
image bg scorp_cafeteria24 = "mods/Scorp1/Cafeteria/scorp_cafeteria24.jpg"
image bg scorp_cafeteria25 = "mods/Scorp1/Cafeteria/scorp_cafeteria25.jpg"
image bg scorp_cafeteria26 = "mods/Scorp1/Cafeteria/scorp_cafeteria26.jpg"
image bg scorp_cafeteria27 = "mods/Scorp1/Cafeteria/scorp_cafeteria27.jpg"
image bg scorp_cafeteria28 = "mods/Scorp1/Cafeteria/scorp_cafeteria28.jpg"
image bg scorp_cafeteria29 = "mods/Scorp1/Cafeteria/scorp_cafeteria29.jpg"
image bg scorp_cafeteria30 = "mods/Scorp1/Cafeteria/scorp_cafeteria30.jpg"
image bg scorp_cafeteria31 = "mods/Scorp1/Cafeteria/scorp_cafeteria31.jpg"
image bg scorp_cafeteria32 = "mods/Scorp1/Cafeteria/scorp_cafeteria32.jpg"
image bg scorp_cafeteria33 = "mods/Scorp1/Cafeteria/scorp_cafeteria33.jpg"
image bg scorp_cafeteria34 = "mods/Scorp1/Cafeteria/scorp_cafeteria34.jpg"
image bg scorp_cafeteria35 = "mods/Scorp1/Cafeteria/scorp_cafeteria35.jpg"
image bg scorp_cafeteria36 = "mods/Scorp1/Cafeteria/scorp_cafeteria36.jpg"
image bg scorp_cafeteria37 = "mods/Scorp1/Cafeteria/scorp_cafeteria37.jpg"
image bg scorp_cafeteria38 = "mods/Scorp1/Cafeteria/scorp_cafeteria38.jpg"
image bg scorp_cafeteria39 = "mods/Scorp1/Cafeteria/scorp_cafeteria39.jpg"
image bg scorp_cafeteria40 = "mods/Scorp1/Cafeteria/scorp_cafeteria40.jpg"

#Setting up events and conditions

init:
    $ event("scorp_cafeteria1", "act == 'cafeteria' and deviance > 80", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria2", "act == 'cafeteria' and deviance > 95 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria3", "act == 'cafeteria' and inhibition < 15", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria4", "act == 'cafeteria' and inhibition < 55 and inhibition > 20", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria5", "act == 'cafeteria' and deviance > 95 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria6", "act == 'cafeteria' and deviance > 65 and deviance < 95", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria7", "act == 'cafeteria' and uniform == 'nude_uniform'", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria8", "act == 'cafeteria' and deviance > 95 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria9", "act == 'cafeteria' and deviance > 35 and deviance < 70", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria10", "act == 'cafeteria' and deviance < 50", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria11", "act == 'cafeteria' and deviance < 60", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria12", "act == 'cafeteria' and deviance < 70 and academics > 50", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria13", "act == 'cafeteria' and inhibition < 25 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria14", "act == 'cafeteria' and deviance > 40 and deviance < 70", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria15", "act == 'cafeteria' and deviance > 5 and deviance < 60", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria16", "act == 'cafeteria' and inhibition < 60 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria17", "act == 'cafeteria' and inhibition > 60", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria18", "act == 'cafeteria' and inhibition > 20 and inhibition < 80", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria19", "act == 'cafeteria' and deviance > 95 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria20", "act == 'cafeteria' and deviance > 10 and deviance < 60", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria21", "act == 'cafeteria' and morale > 60 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria22", "act == 'cafeteria' and deviance > 85 and uniform == 'nude_uniform'", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria23", "act == 'cafeteria' and inhibition < 95", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria24", "act == 'cafeteria' and inhibition < 80 and inhibition > 30", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria25", "act == 'cafeteria' and uniform == 'nude_uniform'", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria26", "act == 'cafeteria' and deviance > 80", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria27", "act == 'cafeteria' and inhibition < 18", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria28", "act == 'cafeteria' and deviance > 85 and inhibition < 20", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria29", "act == 'cafeteria' and deviance > 98 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria30", "act == 'cafeteria' and deviance < 25", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria31", "act == 'cafeteria' and deviance < 45", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria32", "act == 'cafeteria' and academics < 55 and deviance < 75", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria33", "act == 'cafeteria' and morale < 45 and inhibition > 40", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria34", "act == 'cafeteria' and deviance > 70 and deviance < 90", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria35", "act == 'cafeteria' and deviance > 80 and inhibition < 30 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria36", "act == 'cafeteria' and deviance > 90 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria36", "act == 'cafeteria' and deviance > 90 and inhibition < 10", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria37", "act == 'cafeteria' and deviance > 95 and inhibition < 10", event.choose_one('cafeteria'), priority=200) 
    $ event("scorp_cafeteria38", "act == 'cafeteria' and deviance < 60", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria39", "act == 'cafeteria' and inhibition < 70 and inhibition > 25", event.choose_one('cafeteria'), priority=200)
    $ event("scorp_cafeteria40", "act == 'cafeteria' and inhibition < 75 and inhibition > 25", event.choose_one('cafeteria'), priority=200)
    
label scorp_cafeteria1:
    
    "The cafeteria is empty - you've missed lunch break. But you hear moaning noises from the kitchen."
    scene bg scorp_cafeteria1 with fade    
    girl "Oh... hello, [povTitle] [povLastName]... You caught me..."
    girl "I've been having trouble getting this radish inside me... It's just too big... Can you help a girl out?"
    "Pushing as hard as you can, and with the help of plenty of butter, you manage to force some of the giant vegetable into the girl's dripping cunt."
    girl "Ughghguhgu... Thank you..."    
    return
    
label scorp_cafeteria2:
    
    scene bg scorp_cafeteria2 with fade
    "Some girls are just starters, and some are desserts. But this one looks like a true main course."
    return
    
label scorp_cafeteria3:
    
    #Panning up and down
    scene bg scorp_cafeteria3:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_cafeteria3")    
    show screen scorp_screen
    
    "The whole school is a big fan of the cafeteria's new waitress uniform."
    "Well, the whole school apart from some of the waitresses."
    $ morale +=1  
    hide screen scorp_screen
    return
    
label scorp_cafeteria4:
    
    scene bg scorp_cafeteria4 with fade
    "Girls from the school volunteer to be waitresses at the cafeteria. So maybe this one just came in from the pool and didn't have time to change?"
    "Why else would she be wearing nothing but that green bikini? She surely doesn't get off on it, does she?"
    $ inhibition -=1     
    return
    
label scorp_cafeteria5:
    
    scene bg scorp_cafeteria5 with fade
    "You're a big fan of the new direction the Cafeteria seems to have taken. It's open to the public now, and has mostly male customers... who seem to tip very, very heavily."
    "It's good for the school's budget. Less good for its reputation."
    $ cash +=150      
    $ reputation -=1      
    return
    
label scorp_cafeteria6:
    
    scene bg scorp_cafeteria6 with fade
    "One of the teachers puts something in her mouth that's not on the menu."
    guy "Ah! Ms. Miya! Right here?"
    teacher "*slurp* *slurp*"
    return
    
label scorp_cafeteria7:
    
    scene bg scorp_cafeteria7 with fade
    "The cooks have really taken to the new uniform. They wear aprons for safety reasons, of course, but everyone still gets a good view."
    return
    
label scorp_cafeteria8:
    
    #Panning up and down
    scene bg scorp_cafeteria8:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_cafeteria8")    
    show screen scorp_screen
    
    "Serving Girl 1" "AHH AHH HELLO SIR CAN I TAKE YOUR - UHHHNNNNNG - ORDER?"
    "Serving Girl 2" "IF YOU WANT TO FUCK US - OH GOD PLEASE FUCK US - JOIN THE OTHER LINE!"
    "This seems... unsafe. Unsanitary."
    "Oh well." 
    hide screen scorp_screen
    return
    
label scorp_cafeteria9:
    
    scene bg scorp_cafeteria9 with fade
    "You don't know why this girl suddenly turned so red while talking to her female friends. Is something going on beneath the table?"
    return
    
label scorp_cafeteria10:
    
    scene bg scorp_cafeteria10 with fade
    "A girl enjoys lunch with her friend."
    return
    
label scorp_cafeteria11:
   
    scene bg scorp_cafeteria11 with fade
    "The Italian Food Fair went down well!"
    $ morale +=1     
    return

label scorp_cafeteria12:
    
    scene bg scorp_cafeteria12 with fade
    "Some students keep studying even while they eat. Such a hard-working school!"
    $ academics +=1     
    return

label scorp_cafeteria13:
    
    "The waitresses are wearing less and less clothing recently."
    if deviance > 90:
        scene bg scorp_cafeteria13_1 with fade
        "Luckily, they're very eager to please."
        return
    else:
        scene bg scorp_cafeteria13_2 with fade    
        "This girl's tiny thong keeps disappearing between her pussy lips."
        girl "You can look, but don't touch until my shift is done!"
        return    
    
label scorp_cafeteria14:
  
    scene bg scorp_cafeteria14 with fade
    "Aw. A young couple look dreamily into each other's eyes in the Cafeteria. So sweet."
    "...Wait! Is she...?"
    $ deviance +=1    
    return
    
label scorp_cafeteria15:
    
    scene bg scorp_cafeteria15 with fade
    pov "What big... eyes you have."
    girl "*giggle*"
    return
    
label scorp_cafeteria16:

    "A waitress pauses to give you a very public show."
    if inhibition > 40:
        scene bg scorp_cafeteria16_1 with fade
        girl "Like what you see?"
        return
    else:
        scene bg scorp_cafeteria16_2 with fade    
        girl "I forgot something very important this morning. Look! *giggle*"
        pov "...Oh my God."
        return
    
label scorp_cafeteria17:
    
    scene bg scorp_cafeteria17 with fade
    "The Cafeteria is such a peaceful place. Everyone's happy you built it."
    $ morale +=1
    return
    
label scorp_cafeteria18:
    
    scene bg scorp_cafeteria18 with fade
    "The waitresses seem to get happier, and their skirts shorter, every day!"
    return
    
label scorp_cafeteria19:
    
    scene bg scorp_cafeteria19 with fade
    "You're a perverted guy, but it upsets even you to see good spaghetti being ruined this way."
    pov "Is nothing sacred?"
    return
    
label scorp_cafeteria20:
    
    scene bg scorp_cafeteria20 with fade
    "That's a naughty look if you ever saw one!"
    return
    
label scorp_cafeteria21:
    
    scene bg scorp_cafeteria21 with fade
    "The cafeteria sure has become popular! A wise investment!"
    pov "...Maybe I'll come back and have my lunch during class hours."
    $ morale +=1
    return
    
label scorp_cafeteria22:
    
    scene bg scorp_cafeteria22 with fade
    "The new uniform makes cooks and serving girls too tempting to resist."
    return
    
label scorp_cafeteria23:
    
    scene bg scorp_cafeteria23_1 with fade
    "It can be fun to have a nice, quiet lunch with three female friends..."
    if deviance > 90:    
        scene bg scorp_cafeteria23_2 with fade    
        "But just because a man lets them sit at his table, doesn't mean he shouldn't teach them their place afterwards."
        guy "Dammit, whore, your slutty hole is so loose I can barely feel a thing! Tighten up, will you?"
        girl "I'm sorry master!"
        return
    else:
        "Clean, wholesome fun!"
        return
    
label scorp_cafeteria24:

    scene bg scorp_cafeteria24 with fade
    "Her boyfriend has made her wear a vibe all day long..."
    girl "I would like... ahhh... could I have the soup... ohhh..."
    return
    
label scorp_cafeteria25:
    
    scene bg scorp_cafeteria25 with fade
    "The cafeteria looks wonderful, full of so many happy, perverted girls in their glorious naked uniform."
    return
    
label scorp_cafeteria26:
    
    scene bg scorp_cafeteria26 with fade
    "It's only healthy for the girls to have some protein in their diet."
    return
    
label scorp_cafeteria27:
    
    scene bg scorp_cafeteria27 with fade
    "The girls of Ashford Academy seem to have almost completely abandoned their inhibitions."
    girl "[povTitle] [povLastName]! Which of us has the nicest tits?"
    $ inhibition -=1    
    return
    
label scorp_cafeteria28:
    
    scene bg scorp_cafeteria28 with fade
    "She came here for a quiet break, but a girl's work is never done."
    return
    
label scorp_cafeteria29:
      
    scene bg scorp_cafeteria29 with fade
    "Some of the girls have simply become 24-hour sex slaves to a boy."
    "Her eyes look blank and accepting as his cock roughly fucks her squelching cunt."
    return
    
label scorp_cafeteria30:
    
    scene bg scorp_cafeteria30 with fade
    "These girls are drinking tea while they pore over a manga comic! Delightful."
    $ morale +=1    
    return
    
label scorp_cafeteria31:
    
    scene bg scorp_cafeteria31 with fade
    "Lunch break with friends is one of those times that doesn't seem a big deal in the moment, but will be looked back on as a treasure."
    return
    
label scorp_cafeteria32:
   
    "They're both struggling to do the homework they should've done the night before. Not great, but at least they're doing it."
    $ academics +=1    
    return
    
label scorp_cafeteria33:
    
    scene bg scorp_cafeteria33 with fade
    "Sometimes even a milkshake isn't enough to cheer a girl up."
    $ morale -=1     
    return
    
label scorp_cafeteria34:
    
    "You hear rumors of something shocking happening in the Cafeteria. You find a big crowd gathered round a table, and push to the front."
    scene bg scorp_cafeteria34 with fade
    pov "!!!"
    "At first, you thought it was just a brazen display of affection, with the girl straddling the guy as they make out, a single gorgeous tit hanging out for everyone to see. But the way she grinds her hips..."
    "They're totally having sex! In front of everyone!"
    menu:
        "Pull them apart and stop this nonsense.":
            "Cock leaves vagina with a lewd slurp. You march the errant students to your office and punish them according to the school rules."
            $ inhibition +=1   
            $ deviance -=1       
            return
        "Pretend not to have seen them.":
            "As you leave the Cafeteria, you hear the girl scream as she's rocked by an earth-shattering orgasm. All the students whoop and applaud."
            $ inhibition -=1   
            $ deviance +=1       
            return
    
label scorp_cafeteria35:
     
    "A girl trips up in front of you, revealing she's not wearing any panties."
    scene bg scorp_cafeteria35 with fade
    "Rather than get up, or hide herself, she simply looks back at you and spreads open her labia for all to see."
    "You can see her pussy get wetter and wetter as you watch."
    girl "Are you going to punish me, [povTitle] [povLastName]? Am I a very naughty girl?"
    return
    
label scorp_cafeteria36:
    
    scene bg scorp_cafeteria36 with fade
    "There's a reason girls' brains are so suited to multitasking."
    return
    
label scorp_cafeteria37:
    
    #Panning up and down
    scene bg scorp_cafeteria37:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_cafeteria37")    
    show screen scorp_screen
    
    girl "Oh [povTitle] [povLastName]... Every other man in the Cafeteria has had a turn with me... You don't want to miss out, do you?"
    hide screen scorp_screen
    return
    
label scorp_cafeteria38:
    
    scene bg scorp_cafeteria38 with fade
    "Whoops! What a klutz!"
    girl "Oh no!"
    return
    
label scorp_cafeteria39:
    
    scene bg scorp_cafeteria39 with fade
    girl "G-g-good afternoon [povTitle] [povLastName] m-may I take your order~~"
    "She seems very distracted. When she turns to leave, you see why."
    return
    
label scorp_cafeteria40:
    
    scene bg scorp_cafeteria40 with fade
    pov "You shouldn't play with your food!"
    return