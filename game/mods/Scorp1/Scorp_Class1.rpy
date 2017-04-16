#### SCORP EVENT PACK 1 - Classroom ####

## This event pack contains events for all locations in the game except the Baths.
## I am an inexperienced coder and using Flagon's pack as a base for this.
## I believe he, in turn, used Goldo's code as a base - this is known as the circle of life.
## This File is for the Classroom.
## Pictures are located in the subdirectory \Scorp1\Classroom
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
screen scorp_scroll_screen:
    viewport:
        edgescroll (200, 500)
        mousewheel True
        add scorp_bg

#Declaring images

image bg scorp_classroom1 = "mods/Scorp1/Classroom/scorp_classroom1.jpg"
image bg scorp_classroom2 = "mods/Scorp1/Classroom/scorp_classroom2.jpg"
image bg scorp_classroom3 = "mods/Scorp1/Classroom/scorp_classroom3.jpg"
image bg scorp_classroom4 = "mods/Scorp1/Classroom/scorp_classroom4.jpg"
image bg scorp_classroom5 = "mods/Scorp1/Classroom/scorp_classroom5.jpg"
image bg scorp_classroom6 = "mods/Scorp1/Classroom/scorp_classroom6.jpg"
image bg scorp_classroom7 = "mods/Scorp1/Classroom/scorp_classroom7.jpg"
image bg scorp_classroom8 = "mods/Scorp1/Classroom/scorp_classroom8.jpg"
image bg scorp_classroom9 = "mods/Scorp1/Classroom/scorp_classroom9.jpg"
image bg scorp_classroom10 = "mods/Scorp1/Classroom/scorp_classroom10.jpg"
image bg scorp_classroom11 = "mods/Scorp1/Classroom/scorp_classroom11.jpg"
image bg scorp_classroom12 = "mods/Scorp1/Classroom/scorp_classroom12.jpg"
image bg scorp_classroom13 = "mods/Scorp1/Classroom/scorp_classroom13.jpg"
image bg scorp_classroom14 = "mods/Scorp1/Classroom/scorp_classroom14.jpg"
image bg scorp_classroom15_1 = "mods/Scorp1/Classroom/scorp_classroom15_1.jpg"
image bg scorp_classroom15_2 = "mods/Scorp1/Classroom/scorp_classroom15_2.jpg"
image bg scorp_classroom16 = "mods/Scorp1/Classroom/scorp_classroom16.jpg"
image bg scorp_classroom17 = "mods/Scorp1/Classroom/scorp_classroom17.jpg"
image bg scorp_classroom18 = "mods/Scorp1/Classroom/scorp_classroom18.jpg"
image bg scorp_classroom19_1 = "mods/Scorp1/Classroom/scorp_classroom19_1.jpg"
image bg scorp_classroom19_2 = "mods/Scorp1/Classroom/scorp_classroom19_2.jpg"
image bg scorp_classroom19_3 = "mods/Scorp1/Classroom/scorp_classroom19_3.jpg"
image bg scorp_classroom20 = "mods/Scorp1/Classroom/scorp_classroom20.jpg"
image bg scorp_classroom21 = "mods/Scorp1/Classroom/scorp_classroom21.jpg"
image bg scorp_classroom22_1 = "mods/Scorp1/Classroom/scorp_classroom22_1.jpg"
image bg scorp_classroom22_2 = "mods/Scorp1/Classroom/scorp_classroom22_2.jpg"
image bg scorp_classroom22_3 = "mods/Scorp1/Classroom/scorp_classroom22_3.jpg"
image bg scorp_classroom23 = "mods/Scorp1/Classroom/scorp_classroom23.jpg"
image bg scorp_classroom24 = "mods/Scorp1/Classroom/scorp_classroom24.jpg"
image bg scorp_classroom25_1 = "mods/Scorp1/Classroom/scorp_classroom25_1.jpg"
image bg scorp_classroom25_2 = "mods/Scorp1/Classroom/scorp_classroom25_2.jpg"
image bg scorp_classroom25_3 = "mods/Scorp1/Classroom/scorp_classroom25_3.jpg"
image bg scorp_classroom25_4 = "mods/Scorp1/Classroom/scorp_classroom25_4.jpg"
image bg scorp_classroom25_5 = "mods/Scorp1/Classroom/scorp_classroom25_5.jpg"
image bg scorp_classroom26 = "mods/Scorp1/Classroom/scorp_classroom26.jpg"
image bg scorp_classroom27 = "mods/Scorp1/Classroom/scorp_classroom27.jpg"
image bg scorp_classroom28 = "mods/Scorp1/Classroom/scorp_classroom28.jpg"
image bg scorp_classroom29_1 = "mods/Scorp1/Classroom/scorp_classroom29_1.jpg"
image bg scorp_classroom29_2 = "mods/Scorp1/Classroom/scorp_classroom29_2.jpg"
image bg scorp_classroom29_3 = "mods/Scorp1/Classroom/scorp_classroom29_3.jpg"
image bg scorp_classroom30 = "mods/Scorp1/Classroom/scorp_classroom30.jpg"
image bg scorp_classroom31 = "mods/Scorp1/Classroom/scorp_classroom31.jpg"
image bg scorp_classroom32_1 = "mods/Scorp1/Classroom/scorp_classroom32_1.jpg"
image bg scorp_classroom32_2 = "mods/Scorp1/Classroom/scorp_classroom32_2.jpg"
image bg scorp_classroom32_3 = "mods/Scorp1/Classroom/scorp_classroom32_3.jpg"
image bg scorp_classroom32_4 = "mods/Scorp1/Classroom/scorp_classroom32_4.jpg"
image bg scorp_classroom33 = "mods/Scorp1/Classroom/scorp_classroom33.jpg"
image bg scorp_classroom34 = "mods/Scorp1/Classroom/scorp_classroom34.jpg"
image bg scorp_classroom35 = "mods/Scorp1/Classroom/scorp_classroom35.jpg"
image bg scorp_classroom36 = "mods/Scorp1/Classroom/scorp_classroom36.jpg"
image bg scorp_classroom37 = "mods/Scorp1/Classroom/scorp_classroom37.jpg"
image bg scorp_classroom38 = "mods/Scorp1/Classroom/scorp_classroom38.jpg"
image bg scorp_classroom39 = "mods/Scorp1/Classroom/scorp_classroom39.jpg"
image bg scorp_classroom40 = "mods/Scorp1/Classroom/scorp_classroom40.jpg"
image bg scorp_classroom41 = "mods/Scorp1/Classroom/scorp_classroom41.jpg"
image bg scorp_classroom42 = "mods/Scorp1/Classroom/scorp_classroom42.jpg"
image bg scorp_classroom43 = "mods/Scorp1/Classroom/scorp_classroom43.jpg"
image bg scorp_classroom44 = "mods/Scorp1/Classroom/scorp_classroom44.jpg"
image bg scorp_classroom45 = "mods/Scorp1/Classroom/scorp_classroom45.jpg"
image bg scorp_classroom46 = "mods/Scorp1/Classroom/scorp_classroom46.jpg"
image bg scorp_classroom47 = "mods/Scorp1/Classroom/scorp_classroom47.jpg"
image bg scorp_classroom48 = "mods/Scorp1/Classroom/scorp_classroom48.jpg"
image bg scorp_classroom49 = "mods/Scorp1/Classroom/scorp_classroom49.jpg"
image bg scorp_classroom50 = "mods/Scorp1/Classroom/scorp_classroom50.jpg"
image bg scorp_classroom51 = "mods/Scorp1/Classroom/scorp_classroom51.jpg"
image bg scorp_classroom52 = "mods/Scorp1/Classroom/scorp_classroom52.jpg"
image bg scorp_classroom53 = "mods/Scorp1/Classroom/scorp_classroom53.jpg"
image bg scorp_classroom54 = "mods/Scorp1/Classroom/scorp_classroom54.jpg"
image bg scorp_classroom55 = "mods/Scorp1/Classroom/scorp_classroom55.jpg"
image bg scorp_classroom56 = "mods/Scorp1/Classroom/scorp_classroom56.jpg"
image bg scorp_classroom57 = "mods/Scorp1/Classroom/scorp_classroom57.jpg"
image bg scorp_classroom58 = "mods/Scorp1/Classroom/scorp_classroom58.jpg"
image bg scorp_classroom59 = "mods/Scorp1/Classroom/scorp_classroom59.jpg"
image bg scorp_classroom60 = "mods/Scorp1/Classroom/scorp_classroom60.jpg"
image bg scorp_classroom61 = "mods/Scorp1/Classroom/scorp_classroom61.jpg"
image bg scorp_classroom62 = "mods/Scorp1/Classroom/scorp_classroom62.jpg"
image bg scorp_classroom63 = "mods/Scorp1/Classroom/scorp_classroom63.jpg"
image bg scorp_classroom64 = "mods/Scorp1/Classroom/scorp_classroom64.jpg"
image bg scorp_classroom65 = "mods/Scorp1/Classroom/scorp_classroom65.jpg"
image bg scorp_classroom66 = "mods/Scorp1/Classroom/scorp_classroom66.jpg"
image bg scorp_classroom67 = "mods/Scorp1/Classroom/scorp_classroom67.jpg"
image bg scorp_classroom68 = "mods/Scorp1/Classroom/scorp_classroom68.jpg"
image bg scorp_classroom69 = "mods/Scorp1/Classroom/scorp_classroom69.jpg"
image bg scorp_classroom70 = "mods/Scorp1/Classroom/scorp_classroom70.jpg"
image bg scorp_classroom71 = "mods/Scorp1/Classroom/scorp_classroom71.jpg"
image bg scorp_classroom72 = "mods/Scorp1/Classroom/scorp_classroom72.jpg"

#Setting up events and conditions

init:
    $ event("scorp_class1", "act == 'class' and deviance > 98", event.choose_one('class'), priority=200)
    $ event("scorp_class2", "act == 'class' and deviance > 80 and inhibition < 20", event.choose_one('class'), priority=200)
    $ event("scorp_class3", "act == 'class' and deviance > 99 and inhibition < 1", event.choose_one('class'), priority=200)
    $ event("scorp_class4", "act == 'class' and deviance > 90", event.choose_one('class'), priority=200)
    $ event("scorp_class5", "act == 'class' and deviance > 90", event.choose_one('class'), priority=200)
    $ event("scorp_class6", "act == 'class' and inhibition < 10 and deviance > 90", event.choose_one('class'), priority=200)
    $ event("scorp_class7", "act == 'class' and inhibition < 55", event.choose_one('class'), priority=200)
    $ event("scorp_class8", "act == 'class' and behavior < 20", event.choose_one('class'), priority=200)
    $ event("scorp_class9", "act == 'class' and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("scorp_class10", "act == 'class' and deviance > 98 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class11", "act == 'class' and deviance > 98 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class12", "act == 'class' and deviance > 80 and inhibition < 25", event.choose_one('class'), priority=200)
    $ event("scorp_class13", "act == 'class' and deviance > 70 and inhibition < 40 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class14", "act == 'class' and deviance > 98 and inhibition < 5 and behavior_rules == 'behavior_no_limit'", event.choose_one('class'), priority=200)
    $ event("scorp_class15", "act == 'class' and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class16", "act == 'class' and behavior < 70 and morale > 60 and deviance < 60", event.choose_one('class'), priority=200)
    $ event("scorp_class17", "act == 'class' and deviance > 90 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class18", "act == 'class' and uniform == 'nude_uniform' and inhibition < 20", event.choose_one('class'), priority=200)
    $ event("scorp_class19", "act == 'class' and deviance > 98 and inhibition < 3", event.choose_one('class'), priority=200)
    $ event("scorp_class20", "act == 'class' and deviance > 80 and inhibition < 18", event.choose_one('class'), priority=200)
    $ event("scorp_class21", "act == 'class' and deviance > 92 and inhibition < 15", event.choose_one('class'), priority=200)
    $ event("scorp_class22", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class23", "act == 'class' and deviance > 95 and inhibition > 10", event.choose_one('class'), priority=200)
    $ event("scorp_class24", "act == 'class' and inhibition < 55 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class25", "act == 'class' and deviance > 92 and inhibition < 12", event.choose_one('class'), priority=200)
    $ event("scorp_class26", "act == 'class' and inhibition < 80", event.choose_one('class'), priority=200)
    $ event("scorp_class27", "act == 'class' and deviance > 65 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("scorp_class28", "act == 'class' and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class29", "act == 'class' and deviance > 90 and academics > 60", event.choose_one('class'), priority=200)
    $ event("scorp_class30", "act == 'class' and deviance > 30 and inhibition < 90 and deviance < 60", event.choose_one('class'), priority=200)
    $ event("scorp_class31", "act == 'class' and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class32", "act == 'class' and deviance < 50", event.choose_one('class'), priority=200)
    $ event("scorp_class33", "act == 'class' and inhibition < 20", event.choose_one('class'), priority=200)
    $ event("scorp_class34", "act == 'class' and deviance > 80 and inhibition < 25", event.choose_one('class'), priority=200)
    $ event("scorp_class35", "act == 'class' and deviance > 98 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class36", "act == 'class' and deviance > 95 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class37", "act == 'class' and deviance > 95 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class38", "act == 'class' and uniform == 'nude_uniform' and deviance > 70", event.choose_one('class'), priority=200)
    $ event("scorp_class39", "act == 'class' and uniform == 'nude_uniform' and deviance > 85", event.choose_one('class'), priority=200)
    $ event("scorp_class40", "act == 'class' and inhibition < 50 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class41", "act == 'class' and uniform == 'sexy_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class42", "act == 'class' and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class43", "act == 'class' and deviance > 60 and deviance < 90", event.choose_one('class'), priority=200)
    $ event("scorp_class44", "act == 'class' and deviance > 98", event.choose_one('class'), priority=200)
    $ event("scorp_class45", "act == 'class' and deviance > 90", event.choose_one('class'), priority=200)
    $ event("scorp_class46", "act == 'class' and inhibition < 10 and deviance > 95", event.choose_one('class'), priority=200)
    $ event("scorp_class47", "act == 'class' and deviance > 40 and deviance < 90 and behavior_rules == {'behavior_no_limit' or 'behavior_physical'}", event.choose_one('class'), priority=200)
    $ event("scorp_class48", "act == 'class' and deviance > 5 and deviance < 25", event.choose_one('class'), priority=200)
    $ event("scorp_class49", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class50", "act == 'class' and deviance > 60 and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class51", "act == 'class' and deviance < 75", event.choose_one('class'), priority=200)
    $ event("scorp_class52", "act == 'class' and deviance > 95 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class53", "act == 'class' and morale > 50 and deviance < 60", event.choose_one('class'), priority=200)
    $ event("scorp_class54", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("scorp_class55", "act == 'class' and deviance > 98 and inhibition < 4", event.choose_one('class'), priority=200)
    $ event("scorp_class56", "act == 'class' and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class57", "act == 'class' and uniform == 'nude_uniform' and deviance > 85", event.choose_one('class'), priority=200)
    $ event("scorp_class58", "act == 'class' and deviance > 75 and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class59", "act == 'class' and deviance > 50 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class60", "act == 'class' and inhibition < 55 and inhibition > 15", event.choose_one('class'), priority=200)
    $ event("scorp_class61", "act == 'class' and deviance > 70 and inhibition < 30", event.choose_one('class'), priority=200)
    $ event("scorp_class62", "act == 'class' and deviance > 80 and inhibition < 15", event.choose_one('class'), priority=200)
    $ event("scorp_class63", "act == 'class' and deviance > 95 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("scorp_class64", "act == 'class' and deviance > 10 and deviance < 35", event.choose_one('class'), priority=200)
    $ event("scorp_class65", "act == 'class' and deviance > 5 and deviance < 15", event.choose_one('class'), priority=200)
    $ event("scorp_class66", "act == 'class' and inhibition < 60 and deviance < 90 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class67", "act == 'class' and inhibition < 85 and inhibition > 10 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class68", "act == 'class' and inhibition < 85 and deviance < 25 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)
    $ event("scorp_class69", "act == 'class' and inhibition < 25 and deviance > 75", event.choose_one('class'), priority=200)
    $ event("scorp_class70", "act == 'class' and inhibition > 20 and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class71", "act == 'class' and inhibition < 25 and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("scorp_class72", "act == 'class' and inhibition < 65 and uniform == ('uniform' or 'sexy_uniform')", event.choose_one('class'), priority=200)

label scorp_class1:

    #Panning up and down
    scene bg scorp_classroom1:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom1")
    show screen scorp_scroll_screen

    pov "I wish previous classes would clean up their mess. This girl's been fucked completely senseless."
    hide screen scorp_scroll_screen
    return

label scorp_class2:

    scene bg scorp_classroom2 with fade
    "As you enter a classroom, you meet a girl coming out, her face dripping cum and her tits exposed to the world."
    girl "What are you looking at?"
    return

label scorp_class3:

    scene bg scorp_classroom3 with fade
    "Class has once again devolved into a moaning, screaming orgy."
    return

label scorp_class4:

    #Panning up and down
    scene bg scorp_classroom4:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom4")
    show screen scorp_scroll_screen

    "As this girl sits down to get ready for class, she tugs her panties down her thighs absent-mindedly to let the cum spill out."
    guy "Hey Ayami! If you're going to show us your pussy, show us those fine tits too!"
    girl "*giggle* Okay!"
    hide screen scorp_scroll_screen
    return

label scorp_class5:

    #Panning up and down
    scene bg scorp_classroom5:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom5")
    show screen scorp_scroll_screen

    girl "In art class today, we learned that the female body is a blank canvas, that can be painted on with cum!"
    girl "It's an art style known as 'bukkake'!"
    $ artistery += 1
    hide screen scorp_scroll_screen
    return

label scorp_class6:

    #Panning up and down
    scene bg scorp_classroom6:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom6")
    show screen scorp_scroll_screen

    "The teacher walks into the classroom and is greeted by this sight."
    teacher "Hina! Have you been fucking everyone before class again?"
    girl "No, sir... It's just a blowjob, look..."
    "The dick she was sucking until a second ago chooses that moment to spurt thick ropes of cum all over her face."
    girl "See?"
    "The teacher glances at the thick flood of cum dripping from her ravaged pussy, and sighs."
    teacher "Hina, I {b}told{/b} you about this. {b}I{/b} want to be the first one to use your pussy in the morning, when it's nice and tight."
    girl "...Sorry, sir."
    hide screen scorp_scroll_screen
    return

label scorp_class7:

    scene bg scorp_classroom7 with fade
    "It's amazing how girls' clothing keeps seeming to just 'fall off' during class. And at just the right times to tease the boys..."
    $ inhibition -= 1
    return

label scorp_class8:

    scene bg scorp_classroom8 with fade
    "This class really is full of annoying little brats!"
    $ behavior -= 1
    return

label scorp_class9:

    teacher "Marie, could you come to the front and solve this problem for us?"
    girl "*gulp* ...Yes, sir."
    scene bg scorp_classroom9 with fade
    "Difficult mathematics isn't made any easier when you've come to school with a vibrating dildo hidden in your pussy."
    girl "Uhhh... And the square root... Unf... Is..."
    teacher "Hurry up!"
    girl "Yes... Sir... Ahhh... AHHHH... OH GOD YES..."
    "Needless to say, the problem did not get solved."
    $ academics -= 1
    return

label scorp_class10:

    teacher "Class, since you have been very good recently, I have arranged a treat."
    scene bg scorp_classroom10 with fade
    teacher "I would like all the boys to line up behind Karin here. She's been very naughty recently, and we're going to teach her an important lesson."
    teacher "When you've finished fucking her, return to the back of the queue and try to get hard again. Ideally, I'd like everyone to have two turns. I'll be going first."
    "Karin" "*whimper*"
    $ deviance += 1
    return

label scorp_class11:

    scene bg scorp_classroom11 with fade
    teacher "...At the insistence of the principal, today I shall be teaching you about the vagina, using myself and a student as live examples."
    girl "...Sensei, this seems weird..."
    teacher "Ssh. First, notice the pubic hair on my... pussy... is much longer than on Megumi's here. This is because I am older, and what little hair Megumi had, she's shaved off."
    teacher "Now, if you'd like to grab your rulers, I'd like you all to come up here and measure the difference in our pussies' height, width, and... depth."
    return

label scorp_class12:

    scene bg scorp_classroom12 with fade
    "You don't know quite what happened in this art class, but three girls seem to have found their muse, ripping their clothes off and painting their own bodies in some statement of modern art."
    "They all get an A."
    $ artistery += 2
    return

label scorp_class13:

    scene bg scorp_classroom13 with fade
    "Girls like to walk around bottomless now, cum drooling down their inner thighs. It saves everyone a lot of time."
    return

label scorp_class14:

    scene bg scorp_classroom14 with fade
    "Male teachers have started to enjoy 'punishing' the female students. They come up with the feeblest excuses, too."
    teacher "This will teach you not to chew gum in class!"
    $ behavior += 1
    return

label scorp_class15:

    #Panning up and down
    scene bg scorp_classroom15_1:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom15_1")
    show screen scorp_scroll_screen

    "An exhibitionist girl jogs naked along the school corridor, two buzzing vibrators crammed in her gushing pussy, juice pouring down the entire length of her legs, tits swinging side to side."
    girl "I FEEL SO ALIVE! *bounce bounce bounce*"
    "Someone - probably a boy - has put a collar round her neck, with a bell attached. As she runs, the bell rings a merry tune."
    hide screen scorp_scroll_screen

    #Panning up and down
    scene bg scorp_classroom15_2:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom15_2")
    show screen scorp_scroll_screen

    "Finally, the naked girl stops in front of a window and throws her arms in the air to everyone watching in the field below, her thighs shaking with her fifteenth orgasm that day."
    girl "I'M QUEEN OF THE WORLD!"
    "Seeing such a happy, healthy girl is enough to cheer everyone up."
    $ morale += 1
    hide screen scorp_scroll_screen
    return

label scorp_class16:

    scene bg scorp_classroom16 with fade
    "A rowdy, happy class is at least better than a rowdy, unhappy one."
    $ morale += 1
    $ behavior -= 1
    return

label scorp_class17:

    scene bg scorp_classroom17 with fade
    "These days, the toughest question a male student faces in class is: Pussy, or asshole?"
    return

label scorp_class18:

    #Panning up and down
    scene bg scorp_classroom18:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom18")
    show screen scorp_scroll_screen

    "The girls seem to have accepted the nude uniform policy for the most part, and of course the boys love it."
    $ morale += 1
    hide screen scorp_scroll_screen
    return

label scorp_class19:

    scene bg scorp_classroom19_1 with fade
    "A male student has grabbed a female teacher and is pressing her up against the wall, hiking her skirt up and ripping open her shirt."
    teacher "Young man - what are you doing? I am not a student!"
    guy "I know that, but you're a woman, and women don't have any authority any more. Spread your legs."
    teacher "Young man, I am - mph!"
    scene bg scorp_classroom19_2 with fade
    guy "Just shut up and accept my cock. Jeez."
    "The teacher's soft body seems to wilt in his grip, and grow more pliable. She opens her legs further and sinks back against him, grinding her hips as his dick thrusts inside her."
    teacher "Mmmmm..."
    scene bg scorp_classroom19_3 with fade
    guy "UHN! That's it! Yes!"
    "The word soon begins to spread that female teachers can be treated almost as badly as female students, without consequence."
    $ behavior -= 1
    $ academics -= 1
    return

label scorp_class20:

    scene bg scorp_classroom20 with fade
    "This girl is always the victim of the boys' silly pranks."
    "Pranked Girl" "...And after they'd all finished fucking me, they stole all my clothes, wrote mean stuff on my body, and stuffed these pens up by butt and pussy!"
    "Pranked Girl" "And if I take the pens out or wash myself, they'll never give me my clothes back! So I have to spend the whole day like this!"
    "Other Girl" "Ha ha! The boys get so creative with their pranks!"
    "Pranked Girl" "I know right! I just can't be mad at them!"
    return

label scorp_class21:

    scene bg scorp_classroom21 with fade
    "Looks like the boys have had some fun with these two."
    return

label scorp_class22:

    "A male teacher has wandered into one of his colleague's classes on his break, looking for a bit of stress relief."
    scene bg scorp_classroom22_1 with fade
    "He selects a female student, rips her skirt and panties off, and plunges his dick into her without ceremony."
    "It's amusing watching the poor girl try to write notes while the huge cock hammers her wet hole."
    scene bg scorp_classroom22_2 with fade
    girl "T-teacher - I can't do this - can you - nnnn, can you ask Mr. Miyamoto to wait until - AHH - until the lesson is over to - UH - fuck me?"
    teacher "I'm afraid Mr. Miyamoto is entitled to do what he likes on his free time. You'll have to just cope as best you can. Now, to continue..."
    girl "Uhhhh... Okay... I'll just try to ignore... This big cock... Inside me... Oh God..."
    "Mr. Miyamoto fucks the girl for a solid thirty minutes, the room filled with moans and the sound of flesh slapping flesh. Otherwise, class continues as normal."
    scene bg scorp_classroom22_3 with fade
    "When Mr. Miyamoto finally comes, it overwhelms the poor girl, and she lets out one long, ecstatic scream, drowning out the rest of the class for a moment."
    "She slumps over her desk, and Mr. Miyamoto wanders away satisfied."
    girl "My notes are a mess... I'm never going to pass now..."
    $ academics -= 1
    return

label scorp_class23:

    scene bg scorp_classroom23 with fade
    "It's good to see the girls are getting so good at juggling schoolwork with their sexual obligations."
    "Girls truly are better at multitasking, after all."
    return

label scorp_class24:

    scene bg scorp_classroom24 with fade
    "You notice a girl sitting in class, unaware that her top seems to have slipped down."
    pov "Um... Have you noticed that your...?"
    girl "Huh?"
    pov "You know what... Never mind."
    return

label scorp_class25:

    scene bg scorp_classroom25_1 with fade
    "One teacher likes to walk around class with his erect cock sticking nonchalantly out of his pants. Feeling mischievous, he presses it against one girl's cheek, reading from the textbook as though nothing's happening."
    "The girl tolerates the huge dick poking against her face for a while, unsure what to do. But soon enough, her natural female instinct kicks in."
    scene bg scorp_classroom25_2 with fade
    teacher "Mmm... So you finally got the hint, huh...?"
    "He continues to read from the book while, with loud, wet slurps, the girl sucks his throbbing member. She's really getting into it!"
    scene bg scorp_classroom25_3 with fade
    "Finally, the teacher grabs her head and forces the entire length of his dick down her throat. As she gags on it, he pumps a flood of cum into her."
    scene bg scorp_classroom25_4 with fade
    teacher "You better swallow it all, or you get detention."
    scene bg scorp_classroom25_5 with fade
    "With a shuddering gulp, the girl swallows the teacher's cum deposit, and gathers up the rest of the spillage with her fingers and tongue."
    teacher "Good girl. Now, as I was saying..."
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5
    return

label scorp_class26:

    scene bg scorp_classroom26 with fade
    "The class has exploded into some kind of miniature riot!"
    "It takes a long time to restore order."
    $ behavior -= 1
    return

label scorp_class27:

    scene bg scorp_classroom27 with fade
    "If you didn't want your classmates to gossip about the fact that you let strange men fuck you in an empty classroom, you should've locked the dang door!"
    return

label scorp_class28:

    #Panning up and down
    scene bg scorp_classroom28:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom28")
    show screen scorp_scroll_screen

    "The nude uniform is excellent in a heat wave, for students and teachers alike."
    $ morale += 1
    hide screen scorp_scroll_screen
    return

label scorp_class29:

    teacher "Since you girls have been doing so well with your Math recently, I've decided to introduce a new challenge: Hard Mode."
    scene bg scorp_classroom29_1 with fade
    teacher "Hard Mode Math means you will be solving problems in front of the class while I fuck you Harder than you've ever been fucked before."
    teacher "I am going to be brutal. I am going to fuck your slutty pussies and asses raw. And I won't let you orgasm until you answer the question correctly."
    scene bg scorp_classroom29_2 with doubleflash
    "Hard Mode proves to be a huge success. The girls' grades improve almost instantly."
    scene bg scorp_classroom29_3 with doubleflash
    "The only problem is cleanup."
    $ academics += 3
    return

label scorp_class30:

    #Panning up and down
    scene bg scorp_classroom30:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade

    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ scorp_bg=ImageReference("bg scorp_classroom30")
    show screen scorp_scroll_screen

    "This girl has been uncontrollably horny for days, but has been repressing it due to her shame and inhibitions."
    "But, like a horny pressure cooker, she can only keep a lid on it for so long. Today, during class, she explodes in lust, and begins wildly humping a chair."
    "It takes a while to restore order."
    $ inhibition -= 1
    hide screen scorp_scroll_screen
    return

label scorp_class31:

    scene bg scorp_classroom31 with fade
    "Nude uniform makes every day a good day."
    return

label scorp_class32:

    $ r=renpy.random.randint(1, 4)
    image bg scorp_classroom32 = ConditionSwitch("r==1","mods/Scorp1/Classroom/scorp_classroom32_1.jpg","r==2","mods/Scorp1/Classroom/scorp_classroom32_2.jpg","r==3","mods/Scorp1/Classroom/scorp_classroom32_3.jpg","r==4","mods/Scorp1/Classroom/scorp_classroom32_4.jpg")

    scene bg scorp_classroom32 with fade
    "This girl seems to be really getting in touch with her artistic side."
    $ artistery += 1
    return

label scorp_class33:

    scene bg scorp_classroom33 with fade
    "Girl 1" "Today, our class presentation will be on female arousal. It will be a practical demonstration. Sara, can you turn on the vibes please?"
    "Girl 2" "When the presentation is done, we will be taking questions, and if you like, you can all come up and feel how well-lubricated our vaginas are."
    "Everyone learns a lot!"
    $ academics += 1
    return

label scorp_class34:

    scene bg scorp_classroom34 with fade
    "Oops, you didn't realize this classroom was occupied... The two of them are really going at it."
    return

label scorp_class35:

    scene bg scorp_classroom35 with fade
    girl "Let me go! Let me go!"
    teacher "Today's lesson will be in how to turn a 'good girl' into a willing slut. I think we can manage that in the next hour, right class?"
    "Class" "Wooo! Yeah!"
    return

label scorp_class36:

    scene bg scorp_classroom36 with fade
    "You see some boys taking the time to mark out their property."
    return

label scorp_class37:

    scene bg scorp_classroom37 with fade
    "It looks like art class is going well. You suspect that soon these girls are going to be subjected to more than just tickling..."
    $ artistery += 1
    return

label scorp_class38:

    scene bg scorp_classroom38 with fade
    "The girls are cleaning the cum off this classroom's floor as punishment."
    "As you stare at the four beautiful holes they're presenting to you - six, counting their mouths - you can't help but wonder how vulnerable they feel, with their tight young holes constantly exposed to the cool air and lustful eyes of men."
    "You unzip your pants and compliment yourself on the nude uniform idea."
    $ behavior +=1
    return

label scorp_class39:

    scene bg scorp_classroom39 with fade
    "Finding the classroom unoccupied apart from a lone girl, you take the opportunity to treat yourself."
    girl "Fuck me harder, [povTitle] [povLastName]! Harder harder harder!"
    $ deviance +=1
    return

label scorp_class40:

    "One girl seems reluctant to come to the front of the class to solve a problem. Finally, after being threatened with detention, she shamefully comes forward."
    scene bg scorp_classroom40 with fade
    "You see now why she was worried."
    girl "A boy stole my skirt and panties! I'm so embarrassed!"
    "She seems genuinely embarrassed, but despite that you can see her pussy get wetter and wetter as the class stares."
    return

label scorp_class41:

    scene bg scorp_classroom41 with fade
    "A girl models the new sexy uniform for you after class, while you take pictures. You're going to put them in the school magazine!"
    return

label scorp_class42:

    scene bg scorp_classroom42 with fade
    "A girl models the new nude uniform for you after class, while you take pictures. You're going to put them in the school magazine!"
    return

label scorp_class43:

    scene bg scorp_classroom43 with fade
    pov "Um... You have a little something on your face..."
    girl "I do? Oh, you're right!"
    "She carefully wipes the semen from her glasses and walks away, embarrassed, completely oblivious to the load still clinging to her hair."
    return

label scorp_class44:

    scene bg scorp_classroom44 with fade
    "A couple of boys subject a girl to a 'surprise bukkake' in the middle of class. The teacher just laughs and then carries on with the lesson."
    return

label scorp_class45:

    "A teacher stands alone in class, wondering where everyone is."
    scene bg scorp_classroom45 with fade
    "Little does she know, the entire class have crammed into the men's bathroom for a spectacular orgy."
    "The girl on the far left was just laughed at when she wanted him to use a condom."
    return

label scorp_class46:

    scene bg scorp_classroom46 with fade
    teacher "Line the bitches up! Smack their ass! Grab their hair! And fuck them silly! I want to hear these dumb sluts screaming and crying, boys!"
    return

label scorp_class47:

    scene bg scorp_classroom47 with fade
    "If spanking is a punishment, why does it make so many girls' cunts gush?"
    "An interesting question to ponder as you smack a girl's ass for talking out of turn."
    return

label scorp_class48:

    scene bg scorp_classroom48 with fade
    "The girls giggle mischievously. They know that the boy round the corner is reading a hentai comic!"
    girl "How perverted!"
    "Other girl" "Sssh! We're going to jump out and surprise him!"
    $ deviance +=1
    return

label scorp_class49:

    scene bg scorp_classroom49 with fade
    "Girl 1" "We did it, Nariko! We fucked the whole school!"
    "Girl 2" "Uhh... Muhhh... Puhhh..."
    "Girl 1" "So many hard dicks! I hope we get an A for our biology experiment!"
    "Girl 2" "Muhhh... Hurrr..."
    "Girl 1" "Come on, let's pose for the photo!"
    return

label scorp_class50:

    scene bg scorp_classroom50 with fade
    "The only problem with the nude uniform is that freshly-fucked young girls leave little pools of cum wherever they sit down."
    return

label scorp_class51:

    scene bg scorp_classroom51 with fade
    "For a girl, there's nothing as fun as catching up on all the latest gossip."
    if deviance <5:
        girl "Did you hear? Maya and that bad boy Kazuki totally kissed each other! On the lips!"
        "Other girl" "Good for them!"
        $ morale -=1
        return

    elif deviance <15:
        girl "Did you hear? Saiko and Sayuri kissed each other on the way home from school! Can you imagine, two girls kissing!"
        "Other girl" "Ewww! Weird!"
        return

    elif deviance <25:
        girl "Did you hear? Ryoko did oral sex! She totally put her tongue on a boy's thing!"
        "Other girl" "Didn't it taste of pee?"
        return

    elif deviance <35:
        girl "Did you hear? Sayuri let a boy put his dick in her! He said it would just be the tip, but they ended up having full sex!"
        "Other girl" "What a slut!"
        return

    elif deviance <45:
        girl "Did you hear? Maya had anal sex with a boy! She didn't like it, but she said she was going to try again!"
        "Other girl" "Up the butt? That's not for me..."
        return

    elif deviance <55:
        girl "Did you hear? Sayuri was masturbating in class! She had a dildo under her desk!"
        "Other girl" "I know! What's the matter with her, can't she get a real boy?"
        return

    elif deviance <65:
        girl "Did you hear? Ryoko let two boys have sex with her at the same time! Front and back!"
        "Other girl" "Interesting... I kinda want to try that..."
        return

    else:
        girl "Did you hear? Saiko was raped in the bathroom the other day! She said she ended up liking it and had an orgasm!"
        "Other girl" "Not fair! I want to be raped!"
        return

label scorp_class52:

    "Sometimes journalists come by to investigate reports of strange happenings at Ashford."
    scene bg scorp_classroom52 with fade
    "It doesn't take much to 'bribe' them into silence, though the girls don't particularly like it."
    "The journalists write a glowing report on your school."
    $ morale -=2
    $ reputation +=3
    return

label scorp_class53:

    scene bg scorp_classroom53 with fade
    "On a gloomy morning, the bright, young, happy faces of your students is always enough to cheer you up."
    $ morale +=1
    return

label scorp_class54:

    scene bg scorp_classroom54 with fade
    teacher "Because I want to keep my job... Today's lesson will be on my vagina, and why I should let [povTitle] [povLastName] fuck it."
    teacher "First, everyone come up and take a good look inside my vagina. Out of 10, I want you all to score how wet and ready it is for a man's penis..."
    return

label scorp_class55:

    scene bg scorp_classroom55 with fade
    "One of the boys has realized something: A good fucktoy provides not only pleasure for her master, but amusement."
    "Making her do silly sexual antics during class is also a good way to show everyone what good control you have over her. Seeing such a devoted master-slave relationship cheers everyone up."
    $ morale +=1
    return

label scorp_class56:

    scene bg scorp_classroom56 with fade
    "The girls absolutely love the nude uniform!"
    $ morale +=3
    return

label scorp_class57:

    scene bg scorp_classroom57 with fade
    "Most of the boys don't bother to follow the nude uniform rule, even though it's strictly enforced for girls."
    "It does your heart good to see a boy wandering the corridor, with his nude harem following faithfully."
    return

label scorp_class58:

    scene bg scorp_classroom58 with fade
    "Girl 1" "So tell us, [povTitle] [povLastName], what was your inspiration for the nude uniform?"
    "Girl 2" "Was it to liberate us? Make us accept our bodies for what they are? Teach us not to repress healthy sexuality?"
    pov "Well if I'm going to be honest with you ladies, there were two reasons..."
    pov "Ease of access, and ease on the eyes."
    "Girl 1" "*giggle!*"
    return

label scorp_class59:

    "Hearing female moans, you investigate an empty classroom and are met with an interesting sight."
    scene bg scorp_classroom59 with fade
    "They're feverishly making out with each other, sweating, trembling, mouths locked together. One has either taken off her panties, or never wore them in the first place."
    "As you watch her bare butt jiggle, you remember that both of them have boyfriends. Should you break them up?"
    menu:
        "Come on, girls, this isn't the time or place!":
            "The girls blush, leap apart, and struggle to put their panties back on, giving you a good view of everything in the process."
            pov "It's a shame... But girls like this need discipline."
            $ behavior +=1
            $ morale -=1
            return
        "Walk away.":
            if inhibition <60:
                "As you leave, you hear them starting to have second thoughts."
                girl "We should do this somewhere private... I'm sorry, this was totally out of control..."
                $ inhibition +=1
                return
            else:
                "As you turn to leave, you realize they've both seen you."
                "Blonde Girl" "Do you really want to leave, [povTitle] Principal? And miss the show?"
                "Redhead" "*giggle*"
                "Blonde Girl" "Come on Ayami, take off the rest of the clothes... I want the principal to see how easily you orgasm..."
                $ morale +=1
                $ inhibition -=1
                return
    return

label scorp_class60:

    scene bg scorp_classroom60 with fade
    "This girl's friend is so mean to her! She's just ripped open her shirt in front of all the boys!"
    "The girl is embarrassed, but little does she know, revealing such impressive boobs will quickly make her the popular one..."
    $ inhibition -=1
    return

label scorp_class61:

    scene bg scorp_classroom61 with fade
    "Two girls hide in an empty classroom, lost in lust. Their fingers make loud wet sounds as they furiously masturbate each other's soaking cunts."
    return

label scorp_class62:

    scene bg scorp_classroom62 with fade
    "The girls and boys literally can't wait to get down to business, as soon as they enter class."
    return

label scorp_class63:

    scene bg scorp_classroom62 with fade
    "Looking upon scenes like this, with a whole class of once-innocent high school girls reduced to moaning, panting whores, you sometimes wonder if you've gone too far."
    pov "...Nah."
    return

label scorp_class64:

    scene bg scorp_classroom64 with fade
    "Just before class starts, a girl kisses the guy sat behind her full on the mouth, surprising him and everyone else."
    "A moment's lingering passion as they explore the taste of each other's mouth and tongue... Then she breaks away and sits down, blushing furiously."
    "The teacher didn't notice, but the rest of the class certainly did. Such a bold move! He wasn't even her boyfriend! What's got into her?"
    $ inhibition -=1
    return

label scorp_class65:

    girl "Hey, Shin... Wait a second..."
    scene bg scorp_classroom65 with fade
    "She kisses him gently on the lips."
    girl "*giggle* When did I get so bold?"
    return

label scorp_class66:

    teacher "Chiyo, your grades have been falling recently..."
    scene bg scorp_classroom66 with fade
    "Chiyo" "Whoops! *giggle* Teacher, my tit fell out of my shirt."
    teacher "..."
    "Chiyo" "Do you like my boob, teacher? I can tell there's something growing in your pants..."
    teacher "That - that's quite enough, young lady!"
    $ inhibition -=1
    return

label scorp_class67:

    scene bg scorp_classroom67 with fade
    "This girl decided to go without a bra. God must be a pervert, because it promptly poured with rain..."
    "When she ran in to get out of the downpour, she was jiggling like crazy!"
    $ inhibition -=1
    return

label scorp_class68:

    scene bg scorp_classroom68 with fade
    " - Wait! Are you seeing things, or is that girl not wearing any panties!?"
    "She's stopped lifting her skirt now, and it's impossible to tell. You must have been just imagining things..."
    "Either way, look at that self-satisfied smirk! She's a naughty one!"
    $ inhibition -=1
    return

label scorp_class69:

    scene bg scorp_classroom69 with fade
    "The Woodworking class seems to be going well."
    girl "How is it? Shall I try it out?"
    "Other girl" "Uhhhh... Yes, it's working as expected..."
    $ academics +=1
    return

label scorp_class70:

    scene bg scorp_classroom71 with fade
    "A girl arrives to class early, and starts undressing immediately."
    pov "A lot of the girls still aren't quite uninhibited enough to walk to school nude... I should work on that."
    $ inhibition +=1
    return

label scorp_class71:

    scene bg scorp_classroom71 with fade
    "The nude uniform really helps when it comes to art class."
    teacher "Now, girls, why don't you bend over and spread those pussy-lips?"
    girls "Yes, sir!"
    $ artistery +=1
    return

label scorp_class72:

    scene bg scorp_classroom72 with fade
    "This girl came to class like this. Does she realize her tits are out? Does it give her an erotic thrill? Or is she just a bit dumb?"
    $ inhibition -=1
    return
