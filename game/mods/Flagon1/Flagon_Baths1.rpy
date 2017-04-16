#### FLAGON EVENT PACK 1 - Baths ####

## This event pack contains events for all original locations in the game, as well as new events for the monthly actions.
## This File is for the Baths.
## Pictures are located in the subdirectory \Flagon1\Baths
## All custom images, characters, variables... are prefixed with "fla_" (with the exception of temp variables) to avoid conflicts.
## Formatting shamelessly stolen from Goldo. All your Code are belong to us!
#### SETUP ####

#Define characters
define fla_teacher = Character('Teacher', color="#0033FF")

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Declaring images

image bg fla_bath1 = "mods/Flagon1/Bath/fla_bath1.jpg"
image bg fla_bath3 = "mods/Flagon1/Bath/fla_bath3.jpg"
image bg fla_bath5 = "mods/Flagon1/Bath/fla_bath5.jpg"
image bg fla_bath7 = "mods/Flagon1/Bath/fla_bath7.jpg"
image bg fla_bath8_1 = "mods/Flagon1/Bath/fla_bath8_1.jpg"
image bg fla_bath8_2 = "mods/Flagon1/Bath/fla_bath8_2.jpg"
image bg fla_bath9 = "mods/Flagon1/Bath/fla_bath9.jpg"
image bg fla_bath10_1 = "mods/Flagon1/Bath/fla_bath10_1.jpg"
image bg fla_bath10_2 = "mods/Flagon1/Bath/fla_bath10_2.jpg"
image bg fla_bath10_3 = "mods/Flagon1/Bath/fla_bath10_3.jpg"
image bg fla_bath11 = "mods/Flagon1/Bath/fla_bath11.jpg"


#Setting up events and conditions

init:
    $ event("fla_bath1", "act == 'bath' and inhibition < 70", event.choose_one('bath'), priority=200)
    $ event("fla_bath2", "act == 'bath' and inhibition < 25 and deviance > 75", event.choose_one('bath'), priority=200)
    $ event("fla_bath3", "act == 'bath' and inhibition < 85", event.choose_one('bath'), priority=200)
    $ event("fla_bath5", "act == 'bath' and inhibition < 75 and deviance > 10", event.choose_one('bath'), priority=200)
    $ event("fla_bath6", "act == 'bath' and morale > 75 and deviance > 50", event.choose_one('bath'), priority=200)
    $ event("fla_bath7", "act == 'bath' and inhibition < 65", event.choose_one('bath'), priority=200)
    $ event("fla_bath8", "act == 'bath' and inhibition < 60", event.choose_one('bath'), priority=200)
    $ event("fla_bath9", "act == 'bath' and inhibition < 85", event.choose_one('bath'), priority=200)
    $ event("fla_bath10", "act == 'bath' and inhibition < 90", event.choose_one('bath'), priority=200)
    $ event("fla_bath11", "act == 'bath' and inhibition < 90", event.choose_one('bath'), priority=200)


label fla_bath1:

    scene bg fla_bath1 with fade
    "Oh! Sorry [povTitle] [povName]! It's the students turn to bathe right now!"
    $ inhibition -=1
    return

label fla_bath2:

    $ r=renpy.random.randint(1,2)
    image bg fla_bath2 = ConditionSwitch("r==1","mods/Flagon1/Bath/fla_bath2_1.jpg","r==2","mods/Flagon1/Bath/fla_bath2_2.jpg")

    scene bg fla_bath2 with fade
    "Moans of pleasure fill the bathhouse as these girls writhe together."
    $ deviance +=2
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return

label fla_bath3:

    scene bg fla_bath3 with fade
    "A nice bath at the end of a long day can really perk a person up."
    $ morale +=1
    $ inhibition -=1
    return

label fla_bath5:

    scene bg fla_bath5 with fade
    girl1 "Ahhh, no not there!"
    girl2 "Come on now, it's important to clean everywhere!"
    girl1 "AHHHHHHHHHH!"
    $ deviance +=1
    return

label fla_bath6:

    $ r=renpy.random.randint(1,2)
    image bg fla_bath6 = ConditionSwitch("r==1","mods/Flagon1/Bath/fla_bath6_1.jpg","r==2","mods/Flagon1/Bath/fla_bath2_2.jpg")

    scene bg fla_bath6 with fade
    "Some of your students have decided to show their appreciation for all the hard work you've put into the school."
    "As soapy hands move over your body, you can definitely say that it was worth the effort."
    $ deviance +=1
    $ inhibition -=1
    if renpy.random.randint(1, 3) ==1:
        $ deviance += 5
    return

label fla_bath7:

    scene bg fla_bath7 with fade
    "Nothing like a hot bath and a cold drink to wind down after a hard day's teaching!"
    $ inhibition -=1
    return

label fla_bath8:

    scene bg fla_bath8_1 with fade
    girl1 "Look, girls, [povTitle] [povLastName] is peeking again!"
    pov "Now, now, I'm just making sure proper hygiene is being maintained! Are you girls being sure to clean everywhere?"
    girl2 "*giggle* Of course! See for yourself!"
    scene bg fla_bath8_2
    "The girls shift their towels and spread their pussies open for you. After making sure you get a good look, they wrap up and leave the bath giggling."
    $ inhibition -=1
    $ deviance +=1
    if renpy.random.randint (1, 4) ==1:
        $ deviance += 5
    return

label fla_bath9:

    scene bg fla_bath9 with fade
    "A quick peek into the girls' bath always reminds you just why you invested all that money in companies that make back-pain medication."
    return

label fla_bath10:

    scene bg fla_bath10_1 with fade
    "You walk into the girls' bathroom only to spot one of your teachers.  She immediately notices you."

    if inhibition > 70:
        scene bg fla_bath10_2

        teacher "What do you think you're doing in here [povTitle][povLastName]!?"
        pov "Uh, I was just inspecting the..."
        teacher "JUST GET OUT!"
        "You flee before her righteous wrath."
        $ inhibition +=1
        $ reputation -=1

    else:

        scene bg fla_bath10_3
        teacher "Oh, [povFirstName]! What are you doing here?"
        pov "I just wanted to talk to you about this week's lesson plan.  Do you have a moment?"
        teacher "Of course! Could you help me scrub my back while we talk?"
        "You have a VERY stimulating conversation."
        $ inhibition -=1
    return

label fla_bath11:

    scene bg fla_bath11 with fade
    girl1 "WOW!  Those are huge! How did you get them to grow that big?"
    teacher "Oh, nothing special. Plenty of milk and the occasional massage."
    girl2 "I don't see what's so great about big boobs, anyway."
    $inhibition -=1
    $morale -=1
    return