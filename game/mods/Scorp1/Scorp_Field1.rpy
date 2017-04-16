#### SCORP EVENT PACK 1 - Field ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this. 
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Sports Field.
## Pictures are located in the subdirectory \Scorp1\Field.
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

image bg scorp_field1 = "mods/Scorp1/Field/scorp_field1.jpg"
image bg scorp_field2_1 = "mods/Scorp1/Field/scorp_field2_1.jpg"
image bg scorp_field2_2 = "mods/Scorp1/Field/scorp_field2_2.jpg"
image bg scorp_field2_3 = "mods/Scorp1/Field/scorp_field2_3.jpg"
image bg scorp_field3 = "mods/Scorp1/Field/scorp_field3.jpg"
image bg scorp_field4 = "mods/Scorp1/Field/scorp_field4.jpg"
image bg scorp_field5 = "mods/Scorp1/Field/scorp_field5.jpg"
image bg scorp_field6 = "mods/Scorp1/Field/scorp_field6.jpg"
image bg scorp_field7 = "mods/Scorp1/Field/scorp_field7.jpg"
image bg scorp_field8 = "mods/Scorp1/Field/scorp_field8.jpg"
image bg scorp_field9 = "mods/Scorp1/Field/scorp_field9.jpg"
image bg scorp_field10 = "mods/Scorp1/Field/scorp_field10.jpg"
image bg scorp_field11 = "mods/Scorp1/Field/scorp_field11.jpg"
image bg scorp_field12 = "mods/Scorp1/Field/scorp_field12.jpg"
image bg scorp_field13 = "mods/Scorp1/Field/scorp_field13.jpg"
image bg scorp_field14 = "mods/Scorp1/Field/scorp_field14.jpg"
image bg scorp_field15_1 = "mods/Scorp1/Field/scorp_field15_1.jpg"
image bg scorp_field15_2 = "mods/Scorp1/Field/scorp_field15_2.jpg"
image bg scorp_field15_3 = "mods/Scorp1/Field/scorp_field15_3.jpg"
image bg scorp_field15_4 = "mods/Scorp1/Field/scorp_field15_4.jpg"
image bg scorp_field15_5 = "mods/Scorp1/Field/scorp_field15_5.jpg"
image bg scorp_field15_6 = "mods/Scorp1/Field/scorp_field15_6.jpg"
image bg scorp_field15_7 = "mods/Scorp1/Field/scorp_field15_7.jpg"
image bg scorp_field15_8 = "mods/Scorp1/Field/scorp_field15_8.jpg"
image bg scorp_field15_9 = "mods/Scorp1/Field/scorp_field15_9.jpg"
image bg scorp_field16_1 = "mods/Scorp1/Field/scorp_field16_1.jpg"
image bg scorp_field16_2 = "mods/Scorp1/Field/scorp_field16_2.jpg"
image bg scorp_field17 = "mods/Scorp1/Field/scorp_field17.jpg"
image bg scorp_field18 = "mods/Scorp1/Field/scorp_field18.jpg"
image bg scorp_field19 = "mods/Scorp1/Field/scorp_field19.jpg"
image bg scorp_field20 = "mods/Scorp1/Field/scorp_field20.jpg"
image bg scorp_field21 = "mods/Scorp1/Field/scorp_field21.jpg"
image bg scorp_field22 = "mods/Scorp1/Field/scorp_field22.jpg"
image bg scorp_field23 = "mods/Scorp1/Field/scorp_field23.jpg"
image bg scorp_field24 = "mods/Scorp1/Field/scorp_field24.jpg"
image bg scorp_field25 = "mods/Scorp1/Field/scorp_field25.jpg"
image bg scorp_field26 = "mods/Scorp1/Field/scorp_field26.jpg"
image bg scorp_field27 = "mods/Scorp1/Field/scorp_field27.jpg"
image bg scorp_field28 = "mods/Scorp1/Field/scorp_field28.jpg"
image bg scorp_field29 = "mods/Scorp1/Field/scorp_field29.jpg"
image bg scorp_field30 = "mods/Scorp1/Field/scorp_field30.jpg"
image bg scorp_field31 = "mods/Scorp1/Field/scorp_field31.jpg"
image bg scorp_field32 = "mods/Scorp1/Field/scorp_field32.jpg"
image bg scorp_field33 = "mods/Scorp1/Field/scorp_field33.jpg"
image bg scorp_field34_1 = "mods/Scorp1/Field/scorp_field34_1.jpg"
image bg scorp_field34_2 = "mods/Scorp1/Field/scorp_field34_2.jpg"
image bg scorp_field36 = "mods/Scorp1/Field/scorp_field36.jpg"
image bg scorp_field37 = "mods/Scorp1/Field/scorp_field37.jpg"
image bg scorp_field38 = "mods/Scorp1/Field/scorp_field38.jpg"
image bg scorp_field39 = "mods/Scorp1/Field/scorp_field39.jpg"

#Setting up events and conditions

init:
    $ event("scorp_field1", "act == 'sports_field' and deviance > 98 and inhibition < 2", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field2", "act == 'sports_field' and deviance > 95 and inhibition < 15", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field3", "act == 'sports_field' and uniform == 'nude_uniform' and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field4", "act == 'sports_field' and uniform == 'nude_uniform' and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field5", "act == 'sports_field' and deviance > 20 and inhibition < 80 and deviance < 80", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field6", "act == 'sports_field' and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field7", "act == 'sports_field' and deviance > 40 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field8", "act == 'sports_field' and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field9", "act == 'sports_field' and inhibition < 90 and inhibition > 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field10", "act == 'sports_field' and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field11", "act == 'sports_field' and deviance > 95 and inhibition < 15", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field12", "act == 'sports_field' and deviance > 75 and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field13", "act == 'sports_field' and deviance > 65 and inhibition < 30", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field14", "act == 'sports_field' and uniform == 'nude_uniform' and athletics > 60", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field15", "act == 'sports_field' and deviance > 98 and inhibition < 2 and athletics > 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field16", "act == 'sports_field' and uniform == 'nude_uniform' and inhibition < 20 and athletics > 60", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field17", "act == 'sports_field' and deviance > 75 and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field18", "act == 'sports_field' and inhibition > 75", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field19", "act == 'sports_field' and inhibition < 50 and deviance > 50 and deviance < 80", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field20", "act == 'sports_field' and deviance > 15 and deviance < 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field21", "act == 'sports_field' and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field22", "act == 'sports_field' and inhibition < 45 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field23", "act == 'sports_field' and inhibition < 55 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field24", "act == 'sports_field' and inhibition < 95 and inhibition > 80 and athletics > 50", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field25", "act == 'sports_field' and athletics > 30 and inhibition > 60", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field26", "act == 'sports_field' and deviance > 98 and inhibition < 2", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field27", "act == 'sports_field' and deviance > 90 and inhibition < 20 and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field28", "act == 'sports_field' and deviance > 95 and inhibition < 10", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field29", "act == 'sports_field' and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field30", "act == 'sports_field' and deviance < 25", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field31", "act == 'sports_field' and inhibition > 60 and inhibition < 95", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field32", "act == 'sports_field' and inhibition > 60", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field33", "act == 'sports_field' and deviance > 70 and uniform == 'nude_uniform'", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field34", "act == 'sports_field' and deviance > 70 and inhibition < 25 and athletics > 55", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field35", "act == 'sports_field' and deviance > 80 and inhibition < 15 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field36", "act == 'sports_field' and inhibition > 70", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field37", "act == 'sports_field' and deviance > 80 and inhibition < 25", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field38", "act == 'sports_field' and deviance > 85 and inhibition < 25 and athletics > 80", event.choose_one('sports_field'), priority=200)
    $ event("scorp_field39", "act == 'sports_field' and athletics > 80 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('sports_field'), priority=200)
    
label scorp_field1:
    
    pov "You think Ashford Academy has discovered the next evolution of track and field."  
    #Panning up and down    
    scene bg scorp_field1:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_field1")    
    show screen scorp_screen
    
    "Coach" "On your cocks, girls! Get set! Go!"
    "With a chorus of slurping and a synchronized spray of pussy juice, the girls leap off the boys' dicks and start the race, bare asses bouncing."
    "It's unorthodox, but it's certainly made track and field more popular!"
    $ athletics += 1
    if renpy.random.randint(1, 4) == 1:
        $ athletics += 5    
    hide screen scorp_screen
    return
    
label scorp_field2:
    
    scene bg scorp_field2_1 with fade
    "A large group of boys have captured some girls and set up some kind of contest. As you watch, the boys start masturbating furiously, while the girls struggle and cry."
    menu:
        "Put a stop to it.":
            if behavior <50:
                pov "This looks fun and all, but I don't think the girls are into it."
                "Guy 1" "Who gives a fuck what they're into? They're each just a collection of holes."
                "Apart from that comment, the boys completely ignore you! They keep masturbating and then let loose all at once, thick strands of cum flying through the air towards the tied girls."
                scene bg scorp_field2_2 with doubleflash
                "Guy 1" "YES! A direct hit! Right in the cunt!"
                "Guy 2" "Dammit, I only got her tits!"
                "Guy 3" "I hit the blonde bitch's pussy! She's mine, okay?"
                "Blonde Girl" "I'm nobody's! Let me go!"
                "Chastity" "Can I get pregnant from this?"
                "Guy 1" "Shut up, slut. Someone untie her, I want my prize now."
                scene bg scorp_field2_3 with fade   
                "It's a pretty sight, but you're shocked at how little you could do to save the girls' pride. Some of your students are out of control!"                
                $ deviance +=1
                $ behavior -=2                
                return
            else:   
                pov "This looks fun and all, but I don't think the girls are into it."            
                "The boys stop masturbating and stare at you."
                "Guy 1" "Oh, man! Are you seriously ruining our game?"
                "Guy 2" "The fact they're not into it is what makes it funny!"
                "They grumble, but obey you, tucking their dicks away and untying the girls - though you notice their fingers seem to 'accidentally' slip in a few places where they don't belong."
                girls "Thank you so much, [povTitle] [povLastName]!"
                $ morale -=1
                $ inhibition +=1
                $ deviance +=1                
                return      
        "Watch with interest.":
                "The boys seem to gather up steam, and then let loose all at once, thick strands of cum flying through the air towards the tied girls."
                scene bg scorp_field2_2 with doubleflash
                "Guy 1" "YES! A direct hit! Right in the cunt!"
                "Guy 2" "Dammit, I only got her tits!"
                "Guy 3" "I hit the blonde bitch's pussy! She's mine, okay?"
                "Blonde Girl" "I'm nobody's! Let me go!"
                "Chastity" "Can I get pregnant from this?"
                "Guy 1" "Shut up, slut. Someone untie her, I want my prize now."
                scene bg scorp_field2_3 with fade   
                "And to the winner, the spoils."    
                $ deviance +=1
                return    
    
    
label scorp_field3:
    
    scene bg scorp_field3 with fade
    "The nude uniform presented a problem for the cheerleaders, who wanted to keep their sexy outfits. Luckily, they found a compromise."
    return
    
label scorp_field4:
    
    scene bg scorp_field4 with fade
    "The nude uniform presented a problem for the cheerleaders, who wanted to keep their sexy outfits. Luckily, they found a compromise."
    return
    
label scorp_field5:
    
    scene bg scorp_field5 with fade
    pov "How on EARTH did you get in that position?"
    girl "I was running too fast..."
    menu:
        "Help her.":
            "You help the clumsy girl to her feet, where she's able to finally pull up her pants and hide her exposed ass and pussy."
            girl "Oh... How embarrassing! Thank you, principal! I'm so clumsy!"
            $ good_points += 1            
            $ inhibition -=1            
            return
        "Help her, but slip a finger or two inside her as you do so.":
            if deviance >40:
                "As you untangle her with one hand, you place the other hand on her exposed butt." 
                "While she's adjusting her bra, you quickly thrust two fingers in her pussy and a third up her pretty asshole."     
                girl "Eeek! Oh, [povTitle] [povLastName], how naughty! *giggle*"
                "She's lovely, soft and warm inside, and you lift her to her feet using the fingers thrust deep inside her."
                girl "Oooh - ohhh!"
                "You feel her pussy clench, spasm, and gush as she orgasms. With a smile, you pat her butt, and she pulls up her yoga pants and flashes you a smile."
                girl "Thank you for the help, principal!"
                $ good_points += 1                 
                return
            else: 
                "As you untangle her with one hand, you place the other hand on her exposed butt." 
                "While she's adjusting her bra, you quickly thrust two fingers in her pussy and a third up her pretty asshole."
                girl "EEEEK! What are you doing! Waaaaaa!"
                "She struggles out of your grip, and your fingers slide out of her tight holes. The little bitch runs and tells everyone what a pervert you are."
                pov "This won't be good for my reputation."
                $ reputation -=1     
                return                
        "Humiliate her.":
            pov "Hahaha! That's the fucking funniest thing I've ever seen! Everyone! Come look at this!"
            girl "Nooooooo!"
            "You seen have a crowd of laughing boys and girls around you. The trapped girl struggles to get up, but only gets tangled in the net more."
            pov "Look at that little butthole thrust in the air! I should plant the school flag!"
            pov "Why don't we pull up a lawn-chair and use her as a cup holder?"
            pov "Or maybe if we get her wet enough we can use her as a bird bath?"
            "Your comments crack everyone up still further. A few boys take pictures on their phones, to upload onto the internet later."
            "Finally, a few good-hearted girls come and untangle the poor clumsy bitch, much to everyone else's sorrow."
            "Guy 1" "Should've left her like that! We could've all had a go on her!"
            "Her face burning red, the clumsy girl runs away crying. But apart from with her, you're suddenly very popular - most students think you're a really funny guy now."
            $ evil_points += 1 
            $ morale += 1
            $ inhibition -= 1
            return
            
label scorp_field6:
    
    scene bg scorp_field6 with fade
    "The new uniform makes the school races much more popular. Nude girls are so delightfully bouncy!"
    $ athletics += 1
    if renpy.random.randint(1, 4) == 1:
        $ athletics += 5    
    return
    
label scorp_field7:
    
    scene bg scorp_field7 with fade
    "This is an important game against a rival school, but the Ashford pitcher almost seems distracted by something."
    "And the other players keep complaining about this weird buzzing noise..."
    return
    
label scorp_field8:
    
    #Panning up and down    
    scene bg scorp_field8:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_field8")    
    show screen scorp_screen
    
    "The new uniform makes the field a much more attractive place. Girls can't play sports any more without being heckled though."
    guy "I love how you handle balls, bitch!"
    $ athletics += 1    
    hide screen scorp_screen
    return    
    
label scorp_field9:
    
    scene bg scorp_field9 with fade
    "It's great when a beautiful girl gets hot and sweaty. Especially when she's not wearing a bra."
    return
    
label scorp_field10:
   
    scene bg scorp_field10 with fade
    "Girls playing naked tennis! Advantage: boys!"
    $ athletics += 1    
    return
    
label scorp_field11:
    
    "You come across an interesting scene in the middle of the tennis court..."
    scene bg scorp_field11 with fade
    "A girl lies panting and spread-eagled on the turf, a sporty-looking boy pounding her pussy hard. He's clearly not the first to have a turn. A circle of other boys are watching and laughing."
    pov "What's going on here?"    
    "Guy 1" "When a girl plays a game with the boys, we have a rule - if she loses, her body is the prize."
    "Guy 2" "And she challenged all of us."
    pov "She knew she never had a chance, but she played anyway..."
    "One of the guys reaches down and grabs her hair, pulling her head up so her eyes meet yours. She looks lost in a world of her own, moaning and looking right through."
    "Guy 1" "Tell the principal how much you love tennis."
    girl "Oh God! OH GOD! I LOVE IT!"
    $ athletics += 1       
    return

label scorp_field12:
    
    scene bg scorp_field12 with fade
    "Bullies these days don't demand a girl's lunch money."
    $ behavior -= 1     
    return

label scorp_field13:
    
    scene bg scorp_field13 with fade
    girl "[povTitle] [povLastName]! This is so naughty! The big match is on and the whole school could see us!"
    pov "Do you always state the obvious like that? Shut up and don't stop grinding that ass again."
    return
    
label scorp_field14:
    
    #Panning up and down    
    scene bg scorp_field14:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_field14")    
    show screen scorp_screen
    
    "Some of the teachers, without your knowledge, have organized a girls' charity race through town."
    "With the new uniform, it ends up being a beautiful sight, but you're worried what the townspeople will think!"
    "However, much to your surprise, you end up getting a lot of compliments on how happy, healthy and beautiful the girls look!"
    "Middle-aged Woman" "You could just tell those girls were happy in who they are! Well done, Principal. I didn't think it was a good idea at first, but you've changed my mind."
    "Old Man" "It did my old heart good, to see so much flesh in my old age! Really brightened up the town!"
    "Young Boy" "I got to see their titties go boing-boing!"
    "A lot of people in town are more accepting of the nude uniform now."
    $ inhibition -= 1   
    $ reputation += 1
    $ athletics += 1
    if renpy.random.randint(1, 4) == 1:
        $ athletics += 5  
    hide screen scorp_screen
    return
    
label scorp_field15:
    
    scene bg scorp_field15_1 with fade
    "Girls are practicing for a big race when the coach decides to have some fun with them."
    scene bg scorp_field15_2 with fade    
    "Firing the pistol with one hand, he uses the other to grab one girl's plump, raised ass. The other girls take off at a run, but she and a friend stay behind, shocked."
    "Girl's Friend" "Huh?"
    scene bg scorp_field15_3 with fade 
    "Wasting no time, he pulls down her tight shorts - no panties, of course - and pushes the entire length of his cock into the warm, accepting mound of flesh in front of him."
    girl "OH! COACH!"
    scene bg scorp_field15_4 with fade 
    girl "Coach! We should be practicing right now! We can do this in the storeroom afterwards like normal - oh! OH! OH MY GOD!"    
    scene bg scorp_field15_5 with fade     
    "Coach" "You're protesting, but you're the one moving your hips now, silly slut."
    girl "I am? *giggle* Oh God... I am...!"
    scene bg scorp_field15_6 with fade    
    "The coach unloads a great spurt of cum inside her dripping cunt as she orgasms."
    girl "AAAHHHH! AAAAHH OOOOHHHH YESSSS!"
    "Coach" "And you're next, you eager bitch!"
    scene bg scorp_field15_7 with fade   
    "Girl's Friend" "Coach! Coach! Oh fuck I love you coach keep going!"
    scene bg scorp_field15_8 with fade 
    "Girl's Friend" "UHHH! YES! CUM! FILL ME UP!"
    scene bg scorp_field15_9 with fade     
    "Coach" "Good girls. Now get up and finish the race. One of you's going to finish last now, and that one's getting detention."
    "The girls stand up half-naked and stumble down the track, legs quivering and great bursts of cum flooding down from their blushing red pussies."
    girl "Oh, coach, you're so mean!"
    $ athletics += 1
    $ r = renpy.random.randint(1,3)
                    
    if r == 1:
        $ deviance += 5
    elif r == 2:
        $ athletics += 5   
    return
    
label scorp_field16:
    
    scene bg scorp_field16_1 with fade
    "With the nude uniform, identifying girls from each other in a sporting event was starting to be difficult."
    "Luckily, the girls having taken matters into their own hands, using bodypaint and nipple piercings to designate themselves."
    scene bg scorp_field16_2 with fade  
    "What a beautiful sight!"
    "Crowd" "Run, number 72, run!"   
    "Number 72" "My tits hurt..."    
    return
    
label scorp_field17:
    
    scene bg scorp_field17 with fade
    "Hearing a soft slurping noise, you look behind a bush and stumble upon a girl enthusiastically sucking a boy's dick."
    guy "Hey, [povTitle] [povLastName]!"
    "The girl is listening to noise-cancelling headphones while she sucks, and has no idea you're there."
    guy "Touch her, go on. She's lost in the music, she'll just think it's me."
    menu:
        "Play along.":
            "You play with her sopping pussy for a while, sliding a few fingers in her ass while you're at it. The girl just wriggles happily in response."
            guy "Neat, isn't it? I've been telling everyone who walks past to do that. I wonder when she'll notice!"
            "The two of you high-five, and you walk away with an uncomfortable erection."
            $ inhibition -= 1  
            $ behavior -= 1            
            return
        "Act outraged.":
            pov "How dare you suggest such a thing!"
            "You spank the girl's bare ass hard. She gives the boy one last lick, turns around, and yelps when she sees you."
            pov "Both of you are going to be punished!"
            girl "What?"
            pov "I said, both of you are going to be punished!"        
            $ inhibition += 1  
            $ deviance -= 1  
            $ morale -= 1  
            $ behavior += 1             
            return            
    
label scorp_field18:
    
    scene bg scorp_field18 with fade
    "You wonder if she knows what those tight gym shorts do to the boys and men around her."
    return
    
label scorp_field19:
    
    scene bg scorp_field19 with fade
    girl "Hi [povTitle] [povLastName]... It's just lotion... I swear... *wink*"
    return
    
label scorp_field20:
    
    scene bg scorp_field20 with fade
    "Some plucky wannabe-businessman has been stealing girls' panties from their lockers. He's selling them in the field in a makeshift auction."
    "Panty Thief" "These are Chastity's panties. Can I have a starting bid?"
    "Guy 1" "Chastity's? Hmmm, she's pretty good... 100 yen!"
    "Guy 2" "200 yen!"
    "The bidding gets more frenzied as you walk away."
    $ deviance += 1      
    return
    
label scorp_field21:
    
    scene bg scorp_field21 with fade
    "No matter how adult a schoolgirl seems, she's still willing to let go and play like she was a kid again."
    return
    
label scorp_field22:
    

    "You're walking through the field when -"
    with vpunch
    "Everything goes black."
    girl "Is he alright?"
    "Lying prone on the ground where you tripped up, you open your eyes."
    scene bg scorp_field22 with fade    
    "And it's only now that you realize quite how many girls have stopped wearing panties."
    girl "Are you okay, [povTitle] [povLastName]?"
    pov "I think so, but I might have died and gone to heaven..."
    $ inhibition -= 1     
    return
    
label scorp_field23:
    
    scene bg scorp_field23 with fade
    "With so many girls going commando, high winds can lead to high blood pressure."
    return
    
label scorp_field24:

    scene bg scorp_field24 with fade
    "A girl bent over and panting after running a mile can look oddly similar to a girl bent over and panting for... other reasons."
    return
    
label scorp_field25:
    
    scene bg scorp_field25 with fade
    "There's a lot of bouncing going on in this match. You play close attention."
    return
    
label scorp_field26:
    
    scene bg scorp_field26 with fade
    "You can't help but admire the boys' ingenuity in finding new ways to assert themselves over the girls."
    "Simply passing the baton in a relay race has been twisted to make sure any girls involved are naked, fucked, and humiliated."
    return
    
label scorp_field27:
   
    scene bg scorp_field27 with fade
    "To make women's basketball more entertaining, the coach has ensured that all the girls involved are wearing discreet vibrators."
    return
    
label scorp_field28:
    
    scene bg scorp_field28 with fade
    "Some girls have joined the boxing club to learn self-defence, but on their first day they quickly realize it's a full-contact sport."
    girl "AAAH!"
    return
    
label scorp_field29:
  
    scene bg scorp_field29 with fade
    "Anyone for tennis?"
    return
    
label scorp_field30:
    
    scene bg scorp_field30 with fade
    pov "Keep practicing, girl! Maybe one day you'll make the team!"
    $ athletics += 1    
    return
    
label scorp_field31:
    
    scene bg scorp_field31 with fade
    "WHAT A CATCH! Her pants were pulled down in the slide, but she's too proud to care!"
    "The crowd's applauding wildly. You're not sure whether they're applauding the girl's catch or the girl's snatch."
    $ inhibition -= 1      
    return
    
label scorp_field32:

    scene bg scorp_field32 with fade
    "That was a good catch! And it came with a good view!"
    $ inhibition -= 1      
    return
    
label scorp_field33:
    
    scene bg scorp_field33 with fade
    "This girl's tits are so huge, she's been given special dispensation to wear some support during sport, despite the uniform code. All she's allowed is a skimpy bikini top, though."
    "She's not even that good at baseball - the boys just humour her as they love to watch those massive mammaries fly."
    return
    
label scorp_field34:
    
    guy "Momo! Have you got us a new ball yet? This one's still bouncing funny!"
    scene bg scorp_field34_1 with fade
    girl "Just coming! Give me - uh - a sec!"
    guy "It's okay! Take all the time you need!"
    scene bg scorp_field34_2 with fade   
    guy "God, she's stupid if she thinks I can't see this... Can't wait to upload this footage to Youtube..."    
    return
    
label scorp_field35:
      
    "This girl has learned the most important tactic she can use when playing against boys who are stronger, smarter, and faster -"
    scene bg scorp_field35 with fade
    "Keep their eyes off the ball!"    
    return
    
label scorp_field36:
    
    scene bg scorp_field36 with fade
    girl "[povTitle] [povLastName]! Think fast!"
    with vpunch
    girl "Faster than that!"   
    return
    
label scorp_field37:
    
    scene bg scorp_field37 with fade
    "There are a lot more girls than boys at Ashford. Luckily, a girl can accommodate multiple cocks, at once and throughout the day."
    return
    
label scorp_field38:
    
    scene bg scorp_field38 with fade
    guy "Stop struggling, Hana! There's no 'I' in team!"
    "Hana" "That doesn't mean I have to let you all fuck me!"
    guy "Hey, coach said it would be good for morale!"
    "Hana" "...*sigh* Fine."
    $ morale +=1
    return
    
label scorp_field39:
    
    scene bg scorp_field38 with fade
    "Ashford students have been pushing themselves to the limit recently. An active school is a happy school!"
    $ athletics +=1
    return    