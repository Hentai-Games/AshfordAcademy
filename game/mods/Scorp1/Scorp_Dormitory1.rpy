#### SCORP EVENT PACK 1 - Dormitory ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this. 
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Dormitory.
## Pictures are located in the subdirectory \Scorp1\Dormitory
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

image bg scorp_dormitory1 = "mods/Scorp1/Dormitory/scorp_dormitory1.jpg"
image bg scorp_dormitory2 = "mods/Scorp1/Dormitory/scorp_dormitory2.jpg"
image bg scorp_dormitory3 = "mods/Scorp1/Dormitory/scorp_dormitory3.jpg"
image bg scorp_dormitory4 = "mods/Scorp1/Dormitory/scorp_dormitory4.jpg"
image bg scorp_dormitory5 = "mods/Scorp1/Dormitory/scorp_dormitory5.jpg"
image bg scorp_dormitory6 = "mods/Scorp1/Dormitory/scorp_dormitory6.jpg"
image bg scorp_dormitory7_1 = "mods/Scorp1/Dormitory/scorp_dormitory7_1.jpg"
image bg scorp_dormitory7_2 = "mods/Scorp1/Dormitory/scorp_dormitory7_2.jpg"
image bg scorp_dormitory7_3 = "mods/Scorp1/Dormitory/scorp_dormitory7_3.jpg"
image bg scorp_dormitory7_4 = "mods/Scorp1/Dormitory/scorp_dormitory7_4.jpg"
image bg scorp_dormitory7_5 = "mods/Scorp1/Dormitory/scorp_dormitory7_5.jpg"
image bg scorp_dormitory8 = "mods/Scorp1/Dormitory/scorp_dormitory8.jpg"
image bg scorp_dormitory9_1 = "mods/Scorp1/Dormitory/scorp_dormitory9_1.jpg"
image bg scorp_dormitory9_2 = "mods/Scorp1/Dormitory/scorp_dormitory9_2.jpg"
image bg scorp_dormitory10 = "mods/Scorp1/Dormitory/scorp_dormitory10.jpg"
image bg scorp_dormitory11 = "mods/Scorp1/Dormitory/scorp_dormitory11.jpg"
image bg scorp_dormitory12_1 = "mods/Scorp1/Dormitory/scorp_dormitory12_1.jpg"
image bg scorp_dormitory12_2 = "mods/Scorp1/Dormitory/scorp_dormitory12_2.jpg"
image bg scorp_dormitory12_3 = "mods/Scorp1/Dormitory/scorp_dormitory12_3.jpg"
image bg scorp_dormitory12_4 = "mods/Scorp1/Dormitory/scorp_dormitory12_4.jpg"
image bg scorp_dormitory12_5 = "mods/Scorp1/Dormitory/scorp_dormitory12_5.jpg"
image bg scorp_dormitory13 = "mods/Scorp1/Dormitory/scorp_dormitory13.jpg"
image bg scorp_dormitory14 = "mods/Scorp1/Dormitory/scorp_dormitory14.jpg"
image bg scorp_dormitory15_1 = "mods/Scorp1/Dormitory/scorp_dormitory15_1.jpg"
image bg scorp_dormitory15_2 = "mods/Scorp1/Dormitory/scorp_dormitory15_2.jpg"
image bg scorp_dormitory16 = "mods/Scorp1/Dormitory/scorp_dormitory16.jpg"
image bg scorp_dormitory17 = "mods/Scorp1/Dormitory/scorp_dormitory17.jpg"
image bg scorp_dormitory18 = "mods/Scorp1/Dormitory/scorp_dormitory18.jpg"
image bg scorp_dormitory19 = "mods/Scorp1/Dormitory/scorp_dormitory19.jpg"
image bg scorp_dormitory20 = "mods/Scorp1/Dormitory/scorp_dormitory20.jpg"
image bg scorp_dormitory21 = "mods/Scorp1/Dormitory/scorp_dormitory21.jpg"
image bg scorp_dormitory22 = "mods/Scorp1/Dormitory/scorp_dormitory22.jpg"
image bg scorp_dormitory23 = "mods/Scorp1/Dormitory/scorp_dormitory23.jpg"
image bg scorp_dormitory24 = "mods/Scorp1/Dormitory/scorp_dormitory24.jpg"
image bg scorp_dormitory25_1 = "mods/Scorp1/Dormitory/scorp_dormitory25_1.jpg"
image bg scorp_dormitory25_2 = "mods/Scorp1/Dormitory/scorp_dormitory25_2.jpg"
image bg scorp_dormitory26 = "mods/Scorp1/Dormitory/scorp_dormitory26.jpg"
image bg scorp_dormitory27 = "mods/Scorp1/Dormitory/scorp_dormitory27.jpg"
image bg scorp_dormitory28 = "mods/Scorp1/Dormitory/scorp_dormitory28.jpg"
image bg scorp_dormitory29 = "mods/Scorp1/Dormitory/scorp_dormitory29.jpg"
image bg scorp_dormitory30 = "mods/Scorp1/Dormitory/scorp_dormitory30.jpg"
image bg scorp_dormitory31_1 = "mods/Scorp1/Dormitory/scorp_dormitory31_1.jpg"
image bg scorp_dormitory31_2 = "mods/Scorp1/Dormitory/scorp_dormitory31_2.jpg"
image bg scorp_dormitory32 = "mods/Scorp1/Dormitory/scorp_dormitory32.jpg"
image bg scorp_dormitory33 = "mods/Scorp1/Dormitory/scorp_dormitory33.jpg"
image bg scorp_dormitory34 = "mods/Scorp1/Dormitory/scorp_dormitory34.jpg"
image bg scorp_dormitory35 = "mods/Scorp1/Dormitory/scorp_dormitory35.jpg"
image bg scorp_dormitory36 = "mods/Scorp1/Dormitory/scorp_dormitory36.jpg"
image bg scorp_dormitory37 = "mods/Scorp1/Dormitory/scorp_dormitory37.jpg"
image bg scorp_dormitory38 = "mods/Scorp1/Dormitory/scorp_dormitory38.jpg"
image bg scorp_dormitory39_1 = "mods/Scorp1/Dormitory/scorp_dormitory39_1.jpg"
image bg scorp_dormitory39_2 = "mods/Scorp1/Dormitory/scorp_dormitory39_2.jpg"
image bg scorp_dormitory40 = "mods/Scorp1/Dormitory/scorp_dormitory40.jpg"
image bg scorp_dormitory41 = "mods/Scorp1/Dormitory/scorp_dormitory41.jpg"
image bg scorp_dormitory42 = "mods/Scorp1/Dormitory/scorp_dormitory42.jpg"
image bg scorp_dormitory43 = "mods/Scorp1/Dormitory/scorp_dormitory43.jpg"
image bg scorp_dormitory44 = "mods/Scorp1/Dormitory/scorp_dormitory44.jpg"
image bg scorp_dormitory45 = "mods/Scorp1/Dormitory/scorp_dormitory45.jpg"
image bg scorp_dormitory46 = "mods/Scorp1/Dormitory/scorp_dormitory46.jpg"
image bg scorp_dormitory47 = "mods/Scorp1/Dormitory/scorp_dormitory47.jpg"
image bg scorp_dormitory48 = "mods/Scorp1/Dormitory/scorp_dormitory48.jpg"
image bg scorp_dormitory49 = "mods/Scorp1/Dormitory/scorp_dormitory49.jpg"
image bg scorp_dormitory50 = "mods/Scorp1/Dormitory/scorp_dormitory50.jpg"
image bg scorp_dormitory51_1 = "mods/Scorp1/Dormitory/scorp_dormitory51_1.jpg"
image bg scorp_dormitory51_2 = "mods/Scorp1/Dormitory/scorp_dormitory51_2.jpg"
image bg scorp_dormitory52_1 = "mods/Scorp1/Dormitory/scorp_dormitory52_1.jpg"
image bg scorp_dormitory52_2 = "mods/Scorp1/Dormitory/scorp_dormitory52_2.jpg"
image bg scorp_dormitory52_3 = "mods/Scorp1/Dormitory/scorp_dormitory52_3.jpg"
image bg scorp_dormitory52_4 = "mods/Scorp1/Dormitory/scorp_dormitory52_4.jpg"
image bg scorp_dormitory53 = "mods/Scorp1/Dormitory/scorp_dormitory53.jpg"
image bg scorp_dormitory54 = "mods/Scorp1/Dormitory/scorp_dormitory54.jpg"
image bg scorp_dormitory55 = "mods/Scorp1/Dormitory/scorp_dormitory55.jpg"
image bg scorp_dormitory56 = "mods/Scorp1/Dormitory/scorp_dormitory56.jpg"
image bg scorp_dormitory57 = "mods/Scorp1/Dormitory/scorp_dormitory57.jpg"
image bg scorp_dormitory58 = "mods/Scorp1/Dormitory/scorp_dormitory58.jpg"
image bg scorp_dormitory59 = "mods/Scorp1/Dormitory/scorp_dormitory59.jpg"
image bg scorp_dormitory60 = "mods/Scorp1/Dormitory/scorp_dormitory60.jpg"
image bg scorp_dormitory61 = "mods/Scorp1/Dormitory/scorp_dormitory61.jpg"
image bg scorp_dormitory62 = "mods/Scorp1/Dormitory/scorp_dormitory62.jpg"
image bg scorp_dormitory63 = "mods/Scorp1/Dormitory/scorp_dormitory63.jpg"
image bg scorp_dormitory64 = "mods/Scorp1/Dormitory/scorp_dormitory64.jpg"
image bg scorp_dormitory65_1 = "mods/Scorp1/Dormitory/scorp_dormitory65_1.jpg"
image bg scorp_dormitory65_2 = "mods/Scorp1/Dormitory/scorp_dormitory65_2.jpg"
image bg scorp_dormitory65_3 = "mods/Scorp1/Dormitory/scorp_dormitory65_3.jpg"
image bg scorp_dormitory65_4 = "mods/Scorp1/Dormitory/scorp_dormitory65_4.jpg"
image bg scorp_dormitory65_5 = "mods/Scorp1/Dormitory/scorp_dormitory65_5.jpg"
image bg scorp_dormitory65_6 = "mods/Scorp1/Dormitory/scorp_dormitory65_6.jpg"
image bg scorp_dormitory66 = "mods/Scorp1/Dormitory/scorp_dormitory66.jpg"
image bg scorp_dormitory67 = "mods/Scorp1/Dormitory/scorp_dormitory67.jpg"
image bg scorp_dormitory68 = "mods/Scorp1/Dormitory/scorp_dormitory68.jpg"
image bg scorp_dormitory69 = "mods/Scorp1/Dormitory/scorp_dormitory69.jpg"
image bg scorp_dormitory70 = "mods/Scorp1/Dormitory/scorp_dormitory70.jpg"

#Setting up events and conditions

init:
    $ event("scorp_dormitory1", "act == 'dormitory' and deviance > 40", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory2", "act == 'dormitory' and deviance > 25", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory3", "act == 'dormitory' and deviance > 25 and deviance < 50", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory4", "act == 'dormitory' and deviance > 50", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory5", "act == 'dormitory' and deviance > 90", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory6", "act == 'dormitory' and inhibition < 85 and deviance > 15", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory7", "act == 'dormitory' and deviance > 15", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory8", "act == 'dormitory' and inhibition < 90", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory9", "act == 'dormitory' and deviance > 85 and inhibition < 20", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory10", "act == 'dormitory' and deviance > 95 and inhibition < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory11", "act == 'dormitory' and uniform == 'nude_uniform' and behavior < 70", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory12", "act == 'dormitory' and deviance > 90 and inhibition < 20", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory13", "act == 'dormitory' and deviance > 85 and inhibition < 15", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory14", "act == 'dormitory' and deviance > 25 and inhibition < 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory15", "act == 'dormitory' and deviance > 99 and inhibition < 5", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory16", "act == 'dormitory' and deviance > 80 and inhibition < 25", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory17", "act == 'dormitory' and deviance > 85 and inhibition < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory18", "act == 'dormitory' and deviance > 85 and inhibition < 25 and behavior < 70", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory19", "act == 'dormitory' and deviance > 75 and inhibition < 25", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory20", "act == 'dormitory' and deviance > 75", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory21", "act == 'dormitory' and deviance > 75 and behavior < 35", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory22", "act == 'dormitory' and deviance > 10 and deviance < 50", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory23", "act == 'dormitory' and inhibition < 90 and inhibition > 61", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory24", "act == 'dormitory' and inhibition > 75", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory25", "act == 'dormitory' and deviance > 75 and inhibition < 40", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory26", "act == 'dormitory' and inhibition < 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory27", "act == 'dormitory' and deviance > 5 and deviance < 35", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory28", "act == 'dormitory' and deviance > 15 and deviance < 50", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory29", "act == 'dormitory' and inhibition > 80 and deviance < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory30", "act == 'dormitory' and deviance > 60 and behavior_rules == {'behavior_no_limit' or 'behavior_physical'}", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory31", "act == 'dormitory' and deviance > 70", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory32", "act == 'dormitory' and inhibition < 80 and inhibition > 20", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory33", "act == 'dormitory' and deviance > 25 and deviance < 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory34", "act == 'dormitory' and inhibition < 90 and inhibition > 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory35", "act == 'dormitory' and deviance > 55", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory36", "act == 'dormitory' and inhibition > 40 and inhibition < 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory37", "act == 'dormitory' and deviance < 25", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory38", "act == 'dormitory' and deviance > 5 and deviance < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory39", "act == 'dormitory' and deviance > 60", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory40", "act == 'dormitory' and deviance > 40 and deviance < 65", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory41", "act == 'dormitory' and inhibition < 95", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory42", "act == 'dormitory' and deviance > 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory43", "act == 'dormitory' and deviance > 90 and inhibition < 15", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory44", "act == 'dormitory' and deviance > 85", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory45", "act == 'dormitory' and uniform == 'nude_uniform'", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory46", "act == 'dormitory' and inhibition > 60", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory47", "act == 'dormitory' and inhibition > 50 and inhibition < 80", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory48", "act == 'dormitory' and inhibition < 70", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory49", "act == 'dormitory' and deviance < 65", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory50", "act == 'dormitory' and deviance > 20 and deviance < 45", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory51", "act == 'dormitory' and deviance > 95 and inhibition < 10", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory52", "act == 'dormitory' and deviance > 95 and inhibition < 10", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory53", "act == 'dormitory' and artistery > 30 and deviance < 50", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory54", "act == 'dormitory' and deviance < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory55", "act == 'dormitory' and deviance < 30", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory56", "act == 'dormitory' and deviance < 50", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory57", "act == 'dormitory' and deviance < 50", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory58", "act == 'dormitory' and deviance > 65 and inhibition < 65", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory59", "act == 'dormitory' and deviance > 40 and inhibition < 70", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory60", "act == 'dormitory' and deviance > 20", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory61", "act == 'dormitory' and deviance > 65 and inhibition < 30", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory62", "act == 'dormitory' and inhibition < 70", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory63", "act == 'dormitory' and inhibition < 80", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory64", "act == 'dormitory' and deviance > 85 and inhibition < 25", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory65", "act == 'dormitory' and deviance > 80 and inhibition < 20", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory66", "act == 'dormitory' and inhibition < 55", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory67", "act == 'dormitory' and inhibition < 90 and inhibition > 20", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory68", "act == 'dormitory' and inhibition < 55", event.choose_one('dormitory'), priority=200) 
    $ event("scorp_dormitory69", "act == 'dormitory' and uniform == 'nude_uniform'", event.choose_one('dormitory'), priority=200)
    $ event("scorp_dormitory70", "act == 'dormitory' and inhibition < 75", event.choose_one('dormitory'), priority=200)     
    
label scorp_dormitory1:
    
    scene bg scorp_dormitory1 with fade
    "A boy has been running around the girls' dormitory at night, and peeking at their assholes as they sleep. Sometimes he sticks a sharpie or carrot in there before running away."
    "The girls have started calling him the 'Ass Bandit,' and go to bed every night afraid that they're going to wake up with something up their butt."
    $ morale -=1    
    return
    
label scorp_dormitory2:
    
    scene bg scorp_dormitory2 with fade
    "This girl doesn't know it, but this boy is in love with her. He sneaks into her room every night and kisses every inch of her body, focusing on the ass."
    "How romantic!"
    return
    
label scorp_dormitory3:
    
    scene bg scorp_dormitory3 with fade
    "For a boy who's never touched a pussy before, a sleeping, unaware girl is good practice. Very resourceful!"    
    return
    
label scorp_dormitory4:
    
    scene bg scorp_dormitory4 with fade
    girl "Mmmf, don't be so loud! You'll wake her up!"
    
    if deviance < 80:
        guy "Sorry, sorry! It's just... Your pussy feels so good... Ahhh..."
        girl "Wait!"
        guy "...What?"
        girl "I think she just moved!"
        guy "She's just shifting in her sleep. Keep going... Yes, keep going!"
        girl "Ssshhhh!"
        return
    
    else:
        guy "Who cares? I'm going to fuck her next."
        girl "What? You wouldn't dare!"
        guy "HEY MARY! WHEN I'M DONE WITH ALISSA I'M GOING TO FUCK YOU TOO!"
        "Mary" "Hmm... *yawn*... Hehe, okay... Wake me up when you want to do it... zzzz."
        return
    
label scorp_dormitory5:
    
    #Panning up and down
    scene bg scorp_dormitory5:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory5")    
    show screen scorp_screen
    
    "Every night, roving bands of horny boys roam through the dormitories, breaking into girls' rooms for a bit of fun." 
    "This girl is so used to it that the fingers massaging her pussy don't even wake her up."
    $ deviance +=1
    hide screen scorp_screen
    return
   
label scorp_dormitory6:
    
    scene bg scorp_dormitory6 with fade
    "Hmmm... How come this girl is wearing a boy's shirt to bed?"
    "And she's otherwise naked... Ah, something's been going on here!"
    return
    
label scorp_dormitory7:
    
    scene bg scorp_dormitory7_1 with fade
    "The school dormitories present many an attractive opportunity for the intrepid young man."
    "This girl is sleeping topless. Our brave adventurer takes a moment to pull the covers down and admire. He pinches a nipple, experimentally, but she does not wake."
    scene bg scorp_dormitory7_2 with fade
    "By now, the boy's dick is throbbing for relief. He straddles the sleeping girl and places his tip against her lush, soft lips."
    scene bg scorp_dormitory7_3 with fade
    "She's a natural cocksucker, and opens her wet mouth to take the entire shaft. The boy wonders what she's dreaming about as he begins to slide his dick in and out."
    "He pauses for a moment as she makes a wet, moaning noise, her tongue lapping instinctively at the dick in her mouth. But she's still asleep, and he resumes pumping."
    scene bg scorp_dormitory7_4 with fade
    "Finally, it's too much. The boy withdraws and, before he can move away, his dick unleashes a huge spurt of cum over the sleeping girl's serene face."
    guy "Uuuuuh!"
    "In for a dime, in for a dollar. The boy blows his load all over her face and bare tits, and then, when he's finished, wipes the tip on her cheek. Realizing he might have gone too far, he bolts for the door."
    scene bg scorp_dormitory7_5 with fade
    girl "Mmmm... What's this?"
    girl "Eeeeek!"
    return
    
label scorp_dormitory8:
    
    scene bg scorp_dormitory8 with fade
    "It's good to hold the master key to the girls' dorms. At the moment, you're carrying out a quiet 'inspection.'"
    pov "*quietly* Hmmm, yes... This seems to be all in order..."
    return
    
label scorp_dormitory9:
    
    scene bg scorp_dormitory9_1 with fade
    "The girls at Ashford have come a long way. This student's ass has been so well-used that she barely even reacts to the boy fucking her roughly from behind, instead seeming absorbed in reading a hentai manga."
    girl "Hurry up and cum soon, okay? I'm almost on the last page and I want to go to sleep."
    guy "OH! Ohhh yes!"
    scene bg scorp_dormitory9_2 with fade
    "She wiggles her butt and giggles as the guy ejaculates deep inside her."
    girl "Ooh, it's so warm!"
    "The guy slumps over her, his deflating cock still resting inside her ass. As globs of cum drip down over her pussy, she licks a finger and turns the page."
    return
    
label scorp_dormitory10:
      
    #Panning up and down
    scene bg scorp_dormitory10:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory10")    
    show screen scorp_screen
    
    "At this point, it doesn't matter if a girl says 'yes' or 'no', because few boys bother to even ask."
    girl "UH UH UH UH!"
    hide screen scorp_screen
    return   
    
label scorp_dormitory11:
   
    scene bg scorp_dormitory11 with fade
    "You come across a group of nude students, following the uniform policy even in their dorm rooms. They've managed to smuggle in alcohol from somewhere, and are all clearly tipsy."
    "Blonde girl" "It'sh the prinshipal! Do you like our titsh, prinshipal?"
    "Using both hands, she jiggles her breasts wildly to emphasize her question."
    "Red-haired girl" "I bet he wants to fuck us! Do you like what you see? *giggle*"
    "She spreads her labia with one hand, revealing the inner pinkness of her cunt."
    "Glasses girl" "Ashford is the best school ever!"
    pov "You're right there."
    $ behavior -=1
    return

label scorp_dormitory12:
    
    scene bg scorp_dormitory12_1
    "On your nightly rounds, you come across a rapidly-unfolding situation. A gang of boys have invaded one girl's room, and are ripping her clothes off her."
    "They stop as they notice you, but they keep a tight hold of the now-naked girl."
    girl "Help me, principal!"
    "Guy 1" "He's not going to help you, bitch. The principal is great, he's the reason the school is like this."
    "Guy 2" "Yeah, we're just guys indulging our natural urges. If she'd just let us fuck her, she'd love it, right [povTitle] [povLastName]?"

    menu:
        "No, I cannot allow this.":
            pov "Hands off her, criminal scum!"
            "Guy 1" "WHAT? Man, I thought you were cool."
            "Guy 2" "This is what Ashford's like now. The girls don't get a say over whose cocks are shoved where. I thought you knew that!"
            "The girl just looks at you gratefully."
            girl "Thank you."
            pov "No problem. Guys, get out of here before I give you detention."
            "The boys stand up - one of them spanking the girl hard on her naked ass as he does so - and saunter out of the room."
            "Guy 1" "Everyone's going to hear about this. Maybe the new Ashford needs a new principal, huh?"
            "You're left alone with the girl, who blushes and tries to cover her flushed breasts."
            menu:
                "He has a point.":
                    pov "Honestly, it would be a lot easier next time to just lie back and let them fuck you. You'd enjoy it."
                    girl "R - really?"
                    pov "Of course. The kid was right - that's how Ashford works now. Making everyone's lives harder by resisting isn't going to win you any friends."
                    girl "O - okay. I hadn't looked at it that way... I'll keep it in mind."
                    "You give one of her tits a friendly squeeze and leave, confident that you've sown the seed of doubt."
                    
                    $ morale +=1
                    $ behavior +=1
                    $ deviance +=1
                        
                    return
                
                "Don't listen to him.":
                    pov "Ashford is crazy these days, I know, but you always have the right to say no."
                    girl "It's so good to hear you say that! I thought I was the only one who thought that way any more..."
                    pov "Keep strong!"
                    
                    $ morale +=1
                    $ behavior +=1
                    $ deviance -=2
                    $ inhibition +=2
                    
                    return                   
                
        "Of course! Boys will be boys, after all.":
            pov "I think we should treat this as a teaching opportunity, on why girls should respect the desires of men."
            girl "Nooo!"
            "Guy 1" "I knew it! You're the best, principal!"
            "Guy 2" "Let's get this party started!"
            scene bg scorp_dormitory12_2 with flash
            "You stand, arms crossed, watching with approval as the guy forces open the girl's legs. He readies his big, stiff cock and then plunges in, all the way to the hilt." 
            girl "AAAAAAAAAAAAH!"
            "The guy roughly pistons his dick in and out of the girl's soft young cunt. Her screams and sobs fill the room, but it just adds to the chorus of sexual screams that echo through the dorms at night."
            "No sooner does he unleash his load inside her than the second boy pulls her off his friend's dick, with a rasping wet noise, and then shove himself inside her immediately."
            scene bg scorp_dormitory12_3 with doubleflash
            "Guy 1" "Wooo! That bitch is tight as fuck!"
            "Guy 2" "Unnnnh! Yeah, this pussy is just clamping down around my cock!"
            girl "AH AH AH AH AH!"
            "Guy 2" "Haha, see? I told you you'd like it!"
            "Guy 3" "Hey, have you finished yet? It's my turn."
            "The second guy's legs shake as he shoots his sperm deep into the moaning girl's dripping hole. He throws her onto the bed, and his fat friend pulls her on top of him."
            "Guy 3" "Wow, you weren't kidding! This is the tightest cunt I've had in weeks! Good job, slut! Shall we give her a reward?"
            "Guy 1" "Haha, sure thing."
            "The blonde guy steps forward and takes a fat pink dildo from his schoolbag, while his fat friend reaches round and stretches the girl's asshole as wide as it will go."
            girl "Nooooo!"
            "Guy 3" "Will it fit?"
            scene bg scorp_dormitory12_4 with doubleflash
            "Guy 1" "It fits alright!"
            girl "OOOOHHHH! MY ASS!"
            "The guys fuck her and play with her for a few more minutes. Finally, when they're done, they stand back, pulling the dildo from her convulsing asshole."
            "She crawls away from them, a huge amount of cum spilling from between her pussy-lips."#
            scene bg scorp_dormitory12_5 with fade        
            "One of the guys takes the opportunity to give her ass a friendly spank."
            "Guy 2" "You did good tonight, slut. We'll probably come by again in a few days, if you're good. You can start by thanking us for treating you so nicely."
            girl "Th - thank you."
            "Guy 1" "And thank our wonderful principal for the lesson."
            girl "Th - thank you, [povTitle] [povLastName], for the lesson in respecting men."
            pov "It's what I do."
            "Guy 2" "Right, we'll see you later then, fucktoy. In the meantime, though, we'll have this video to remember you by."
            girl "Wait - you - you've been recording this?"
            "The last big glob of cum drips from her raw cunt as she realizes she's surrounded by glowing cellphones."
            "Later, the video will get 2 million hits on Pornhub."

            $ inhibition -=1
            $ deviance +=1
            $ behavior -=2
            $ morale -=2
            if renpy.random.randint(1, 3) == 1:
                $ deviance += 5           
            return

label scorp_dormitory13:
    
    scene bg scorp_dormitory13 with fade
    "A group of girls, who've been missing for over a week, turn up imprisoned in one of the male student's dorm rooms."
    "It doesn't do much for the school's reputation, but the male student avoids trouble by demonstrating that the girls did, in fact, 'ask for it.'"
    $ reputation -=1
    return
    
label scorp_dormitory14:
   
    scene bg scorp_dormitory14 with fade
    "It can be embarrassing waking up in someone else's bed after a passionate night. Especially when you didn't, until now, consider yourself attracted to girls."
    $ deviance +=1  
    return
    
label scorp_dormitory15:
    
    "You're on one of your nightly rounds of the dormitory, when you hear cries for help coming from one of the rooms."
    "When you use your master key to enter the room, you're confronted with a wonderful sight - a busty blonde, standing tied and naked before you."
    scene bg scorp_dormitory15_1 with fade    
    girl "Oh my God, I'm so glad you found me!"
    pov "What seems to be the problem?"
    "The ropes bind her in such a way that her tits are squeezed between them, and thrust out in front of her. You give them an experimental squeeze."
    girl "W-what are you doing?"
    pov "Relax, if you didn't want me to give them a squeeze, you shouldn't have been tied up naked in here."
    girl "I didn't want to be here! I was kidnapped!"
    pov "Oh really? By who?"
    "The door opens behind you, and two boys enter. The one at the front is carrying a bit-gag and a piece of chalk."
    "Guy 1" "There's no time to waste, [povTitle] [povLastName]! Me and my friend have to have sex with this fair maiden!"
    "Guy 2" "The fate of the world depends on it!"
    pov "...What?"
    "Guy 1" "The ritual must be completed!"
    "Guy 2" "The ritual!"
    pov "I say again. What?"
    "Guy 1" "We have started a cult, you see, that worships this school. Ashford has provided us such a wonderful bounty of willing sluts, how could we not?"
    "Guy 2" "But we must make use of the bounty that Ashford provides, or the world will end! Join us!"
    pov "...Forget it, this is too weird. I'm out."
    scene bg scorp_dormitory15_2 with fade
    girl "Hey! What about me! Principal...?"
    "As you leave, the boys have gagged the blonde and already started to fuck her on top of a chalk circle, one pumping in and out of her ass, the other using her pussy."
    "Guy 2" "Glory to Ashford!"
    "Guy 1" "All praise Ashford, the Creator!"
    return
    
label scorp_dormitory16:

    scene bg scorp_dormitory16 with fade
    "During your nightly rounds, you come across a wide-open door. Looking inside, you see a girl lying spread-legged on her bed, fast asleep, her cum-filled pussy on display to the whole world."
    pov "Poor girl is all tuckered out. Busy day, I bet. And a busy night ahead."
    return
    
label scorp_dormitory17:
    
    scene bg scorp_dormitory17 with fade
    "These girls have stayed up far too late. They're being tormented by their master, a boy sitting cross-legged in front of them, casually watching their naked bodies sweat and writhe."
    "Girl 1" "Please - master - fuck me - let me orgasm -"
    "Girl 2" "No - please - I'm so horny - fuck me first -"
    guy "I won't fuck either of you until one of you cums, and I'll only fuck the one who lasts longest. I just want you to watch you both try to hold back."
    "Girl 2" "Awwww! Master, you're so mean!"
    "Girl 1" "Ohhh! Master, that's so unfair, the vibe in my asshole will make me cum way sooner than the vibes on your other slut's tits!"
    "Girl 2" "Master knows that I have sensitive nipples! I'd much rather have a vibe up my butt, but master's so so mean!"
    "Many of the boys have adapted to the new Ashford admirably."    
    $ deviance -=1
    return
    
label scorp_dormitory18:
    
    scene bg scorp_dormitory18 with fade
    "At night, the boys have started fighting brutal turf wars in the dormitories over who 'owns' which girls."
    "Beaten Guy" "Get off her! She's been mine for weeks!"
    "Victorious Guy" "Haha! Then you've had her too long, and now she's mine! Take a good look, this is the last time you'll see this pussy!"
    girl "Uh - uh - don't I get a say in this?"
    "Both Guys" "NO!"
    $ behavior -= 2    
    return
    
label scorp_dormitory19:
    
    scene bg scorp_dormitory19 with fade
    "Girls at the dormitories can expect night visitors to sneak in sometimes. You don't consider it a problem."
    $ morale -=1   
    return
    
label scorp_dormitory20:
    
    scene bg scorp_dormitory20 with fade
    "You find out that one of the girls has been taking strange men back to her dorm room and prostituting herself. She offers you a substantial bribe to look the other way - she must be raking it in!"
    menu:
        "Accept the bribe.":
            girl "You've made a very, VERY good decision. Now if you'll excuse me, I have another 10 men to fuck today if I want to make that money back..."
            girl "I love this job!"
            pov "You know what? Me too!"
            $ behavior -=2
            $ deviance +=1
            $ cash += 500           
            return
        
        "Decline the bribe and bust her little operation.":
            girl "You're making a big mistake!"
            pov "You're going to be in detention for a very long time, miss! Whoring your body out on school property is a serious offence!"
            $ behavior +=1
            $ deviance -=1
            $ inhibition +=1              
            return
    
label scorp_dormitory21:
    
    scene bg scorp_dormitory21 with fade
    "The dormitories have turned into a complete den of iniquity. The sex you can handle, but drugs? Such bad behavior..."
    $ behavior -=3   
    return
    
label scorp_dormitory22:
    
    scene bg scorp_dormitory22 with fade
    "Girls have started sneaking into the boys' dormitory, and vice versa. They're not doing anything sexual, as far as you can tell, but it's still very naughty!"
    $ behavior -=1   
    return
    
label scorp_dormitory23:
    
    scene bg scorp_dormitory23 with fade
    "Apparently, some boys have been finding it amusing to flash their erect cock at unsuspecting girls who come round to their dorm room."
    "The girls' reactions have been flustered and upset, but also... curious."
    $ inhibition -=1    
    return
    
label scorp_dormitory24:

    #Panning up and down
    scene bg scorp_dormitory24:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory24")    
    show screen scorp_screen
    
    girl "EEEEEK! What are you doing in the girls' dorm?!"
    pov "Whoops!"
    $ morale -=1  
    hide screen scorp_screen
    return
    
label scorp_dormitory25:
    
    scene bg scorp_dormitory25_1 with fade
    "You've heard there's problems in the dorm. Boys are waking up the girls every morning by sticking a cock in their mouth."
    scene bg scorp_dormitory25_2 with fade
    "The girls are mainly complaining about the mess it makes of their clothes."
    pov "The obvious solution to this problem would be for them to sleep nude."
    $ inhibition -=1     
    return
    
label scorp_dormitory26:
    
    scene bg scorp_dormitory26 with fade
    "The girls who go home every night at least have a break from the constant sex. But the ones staying at the dorms don't have a moment's rest."
    return
    
label scorp_dormitory27:
   
    scene bg scorp_dormitory27 with fade
    "On your nightly patrol of the dormitory, you hear quiet moans. Peeking into the girl's room, you see her... 'experimenting,' rubbing her crotch through her panties."
    "It's simultaneously sexy and adorable."
    return
    
label scorp_dormitory28:
    
    scene bg scorp_dormitory28 with fade
    "You open the door to a girl's room and spy her kneeling on the floor, one hand thrust down the front of her panties and furiously rubbing her clit."
    "She keeps going for a minute or so, then opens her eyes and screams when she sees you."
    girl "Aiiiieee!"
    "You beat a hasty retreat."
    $ inhibition -=1    
    return
    
label scorp_dormitory29:
    
    scene bg scorp_dormitory29 with fade
    girl "Umm... [povTitle] [povLastName]? What are you doing in my room?"
    pov "Uh, just doing the nightly rounds. Making sure everything's in order. Carry on."
    return
    
label scorp_dormitory30:
    
    scene bg scorp_dormitory30 with fade
    "It's perfectly normal for a male teacher to take a girl back to her dorm room in order to punish her privately."
    "It's perfectly normal for him to strip entirely naked, then get her to do the same."
    "And it's perfectly normal for him to have a huge, throbbing erection as he smacks her naked ass red and raw."
    "Right?"
    with vpunch
    "*spank*{w=1.0}{nw}"
    girl "Aaaaw!"
    with vpunch
    "*spank*{w=1.0}{nw}"
    girl "Aaaah!"
    $ behavior +=1   
    return
    
label scorp_dormitory31:
    
    scene bg scorp_dormitory31_1 with fade
    "One of the new trends going round the dorms is 'surprise bukkake.' A girl is held down, and then..."
    scene bg scorp_dormitory31_2 with fade
    "Surprise!"
    girl "Tch... You boys are so obnoxious sometimes..." 
    return
    
label scorp_dormitory32:
    
    scene bg scorp_dormitory32 with fade   
    "When you're indulging in some 'me time,' best to make sure you lock the door!"
    $ inhibition -=1     
    return
    
label scorp_dormitory33:
    
    scene bg scorp_dormitory33 with fade
    "Surprised Girl" "Oh my God! Susanna, if you're giving your boyfriend a handjob, can't you at least shut the door?"
    "Susanna" "Oh, just accept it, you prude! It's just a little handjob, no big deal. Don't pretend you've never seen a dick before!"
    $ inhibition -=1 
    return
    
label scorp_dormitory34:
    
    #Panning up and down
    scene bg scorp_dormitory34:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory34")    
    show screen scorp_screen
    
    girl "Ahhh! Principal! You should really knock before you come in!"
    pov "Hmmm, are you looking at hentai sites?"
    girl "N-no! Don't look!"
    pov "Relax. Let me show you some good doujin. Have you read 'Gun Tribe'?..."
    $ deviance +=1
    hide screen scorp_screen
    return
    
label scorp_dormitory35:
  
    scene bg scorp_dormitory35 with fade
    "Girls" "EEEEK! Close the door! Close the door!"
    pov "Whoops! Sorry ladies!"
    "You shut the door quietly. After a moment, you hear moans and slurping wet noises as the girls resume their play."
    $ inhibition -=1   
    return
    
label scorp_dormitory36:
    
    scene bg scorp_dormitory36 with fade
    "When modelling your new swimsuit in your dorm, first make sure everyone's actually gone to class."
    return
    
label scorp_dormitory37:
    
    scene bg scorp_dormitory37 with fade
    "The boys are settling into their dorm rooms just fine, it seems."
    return
    
label scorp_dormitory38:
    
    scene bg scorp_dormitory38 with fade
    "They're sleeping together, but they're not 'sleeping together.' Just sleeping, fully-clothed in pajamas, side by side."
    "Yet she still stays awake and worries if she's being a slut. They're back to back, because otherwise she can feel his erect cock pressing insistently against her."
    $ inhibition +=1
    return
    
label scorp_dormitory39:
    
    scene bg scorp_dormitory39_1 with fade
    "There's nothing quite like enjoying the mouth of a sleeping girl."
    scene bg scorp_dormitory39_2 with fade
    "She'll be surprised when she wakes up tasting cum tomorrow morning, and realizes this wasn't a dream."
    return
    
label scorp_dormitory40:
     
    scene bg scorp_dormitory40 with fade
    "Theoretically, separating girls' dorms from boys' dorms is done to stop students climbing into each other's beds and having sex."
    "There's one important flaw in that plan, however."
    return
    
label scorp_dormitory41:
    
    scene bg scorp_dormitory41 with fade
    "You peer into one of the girl's rooms, and are greeted with a wonderful sight."
    "With tits this big, button-up pajama tops are prone to just bursting open in the night."
    return
    
label scorp_dormitory42:
    
    #Panning up and down
    scene bg scorp_dormitory42:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory42")    
    show screen scorp_screen
    
    "Man" "Ahhhh, you're a good lay, bitch... Here's the cash you wanted..."
    girl "Uhhh... You really went for it... My poor pussy..."
    "Man" "Well, it's not every day you get to fuck a schoolgirl in her own dormitory. You going to keep whoring yourself like this?"
    girl "I get fucked all the time anyway... Might as well make money from it..."
    hide screen scorp_screen
    return
    
label scorp_dormitory43:
   
    scene bg scorp_dormitory43 with fade
    girl "Hello, [povTitle] [povLastName], are you going round the dormitories again?"
    "You stare at the cum-soaked girl. Sperm is leaking from between her spread legs."
    pov "Busy night?"
    "She reaches down and collects some of the cum from her open pussy on her fingers. With a wink, she puts her fingers in her mouth and sucks them clean."
    girl "VERY busy."
    return
    
label scorp_dormitory44:
    
    scene bg scorp_dormitory44 with fade
    "You believe this boy used to be known as a 'player'. Nowadays, though, fucking two girls at once isn't even considered unusual."
    return
    
label scorp_dormitory45:
    
    scene bg scorp_dormitory45 with fade
    "Girls go to school naked. They eat lunch naked. Then, at the end of the day, they go back to their dorm and sleep naked. In the morning, they go to school naked..."
    "You wonder if any of them have forgotten what clothes feel like."
    return

label scorp_dormitory46:
    
    scene bg scorp_dormitory46 with fade
    "After a long day of school, it's nice to go back to your dorm and get some well-earned rest."
    return

label scorp_dormitory47:
    
    scene bg scorp_dormitory47 with fade
    "Most of the girls now are sleeping nude. It's the first step in losing your inhibitions."
    $ inhibition -= 1    
    return

label scorp_dormitory48:
    
    scene bg scorp_dormitory48 with fade
    "God bless girls who sleep on top of the covers."
    return

label scorp_dormitory49:
    
    #Panning up and down
    scene bg scorp_dormitory49:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory49")    
    show screen scorp_screen
    
    "When girls get restless in their sleep, they can end up in the funniest positions..."
    hide screen scorp_screen
    return

label scorp_dormitory50:
    
    scene bg scorp_dormitory50 with fade
    "A boy gets his first blowjob in his dorm room. Having a private place to experiment, away from teachers, is only accelerating the student's sexual experimentation."
    $ deviance += 1     
    return

label scorp_dormitory51:
    
    scene bg scorp_dormitory51_1 with fade
    "The boys break into girls' rooms and gang up on them. Sometimes, the girls are entirely willing to participate..."
    girl "Ahhh... I love cocks... I'm completely addicted..."
    scene bg scorp_dormitory51_2 with fade
    girl "Yes... Cover me in your sticky cum..."
    return

label scorp_dormitory52:
    
    scene bg scorp_dormitory52_1 with fade
    "On your usual patrol of the dormitory, you hear low moans coming from the boys' toilets. Entering, you find one cubicle door covered in lewd writing and photos of a particular girl."
    scene bg scorp_dormitory52_2 with fade    
    "Opening the cubicle door, you're greeted with quite a sight."
    scene bg scorp_dormitory52_3 with fade
    "The girl moans mindlessly through her gag. Her pussy and asshole both look very well-used, and her body is covered in more lewd writing."    
    
    menu:
    
        "Free her.":
            scene bg scorp_dormitory52_4 with fade
            "You take off the girl's gag."
            girl "Uhhhn. Cock. Give me cock."
            pov "I'd have thought you'd had enough of that for a while."
            girl "I am a cumbucket... A slave to cock... Please use me for my intended purpose..."
            "The poor girl seems to have been completely broken by the endless fucking the boys subjected her to."
            with vpunch
            "*slap*{w=1.0}{nw}"
            pov "Snap out of it!"
            girl "I... Oh God... Are you here to let me go? I've been here for days..."
            "You untie the girl and help her stand, her legs shaking and huge amounts of cum spilling from her pussy and ass."
            girl "I was fucked, like, hundreds of times... It was horrible... But why do I feel so horny thinking about it?"
            "You take the girl to the nurse. She leaves a trail of cum behind her as she walks, her loose pussy-lips slapping against each other as she moves her thighs."
            girl "Thank you for saving me..."
            "Unfortunately, later you learn that taking their favourite toy away from them has made the boys very rebellious and upset."            
            $ morale -=1
            $ behavior -=1
            $ deviance -=1
            if renpy.random.randint(1, 3) == 1:
                $ good_points += 1             
            return
        
        "Leave her.":
            girl "Uhhhn... Uhhnnn..."
            pov "A few days as a sex slave is healthy for a growing girl. I think I'll leave you and let the boys have their fun."
            scene bg scorp_dormitory52_3 with fade
            "You close the door and walk away."
            $ morale +=1
            $ deviance +=1
            if renpy.random.randint(1, 3) == 1:
                $ evil_points += 1            
            return

label scorp_dormitory53:
    
    scene bg scorp_dormitory53 with fade
    "A girl is sketching in her room. She's keen to be a great artist!"
    $ artistery +=1   
    return
   
label scorp_dormitory54:
    
    scene bg scorp_dormitory54 with fade
    "Most dorm rooms have normal beds rather than bunk beds, but space is tight and some people get unlucky."  
    return   
    
label scorp_dormitory55:
    
    scene bg scorp_dormitory55 with fade
    "The dorm rooms are looking good! No trouble here!"  
    return
    
label scorp_dormitory56:
    
    scene bg scorp_dormitory56 with fade
    "It's nice to see girls just hanging out and having fun."
    "Girls" "Hello [povTitle] [povLastName]!"    
    return        
    
label scorp_dormitory57:
    
    scene bg scorp_dormitory57 with fade
    "Space is tight in the dorms, but this going too far!"    
    return    
    
label scorp_dormitory58:
    
    scene bg scorp_dormitory58 with fade
    "This guy's girlfriend brought her friend into his dorm room, to suck his cock as a birthday present." 
    "He kisses her in gratitude, while her friend gulps his penis head down to the back of her throat."
    guy "Best girlfriend ever!"
    return    
    
label scorp_dormitory59:
    
    scene bg scorp_dormitory59 with fade
    "A girl's lust can be a powerful thing. Put two of them in the same bed, and they can go all night long."
    return       
    
label scorp_dormitory60:
    
    scene bg scorp_dormitory60 with fade
    "Aww. Technically, the boys and girls' dorms are separated, but would you disrupt what could be true love's first kiss?"#
    "Not to mention true love's first finger inside a warm, wet cunt..."
    $ deviance +=1       
    return     
    
label scorp_dormitory61:
    
    scene bg scorp_dormitory61 with fade
    "You have no idea how this girl got tied up in this position - some incomplete sex game, perhaps? - but whoever did it, they left without freeing her."
    "You're sure someone will find her soon, and you hope for her sake it's a straight girl!"
    return   
    
label scorp_dormitory62:
    
    scene bg scorp_dormitory62 with fade
    "As soon as this girl returned to her dorm for the night, she removed her bra and panties, practically before she was even through the door."
    girl "I just like to feel free!"
    pov "Oh, what sweet temptation..."
    $ inhibition -=1    
    return       
    
label scorp_dormitory63:
    
    scene bg scorp_dormitory63 with fade
    "This girl spent the entire day without panties, constantly horny and a complete bag of nerves. It was exciting, but as she leans back against the door, she's glad to be back in the privacy of her room."
    girl "It was so exciting though.... I'll definitely do this again..."
    $ inhibition -=1    
    return   

label scorp_dormitory64:
    
    #Panning up and down
    scene bg scorp_dormitory64:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_dormitory64")    
    show screen scorp_screen
    
    "The boys didn't really appreciate being beaten at Go by a girl."
    hide screen scorp_screen
    return
    
label scorp_dormitory65:
    
    scene bg scorp_dormitory65_1 with fade
    "A boy is experimenting with his girlfriend in his dorm room."
    guy "You ready? It's going in..." 
    scene bg scorp_dormitory65_2 with fade   
    girl "Oooh... I can't believe I let you talk me into this..."
    guy "Just wait, I haven't even turned it on yet!"
    scene bg scorp_dormitory65_3 with fade
    guy "There we go! How does that feel?"
    girl "Aaaah... Aaaah... This is overwhelming... We should stop..."
    guy "Oh, don't be a little bitch about it. I'm turning the intensity way up."
    scene bg scorp_dormitory65_4 with fade   
    girl "NNNGHHHH... OH MY GOD..."
    guy "Well, see you in an hour or so!"
    girl "WHAT? WHERE ARE YOU - AAAHHH - AHHHH -"
    scene bg scorp_dormitory65_5 with fade
    "An hour later, the boy returns to find his girlfriend's pussy a juicy, convulsing mess, and her eyes rolled back in her head as she mindlessly groaned in torturous pleasure."
    guy "I was bored, so I went and fucked the girl next door. Wow, you're quite a sight to behold!"
    scene bg scorp_dormitory65_6 with fade
    "He removes the vibrator from her swollen, red pussy, and licks the salty juice from it."
    guy "Yum. You taste great! I might just put this back in and leave you all night..."
    girl "Waaa... You're so mean..."
    girl "...Please put it back in..."
    return  
    
label scorp_dormitory66:
    
    scene bg scorp_dormitory66 with fade
    "When you know that a lot of people are going to be seeing your pussy, it's important for a girl to make sure it looks as good as possible."
    girl "Hmmm... My asshole looks so pretty and pink too... The boys are totally going to love seeing this!"
    $ inhibition -=1    
    return  
    
label scorp_dormitory67:
    
    scene bg scorp_dormitory67 with fade
    "In a sexually-charged environment like Ashford, a girl's pussy can overheat quite easily. You walk in on a girl cooling hers down."
    
    if inhibition > 65:
        girl "Ahhh! [povTitle] [povLastName]! Don't come in, I'm busy!"
        pov "Sorry, sorry!"
        girl "Pervert!"
        $ morale -=1
        $ inhibition +=1         
        return        
    
    else:
        girl "Hello, [povTitle] [povLastName]."
        pov "Haha, I see you're cooling down?"
        girl "Yeah, my pussy's been burning hot and dripping wet all day... *giggle* Sorry, too much information?"
        return
        
label scorp_dormitory68:
    
    scene bg scorp_dormitory68 with fade
    "This girl turns her head innocently as you open the door."
    girl "Hmmm? What do you need?"
    "She gazes at you confidently, not caring at all about the naked ass cheeks easily visible beneath her long shirt."
    pov "Mary Mother of God..."
    $ inhibition -=1    
    return  
    
label scorp_dormitory69:
    
    scene bg scorp_dormitory69 with fade
    "Some shy girls have responded to the nude uniform policy by using bandaids to hide their nipples and the slit of their pussy."
    "If they think it's somehow made them less sexy, though, they're sorely mistaken."
    $ inhibition +=1    
    return  
    
label scorp_dormitory70:
    
    scene bg scorp_dormitory70 with fade
    "When you're not wearing panties, it's best not to sit in a position like this, or you could give your roommate an eyeful!" 
    return      