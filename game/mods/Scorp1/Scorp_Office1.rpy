#### FLAGON EVENT PACK 1 - Office ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this. 
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Office.
## Pictures are located in the subdirectory \Scorp1\Office
## All custom images, characters, variables... are prefixed with "scorp_" (with the exception of temp variables) to avoid conflicts.
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

image bg scorp_office = "mods/Scorp1/Office/scorp_office.jpg"

image bg scorp_office1 = "mods/Scorp1/Office/scorp_office1.jpg"
image bg scorp_office2 = "mods/Scorp1/Office/scorp_office2.jpg"
image bg scorp_office3 = "mods/Scorp1/Office/scorp_office3.jpg"
image bg scorp_office4_1 = "mods/Scorp1/Office/scorp_office4_1.jpg"
image bg scorp_office4_2 = "mods/Scorp1/Office/scorp_office4_2.jpg"
image bg scorp_office4_3 = "mods/Scorp1/Office/scorp_office4_3.jpg"
image bg scorp_office4_4 = "mods/Scorp1/Office/scorp_office4_4.jpg"
image bg scorp_office5 = "mods/Scorp1/Office/scorp_office5.jpg"
image bg scorp_office6 = "mods/Scorp1/Office/scorp_office6.jpg"
image bg scorp_office7_1 = "mods/Scorp1/Office/scorp_office7_1.jpg"
image bg scorp_office7_2 = "mods/Scorp1/Office/scorp_office7_2.jpg"
image bg scorp_office8_1 = "mods/Scorp1/Office/scorp_office8_1.jpg"
image bg scorp_office8_2 = "mods/Scorp1/Office/scorp_office8_2.jpg"
image bg scorp_office8_3 = "mods/Scorp1/Office/scorp_office8_3.jpg"
image bg scorp_office9 = "mods/Scorp1/Office/scorp_office9.jpg"
image bg scorp_office10 = "mods/Scorp1/Office/scorp_office10.jpg"
image bg scorp_office11 = "mods/Scorp1/Office/scorp_office11.jpg"
image bg scorp_office12 = "mods/Scorp1/Office/scorp_office12.jpg"
image bg scorp_office13_1 = "mods/Scorp1/Office/scorp_office13_1.jpg"
image bg scorp_office13_2 = "mods/Scorp1/Office/scorp_office13_2.jpg"
image bg scorp_office13_3 = "mods/Scorp1/Office/scorp_office13_3.jpg"
image bg scorp_office13_4 = "mods/Scorp1/Office/scorp_office13_4.jpg"
image bg scorp_office13_5 = "mods/Scorp1/Office/scorp_office13_5.jpg"
image bg scorp_office14_1 = "mods/Scorp1/Office/scorp_office14_1.jpg"
image bg scorp_office14_2 = "mods/Scorp1/Office/scorp_office14_2.jpg"
image bg scorp_office14_3 = "mods/Scorp1/Office/scorp_office14_3.jpg"
image bg scorp_office15 = "mods/Scorp1/Office/scorp_office15.jpg"
image bg scorp_office16 = "mods/Scorp1/Office/scorp_office16.jpg"
image bg scorp_office17_1 = "mods/Scorp1/Office/scorp_office17_1.jpg"
image bg scorp_office17_2 = "mods/Scorp1/Office/scorp_office17_2.jpg"
image bg scorp_office18 = "mods/Scorp1/Office/scorp_office18.jpg"
image bg scorp_office19 = "mods/Scorp1/Office/scorp_office19.jpg"
image bg scorp_office20 = "mods/Scorp1/Office/scorp_office20.jpg"

#Setting up events and conditions

init:
    $ event("scorp_office1", "act == 'office' and inhibition < 15 and deviance > 90", event.choose_one('office'), priority=200)
    $ event("scorp_office2", "act == 'office' and deviance > 75 and inhibition < 25 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office3", "act == 'office' and deviance > 50 and inhibition < 50 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office4", "act == 'office' and inhibition < 80 and deviance > 30", event.choose_one('office'), priority=200)
    $ event("scorp_office5", "act == 'office' and deviance > 75 and inhibition < 25 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office6", "act == 'office' and deviance > 90 and inhibition < 30", event.choose_one('office'), priority=200)
    $ event("scorp_office7", "act == 'office' and deviance > 75 and inhibition < 25 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office8", "act == 'office' and inhibition < 45 and deviance > 65", event.choose_one('office'), priority=200)
    $ event("scorp_office9", "act == 'office' and inhibition < 50 and deviance > 20", event.choose_one('office'), priority=200)
    $ event("scorp_office10", "act == 'office' and deviance > 60 and inhibition < 40 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office11", "act == 'office' and deviance > 60 and inhibition < 20 and uniform == 'sexy_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office12", "act == 'office' and inhibition < 20 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office13", "act == 'office' and inhibition < 40 and deviance > 65", event.choose_one('office'), priority=200)
    $ event("scorp_office14", "act == 'office' and inhibition < 50 and deviance > 40 and uniform == ('uniform' or 'conservative_uniform')", event.choose_one('office'), priority=200)
    $ event("scorp_office15", "act == 'office' and deviance > 95", event.choose_one('office'), priority=200)
    $ event("scorp_office16", "act == 'office' and deviance > 95", event.choose_one('office'), priority=200)
    $ event("scorp_office17", "act == 'office' and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("scorp_office18", "act == 'office' and inhibition > 70 and deviance < 25", event.choose_one('office'), priority=200)
    $ event("scorp_office19", "act == 'office' and inhibition < 30", event.choose_one('office'), priority=200)
    $ event("scorp_office20", "act == 'office' and inhibition < 10 and deviance > 95", event.choose_one('office'), priority=200)

label scorp_office1:

    scene bg scorp_office1 with fade
    "These days, your secretary makes sure you have a girl waiting in your office every morning. Usually under your desk."
    girl "Would you like a blowjob, [povTitle] [povFirstName]?"
    pov "I love this school!"

    return
    
label scorp_office2:
    
    scene bg scorp_office2 with fade
    "The nude uniform policy makes assemblies much more fun. Girls go so red when they're up on stage!"
    "This girl's speech is being recorded. She'll be on the school website soon enough."
    "As you watch her talk, oblivious, the cameraman slowly pans down to her dripping pussy, and zooms in."
    return
    
label scorp_office3:
    
    scene bg scorp_office3 with fade
    "The nude uniform policy makes assemblies much more fun. Girls go so red when they're up on stage!"
    "And get so wet..."
    return
    
label scorp_office4:
    
    scene bg scorp_office4_1 with fade

    "As you travel into work today, you notice one of your pupils being molested on the train."

    if deviance <= 80:
        
        "She's writhing in the commuters' grasp, as their fingers massage her breasts and slide inside her."
        
        menu:
            "Intervene on her behalf.":
                pov "Hey! Hands off my student, perverts!"
                "The commuters look shocked, and let the girl go. She falls to her knees and adjusts her clothes, covering herself."
                girl "Oh my God, [povTitle] [povFirstName], thank you so much! They were... They were..."
                pov "I know, I know. Come on, stick with me, we'll walk to school together."
            
                $ morale +=1
                $ deviance -=1
                $ inhibition +=1
                if renpy.random.randint(1, 5) == 1:
                    $ good_points += 1
                        
                return
            
            
            "Let the commuters have their fun.":
                scene bg scorp_office4_2 with flash
                "The commuters grow more and more bold, pulling aside the girl's panties and revealing her soaking pussy to the whole train."
                girl "Aiiieee!"
                "They're shoving their fingers roughly into her sopping cunt. Finally, she manages to break free, and clutches you, sobbing."
                girl "Waaa! Why didn't you help me?"
                pov "Uh..."
                "This isn't going to do your reputation any favours."

                $ inhibition -=1
                $ deviance +=1
                $ reputation -=1
                $ morale -=1
                if renpy.random.randint(1, 3) == 1:
                    $ evil_points += 1
            
                return
        
    else:
        "After a few minutes of obligatory struggle, the girl seems to accept what's happening and start to enjoy it."
        girl "Unnnnh, yes, keep going!"
        "The commuters can't believe their luck, and tear her panties to one side."
        scene bg scorp_office4_2 with flash
        guy "Look at her! She's begging for it! What a slut!"
        "The girl's sighs, and the wet noises of their fingers pumping in and out of her pussy, fill the carriage. A few look away in disgust."
        "Soon enough, the commuters have pulled their cocks out and begun to close in."
        girl "No - not here -"
        scene bg scorp_office4_3 with flash
        "A commuter slams his throbbing dick into the girl's pussy with a loud, wet noise, and he begins to pump in and out."
        pov "Damn... This is the stop for the school... It was just getting good..."
        pov "Surely she should be getting off here too?"
        "As the train doors slide shut behind you, you hear the girl let out a scream of uncontrollable ecstasy."
        pov "Well, I guess she is getting off after all, heh."
        scene bg scorp_office4_4 with flash
        "You later hear that the girl turned up to school, half-naked and soaked in cum, three hours late." 

        $ behavior -= 1
        $ deviance += 1
        $ inhibition -= 1
        return

label scorp_office5:
    
    scene bg scorp_office5 with fade
    "The nude uniform policy makes assemblies much more fun. Girls go so red when they're up on stage!"
    "Look at that line of naked asses..."
    "When the girls finish their speech and hurry backstage, you spank each one as they go past, making them yelp slightly."
    return
    
label scorp_office6:
    
    scene bg scorp_office6 with fade
    "You walk past a male teacher, on his way to the teachers' lounge."
    "He's pushing a half-naked girl in front of him, holding her by her legs like a wheelbarrow, impaled on his cock."
    girl "AAaaah, oh my God AAAAAAAAAAAAH YES!"
    teacher "Thank you, [povFirstName]. You've improved this school beyond measure."
    "He walks off, pumping merrily into the cunt of the teenage girl waddling on her hands before him."
    $ deviance +=1
    return
    
label scorp_office7:
    
    scene bg scorp_office7_1
    "This naughty-looking slut has been sent directly to your office for wearing bandaids over her nipples and the slit of her pussy, in defiance of the nude uniform policy."
    girl "[povTitle] [povFirstName]!"
    "She stands with her tits thrust out and hands on her hips. Despite the bandaids, she's clearly not modest."
    pov "What is the meaning of this? You realize these bandaids are against the new school policy?"
    girl "I know, but when I walk around butt-naked, I'm just a fucktoy! Boys fuck my holes, cum inside me, and move on to the next girl! I had to find a way to preserve the mystery and make myself more of a challenge."
    girl "Now I get treated better than any other girl in school!"

    menu:
        "Fine, you can keep wearing them, if it makes you happy.":
            pov "How could I argue with that? Go forth and conquer, I wish you the best of luck."
            "She hugs you, pressing her warm loose breasts against your chest."
            girl "You're the best principal ever!"
            
            $ morale +=1
            $ behavior -=1
            $ good_points +=1
                        
            return
            
            
        "You *are* just a fucktoy, slut. Those holes should be open season.":
            scene bg scorp_office7_2 with flash
            "You pull the bandaids off her nipples. Then you peel away the one covering her pussy, slipping a finger in her soaking wet hole once you've done so."
            pov "Get out of here before I spank some sense into you."
            "The girl's eyes widen. She backs away - your finger leaves her with a *schlup* - and then runs out, her thighs wet with pussy juice and her bare ass jiggling pleasantly."

            $ inhibition -=1
            $ deviance +=1
            $ behavior +=1
            $ morale -=1
            
            return
    
label scorp_office8:

    scene bg scorp_office with fade

    "On your way to your office, you hear a muffled sound coming from the nearby men's bathroom."

    scene bg scorp_office8_1 with fade

    "Looking inside one of the stalls, you find a beautiful female student, completely naked and trussed up like a turkey!"
    "She starts squirming, knowing someone's there, but she has no idea who. You could just leave."
    menu:
        "Leave.":
            "You leave the girl without saying a word. As you close the door, she starts squirming even harder."
            "You're sure the male students are going to have a lot of fun with her."

            $ deviance +=1
            $ morale -=1
            if renpy.random.randint(1, 3) == 1:
                $ evil_points += 1
            return

        "Free her.":
            "You remove the girl's gag and blindfold."
            scene bg scorp_office8_2 with fade
            girl "Thank you! *gasp* The boys tied me up here... Told me I was going to spend the day as the school cum bucket!"
 
            if deviance > 90:
                girl "I wouldn't have minded, really... But I'd rather choose who I fuck, you know?"
                pov "Oh really?"
                scene bg scorp_office8_3 with fade
                "You escort the naked girl back to your office, shut the door, and fuck her absolutely senseless."
                girl "OH YES! GIVE IT TO ME!"

                $ morale += 1
                if renpy.random.randint(1, 4) == 1:
                    $deviance += 5
                return

            else:
                girl "I'm glad you got me out of there! *giggle*"
                "You get the feeling that, no matter your efforts, this girl is going to end up a cum bucket sooner or later..."

                $ morale += 1
                if renpy.random.randint(1, 4) == 1:
                    $ good_points += 1
                return

label scorp_office9:
    
    scene bg scorp_office9 with fade
    "While performing for the talent show, this girl takes the opportunity to show off her true 'talent'."
    if inhibition > 20:
        "There's a shocked silence... And some scattered applause and jeering from the boys. She ends up getting detention."
        $ inhibition -=1
        return

    else:
        "Everyone applauds, especially when she makes the microphone 'disappear'."
        $ inhibition -=1
        $ morale +=1
        return

label scorp_office10:
    
    scene bg scorp_office10 with fade
    "Most of the female teachers are following the nude uniform policy. Watching them play table tennis in the teachers' lounge is hypnotic."
    return

label scorp_office11:
    
    scene bg scorp_office11 with fade
    girl "Principal! I want to speak to you!"
    "You stare at the girl who just entered your office - she's practically nude! This is way beyond what even the sexy uniform policy allows."
    girl "As you can see, [povTitle] [povFirstName], I was forced to make some... adjustments to the uniform."
    girl "I know some of the other girls are prudes, but *I* am proud of my body! And I want to show all of it off!"
    "She twirls around for you. Her tits, ass and pussy are all completely exposed, and she loves it. She wiggles her naked ass at you."
    girl "The sexy uniforms don't go far enough. You should implement some kind of a nude policy! Think about it!"
    "Before you can say a word, she bounces out of the room."
    $ inhibition -=1
    $ morale +=1
    return

label scorp_office12:
    
    scene bg scorp_office12 with fade
    "The nude uniform policy means the girls don't have to spend ages getting ready each morning!"
    pov "Punctuality is a virtue!"
    $ behavior +=1    
    return
    
label scorp_office13:
    
    scene bg scorp_office13_1 with fade
    "One of the school's star students has been asked to give a speech for the day's assembly. She looks nervous."
    "Star student" "I was told to give... a presentation... on the importance of keeping your pussy clean and lubricated..."
    "She sighs, and glances at you. Then she takes a deep breath, and carries on."
    "Star student" "But I'm not going to. I think it's - it's disgusting what this school has become!"
    "Star student" "My presentation today is going to be on the importance of modesty, and how you should all be ashamed of yourselves!"
    "Star student" "Especially the principal!"
    menu:
        "Assert your authority.":
            if deviance <85:
                "You try to say something but the nervous girl just shouts over you."
                "Star student" "I'm not finished!"
                "She won't take no for an answer, and keeps on trying to lecture even as you drag her from the stage."
                "Star student" "I will not be silenced! Wake up, sheeple! Regain your dignity!"
                "God, what a nightmare. You can tell your attempt to silence her has only made people pay more attention to her message."
                $ morale -=1
                $ deviance -=1
                $ inhibition +=1
                return

            else:
                scene bg scorp_office13_2 with fade    
                "You move directly behind the girl. Firm action needs to be taken. She looks back at you, nervously."
                "Star student" "Well, I, uh, I wanted to start by talking about, um, dignity..."
                "You lean forward and whisper in her ear."
                pov "You don't understand the power that I have here, bitch."
                "Star student" "Eek! Um, I should also mention uh, feminism, and Christian family values..."
                "Slowly, deliberately, you pull down her skirt and panties. Her luscious ass is visible to you, but hidden from the crowd by the podium."
                "Star student" "[povTitle] [povLastName]! What are you doing?"
                scene bg scorp_office13_3 with doubleflash
                "Without replying, you grab her arms to stop her escaping, and then ram your dick into her pussy."
                "Star student" "UNNNGH! AAAH!"
                "You pump your cock in and out of her, feeling her tight lips moisten around your shaft."
                pov "What's the matter? Carry on with your speech, please."
                "Although your lower halves are hidden by the podium, from the way you're both moving, the entire audience know what's happening! They whoop and cheer!"
                pov "I said carry on - *squish* - and tell me - *squelch* - all about dignity."
                "Star student" "Uhhh uhhh you're so big... Oh OH AHHHHH!"
                pov "It seems our star pupil here is having trouble remembering what to say! You, you! Come up here and help me calm her down!"
                scene bg scorp_office13_4 with doubleflash
                "They don't have to be told twice. Two strapping lads strip down and join you in taming the feisty slut, who is moaning uncontrollably."
                "In their haste, they knock the podium away, revealing her hungry, dripping pussy to the entire audience, with your dick slamming in and out of it."
                with vpunch
                pov "Give! Your! Speech!"
                "Star student" "Ahhh... Ahhhh... Yes, [povTitle] [povLastName]... I am a feminist and I... uhhhh... I believe in modesty..."
                "A particularly powerful thrust sends her into the throes of orgasm, and her speech degenerates into moans again."
                pov "You're not getting away with it that easily. I'm going to keep fucking you until you give the entire speech."
                "Star student" "UUUUHHHH YESSSS SSSIRR! MODESTY IS UNNNH A VIRTUE... Yes, yes, yessssss fuck me THIS SCHOOL HAS LOST ITS unh unh WAY AAAAHHH!"
                "You keep fucking her for what seems like hours, until finally, her legs quivering from the multiple orgasms you gave her, she reaches the end of her speech."
                "Star student" "And IN CONCLUSIOOOON, I think we NEED TO {b}FUCK{/b}, I mean, need to FIND OUR DIGNITY AGAIN! AAAAH!"
                scene bg scorp_office13_5 with doubleflash
                "Star student" "COVER ME IN CUM! AAAH FUCK, I AM SUCH A DIRTY WHORE! I AM SUCH A DIRTY SLUT WHO GOT FUCKED IN FRONT OF THE WHOLE SCHOOL!"
                "You finally let her go. She whimpers with disappointment and sinks to her knees."
                pov "And don't you forget it."
                "The crowd erupts in ecstatic cheering."
                $ deviance +=1
                $ morale +=1
                $ inhibition -=1
                if renpy.random.randint(1, 3) == 1:
                    $ deviance += 5
                return

        "Let her continue.":
            if morale >75:
                pov "So what do you have to say for yourself?"
                "Star student" "Well, I wanted to start by talking about a little thing called dignity..."
                "She drones on and on for what seems like hours. You can tell the audience are getting bored."
                "Star student" "Blah blah, feminism, blah blah, modesty, blah blah, Christian family values..."
                girl "This is boring! Get off the stage!"
                guy "We all love this school! It's amazing!"
                "Other girl" "You're just a frigid bitch who needs some cock!"
                "Other guy" "Yeah, use that mouth for sucking, not talking, slut!"
                "Star student" "I - I - You have to listen -"
                "She's soon drowned out in the boos and jeers of the crowd, and slinks away. But you can tell she's not going to stop here..."
                $ deviance -=1
                return

            else:
                pov "So what do you have to say for yourself?"
                "Star student" "Well, I wanted to start by talking about a little thing called dignity..."
                "She drones on and on for what seems like hours. You can tell the audience are getting bored."
                "Star student" "Blah blah, feminism, blah blah, modesty, blah blah, Christian family values..."
                "Much to your dismay, you see a few people in the crowd nodding thoughtfully."
                "A few guys boo and jeer, but the girls are respectfully silent."
                "When the girl finally finishes her speech and leaves the stage, you can tell many have been swayed."
                pov "A good, but misguided, speech. Fortunately, most of us have left such regressive ideas behind. Everyone, go to class."
                "Maybe if your students were happier, they wouldn't have listened to the loudmouth on stage..."
                $ deviance -=2
                $ inhibition +=2
                $ morale -=2
                return

label scorp_office14:

    scene bg scorp_office14_1 with fade
    
    "A girl has been sent to your office for flashing her huge tits in the schoolyard for everyone to see."
    pov "Why did you do such a thing?"
    girl "I don't know! A boy dared me... He told me they were too good to keep to myself, and I should share them with the world.."
    menu:
        "Let her off the hook.":
            pov "Well, he was right. You've got some wonderful tits, and shouldn't be ashamed of them."
            girl "*giggle* Should you be saying that, [povTitle] [povLastName]?"
            pov "Probably not, but I'm an honest man. You should listen to that boy - he sounds like he knows a thing or two!"
            girl "Does this mean I'm not going to be punished?"
            pov "You're free to go. Go and share those spectacular fun-bags with the world, okay?"
            girl "*giggle* You're so funny! I promise I will!"
            $ inhibition -=1
            $ morale +=1
            return

        "Punish her.":
            pov "This is a very serious matter, and I'm going to have to treat it with the seriousness it deserves."
            girl "Awwww..."
            pov "Take off your skirt and panties, and bend over my knee."
            girl "Wait, what?"
            pov "NOW!"
            scene bg scorp_office14_2 with doubleflash
            girl "Are you going to... spank me?"
            pov "Yes. I think you need some good old-fashioned discipline."
            "Her ass is almost as good as her tits. You take a moment to squeeze one cheek, and find it pleasantly squishy."
            girl "Ohhhh... What are you..."
            "As she speaks, you lift your hand and begin to spank. Her ass wobbles beautifully with each hard smack."
            scene bg scorp_office14_3 with doubleflash
            with vpunch
            "*spank*{w=1.0}{nw}"
            girl "Aaaaw!"
            with vpunch
            "*spank*{w=1.0}{nw}"
            girl "Aaaah!"
            "Soon, her ass is bright red, but her pussy is so wet it drips juice all down your pant leg."
            pov "You're enjoying this, aren't you?"
            girl "*sob* Yes... *sob* No... I don't know... *sob* Let me go..."
            pov "Let me give you one more for luck."
            with vpunch
            "*spank*{w=1.0}{nw}"
            "The girl stands up, rubbing her ass cheeks ruefully, and goes to pick up her skirt and panties."
            pov "No. You're going to stay bottomless for the rest of the day, so everyone can see from your big red butt what happens to flashers."
            girl "*gasp!* But... Everyone will see my pussy!"
            pov "They've all seen your breasts already, they'd have seen the rest of you sooner or later."
            pov "If a teacher asks why you're naked, show them my hand-print on your ass and explain what happened. Now get out of my office."
            "You watch her stumble half-naked away, dripping juices down her thighs, and allow yourself a small smile."
            $ inhibition -=1
            $ deviance +=1
            return

label scorp_office15:
    
    scene bg scorp_office15 with fade
    "There's something beautiful about the despoiled appearance of a girl after you've finished with them."
    pov "Thank you for attending your weekly assessment session, Susie."
    "She crawls out on her hands and knees."
    return

label scorp_office16:
    
    scene bg scorp_office16 with fade
    "Parent-teacher meetings these days are usually a tense affair, but sometimes you get to meet a father who understands."
    pov "It was very nice of you to come in to see me."
    "Father" "Oh, it was no problem. It's an honour to finally be able to thank you for the good work you've done with my daughter."
    pov "Well, the reason I called you in today is relating to that. Your daughter needs to work on her gag reflex. If I may demonstrate..."
    girl "*gurgle*...*glub*...*cough*"
    return
    
label scorp_office17:
    
    $ r=renpy.random.randint(1, 2)
    image bg scorp_office17 = ConditionSwitch("r==1","mods/Scorp1/Office/scorp_office17_1.jpg","r==2","mods/Scorp1/Office/scorp_office17_2.jpg")

    scene bg scorp_office17 with fade
    "Since the nude uniform policy was implemented, girls' exposed assholes present very tempting targets. There's been a craze going round where boys ram a finger or two up there, without warning, for fun."
    "Apparently, they keep track of the number of girls they've 'surprised' like this. The top scorer at the moment has an impressive 49-asshole record."
    return
    
label scorp_office18:
    
    scene bg scorp_office18 with fade
    "The train to school today is packed with your students. Such bright young things!"
    return
    
label scorp_office19:
    
    #Panning up and down
    scene bg scorp_office19:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_office19")    
    show screen scorp_screen
    
    "On the train to work, you notice a student who seems to have forgotten something important."
    pov "What a scatter-brain!"
    $ inhibition -=1
    hide screen scorp_screen
    return
    
label scorp_office20:
    
    scene bg scorp_office20 with fade
    "You notice two girls outside the door to your office, kneeling ass-to-ass, a buzzing vibrator in both their pussies."
    pov "Nice! Any reason you're doing this outside my office?"
    "Girl 1" "Nnnngh, a teacher made us do this as punishment... he said we had to keep the vibrator between us for two hours..."
    "Girl 2" "And if it falls out... We get ass-fucked by the entire class... Ohhh..."
    "You notice that their cunts are soaking, and the vibrator is almost entirely slipping out of them."
    pov "Good to see our staff are enforcing discipline."
    $ behavior +=1
    return