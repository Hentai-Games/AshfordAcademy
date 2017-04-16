image bg alt_class1 = "mods/alt1/alt_class1.jpg"

image bg alt_library1 = "mods/alt1/alt_library1.png"
image bg alt_library2 = "mods/alt1/alt_library2.png"
image bg alt_library3 = "mods/alt1/alt_library3.png"

image bg alt_gym0 = "mods/alt1/alt_gym0.jpg"
image bg alt_gym1 = "mods/alt1/alt_gym1.png"
image bg alt_gym2 = "mods/alt1/alt_gym2.png"

#Setting up events and conditions
init:
    $ event("alt_class1", "act == 'class' and deviance > 50 and inhibition < 50", event.choose_one('class'), priority=150)

    $ event("alt_library1", "act == 'library' and inhibition > 40", event.choose_one('library'), priority=200)
    $ event("alt_library2", "act == 'library' and inhibition < 90", event.choose_one('library'), priority=190)
    $ event("alt_library3", "act == 'library' and inhibition < 80 and deviance > 20", event.choose_one('library'), priority=180)

    $ event("alt_gym0", "act == 'gym' and deviance > 20 and inhibition < 60", event.choose_one('gym'), priority=150)
    $ event("alt_gym1", "act == 'gym' and deviance > 25", event.choose_one('gym'), priority=170)
    $ event("alt_gym2", "act == 'gym' and deviance > 20", event.choose_one('gym'), priority=150)

label alt_class1:
    scene bg alt_class1 with fade
    "Immoral behaviour! I love it!"
    if renpy.random.randint(1,4) == 1:
        $ reputation -= 1
        $ deviance += 1
    else:
        $ deviance += 5
        $ deviance += 1
    return

label alt_library1:
    scene bg alt_library1 with fade
    pov "Aww, are you alright? You should be more careful!"
    $ morale += 1
    return

label alt_library2:
    scene bg alt_library2 with fade
    "While passing through the library, you suddenly come across a young girl who apparently fell asleep in the middle of studying."
    menu:
        "She must be exhausted.":
            pov "I don't have the heart to wake her up."
            $ morale += 1
            $ academics -= 1
        "This is no place for napping!":
            pov "What's this?"
            girl "Uh... oh... I must have dozed off."
            pov "As long as you are at school premises, you follow our code young lady."
            girl "I - I'm sorry [povTitle]... I was just so tired."
            pov "From now on I expect you to go to bed early on weekdays. Less fooling around after school is the right medicine."
            girl "Y - yes sir."
            $ deviance -= 1
            $ behavior += 1
        "Hey, sleepy head, it's time to wake up." if evil_points < 1:
            girl "U...uhm..."
            pov "Wow, you were really out of it."
            girl "Oh [povTitle]... I'm so sorry. I had the strangest dream."
            pov "Now now, that's alright. We all get tired, don't we?"
            girl "I - I guess... But, you're so kind. I really shouldn't be sleeping while in school."
            pov "Nothing to worry about. What kind of dream was it?"
            girl "Oh... Umm..."
            pov "Ha - ha, I think I can guess..."
            girl "*giggle*"
            $ morale += 1
            $ inhibition -= 1
    return

label alt_library3:
    "While walking in the library you hear a slurping sound, you decide to find out where it comes from."
    scene bg alt_library3 with fade
    "Suddenly you see the source. It seems like they haven't noticed you yet."
    menu:
        "Leave them":
            "You decide not to spoil the fun and quickly walk away."
            $ inhibition -= 1
            $ deviance += 1
            if renpy.random.random() > 0.5:
                $ deviance += 5
        "Give them a warning":
            $ inhibition += 1
            $ deviance -= 1
            $ behavior += 1
            "You give them both a very strict warning and they both promise that it will never happen again."
        "Expel them." if pda_rules == 'pda_expulsion':
            $ inhibition += 3
            $ deviance -= 3
            $ behavior += 4
            "You bring them to your you office and you quickly sign the paperwork. You tell them to clean up and get their stuff before leaving the school."
    return

label alt_gym0:
    "As you enter the gym you can hear a faint but familiar sound and in your curiosity you search for the source."
    scene bg alt_gym0 with fade
    girl "Ah! P-please... Mhmm... This is... Ah! W-w-wrong..."
    "Oh, girls these days... This is why I love my job."
    $ deviance +=1
    $ morale -=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5
    return

label alt_gym1:
    "In the locker room, you suddenly hear a squeaking noise. Carefully, you peek around the corner and see a young couple at it."
    scene bg alt_gym1 with fade
    girl "Shh, I thought I heard something!"
    guy "Huh?"
    menu:
        "Stand real still":
            "After a while they carry on their business. You leave real silently."
            $ deviance += 1
        "Make some noise":
            "You knock on one of the lockers and hear how they quickly gather their clothes."
            $ deviance -= 1
        "Burp" if new_game_plus == True:
            girl "What the hell!?"
            guy "H- hello?"
            pov "* giggle *"
            $ deviance -= 1
    return

label alt_gym2:
    scene bg alt_gym2 with fade
    "Looks like you arrived just in time to witness how the schools cheerleading actually works."
    if renpy.random.randint(1,2) == 1:
        $ morale += 1
    else:
        $ inhibition -= 1
    return
