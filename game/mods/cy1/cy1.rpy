#Init variables
define cy_carryon = False
define cy_boyfight = False
define cy_showpanties = False
define cy_sidecoach = False
define cy_obsessive = False

#Define characters
define boy1 = Character('Boy 1', color="#0000CC")
define boy2 = Character('Boy 2', color="#00CC00")
define boy3 = Character('Boy 3', color="#CC0000")
define boys = Character('Boys', color="#CC00CC")
define mysterious_voice = Character('Mysterious Voice', color="#CCCC00")
define pure_girl = Character('Pure Girl', color="#00CCCC")
define hot_girl = Character('Hot Girl', color="#009999")
define bold_girl = Character('Bold Girl', color="#009999")
define shy_girl = Character('Shy Girl', color="#00CCCC")
define delinquent = Character('Delinquent', color="#000099")
define obsessive_girl = Character('Obsessive Girl', color="#990099")

#Declaring images
image bg cy_class1 = "mods/cy1/cy_class1.jpg"
image bg cy_class2 = "mods/cy1/cy_class2.jpg"
image bg cy_class3 = "mods/cy1/cy_class3.jpg"
image bg cy_class4_1 = "mods/cy1/cy_class4_1.png"
image bg cy_class4_2 = "mods/cy1/cy_class4_2.png"
image bg cy_class4_3 = "mods/cy1/cy_class4_3.png"
image bg cy_class5_1 = "mods/cy1/cy_class5_1.png"
image bg cy_class5_2 = "mods/cy1/cy_class5_2.png"
image bg cy_class6 = "mods/cy1/cy_class6.png"
image bg cy_class7_1 = "mods/cy1/cy_class7_1.png"
image bg cy_class7_2 = "mods/cy1/cy_class7_2.png"
image bg cy_class8 = "mods/cy1/cy_class8.png"
image bg cy_class9_1 = "mods/cy1/cy_class9_1.png"
image bg cy_class9_2 = "mods/cy1/cy_class9_2.png"
image bg cy_class10_1 = "mods/cy1/cy_class10_1.jpg"
image bg cy_class10_2 = "mods/cy1/cy_class10_2.jpg"
image bg cy_class11_1 = "mods/cy1/cy_class11_1.png"
image bg cy_class11_2 = "mods/cy1/cy_class11_2.png"
image bg cy_class12_1 = "mods/cy1/cy_class12_1.png"
image bg cy_class12_2 = "mods/cy1/cy_class12_2.png"
image bg cy_class13 = "mods/cy1/cy_class13.png"
image bg cy_class14_1 = "mods/cy1/cy_class14_1.png"
image bg cy_class14_2 = "mods/cy1/cy_class14_2.png"
image bg cy_class14_3 = "mods/cy1/cy_class14_3.png"

image bg cy_field1_1 = "mods/cy1/cy_field1_1.png"
image bg cy_field1_2 = "mods/cy1/cy_field1_2.png"
image bg cy_field1_3 = "mods/cy1/cy_field1_3.png"
image bg cy_field2 = "mods/cy1/cy_field2.png"
image bg cy_field3_1 = "mods/cy1/cy_field3_1.png"
image bg cy_field3_2 = "mods/cy1/cy_field3_2.png"
image bg cy_field3_3 = "mods/cy1/cy_field3_3.png"
image bg cy_field3_4 = "mods/cy1/cy_field3_4.png"
image bg cy_field3_5 = "mods/cy1/cy_field3_5.png"
image bg cy_field4 = "mods/cy1/cy_field4.jpg"
image bg cy_field5 = "mods/cy1/cy_field5.jpg"
image bg cy_field6_1 = "mods/cy1/cy_field6_1.jpg"
image bg cy_field6_2 = "mods/cy1/cy_field6_2.jpg"
image bg cy_field7 = "mods/cy1/cy_field7.jpg"

image bg cy_grounds1 = "mods/cy1/cy_grounds1.jpg"
image bg cy_grounds2_1 = "mods/cy1/cy_grounds2_1.jpg"
image bg cy_grounds2_2 = "mods/cy1/cy_grounds2_2.jpg"
image bg cy_grounds3_1 = "mods/cy1/cy_grounds3_1.jpg"
image bg cy_grounds3_2 = "mods/cy1/cy_grounds3_2.jpg"
image bg cy_grounds4 = "mods/cy1/cy_grounds4.jpg"
image bg cy_grounds5 = "mods/cy1/cy_grounds5.jpg"
image bg cy_grounds6 = "mods/cy1/cy_grounds6.png"
image bg cy_grounds7 = "mods/cy1/cy_grounds7.png"
image bg cy_grounds8 = "mods/cy1/cy_grounds8.png"
image bg cy_grounds9_1 = "mods/cy1/cy_grounds9_1.png"
image bg cy_grounds9_2 = "mods/cy1/cy_grounds9_2.png"
image bg cy_grounds9_3 = "mods/cy1/cy_grounds9_3.png"
image bg cy_grounds10 = "mods/cy1/cy_grounds10.png"
image bg cy_grounds11_1 = "mods/cy1/cy_grounds11_1.png"
image bg cy_grounds11_2 = "mods/cy1/cy_grounds11_2.png"
image bg cy_grounds12 = "mods/cy1/cy_grounds12.jpg"
image bg cy_grounds13 = "mods/cy1/cy_grounds13.png"
image bg cy_grounds14 = "mods/cy1/cy_grounds14.jpg"
image bg cy_grounds15 = "mods/cy1/cy_grounds15.jpg"
image bg cy_grounds16 = "mods/cy1/cy_grounds16.jpg"

image bg cy_gym1_1 = "mods/cy1/cy_gym1_1.png"
image bg cy_gym1_2 = "mods/cy1/cy_gym1_2.png"

image bg cy_library1 = "mods/cy1/cy_library1.png"
image bg cy_library2 = "mods/cy1/cy_library2.jpg"
image bg cy_library3 = "mods/cy1/cy_library3.jpg"
image bg cy_library4 = "mods/cy1/cy_library4.jpg"
image bg cy_library5_1 = "mods/cy1/cy_library5_1.png"
image bg cy_library5_2 = "mods/cy1/cy_library5_2.png"
image bg cy_library6 = "mods/cy1/cy_library6.png"
image bg cy_library7_1 = "mods/cy1/cy_library7_1.jpg"
image bg cy_library7_2 = "mods/cy1/cy_library7_2.jpg"
image bg cy_library7_3 = "mods/cy1/cy_library7_3.jpg"
image bg cy_library7_4 = "mods/cy1/cy_library7_4.jpg"
image bg cy_library7_5 = "mods/cy1/cy_library7_5.jpg"
image bg cy_library8_1 = "mods/cy1/cy_library8_1.jpg"
image bg cy_library8_2 = "mods/cy1/cy_library8_2.jpg"

image bg cy_office1 = "mods/cy1/cy_office1.png"
image bg cy_office2_1 = "mods/cy1/cy_office2_1.jpg"
image bg cy_office2_2 = "mods/cy1/cy_office2_2.jpg"
image bg cy_office2_3 = "mods/cy1/cy_office2_3.jpg"

image bg cy_office3_1 = "mods/cy1/cy_office3_1.jpg"
image bg cy_office3_2 = "mods/cy1/cy_office3_2.jpg"
image bg cy_office4 = "mods/cy1/cy_office4.jpg"
image bg cy_office5_1 = "mods/cy1/cy_office5_1.jpg"
image bg cy_office5_2 = "mods/cy1/cy_office5_2.jpg"
image bg cy_office5_3 = "mods/cy1/cy_office5_3.jpg"
image bg cy_office6 = "mods/cy1/cy_office6.jpg"
image bg cy_office7_1 = "mods/cy1/cy_office7_1.jpg"
image bg cy_office7_2 = "mods/cy1/cy_office7_2.jpg"
image bg cy_office8 = "mods/cy1/cy_office8.png"
image bg cy_office9 = "mods/cy1/cy_office9.png"
image bg cy_office10 = "mods/cy1/cy_office10.png"
image bg cy_office11_1 = "mods/cy1/cy_office11_1.png"
image bg cy_office11_2 = "mods/cy1/cy_office11_2.png"
image bg cy_office12_1 = "mods/cy1/cy_office12_1.png"
image bg cy_office12_2 = "mods/cy1/cy_office12_2.png"
image bg cy_office12_3 = "mods/cy1/cy_office12_3.png"
image bg cy_office12_4 = "mods/cy1/cy_office12_4.png"
image bg cy_office12_5 = "mods/cy1/cy_office12_5.png"
image bg cy_office12_6 = "mods/cy1/cy_office12_6.png"
image bg cy_office13 = "mods/cy1/cy_office13.jpg"
image bg cy_office14 = "mods/cy1/cy_office14.png"

image bg cy_pool1 = "mods/cy1/cy_pool1.png"
image bg cy_pool2 = "mods/cy1/cy_pool2.jpg"

#Setting up events and conditions
init:
    $ event("cy_class1", "act == 'class' and deviance >= 75 and inhibition <= 25", event.choose_one('class'), priority=200)
    $ event("cy_class2", "act == 'class' and deviance >= 75 and inhibition >= 75 and behavior <= 25 and behavior_rules == ('behavior_no_limit')", event.choose_one('class'), priority=200)
    $ event("cy_class3", "act == 'class' and deviance >= 90 and inhibition <= 25 and morale >= 75", event.choose_one('class'), priority=200)
    $ event("cy_class4", "act == 'class' and deviance >= 25 and inhibition <= 75", event.choose_one('class'), priority=200)
    $ event("cy_class5", "act == 'class' and deviance >= 40 and inhibition >= 75", event.choose_one('class'), priority=200)
    $ event("cy_class6", "act == 'class' and deviance >= 75 and inhibition <= 25", event.choose_one('class'), priority=200)
    $ event("cy_class7", "act == 'class' and deviance >= 40 and inhibition <= 60", event.choose_one('class'), priority=200)
    $ event("cy_class8", "act == 'class' and deviance >= 75 and inhibition <= 25", event.choose_one('class'), priority=200)
    $ event("cy_class9", "act == 'class' and inhibition >= 75 and deviance >= 40", event.choose_one('class'), priority=200)
    $ event("cy_class10", "act == 'class' and deviance >= 75 and inhibition >= 75", event.choose_one('class'), priority=200)
    $ event("cy_class11", "act == 'class'", event.choose_one('class'), priority=200)
    $ event("cy_class12", "act == 'class' and deviance >= 75 and inhibition <= 25 and behavior_rules == ('behavior_no_limit')", event.choose_one('class'), priority=200)
    $ event("cy_class13", "act == 'class' and deviance >= 75 and inhibition <= 60", event.choose_one('class'), priority=200)
    $ event("cy_class14", "act == 'class' and deviance >= 75 and inhibition <= 60", event.choose_one('class'), priority=200)

    $ event("cy_field1", "act == 'sports_field'", event.choose_one('sports_field'), priority=200)
    $ event("cy_field2", "act == 'sports_field' and athletics <= 60", event.choose_one('sports_field'), priority=200)
    $ event("cy_field3", "act == 'sports_field'", event.choose_one('sports_field'), priority=200)
    $ event("cy_field4", "act == 'sports_field' and behavior <= 25 and deviance >= 40 and athletics >= 75", event.choose_one('sports_field'), priority=200)
    $ event("cy_field5", "act == 'sports_field' and deviance >= 40 and inhibition <= 60", event.choose_one('sports_field'), priority=200)
    $ event("cy_field6", "act == 'sports_field'", event.choose_one('sports_field'), priority=200)
    $ event("cy_field7", "act == 'sports_field' and inhibition >= 75", event.choose_one('sports_field'), priority=200)

    $ event("cy_grounds1", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds2", "act == 'school_grounds' and deviance >= 75 and inhibition <= 60 and behavior <= 25", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds3", "act == 'school_grounds' and deviance >= 25 and inhibition <= 75 and uniform == ('sexy_uniform')", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds4", "act == 'school_grounds' and behavior <= 25 and deviance >= 75 and inhibition <= 25 and evil_points > 2", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds5", "act == 'school_grounds' and deviance >= 75 and inhibition <= 25 and uniform == ('sexy_uniform') and cy_showpanties == True", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds6", "act == 'school_grounds' and deviance >= 40 and inhibition <= 60", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds7", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds8", "act == 'school_grounds' and behavior <= 25", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds9", "act == 'school_grounds' and deviance >= 90 and inhibition <= 25 and behavior <= 25", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds10", "act == 'school_grounds' and deviance >= 75 and inhibition <= 25 and evil_points > 2", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds11", "act == 'school_grounds' and inhibition >= 60 and deviance <= 40", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds12", "act == 'school_grounds' and deviance >= 40 and inhibition <= 60", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds13", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds14", "act == 'school_grounds'", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds15", "act == 'school_grounds' and inhibition >= 75", event.choose_one('school_grounds'), priority=200)
    $ event("cy_grounds16", "act == 'school_grounds' and uniform == ('nude_uniform')", event.choose_one('school_grounds'), priority=200)

    $ event("cy_gym1", "act == 'gym' and deviance >= 90 and inhibition <= 25", event.choose_one('gym'), priority=200)

    $ event("cy_library1", "act == 'library'", event.choose_one('library'), priority=200)
    $ event("cy_library2", "act == 'library' and deviance >= 75 and inhibition <= 25 and good_points > 0", event.choose_one('library'), priority=200)
    $ event("cy_library3", "act == 'library' and deviance >= 40 and inhibition <= 60 and uniform == ('sexy_uniform')", event.choose_one('library'), priority=200)
    $ event("cy_library4", "act == 'library' and deviance >= 40 and inhibition <= 60 and uniform == ('sexy_uniform')", event.choose_one('library'), priority=200)
    $ event("cy_library5", "act == 'library'", event.choose_one('library'), priority=200)
    $ event("cy_library6", "act == 'library' and inhibition <= 60 and deviance >= 75", event.choose_one('library'), priority=200)
    $ event("cy_library7", "act == 'library' and deviance >= 40 and evil_points > 0", event.choose_one('library'), priority=200)
    $ event("cy_library8", "act == 'library' and deviance >= 40 and inhibition <= 60", event.choose_one('library'), priority=200)

    $ event("cy_office1", "act == 'office' and inhibition <= 60 and deviance >= 40 and uniform == ('sexy_uniform')", event.choose_one('office'), priority=200)
    $ event("cy_office2", "act == 'office' and inhibition <= 75", event.choose_one('office'), priority=200)
    $ event("cy_office3", "act == 'office' and deviance >= 75 and inhibition <= 25 and pda_rules == 'pda_bdsm'", event.choose_one('office'), priority=200)
    $ event("cy_office4", "act == 'office'", event.choose_one('office'), priority=200)
    $ event("cy_office5", "act == 'office' and academics >= 75 and deviance >= 75 and inhibition <= 25", event.choose_one('office'), priority=200)
    $ event("cy_office6", "act == 'office' and deviance >= 90 and inhibition <= 25", event.choose_one('office'), priority=200)
    $ event("cy_office7", "act == 'office' and inhibition <= 60 and deviance >= 40 and uniform == ('sexy_uniform') and cy_showpanties == False", event.choose_one('office'), priority=200)
    $ event("cy_office8", "act == 'office' and deviance >= 75 and inhibition <= 25 and morale >= 75 and behavior >= 75", event.choose_one('office'), priority=200)
    $ event("cy_office9", "act == 'office' and morale >= 40", event.choose_one('office'), priority=200)
    $ event("cy_office10", "act == 'office'", event.choose_one('office'), priority=200)
    $ event("cy_office11", "act == 'office' and inhibition <= 25 and deviance >= 40 and behavior_rules == ('behavior_no_limit')", event.choose_one('office'), priority=200)
    $ event("cy_office12", "act == 'office' and deviance >= 75 and inhibition >= 60", event.choose_one('office'), priority=200)
    $ event("cy_office13", "act == 'office' and morale >= 40", event.choose_one('office'), priority=200)
    $ event("cy_office14", "act == 'office' and deviance >= 75 and inhibition <= 25", event.choose_one('office'), priority=200)

    $ event("cy_pool1", "act == 'pool' and deviance >= 75 and inhibition <= 25", event.choose_one('pool'), priority=200)
    $ event("cy_pool2", "act == 'pool' and athletics >= 25", event.choose_one('pool'), priority=200)

#### CLASSROOM EVENTS ####

label cy_class1:
    scene bg cy_class1 with fade
    "Not every student is thrilled about all the lesbian activity in the school. This girl seems to really dislike watching her teacher masturbate, but a helpful student seems to have found some way to motivate her. When you ask, she reluctantly states that she’s thrilled to watch, and the teacher says happy to give her the lessons. They're probably lying, but won't deviate from their story. The student just grins."
    $ morale -=1
    $ inhibition -=1
    $ deviance +=1
    return

label cy_class2:
    scene bg cy_class2 with fade
    "It seems that some of the teachers are starting to give their students lessons that aren’t entirely academic."
    $ academics -=1
    $ deviance +=1
    return

label cy_class3:
    scene bg cy_grounds3 with fade
    "Even the teachers aren’t immune to sudden gangbangs these days. They don’t seem to be complaining though."
    $ inhibition -=1
    $ deviance +=1
    return

label cy_class4:
    if deviance >= 40 and inhibition <= 60:
        scene bg cy_class4_2 with fade
        "A student just confessed his love for his teacher. How sweet. She definitely likes him back."
    elif deviance >= 60 and inhibition <= 40:
        scene bg cy_class4_3 with fade
        "A student just confessed his love for his teacher. How sweet. She definitely likes him back."
    else:
        scene bg cy_class4_1 with fade
        "A student just confessed his love for his teacher. How sweet. She doesn’t look too happy about it."
    return

label cy_class5:
    scene bg cy_class5_1 with fade
    "These two are furiously making out in the middle of the class."
    menu:
        "Punish them":
            "You break them up and apply the school’s punishment."
        "Smile and move on":
            scene bg cy_class5_2 with fade
            "You wave and move on. Other students realize you don’t care if they kiss in class, and more are starting to do it."
    return

label cy_class6:
    scene bg cy_class6 with fade
    teacher "Come on boys, you’ve got to do better than that if you don’t want me to turn you into the principal for trying to rape me."
    boy1 "P-please, let us rest! I can’t cum anymore!"
    boy2 "I’m gonna die!"
    boy3 "I'm sorry! I'm so sorry!"
    teacher "Not until I’m satisfied! Go faster!"
    boys "*Sob*"
    "The teachers are starting to get a little scary."
    return
label cy_class7:
    scene bg cy_class7_1 with fade
    "Class is over but you hear some mysterious voices in a classroom that should be empty."
    mysterious_voice "Oooh, ooh, ohh..."
    "You look in the door window and see two students going at it."
    menu:
        "Allow it":
            scene bg cy_class7_2 with fade
            "They keep going for almost an hour."
        "Punish them":
            "You step in. They hurriedly move to cover themselves. You apply the school punishment."
    return

label cy_class8:
    scene bg cy_class8 with fade
    "You come across a student outside her classroom. Her breasts are exposed and she’s covered in cum. Apparently she’s been deemed the class 'titjob representative'. She’s not sure whether or not to be happy about it."
    return

label cy_class9:
    if deviance >= 40 and inhibition <= 60:
        scene bg cy_class9_1 with fade
        "You see a boy grope a girl’s breasts in the hallway. She totally flips out, and it turns into a huge scene. This is not going to be good for the school’s reputation."
        $ reputation -=1
        $ deviance +=1
    else:
        scene bg cy_class9_2 with fade
        "You see a boy grope a girl’s breasts in the hallway. She doesn’t seem thrilled, but she doesn’t stop him either."
        girl "Boys. Is that all that’s on your mind?"
        $ deviance +=1
    return

label cy_class10:
    scene bg cy_class10_1 with fade
    "You run across two students in the corner of an abandoned classroom."
    girl "Okay, fine, but I’m not actually gonna do it."
    boy "Awesome awesome awesome! Let’s practice."
    girl "Fine. Give me your hand."
    scene bg cy_class10_2 with fade
    boy "Oh man, this is so great!"
    girl "Just remember, it’s just practice, alright? I don’t know if I’m even going to give you a blowjob."
    boy "I know, I know. But this is the best! When you do, it’s gonna be awesome!"
    girl "..."
    return

label cy_class11:
    if deviance >= 75 and inhibition <= 25:
        scene bg cy_class11_2 with fade
        "You see a student hard at work in the cooking club. She seems to have added to the sexy school uniform a bit."
        girl "It improves the flavor!"
        pov "I bet it does."
    else:
        scene bg cy_class11_1 with fade
        "You see a student hard at work in the cooking club."
    return

label cy_class12:
    scene bg cy_class12_1 with fade
    teacher "Ohho, so you’re confessing to your teacher now?"
    girl "I- I love you."
    teacher "You’re so cute. Show me your love with a kiss."
    menu:
        "Stop them":
            pov "What do you think you’re doing?"
            teacher "Er-"
            pov "No, I don’t want to hear it. I’m going to keep this quiet, but I don’t want to hear about it again. Teachers shouldn’t be doing this sort of thing with students."
            girl "But-"
            pov "You don’t know better, but HE should."
            teacher "I’m sorry!"
            pov "You’d better be."
        "Let it go":
            scene bg cy_class12_2 with fade
            "She let her lips answer him. He clearly doesn’t have romance on his mind, though."
    return

label cy_class13:
    scene bg cy_class13 with fade
    teacher "And what is the capital of New Orly?"
    girl "N-Nohwai."
    "Somehow this student seems to have kept her wits about her in spite of the buzzing coming from between her legs. Keep getting those good grades, you hear?"
    return

label cy_class14:
    scene bg cy_class14_1 with fade
    pure_girl "Oh no, not you too!"
    hot_girl "I just can’t help it! I can’t get the dicks out of my head. I’m sorry! I need this so bad. Jam it in!"
    scene bg cy_class14_2 with fade
    pure_girl "Everyone in the whole school is going sex crazy. You promised you’d stay pure for marriage too, but you’re going just as crazy as everyone else!"
    hot_girl "I am your friend!  I can't believe I ever made a promise not to feel this good. I keep seeing these every day and I just couldn't take it anymore. Stop being such a prude and grab a dick. It feels soooo good. Staying a virgin is stupid."
    pure_girl "Never! I don’t break my promises like SOME people!"
    hot_girl "More for me then. Hey you, my mouth is open!"
    boy "Oh fuck yeah."
    scene bg cy_class14_3 with fade
    "I guess not everyone is thrilled that the school has gone completely sex crazy, but they’re definitely a minority now."
    return

#### SPORTS FIELD EVENTS ####

label cy_field1:
    if uniform == ('nude_uniform'):
        scene bg cy_field1_3 with fade
        "You see a student on the track team. She seems pretty comfortable with the school uniform, even when she notices your gaze."
    elif deviance >= 40 and inhibition <= 60:
        scene bg cy_field1_2 with fade
        "You see a student on the track team. She seems to have made a few modifications to her uniform. It’s probably not to help her run faster though."
    else:
        scene bg cy_field1_1 with fade
        "You see a student on the track team. She seems pretty comfortable in her gym outfit."
    return

label cy_field2:
    scene bg cy_field2 with fade
    "Sports are still hard for a lot of students. This one keeps trying to catch her breath, unaware of the view she’s giving to everyone else."
    $ inhibition -=1
    $ athletics +=1
    return

label cy_field3:
    if deviance >= 40 and inhibition <= 60 and athletics >= 40 and cy_sidecoach == False:
        scene bg cy_field3_2 with fade
        "You see some girls from the tennis club. They’re not too happy to see you, because they just lost a match with the boys team and are facing 'penalties' they were hoping no one would find out about."
        "They say they never wanted the match in the first place or the penalties, but their teacher forced them into it. The teacher says she believes it’s necessary to improve their performance. They’ve been doing terribly. She keeps rubbing her lower stomach and biting her lip as she says it though."
        menu:
            "Side with the girls":
                "The girls are thankful and events return to normal. The teacher is reprimanded."
                $ athletics -=1
                $ morale +=1
                $ deviance -=1
            "Side with the teacher":
                scene bg cy_field3_3 with fade
                "The teacher thanks you for your understanding and schedules another match for the next day with even greater penalties for the loser."
                scene bg cy_field3_4 with fade
                "The girls are starting to improve but still don't stand a chance against the boys team."
                $ athletics +=1
                $ morale -=1
                $ deviance +=1
                $ cy_sidecoach = True
    elif deviance >= 75 and inhibition <= 25 and cy_sidecoach == True:
        scene bg cy_field3_5 with fade
        "You see some girls from the tennis club. They’re happy to see you, and don’t seem to be bothered by the rather skimpy outfits they’re wearing these days."
    else:
        scene bg cy_field3_1 with fade
        "You see some girls from the tennis club. They’re happy to see you, and don’t seem to be bothered by the rather skimpy outfits they’re wearing these days."
    return

label cy_field4:
    scene bg cy_field4 with fade
    "There are bullies, but there are also those strong enough to fight them. This girl made sure they left her friends alone."
    return

label cy_field5:
    scene bg cy_field5 with fade
    "Some students are having lunch out on the sports field. They’re having a pretty good time in the fresh air."
    $ morale +=1
    return

label cy_field6:
    if deviance >= 40 and inhibition <= 60:
        scene bg cy_field6_2 with fade
        girl2 "Shame the double date with the boys didn’t work out."
        girl1 "But it’s nice that we figured out how much fun we could have with each other!"
        girl2 "Mmmm. Kiss me some more."
        girl1 "Hee!"
    else:
        "You see two students chatting in the halls between classes."
        scene bg cy_field6_1 with fade
        girl1 "He asked you out? That’s so exciting!"
        girl2 "He fell for my charms."
        girl1 "Ooh, I’m so jealous!"
        girl2 "You know, he has a friend, and he has a thing for girls with short hair..."
        girl1 "Double date! Double date! Double date!"
        girl2 "Hahaha."
        "It's good to see the students so cheery."
    return

label cy_field7:
    scene bg cy_field7 with fade
    boy "This is embarrassing!"
    girl "Oh come on, just take a nap! You were up all night studying and you don’t want to flunk your test. Isn’t this what friends are for?"
    boy "People are laughing right now!"
    girl "Stop worrying, or you won’t get any rest."
    "The boy clearly isn’t going to be getting any sleep at all."
    $ inhibition -=1
    return

#### SCHOOL GROUNDS EVENTS ####

label cy_grounds1:
    scene bg cy_grounds1 with fade
    "These two have been friends since grade school, but when people grow older they can also grow differently. She grew into a knockout but he grew into a shrimp."
    "Still, looking at the way she teases him it’s pretty clear they’ll be more than friends eventually. It’s good to see the students playing around."
    $ morale +=1
    $ inhibition -=1
    return

label cy_grounds2:
    if cy_carryon == True:
        scene bg cy_grounds2_2 with fade
        "You see the delinquent with the teacher he's claimed having sex in front of the school."
        teacher "Please, please, let me go! Don't rape me in front of everyone again!"
        delinquent "You tried to skip work. I had to go to your house and drag you out here! I told you I hate it when you make me work, you dumb fuckhole. This is your punishment. You're my woman now, and you'll do what I say!"
        teacher "I'm sorry for skipping work! I'm sorry! Please stop!"
        "You smile and wave as you walk by. The delinquent gives you a thumbs up. You can still hear her crying as you step inside."
        $ behavior -=1
        $ deviance +=1
        $ reputation -=2
        $ sex +=1
        $ inhibition -=1
        $ athletics +=1
    else:
        scene bg cy_grounds2_1 with fade
        "You walk down the hall until you hear the sounds of a struggle. Wondering if there's a fight between students you peek around the corner. You see a student molesting a teacher right in the middle of the hall."
        teacher "Stop! Stop! I'm your teacher! You shouldn't be doing this!"
        delinquent "Who cares if you're a teacher? This nice little spot between your legs. I'll take my cock just as well as any girl in class."
        teacher "We're in public! You won't get away with this!"
        delinquent "Who cares? They'll just know you're my woman now. Nobody's gonna do anything. \"
        Quite suddenly they spot you."
        teacher "pov, help! He's trying to rape me!"
        delinquent "Pfft. You can TRY to stop me, asshole. I'm way too strong for you. She's mine."
        menu:
            "Stop him":
                pov "Are you some kind of moron?"
                delinquent "What did you say?"
                "You pull out your cell phone and dial the police."
                pov "I have a violent student trying to rape a teacher. Please send a squad to the high school."
                "You calmly turn off the phone."
                "He stops, shocked. The teacher takes advantage of the confusion to run away from him."
                pov "I'm not going to fight you because you're not worth my time. If I were you I'd start running. The police will be here any second. You might think you're strong enough to fight me - which I doubt - but I doubt you'll fight off a squad of men with guns. Get out of my school."
                "He takes off running. The teacher thanks you over and over. The police later catch him and he goes to jail."
                "If you don't get these behavior problems under control it's going to be very bad for the school. Even though this was successfully resolved it's definitely going to hurt your reputation."
                $ behavior +=2
                $ morale +=2
                $ reputation -=1
                $ good_points +=1
            "Carry on":
                scene bg cy_grounds2_2 with fade
                "You wave to him."
                pov "Why would I try to stop you? It's always good to see student teacher bonding."
                "The teacher looks shocked, her features giving way to absolute despair. The student's face splits into a wide, evil grin."
                delinquent "Hahahaa! See? You're my woman now. Even the principal isn't going to stop me. Let's take off those panties. "
                teacher "No! NO!"
                "You turn to walk away."
                pov "Have fun, you two!"
                "As the delinquent forces the teacher to bend over, he gives you a thumbs up. The sound of the teacher's protests, cries, and howls echoes through the halls and shocked teachers and students end up seeing them going at it. A few teachers, witnessing how you handled the situation, look at you angrily."
                "The teachers are NOT going to be happy, and this is going to be devastating for your reputation. The students have gotten the message though: If they want a teacher they can have them if they're strong enough to claim them."
                $ behavior -=2
                $ morale -=1
                $ reputation -=3
                $ sex +=3
                $ inhibition -=1
                $ athletics +=2
                $ cy_carryon = True
    return

label cy_grounds3:
    if (deviance >= 75 and inhibition <= 25) or (cy_boyfight == True):
        scene bg cy_grounds3_2 with fade
        "The two students you saw fighting over a girl before have decided to stop fighting and share the girl. She doesn't seem to have any arguments against it at the moment. A friendship preserved. Heartwarming."
        $ morale -=1
        $ inhibition -=1
        $ deviance +=1
        $ cy_boyfight = True
    else:
        scene bg cy_grounds3_1 with fade
        "Getting students turned on can have a downside as well as an upside. As you leave the school you see two students fighting over a girl. After you break them apart they make it clear the sexy school uniform got them both so worked up over the girl that they ended up fighting. They're clearly friends and quickly apologize to each other."
        "She's angry with both of them."
        "You quickly give both boys a light detention and send the three on their way."
        "You later hear the two made up but both are still trying to date her."
        $ behavior -=1
        $ inhibition -=1
        $ deviance +=1
    return

label cy_grounds4:
    scene bg cy_grounds4 with fade
    "Some boys in the school are practically keeping some of the girls as pets, blackmailing or just outright raping them into servitude."
    return

label cy_grounds5:
    scene bg cy_grounds5 with fade
    girl "Hey Mr. pov, I’ve got something you’ll want to see~!"
    pov "Oh, wha- oh."
    "Very nice."
    $ inhibition -=1
    $ deviance +=1
    return

label cy_grounds6:
    scene bg cy_grounds6 with fade
    boy "Come on, let me see!"
    girl "Well, okay. Just a peek."
    boy "Wow! You really did it! You came without them on!"
    girl "Just don’t tell anyone, okay?"
    "I won’t tell if you won’t tell."
    $ inhibition -=1
    $ deviance -=1
    return

label cy_grounds7:
    scene bg cy_grounds7 with fade
    "This girl just joined the music club. She doesn’t have any prior experience but she’s going after her practice sessions with a ferocity that’s a little scary. She's going to be great someday."
    $ morale +=1
    return

label cy_grounds8:
    scene bg cy_grounds8 with fade
    "There’s been a fight in the halls between two girls. You break it up and apply the school’s punishment policy to them."
    return

label cy_grounds9:
    scene bg cy_grounds9_1 with fade
    scene bg cy_grounds9_2 with fade
    girl "pov, please help me! A bunch of boys brought me in here and they just keep coming!"
    menu:
        "Help Her":
            "You free the girl and take her out of the toilets. The boys are expelled."
        "Leave":
            scene bg cy_grounds9_3 with fade
            "You come back a few days later. There’s no fight left in her now."
    return

label cy_grounds10:
    scene bg cy_grounds10 with fade
    "You witness a girl walking in on a guy who has a female classmate tied up. He has her up against the wall and is fucking her hard, despite her muffled protests. The girl that just walks in suddenly looks furious and punches the wall. He turns his head to face the loud noise and suddenly looks terrified."
    guy "Uh, wait! I can explain!"
    girl "You’re cheating on me!?!"
    guy "N-no, of course not!"
    girl "So she just tied herself up and MADE you rape her? What were you thinking!"
    guy "Yes! Er-No! Aw, come on, come back! It didn’t mean anything!"
    "He drops the tied up girl to the ground and chases after his former girlfriend."
    "Ugh. Teen drama."
    return

label cy_grounds11:
    scene bg cy_grounds11_1 with fade
    "Not every relationship has the boy in charge. These two are on the school roof and it's clear the girl is in charge."
    girl "Come on, suck on my tongue!"
    boy "You’re so gross. What if someone sees us?"
    girl "If they see us right now I’ll tell them you weren’t man enough to do something sexy with a girl. Get on with it!"
    boy "Fine."
    scene bg cy_grounds11_2 with fade
    girl "Mmm. Maybe I’ll make you use your tongue somewhere else soon."
    boy "Eep!"
    "Ah, young love."
    return

label cy_grounds12:
    scene bg cy_grounds12 with fade
    "Students have begun to show their affections at lunch."
    return

label cy_grounds13:
    scene bg cy_grounds13 with fade
    "You witness a confession of young love. Adorable."
    $ inhibition -=1
    $ morale +=1
    return

label cy_grounds14:
    scene bg cy_grounds14 with fade
    "Is that what they’re serving in the cafeteria these days? The parents are going to kill you for serving something so unhealthy... ah, screw ‘em. You don’t want the students to eat cardboard food like you did when you were in school."
    $ athletics -=1
    $ morale +=1
    return

label cy_grounds15:
    scene bg cy_grounds15 with fade
    "Where there’s love there’s also breakups. Their hearts will mend soon enough, but it’s always a little sad to see a relationship end."
    return

label cy_grounds16:
    scene bg cy_grounds16 with fade
    "The cooking club is still allowed to wear aprons even with the nude dress code policy. You don’t want to get splashed with hot grease!"
    return

#### GYM EVENTS ####

label cy_gym1:
    $ randImg = renpy.random.choice(["1", "2"])
    $ renpy.show("bg gym1_"+randImg)
    with fade
    "There’s certainly a lot of exercise going on in gym these days, but it doesn’t seem to actually involve sports."
    return

#### LIBRARY EVENTS ####

label cy_library1:
    scene bg cy_library1 with fade
    "You see a student in study hall struggling with some homework. The problems are laughably easy to you so you spare a quick moment to point out where she’s making mistakes. She thanks you and you leave."
    "This doesn’t turn her into a model student overnight, but you later hear she did better in her class than she has been."
    $ academics +=1
    return

label cy_library2:
    scene bg cy_library2 with fade
    "It isn’t all just lust in class. Sometimes the endless sex can lead to true love."
    $ morale +=1
    return

label cy_library3:
    scene bg cy_library3 with fade
    "It isn’t just the students that are going without panties these days. In order to set a good example some of the teachers have joined in."
    return

label cy_library4:
    scene bg cy_library4 with fade
    girl "B-but I don’t know if I want people to see me like this!"
    boy "It’s just a skirt, relax. I’m sure it’ll be fine. The teacher will like it. Nothing bad will happen."
    menu:
        "Agree":
            "You walk in and wave to the students."
            girl "Mr. pov, I can explain!"
            pov "Explain what? I don't see anything bad going on here."
            boy "See? Even the principal approves. Come on, let's go to class."
            girl "Eeep!"
            "You wave them on their way. She practically sets a new fashion trend."
            $ deviance +=1
            $ inhibition -=1
        "Disagree":
            "You walk in looking stern."
            girl "Mr. pov, I can explain!"
            pov "Don't bother. My office, now."
            boy "Aww man."
            "You apply the school policy."
            $ inhibition +=1
            $ deviance -=1
            $ behavior +=1
    return

label cy_library5:
    scene bg cy_library5_1 with fade
    "Maybe you’re giving them too much homework. Unless - is she hiding something?"
    scene bg cy_library5_2 with fade
    "Hey! No eating in the library!"
    $ behavior +=1
    return

label cy_library6:
    scene bg cy_library6 with fade
    "This student is helping in the library. She’s happy to show anyone to a book they’re trying to find, but she can’t help trying to show a little more in the process."
    return

label cy_library7:
    scene bg cy_library7_1 with fade
    guy "Do you want to protect your friends or don’t you?"
    girl "Y-yes but!"
    guy "Look, I won’t show anyone these nice pictures. All you have to do is play along."
    girl "Fine."
    scene bg cy_library7_2 with fade
    guy "Good. Let’s get this shirt off."
    scene bg cy_library7_3 with fade
    guy "Wow. These are amazing!"
    girl "Are you happy now...?"
    guy "Oh come on, I haven’t even copped a feel yet."
    girl "Alright, just get it over with."
    scene bg cy_library7_4 with fade
    guy "Hmm. They’re soft. They look so tasty."
    girl "Oh no, you’re not going to - eek!"
    scene bg cy_library7_5 with fade
    guy "Mmm. Well, that was fun. Remember - same time next week."
    girl "..."
    return

label cy_library8:
    scene bg cy_library8_1 with fade
    bold_girl "Come on. If you’re going to flash people in public you’ve got to practice."
    shy_girl "But it’s so embarrassing!"
    bold_girl "Exactly. If you can’t even show me, how are you going to show a crowd? Pull your panties down."
    shy_girl "O-okay..."
    scene bg cy_library8_2 with fade
    bold_girl "Good job. Don’t worry. I’m sure you’ll be able to do it. Look how wet you are."
    shy_girl "Aaah! Stop pointing it out! It’s embarrassing!"
    "You leave the two to their strange practice session."
    return

#### OFFICE EVENTS ####

label cy_office1:
    scene bg office with fade
    "You get an e-mail from one of your teachers about a problem student. The teacher is requesting a disciplinary hearing for a student in her class. However, she requests that the student tell you the details of her misbehavior, seeming... embarrassed? Annoyed, you call the girl to the principals office."
    scene bg cy_office1 with fade
    "As soon as she sits down you can see precisely why she was called in here. The sexy school uniforms skirt is pretty short, but she’s not even making an effort to hide the fact that she’s not wearing panties at all. She’s completely soaked and visibly aroused. She immediately begins speaking, not waiting for your prompt."
    girl "I like not wearing panties. There’s nothing wrong with it. I want everyone to see me! I love it. Everyone used to think I was average before - but now everyone pays attention to me. Please don’t make me wear them again."
    "Her voice is alternately pleading and thick with arousal. She clearly likes being watched."
    menu:
        "Side with the Student":
            "You tell the girl not to worry and send her back to class. You send back an e-mail to the teacher stating that the matter has been reviewed and is not an issue."
            "No doubt this will hurt the reputation of your school, but the girl will certainly enjoy herself - and be enjoyed. With your support the teacher backs down and the other students realize it’s acceptable not to wear panties to school."
            if renpy.random.randint(1, 2) == 1:
                $ deviance += 5
            $ reputation -=1
            $ inhibition -=1
        "Side with the Teacher":
            if pda_rule_level < 3:
                "You scold the girl for not wearing panties in class and send her back. You hear that she continued doing it anyway. Without your support the other students are influenced by the teacher and treat her as a bad example."
                $ reputation -=1
                $ inhibition +=1
            else:
                "You scold the girl for not wearing panties in class and enforce the school’s punishment policy."
                $ reputation +=1
                $ inhibition +=1
    return

label cy_office2:
    scene bg cy_office2_1 with fade
    "A boy is sent to your office for punishment. Apparently he likes flipping girls skirts in class and a teacher caught him."
    menu:
        "Don’t punish him":
            "He’s later seen doing it again. The teachers discipline him as much as they can but it seems no skirt is safe from his hands, including the teachers. He simply grows bolder by the day. The girls and the teachers are extremely unhappy with it, but everyone does get a nice view."
            scene bg cy_office2_2 with fade
            $ reputation -=1
            $ morale -=1
            $ deviance +=1
            $ inhibition -=1
        "Punish him":
            if pda_rule_level < 3:
                scene bg cy_office2_3 with fade
                "You scold the student fiercely. He turns around and moons you before strolling out of the office, flipping a teacher’s skirt in the process. He’s even worse than before. The girls are wearing tighter clothes to avoid him. The teachers are almost ready to rebel."
                $ reputation -=1
                $ deviance +=1
                $ inhibition +=1
                $ morale -=1
            else:
                "You apply the school’s policy to him, ensuring he doesn’t do it again. The girls are pretty happy about it, but your strolls through the hall are much less interesting than before."
                $ deviance -=1
                $ inhibition +=1
                $ morale +=1
    return

label cy_office3:
    scene bg cy_office3_1 with fade
    "Tolerance is a virtue, and this girl was caught mocking one of the lesbians in the class. She’s been assigned to sensitivity training in the privacy of the teacher's areas rather than get expelled."
    scene bg cy_office3_2 with fade
    "Her teacher is making sure she learns her lesson well."
    $ inhibition -=2
    $ deviance +=1
    return

label cy_office4:
    scene bg cy_office4 with fade
    "You’re reading some reports as you’re walking to your office when you collide with a teacher. You drop into a rather compromising position."
    menu:
        "Nice panties":
            if deviance < 25:
                teacher "Get off me."
                "She looks ticked and storms away."
                $ morale -= 1
            elif deviance < 75:
                teacher "Oh... thank you."
                "You help her up and she continues on her way."
                $ deviance += 1
            else:
                teacher "Mmm. Thank you. See me in my office later and maybe you'll get to see what's under them, too."
                "As you help her up she rubs her body against you, leaving you with a raging hard-on."
                $ inhibition -= 1
        "Sorry." if inhibition > 70:
            teacher "Don't worry [povTitle] [povLastName], I understand."
            "She smiles and walk away."
            $ morale += 1
        "Sorry." if inhibition <= 70:
            teacher "Oh... you don't like them?"
            "She smirks and walk away."
            $ morale -= 1
    return

label cy_office5:
    scene bg cy_office5_1 with fade
    boy "Come on teach! Open up! You promised us a reward if we got the highest grade in the school, and we did!"
    scene bg cy_office5_2 with fade
    teacher "But I didn’t mean this! I- blurrbl!"
    scene bg cy_office5_3 with fade
    "It’s nice to see the teachers motivating their students to excel."
    $ academics +=1
    $ morale +=1
    $ inhibition -=1
    $ deviance +=1
    return

label cy_office6:
    scene bg cy_office6 with fade
    teacher "M-mr. principal, get your finger out of there!"
    pov "Weren’t you the one who said you wanted me to finger you?"
    teacher "Yes, but not there!"
    pov "Too late now. Just wait until you see what else I put up there."
    teacher "Eeep."
    return

label cy_office7:
    if inhibition <= 40 and deviance >= 60:
        scene bg cy_office7_2 with fade
        girl "How long do I have to stand here like this?"
        pov "Until you remember to wear the new uniform instead of the old one."
        girl "But that uniform is indecent! People can see my panties!"
        pov "If you’re this shy about showing your panties to people then showing off your bare pussy ought to convince you that it's not a bad alternative."
        girl "B-but people will see! They’ll take pictures!"
        pov "You should have thought of that before you decided not to wear the uniform."
    else:
        scene bg cy_office7_1 with fade
        girl "How long do I have to stand here like this?"
        pov "Until you remember to wear the new uniform instead of the old one."
        girl "But that uniform is indecent! People can see my panties!"
        pov "If you’re this shy about showing your panties to people you need to get used to it. Hence your punishment."
        girl "B-but people will see! They’ll take pictures!"
        pov "You should have thought of that before you decided not to wear the uniform."
    $ inhibition -=1
    $ deviance +=1
    $ cy_showpanties = True
    return

label cy_office8:
    scene bg cy_office8 with fade
    "Parent teacher conferences are starting to get a little bit weird, especially once the mothers started requesting some of the more attractive male students join the discussions. Surprisingly the more open minded parents are now helping your reputation instead of hurting it, being more than willing to praise you in public."
    $ reputation +=2
    $ deviance +=1
    return

label cy_office9:
    scene bg cy_office9 with fade
    "You see a lovely young student in the hallway, confident and ready for her classes. You give her a little wave and she waves back."
    return

label cy_office10:
    scene bg cy_office10 with fade
    "A student accidentally bumps into you on her way to class. She hurriedly says she’s sorry and runs away."
    return

label cy_office11:
    scene bg cy_office11_1 with fade
    "The teachers have become rather aggressive lately."
    teacher "Come on, you’ve got to do better than that if you’re going to confess to your teacher."
    boy "B-but I don’t know how to kiss! And I didn’t confess, you just-mmph!"
    scene bg cy_office11_2 with fade
    teacher "Less talk, more tongue. Oooh, you’re all mine now!"
    boy "Eep!"
    return

label cy_office12:
    if cy_obsessive == False:
        scene bg cy_office12_1 with fade
        obsessive_girl "Come on, you’re going to be my girlfriend either way. Why not give me a smile?"
        girl "I’m not a lesbian! Stop hitting on me!"
        scene bg cy_office12_2 with fade
        "They suddenly spot you. You decide you have to say something."
        pov "What’s going on here?"
        obsessive_girl "Oh, she’s my girlfriend. She’s just playing hard to get. But she’ll come around eventually."
        girl "I’m not her girlfriend! She’s crazy and she keeps trying to make me have sex with her! I’m NOT a lesbian! Help me!"
        menu:
            "Side with the Obsessive Girl":
                pov "Oh don’t worry, I don’t want to get involved with your private relationship issues. You two can carry on."
                obsessive_girl "Wait! You mean y-you’re not going to stop me?"
                "Her shocked expression slowly changes. Her features suddenly make her seem like she’s intoxicated by lust and power."
                girl "What do you mean you’re not gonna stop her? Help me!"
                pov "I’m certainly not going to stop anyone from doing what they like with their girlfriend. You two can sort this out by yourselves."
                "You spot a janitor’s cart abandoned in the hall and some insta-wall, used to patch holes in walls. It bonds quickly and is pretty strong. You pick it up and hand it to the Obsessive Girl."
                pov "Here, this’ll probably help."
                girl "Wait! Noooo!"
                scene bg cy_office12_3 with fade
                obsessive_girl "Ha! Hahaha! You hear that? You’re not getting away now. I’m keeping you until you love me."
                scene bg cy_office12_4 with fade
                "You hear muffled moans coming from the hallway for hours."
                girl "*sob*"
                $ cy_obsessive = True
            "Side with the other girl":
                pov "Do you think I look like a moron? No means no. Let the girl go."
                girl "Thank you!"
                "I’ll see YOU in my office."
                "You apply the school punishment."
    else:
        scene bg cy_office12_5 with fade
        "You see the obsessive girl and the other girl together in the hallway again. The obsessive girl has already used the insta-wall to trap her there."
        girl "P-please, not again, I can’t - I can’t oooOOOohhh!"
        scene bg cy_office12_6 with fade
        obsessive_girl "Ten orgasms a day until you love me. We’re only at three. How long do you think you'll last before you break?"
        girl "But I’m not-"
        obsessive_girl "Still saying that? You wouldn’t have cum so many times already if you didn’t like me. Come on. Give me another."
        girl "haaahHHHAAAAAaaaaaaaaaeeeeeeee!"
        obsessive_girl "Good girl. That’s four. Ready to say you love me yet? Be my girlfriend?"
        girl "I lo- I lov- I - NO!"
        obsessive_girl "Oh well, there’s still six more to go, and there’s tomorrow after that. And the day after that, and the day after that..."
        girl "*sob*"
        "You leave them to their fun."
    return

label cy_office13:
    scene bg cy_office13 with fade
    if morale >= 75:
        "The students seem to be really happy during class break. You congratulate yourself on a good job with morale."
    else:
        "You see a gaggle of girls in-between classes. They seem pretty happy."
    return

label cy_office14:
    scene bg cy_office14 with fade
    "Some students are starting to bring a few accessories to school. You hear buzzing on occasion but you never seem to catch one in the act."
    return

#### POOL EVENTS ####

label cy_pool1:
    scene bg cy_pool1 with fade
    girl "Get off of me!"
    guy "Oh come on, you three were asking for it, wearing your swimsuits out of class."
    girl "We were on our way to the pool!"
    guy "Too late now."
    girl "Ugh, boys. Fine, but make it quick or we'll be late for class!"
    return

label cy_pool2:
    scene bg cy_pool2 with fade
    "The students are working hard in the pool. They’re trying their best to get good for the competitions coming up."
    $ athletics +=1
    return
