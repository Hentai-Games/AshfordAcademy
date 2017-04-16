init:
    $ dormitory22_level = 0
    $ event("dormitory_introduction", "act == 'dormitory'", event.once(), event.only(), priority=20)
    if persistent.mod_disable_original_events == False:
        $ event("dormitory1", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory2", "act == 'dormitory' and academics > 50", event.choose_one('dormitory'))
        $ event("dormitory3", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'))
        $ event("dormitory4", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'))
        $ event("dormitory5", "act == 'dormitory' and inhibition > 90", event.choose_one('dormitory'))
        $ event("dormitory6", "act == 'dormitory' and deviance > 0", event.choose_one('dormitory'))
        $ event("dormitory7", "act == 'dormitory' and inhibition != 100", event.choose_one('dormitory'))
        $ event("dormitory8", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory9", "act == 'dormitory' and new_game_plus", event.choose_one('dormitory'))
        $ event("dormitory10", "act == 'dormitory' and inhibition < 100 and inhibition > 75", event.choose_one('dormitory'))
        $ event("dormitory11", "act == 'dormitory' and inhibition < 100 and inhibition > 75", event.choose_one('dormitory'))
        $ event("dormitory12", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory13", "act == 'dormitory' and deviance > 5 and inhibition < 100", event.choose_one('dormitory'))
        $ event("dormitory14", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory15", "act == 'dormitory' and academics < 30", event.choose_one('dormitory'))
        $ event("dormitory16", "act == 'dormitory' and inhibition < 90", event.choose_one('dormitory'))
        $ event("dormitory17", "act == 'dormitory' and inhibition > 85", event.choose_one('dormitory'))
        $ event("dormitory18", "act == 'dormitory' and inhibition > 50 and inhibition < 75", event.choose_one('dormitory'))
        $ event("dormitory19", "act == 'dormitory' and inhibition > 75 and deviance < 5", event.choose_one('dormitory'))
        $ event("dormitory20", "act == 'dormitory' and inhibition > 50 and inhibition < 75", event.choose_one('dormitory'))
        $ event("dormitory21", "act == 'dormitory' and morale < 40 and inhibition < 95", event.choose_one('dormitory'))
        $ event("dormitory22", "act == 'dormitory'", event.choose_one('dormitory'))
        #$ event("dormitory23", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory24", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory25", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory26", "act == 'dormitory' and inhibition < 95 and deviance > 5", event.choose_one('dormitory'))
        $ event("dormitory27", "act == 'dormitory'", event.choose_one('dormitory'))
        $ event("dormitory28", "act == 'dormitory' and academics > 40", event.choose_one('dormitory'))
        $ event("dormitory29", "act == 'dormitory' and academics > 75 and deviance > 50", event.choose_one('dormitory'))
        $ event("dormitory30", "act == 'dormitory' and inhibition < 40 and deviance > 40", event.choose_one('dormitory'))
        $ event("dormitory31", "act == 'dormitory' and inhibition < 90 and behavior < 25", event.choose_one('dormitory'))
        $ event("dormitory32", "act == 'dormitory' and inhibition < 60 and morale > 75", event.choose_one('dormitory'))


label dormitory_introduction:
    scene school_grounds2 with fade
    pov "Today is a special day for me and the rest of the staff here at Ashford. From now on, we can finally offer our students the opportunity to live near the heart of study."
    pov "It gives me great pleasure to introduce a person who is the embodiment of our Ashford spirit:"
    menu:
        "Susan Marina":
            show susan_marina normal at center
            susan_marina "Thank you [povTitle] [povLastName]. \nAs I stand here before you all, I remember my own years as a student. Though many changes has come to pass, I am really proud to be able to tell you this: Ashford is still a front runner in modern education."
            susan_marina "You students hold our banner high, you make us proud and you make us want to work even harder to assist you in becoming the pride of our nation. \nThank you all, I hope that our new dormitory will be another solid reason for future students to choose Ashford as their catapult into the wonderful world of knowledge."

        "Jack Drake" if new_game_plus == True and povGender != 'female':
            show jack_drake smile at center
            jack_drake "Whoaa, whazup kids?! This is gonna be so sweet, I mean - now you get the chance to actually sleep at school! And it's ok! \nI remember when I studied here, well - I didn't exactly study, and not here but that's not important right now. What's important is that we have each other, and that we know how to dance! As long as you dance, they can't take your shoes, right?"
            "students" "Uh, right..."
            jack_drake "Yeeeeehaaaaw!"
            pov "Eh, Jack..."
            jack_drake "I'm so happy right now, I only wish I could show you even more gratitude for showing up to celebrate me!"
            pov "Wait, no Jack, It's..."
            jack_drake "I'm gonna Jack-o-lantern you all!"
            "Student" "That sounds... weird..."
            jack_drake "Right in the schnaaauuuz!"
            pov "Jack!"
            jack_drake "Achtung!"
            pov "Oh, for the love of..!"
            "Students" "Run!"
            jack_drake "We're gonna drop it like it's cold!"

        "Jack Drake" if new_game_plus == True and povGender == "female":
            show jack_drake smile at center
            jack_drake "As [povTitle] [povLastName] once said to me \"Jack, We're just two lost souls swimming in a fish bowl.\"."
            "I am quite sure I {i}never{/i} said anything like that."
            jack_drake "... and in this great bowl we can now all be fishes swimming trough our daily life. Our bowl is called Ashford Academy and all of you mermaids can swim with me."
            jack_drake "Remember time can bring you down, time can bend your knees, but here at Ashford time will never stand still.\nWe are in this together and together we will create a future where you my young padawans will be kings and queens."
            jack_drake "And in closing, I would love to see you do all the great things that I will never do.\nThank you."
    return


label dormitory1:
    if behavior < 45:
        scene dormitory1-1 with fade
        "A new student is moving into the dormitory, I hope she will get accustomed quickly."
    else:
        scene dormitory1-2 with fade
        "When a student moves into the dormitory you can be sure that a helping hand and a new friend is close by."
        $ morale += 1
    $ population += 1
    return


label dormitory2:
    scene dormitory2 with fade
    girl "Umm, hello?"
    pov "Hello there, is everything okay?"
    if inhibition > 90:
        girl "Yeah [povTitle] [povLastName], but would you please knock before entering next time?"
        pov "Ah, yes, yes of course."
    else:
        girl "Yeah [povTitle] [povLastName], you just surprised me"
        pov "Oh, sorry about that."
    return


label dormitory3:
    scene dormitory3 with fade
    girl "Ah!"
    pov "Oh, sorry about that!"
    $ morale -= 1
    return


label dormitory4:
    if renpy.random.randint(1,2) == 1:
        scene dormitory4-1 with fade
    else:
        scene dormitory4-2 with fade
    if renpy.random.randint(1,2) == 1:
        girl "Oh!"
        pov "I'm terribly sorry."
        girl "I-it's ok..."
        "You quickly make an exit."
    else:
        girl "Eek!"
        pov "So sorry!"
    $ morale -= 1
    return


label dormitory5:
    scene dormitory5 with fade
    "Looks like some of the students are ready to bunk."
    pov "I'm sorry, I didn't realize..."
    "sleepy girl" "M-[povTitle] [povName]..."
    pov "Bye!"
    return


label dormitory6:
    scene dormitory6-1 with fade
    if deviance < renpy.random.randint(1,10) and inhibition > (85 + renpy.random.randint(1,10) ):
        if deviance < renpy.random.randint(1,10):
            if renpy.random.randint(1,2) == 1:
                "You walk into the dormitory and see a girl reading in bed."
                scene dormitory6-7
                girl "W-hoa..."
                scene dormitory6-8
                girl "Oh, [povTitle] [povLastName], I didn't hear you come in!"
                pov "Just passing through."
                "Hmm, I wonder what she was reading?"
                $ inhibition -= 1
            else:
                "You walk into the dormitory and see a girl reading in bed."
                scene dormitory6-7
                girl "W-hoa..."
                scene dormitory6-8
                girl "Oh, [povTitle] [povLastName], I didn't hear you come in!"
                pov "Just passing through."
                "Hmm, I wonder what she was reading?"
        else:
            "It's nice to relax a bit after school!"
            scene dormitory6-2
            girl "Hey!"
            pov "On my way."
            $ inhibition -= 1
    else:
        "Hey, it's that girl again."
        scene dormitory6-7
        girl "..."
        scene dormitory6-2
        "She's so into the magazine, she doesn't even know you're there!"
        girl "Mmm..."
        pov "Geez, she's really got a sweet little body..."
        scene dormitory6-3
        girl "Oh, that's it..."
        "She still doesn't now she's got a spectator. How is it possible?"
        scene dormitory6-4
        girl "Aaah!"
        pov "Oh Lord!"
        scene dormitory6-5
        girl "..."
        pov "Ah, I didn't... I mean..."
        girl "W-what!"
        "You turn around and get the hell outta there!"
        $ deviance += 1
        $ morale -= 1
    return


label dormitory7:
    scene dormitory7-1 with fade
    if inhibition < 85 and deviance > 10:
        girl "Gee [povTitle] [povLastName], you seem to have grown a likeness to the dormitory."
        pov "But of course, it was build thanks to me after all."
        scene dormitory7-2
        girl "That's right, you must be really proud!"
        pov "I take it you like the rooms?"
        girl "Oh yes, very much."
        pov "You seem to have a little more experience than your fellow students."
        girl "Ya think?"
        menu:
            "Sure, and really well developed too.":
                scene dormitory7-2
                girl "Oh hush!"
                pov "I'm dead serious, you're more of a woman than any of the other girls I've seen so far."
                scene dormitory7-3
                girl "I-I wish I could believe you."
                pov "Trust me, you're simply beautiful."
                girl "T-thank you, I'm just not used to..."
                pov "I never say stuff I don't mean. You're a true beauty, and I bet all the boys glance at your sexy curves."
                scene dormitory7-4
                girl "You're so sweet..."
                pov "And you're so hot."
                girl "Oh, this is so strange... but it feels so sexy!"
                pov "I'm gonna go now, but I'd really love to have a glimpse of that sweet body of yours first."
                girl "I-I'm not sure..."
                menu:
                    "It would surely make me dream about you, not only day dreaming that is.":
                        scene dormitory7-3
                        girl "I-I think you'd better go before someone walks in on us."
                        if new_game_plus == True:
                            "What a fucking waste of sweet talk..."

                    "I wouldn't want you to feel uncomfortable, I just... your eyes are so beautiful...":
                        girl "Mhm, you're really sexy."
                        pov "God, you make me so hard."
                        girl "*gasp*"
                        scene dormitory7-5
                        "Sweet maker... they're perfect!"
                        girl "B-but don't tell anybody about this!"
                        pov "I would never."
                        "This day... Think I'll mark it in my calendar."

            "I'm serious! I know experience when I see it.":
                scene dormitory7-3
                girl "I-I'm not that kind of girl. I don't date a lot of boys."
                pov "You misunderstood me, I..."
                girl "It's getting late and you really shouldn't be here."
                pov "I'm truly sorry if I offended you in some way."
                girl "..."
                "Just great..."
    else:
        if renpy.random.randint(1,2) == 1:
            girl "It's nighty night-time!"
            pov "Sweet dreams."
        else:
            girl "Oh, it's time to go to bed!"
            pov "Already?"
            scene dormitory7-2
            girl "Mhm, it's important to get proper rest."
            pov "Good girl."
    return


label dormitory8:
    if renpy.random.randint(1,2) == 1 and new_game_plus == True:
        scene dormitory8-3 with fade
        pov "Hello girls!"
        girl1 "*giggle*"
        girl2 "*sigh*"
        pov "Oh, I won't bother you. I was just wandering around, thinking about the unscheduled test you're going to have tomorrow... ah shucks! Did I say that out loud?"
        scene dormitory8-4
        girl1 "W-what?"
        girl2 "T-test?"
        pov "It was supposed to be a surprise. Just forget I said anything, ok?"
        girls "..."
    else:
        scene dormitory8-1 with fade
        pov "Good evening girls, getting ready for bed already?"
        girl1 "Well, it has been a long day..."
        pov "And you've earned some rest!"
        scene dormitory8-2
        girl1 "*giggle*"
        girl2 "..."
    return


label dormitory9:
    scene dormitory9-1 with fade
    "girlie" "[povTitle] [povName], I'm so glad to see you!"
    pov "Ok? Is there something wrong?"
    "girlie" "Well, it's so awfully dark and..."
    pov "Yes, it's a pitch black in here."
    "girlie" "[povTitle] [povName]..."
    "girlie" "..."
    "girlie" "Is there a Boogeyman?"
    pov "Oy! That was unexpected."
    "girlie" "What?"
    menu:
        "Oh, nevermind. Dry those tears sweetie, there's nothing to be afraid of here.":
            scene dormitory9-2
            "Girlie" "Are you sure?"
            pov "I can assure you that no Boogeyman will ever find his way to Ashford while I'm principal."
            "girlie" "Really?"
            pov "Really."
            "girlie" "Pinkie promise?"
            pov "Eh, yeah, pinkie... promise..."
            "This seems to calm her somewhat. As you leave, you start to wonder if there actually is such a thing as a Boogeyman."
            pov "One weird evening, coming up."
            $ morale += 1

        "Well, scientists have never found any evidence pointing in that direction.":
            "Girlie" "But my friend said that he comes at night when you least expect it!"
            pov "In this case, I'd put my money on the scientists."
            "Girlie" "But can you trust the scientists?"
            pov "See THAT'S a different story."
            "Girlie" "Wha..?"
            pov "You see, scientists usually work in the direction of the money."
            scene dormitory9-2
            "Girlie" "What does that mean?"
            pov "It means that if there are strong, monetary forces at large, some scientists tend to let their work adjust to who's paying the bill."
            "Girlie" "So... If the Boogeyman had more money than the... Eh..."
            pov "Monetary forces."
            "Girlie" "Monetary forces, right. If so, the scientists would listen to HIM?"
            pov "Well, in theory, I guess you could say that."
            "Girlie" "So what if he EXISTS, and just pay the scientists so that they will say he DOESN'T?"
            pov "I guess we'll never know for sure, unless..."
            "Girlie" "Unless?"
            pov "Haha, unless you don't wake up in the morning!"
            scene dormitory9-3
            "girlie" "Oh!"
            pov "Well, I'll be on my way now. Don't let the bed bugs bite. Or the Boogeyman for that matter, bwahahahaha!"
            scene dormitory9-1
            "Girlie" "I don't want to..."
            "You walk away with a smile on your face. Your students are so imaginative and open minded!"
            "*singing* Hush now, hush – here comes the Boogeyman!"
            $ morale -= 1
    return


label dormitory10:
    scene dormitory10-1 with fade
    "You stumble in on a girl who is ether examining her underwear or her body."
    menu:
        "Leave as quietly as possible.":
            "You realize that there is a thin line between a students trust and her disliking."

        "Just a few more seconds...":
            "It looks like she's measuring or comparing herself..."
            girl "He said I was pretty... But I KNOW that Yuki's got a thing for him."
            pov "Oh boy..."
            scene dormitory10-2
            girl "I just wish I had a better body..."
            pov "This is ridiculous!"
            menu:
                "Walk away before it's to late!":
                    "As you leave, you think to yourself about how fragile it can be to be young."

                "Only a couple of seconds more...":
                    girl "Perhaps he's not into me at all. Are my breasts to small?"
                    pov "I better bite my tongue."
                    girl "Am I starting to get fat?"
                    pov "Are you serious?"
                    scene dormitory10-3
                    girl "I'm really nothing special at all..."
                    pov "This is to much."
                    "You leave, convinced that someone will talk some sense into her and tell her that she's beautiful."
                    pov "To be young..."
    return


label dormitory11:
    scene dormitory11-1 with fade
    "In their spare time, some of the students express themselves with rather spectacular outfits."
    scene dormitory11-2
    girl "Hey, don't sneak up like that!"
    pov "My bad, I'll just go now."
    $ morale += 1
    return


label dormitory12:
    if renpy.random.randint(1,3) == 1:
        scene dormitory12-1 with fade
        "It's a good feeling when school's done and you can take some time to just relax."
    else:
        if renpy.random.randint(1,2) == 1:
            scene dormitory12-2 with fade
            "Sometimes you wish that the lessons would never end."
        else:
            scene dormitory12-3 with fade
            "You almost run into a wide eyed girl clutching her bag real tight."
            scene dormitory12-4
            girl "Oh!"
            if evil_points > 0:
                pov "Hey, stop ogling the floor when moving, will you?"
                girl "Yikes!"
                pov "*grumble grumble*"
                $ morale -= 1
            else:
                pov "Whoopsie daisey!"
    return


label dormitory13:
    $ randImg = renpy.random.choice(["a", "b"])
    $ renpy.show("dormitory13_1"+randImg)
    with fade
    "glasses" "Hey Uki, check out my..."
    $ renpy.show("dormitory13_2"+randImg)
    "glasses" "Oh! You're not Uki!"
    menu:
        "No I am not.":
            pov "Haha, I'm afraid not!"
            "glasses" "..."
            "She doesn't seem to respond that well to your disarming sense of humor."
            $ morale -= 1

        "Yes I am!":
            pov "Actually, my full name is [povFirstName] Uki [povLastName]! Isn't that weird?"
            "glasses" "That IS weird!"
            $ renpy.show("dormitory13_1"+randImg)
            "You laugh it off and then you leave."

        "Disappointed?" if evil_points > 0:
            pov "Sorry to make you disappointed, but I gotta tell you that I'm not."
            "glasses" "R-really? I-I mean thanks!"
            "This will make dreaming a whole lot sweeter tonight!"
    return


label dormitory14:
    scene dormitory14 with fade
    "It feels so good retiring to the dorm, filling your head with fresh air and positive thinking!"
    return


label dormitory15:
    scene dormitory15-1 with fade
    "pink" "Then she said that she found my speech really interesting and that It certainly didn't pass unnoticed by the audience!"
    "blue" "Good for you!"
    "pink" "Yeah! She said that the only time she's ever heard something like that was when she watched these old retrospective movies with her grandfather."
    "blue" "Must be really cool movies."
    "pink" "I guess so! Her grandfather is from Germany and apparently fought in some big war."
    "blue" "That makes it even more impressive, I mean, he must have heard a lot of speeches."
    scene dormitory15-2 with fade
    "pink" "Wait a minute..."
    "blue" "And so sweet of her to draw that picture of you holding a speech in front of that crowd of people!"
    "pink" "Yeah... but she spelled my name wrong."
    "blue" "She did?"
    "pink" "My family name is Hiller, you know."
    "blue" "What did she write?"
    "pink" "I can't remember..."
    scene dormitory15-1 with fade
    "pink" "But I put it up in my locker!"
    $ academics -= 1
    return


label dormitory16:
    scene dormitory16 with fade
    "After a hard days work, a cuddle with someone you care for refills the energy."
    return


label dormitory17:
    scene dormitory17 with fade
    girl "Umm... What are you doing in here?"
    pov "Oh, wrong door, bye!"
    return


label dormitory18:
    scene dormitory18 with fade
    girl "Hey [povFirstName]!"
    pov "Hello there!"
    girl "Any particular reason I get a visit?"
    pov "Oh no, I just saw a open door and..."
    girl "Oh, silly me, would you mind closing it on your way out?"
    pov "No problem."
    return


label dormitory19:
    if renpy.random.randint(1,2) == 1:
        scene dormitory19-1 with fade
        girl "Hello~ [povLastName]!"
        pov "Hello there!"
    else:
        scene dormitory19-2 with fade
        girl "AHHH!!!"
        "Good view, bad timing."
        $ inhibition += 1
    return


label dormitory20:
    scene dormitory20 with fade
    girl "Ah! *blush* What are you doing here?"
    pov "Sorry miss, wrong door obviously!"
    $ inhibition -= 1
    return


label dormitory21:
    scene dormitory21 with fade
    "Those sad eyes, sometimes you just need a hug..."
    return


label dormitory22:
    if dormitory22_level == 0:
        scene dormitory22-1 with fade
        girl "Hey there [povTitle] [povLastName], what are you up to?"
        if inhibition > 90:
            pov "Not much, just making sure everyone is safe and sound!"
            girl "*giggle* That's our principal!"
        else:
            menu:
                "It's cute girl inspection day!":
                    scene dormitory22-2
                    girl "Oh... So you think I'm cute [povLastName]?"
                    pov "I think so very much."
                    girl "*giggle* You're such a sweet talker!"
                    if deviance > 0:
                        pov "Can I see just how cute you are?"
                        scene dormitory22-3
                        girl "Umm... Something like this..?"
                        if deviance > 5 or inhibition < 85:
                            menu:
                                "Good girl":
                                    girl "*giggle* You want to {i}inspect{/i} me some more?"
                                    pov "I sure do miss, I sure do."
                                    scene dormitory22-5
                                    girl "So... {w}Do you like what you see?"
                                    pov "I {i}love{/i} what I see, you have a great body."
                                    girl "*giggle* Thanks [povLastName]!"

                                    # TODO: Finish event!
                                    #$ dormitory22_level = 1

                                "What's under that skirt of yours?":
                                    scene dormitory22-4
                                    girl "Is this {i}really{/i} cute girl inspection day?"
                                    pov "Yeah... Yeah, trust me."

                "Just making sure everyone is safe and sound!":
                    girl "*giggle* That's our principal!"

            if dormitory22_level == 1: #TODO: Fix me!
                scene dormitory22-1 with fade
                girl "Hey [povTitle] [povLastName], is it inspection day today?"
                menu:
                    "Not today":
                        if inhibition < 90 or deviance > 5:
                            girl "Aww, I was looking forward to it..."
                        else:
                            girl "Okay, you have a good evening then!"

                    "I want to inspect all of you" if povGender != "female":
                        if inhibition < 90 or deviance > 10:
                            scene dormitory22-5
                            girl "Like this?"
                            pov "That's definitely a good start, but I was considering something a little more in depth."
                            girl "...In depth..?"
                            pov "You don't mind do you?"
                            girl "..."
                            scene black
                            pov "Lie down... Good girl. Now spread your legs and don't worry about a thing."
                            scene dormitory22-6
                            girl "Umm... *giggle* Like this?"
                            pov "Very good, now it's time to remove those cute panties of yours."
                            girl "..."
                            girl "Umm, please don't look at it directly [povLastName]..."
                            scene dormitory22-7
                            pov "Mhmm, your tight... I like that."
                            girl "Ah! S-s-slowly [povLastName]!"
                            girl "AH! Y-you're so big... Mhmm... S-slowly!"
                            "You slowly push deeper between her legs."
                            scene dormitory22-8
                            girl "Ah! Ahhh! *gasp* Y-you w-will break me-AH!"
                            pov "Don't worry miss."
                            "Before ending your sentence you push harder into her."
                            scene dormitory22-9
                            girl "AH! Ah! Mhmmm, I-it feels *gasp* so.... Mhmm-good!"
                            "You feel how she starts twitching and gets closer to climax."
                            girl "Oh, pl-please! Ah! AH! M-more!"
                            scene dormitory22-10
                            girl "Ahhhh! *gasp* Mhmmm... Oh [povLastName]..."
                            pov "Good girl."
                            "You pat her head and clean yourself off before leaving."
                            $ deviance += 1
                            $ dormitory22_level += 1

                        else:
                            scene dormitory22-4
                            girl "...{w} Can i go to sleep now?"
                            pov "Yeah... Sure."

                    "It's your turn to inspect me" if povGender != "Female":
                        if inhibition < 90 or deviance > 15:
                            pass
    return


label dormitory23:
    scene dormitory23 with fade
    "Sad girl is sad."
    return


label dormitory24:
    scene dormitory24 with fade
    girl "Yay! I'm saving to buy a hat!"
    pov "Put it in the piggy."
    girl "Piggy power!"
    pov "Yay!"
    return


label dormitory25:
    scene dormitory25 with fade
    girl "Umm, do you mind?"
    return


label dormitory26:
    "As you stroll the dorm you notice a slightly open door and decide to take a peek."
    scene dormitory26 with fade
    girl "Ah.... Mhmm... mm..."
    $ deviance += 1
    return


label dormitory27:
    scene dormitory27 with fade
    $ subject = random_topic('academics')
    girl "Hmm... This homework is hard. Why do I need to learn [subject] anyway..."
    return


label dormitory28:
    scene dormitory28 with fade
    if academics > 80:
        girl "... so if you work on those parts I'm sure you will win and get a FIDE rating above 2500."
    elif renpy.random.randint(1,2) == 1:
        girl "In this game don't forget to play Zwischenzug and try to test some of the tactics we discussed."
    else:
        "I'm happy to see our students playing such a timeless game based on pure logic."
    return


label dormitory29:
    scene dormitory29 with fade
    girl "I'm a good girl- Ah!\nPlease, help me-Mhmm-study...\nHarder... harder!"
    return


label dormitory30:
    "You see several students standing outside a dorm room.\nAs you get closer you hear a familiar sound...  squeals of delight."
    scene dormitory30 with fade
    "Together with the students you are granted a short but very explicit show."
    girl "Mhmm... Ah... AH!\nPlease all, ah-look at me!\nMhmm, can you see my-Mhm, wet pussy dripping...\n*gasp* Mhmm..."
    return


label dormitory31:
    if renpy.random.randint(1,2) == 1:
        "Zzzzzz..."
        scene dormitory31-1 with fade
        "Well, I guess not everyone sleeps gracefully..."
    elif renpy.random.randint(1,2) == 1:
        scene dormitory31-2 with fade
        "Not all students are picture perfect straight A's. Some are slouches playing games in their undies."
    else:
        scene dormitory31-3 with fade
        "Underage drinking on campus, passing out on the dormitory floor.\nOh well, I can look the other way."
    return


label dormitory32:
    scene dormitory32 with fade
    girl "Hello there [povTitle] [povLastName].\nFancy meeting you here, In my room."
    pov "Hrm, yes.\nDid you enjoy your shower?"
    girl "Indeed.\nThe hot water running down my body.\nAnd afterwards, a glass of... milk.\nDelicious."
    return
