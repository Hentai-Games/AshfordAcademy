#### FLAGON EVENT PACK 1 - Office ####

## This event pack contains events for all original locations in the game, as well as new events for the monthly actions.
## This Files is for the Office, and includes Bondage Detention events.
## Pictures are located in the subdirectory \Flagon1\Office
## All custom images, characters, variables... are prefixed with "fla_" (with the exception of temp variables) to avoid conflicts.
## Formatting shamelessly stolen from Goldo. All your Code are belong to us!
#### SETUP ####

#Define characters
#Characters go here if needed

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Declaring images

image bg fla_office1 = "mods/Flagon1/Office/fla_office1.jpg"
image bg fla_office2 = "mods/Flagon1/Office/fla_office2.jpg"
image bg fla_office3_1 = "mods/Flagon1/Office/fla_office3_1.jpg"
image bg fla_office3_2 = "mods/Flagon1/Office/fla_office3_2.jpg"
image bg fla_office3_3 = "mods/Flagon1/Office/fla_office3_3.jpg"
image bg fla_office4 = "mods/Flagon1/Office/fla_office4.jpg"
image bg fla_office5 = "mods/Flagon1/Office/fla_office5.jpg"
image bg fla_office8 = "mods/Flagon1/Office/fla_office8.jpg"
image bg fla_office9 = "mods/Flagon1/Office/fla_office9.jpg"
image bg fla_office10 = "mods/Flagon1/Office/fla_office10.jpg"
image bg fla_office11 = "mods/Flagon1/Office/fla_office11.jpg"
image bg fla_office12 = "mods/Flagon1/Office/fla_office12.jpg"
image bg fla_office13 = "mods/Flagon1/Office/fla_office13.jpg"


#Setting up events and conditions

init:
    $ event("fla_office1", "act == 'office' and behavior > 10", event.choose_one('office'), priority=200)
    $ event("fla_office2", "act == 'office' and morale > 25", event.choose_one('office'), priority=200)
    $ event("fla_office3", "act == 'office' and inhibition < 90", event.choose_one('office'), priority=200)
    $ event("fla_office4", "act == 'office' and inhibition < 60 and deviance > 20", event.choose_one('office'), priority=200)
    $ event("fla_office5", "act == 'office' and behavior > 50 and morale > 50", event.choose_one('office'), priority=200)
    $ event("fla_office6", "act == 'office' and pda_rules == 'pda_bdsm'", event.choose_one('office'), priority=200)
    $ event("fla_office7", "act == 'office' and deviance > 75", event.choose_one('office'), priority=200)
    $ event("fla_office8", "act == 'office' and inhibition < 25 and deviance > 75", event.choose_one('office'), priority=200)
    $ event("fla_office9", "act == 'office' and deviance > 75 and inhibition < 25 and uniform == 'nude_uniform'", event.choose_one('office'), priority=200)
    $ event("fla_office10", "act == 'office' and deviance > 20 and inhibition < 70 and uniform == 'sexy_uniform'", event.choose_one('office'), priority=200)
    $ event("fla_office11", "act == 'office' and deviance > 75 and inhibition < 25", event.choose_one('office'), priority=200)
    $ event("fla_office12", "act == 'office' and deviance > 75", event.choose_one('office'), priority=200)
    $ event("fla_office13", "act == 'office' and deviance > 40", event.choose_one('office'), priority=200)

label fla_office1:

    scene bg fla_office1 with fade
    "As you walk to your office, you are glad to see the halls filled with happy students."
    $ morale +=1
    return

label fla_office2:

    scene bg fla_office2 with fade
    "You look out your window to see a blushing girl hand-delivering a love note."
    return

label fla_office3:

    scene bg fla_office3_1 with flash
    "You leave your office and smack right into a student. You both go down and end up in a compromising position."

    if deviance < 30:
        scene bg fla_office3_2
        girl "EEEEEEEEEEEEK!"
        pov "Sorry! Sorry! Sorry!"
        $ morale -=1
    else:
        scene bg fla_office3_3
        girl "Ooooh, [povTitle][povLastName]! You're so bold!"
        pov "Ha Ha! Sorry about that! Let me help you up."
        $ morale +=1
    return

label fla_office4:

    scene bg fla_office4 with fade
    "Looks like these two girls had a little accident on the stairs. Fortunately, no one seems hurt."
    $ inhibition -=1
    return

label fla_office5:

    scene bg fla_office5 with fade
    girl "And while the school has made great strides in the last few months, we still have a long way to go!"
    girl "I'm sure I can count on all of you to give our principal your full support!"
    "The assembly bursts into cheers."
    $ morale +=1
    $ behavior +=1
    if renpy.random.randint(1, 3) == 1:
        $ reputation += 1
    return

label fla_office6:

    $ r=renpy.random.randint(1, 5)
    image bg fla_office6 = ConditionSwitch("r==1","mods/Flagon1/Office/fla_office6_1.jpg","r==2","mods/Flagon1/Office/fla_office6_2.jpg","r==3","mods/Flagon1/Office/fla_office6_3.jpg","r==4","mods/Flagon1/Office/fla_office6_4.jpg","r==5","mods/Flagon1/Office/fla_office6_5.jpg")

    scene bg fla_office6 with fade
    "A quick check of the detention room shows that things seem to be going well."
    girls "Aaaah, AAaaah, AAAAAAAAAAAAH YES!"
    $ behavior +=2
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance+= 5
    return

label fla_office7:

    $ r=renpy.random.randint(1, 3)
    image bg fla_office7 = ConditionSwitch("r==1","mods/Flagon1/Office/fla_office7_1.jpg","r==2","mods/Flagon1/Office/fla_office7_2.jpg","r==3","mods/Flagon1/Office/fla_office7_3.jpg")

    scene bg fla_office7 with fade
    "With your student's help, the paperwork has become much less of a burden."
    $ deviance +=1
    return

label fla_office8:

    scene bg fla_office8 with fade
    "This student is helping you make a new educational video for health class."
    girl "And as you, AH!, insert the vibrator be sure to tweak the nipple..."
    return

label fla_office9:

    scene bg fla_office9 with fade
    "These girls have come to your office to show off their uniforms."
    if renpy.random.randint(1, 3) == 1:
        $ deviance+= 5
    return

label fla_office10:

    scene bg fla_office10 with fade
    "Your teachers are enjoying No Pants Day, the greatest of all days."
    $ inhibition -=1
    return

label fla_office11:

    scene bg fla_office11 with fade
    girl "And as we move into the future *pant* *pant* it's important to remember the importance of... of..."
    girl "I'm cumming! CUMMMING! YEEEEEEEEEES!"
    $ inhibition -=1
    $ deviance +=1
    return

label fla_office12:

    scene bg fla_office12 with fade
    teacher "All right, boys. You got the highest marks on the test so here's your reward!"
    guy "Yay!"
    return

label fla_office13:

    scene bg fla_office13 with fade
    "It's important to know how to safely use equipment."
    teacher "All right, it's important to make sure the dildo is properly lubricated before use. I want you to drop your panties while I suck on this a bit."
    $ deviance +=1
    return