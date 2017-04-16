##########################################################
#
#                       Nurse Lia
#
# The school nurse.
#
##########################################################

define lia_outfit = 'nurse'          # This can be 'nurse', 'casual', 'undies' or 'nude'.
define lia_points = 0

define lia = Character('Nurse Lia', color="#AF90A4")

# Sprites
image nurse_lia smile                  = "characters/lia_foster/nurse_lia_smile.png"
image nurse_lia smile_blush            = "characters/lia_foster/nurse_lia_smile_blush.png"
image nurse_lia happy                  = "characters/lia_foster/nurse_lia_happy.png"
image nurse_lia blush                  = "characters/lia_foster/nurse_lia_blush.png"
image nurse_lia blink                  = "characters/lia_foster/nurse_lia_blink.png"
image nurse_lia angry                  = "characters/lia_foster/nurse_lia_angry.png"
image nurse_lia sad                    = "characters/lia_foster/nurse_lia_sad.png"
image nurse_lia surprised              = "characters/lia_foster/nurse_lia_surprised.png"

image casual_lia smile                  = "characters/lia_foster/casual_lia_smile.png"
image casual_lia happy                  = "characters/lia_foster/casual_lia_happy.png"
image casual_lia blush                  = "characters/lia_foster/casual_lia_blush.png"
image casual_lia blink                  = "characters/lia_foster/casual_lia_blink.png"
image casual_lia angry                  = "characters/lia_foster/casual_lia_angry.png"
image casual_lia sad                    = "characters/lia_foster/casual_lia_sad.png"
image casual_lia surprised              = "characters/lia_foster/casual_lia_surprised.png"

image undies_lia smile                  = "characters/lia_foster/undies_lia_smile.png"
image undies_lia happy                  = "characters/lia_foster/undies_lia_happy.png"
image undies_lia blush                  = "characters/lia_foster/undies_lia_blush.png"
image undies_lia blink                  = "characters/lia_foster/undies_lia_blink.png"
image undies_lia angry                  = "characters/lia_foster/undies_lia_angry.png"
image undies_lia sad                    = "characters/lia_foster/undies_lia_sad.png"
image undies_lia surprised              = "characters/lia_foster/undies_lia_surprised.png"

image nude_lia smile                  = "characters/lia_foster/nude_lia_smile.png"
image nude_lia happy                  = "characters/lia_foster/nude_lia_happy.png"
image nude_lia blush                  = "characters/lia_foster/nude_lia_blush.png"
image nude_lia blink                  = "characters/lia_foster/nude_lia_blink.png"
image nude_lia angry                  = "characters/lia_foster/nude_lia_angry.png"
image nude_lia sad                    = "characters/lia_foster/nude_lia_sad.png"
image nude_lia surprised              = "characters/lia_foster/nude_lia_surprised.png"

init:
    pass
    $ event("lia_office_medical_supplies", "act == 'office' and lia_points >= 0", event.once(), event.only(), priority=1)
    $ event("lia_office1", "act == 'office' and lia_points >= 0 and lia_points < 5", event.choose_one('office'), event.depends("lia_office_medical_supplies"))
    $ event("lia_office2", "act == 'office' and lia_points >= 5 and lia_points < 15", event.choose_one('office'), event.depends("lia_office1"))

    #The povGender == 'female' ones:
    #$ event("office_introduction_female", "act == 'office' and povGender == 'female'", event.once(), event.only(), priority=1)


label lia_office_medical_supplies:
    scene bg office with fade
    "*knock knock*"
    pov "Come in."
    $ renpy.show(lia_outfit+"_lia smile")
    lia "Hello [povName], do you have a minute?"
    menu:
        "No, I'm sorry, can you take it with Susan?":
            $ renpy.show(lia_outfit+"_lia sad")
            lia "Oh... Well, yeah...\nSorry for the intrusion. "
            pov "No worries."

        "What can I help you with?":
            lia "There is a lack of medical supplies and I was wondering if we could reschedule the next delivery to a earlier date."
            pov "What kind of supplies are we talking about?"
            lia "Most of them... The old administration gave us very little leeway."
            pov "Ah, the old administration... Bring me the pappers and I will see what can be done."
            $ renpy.show(lia_outfit+"_lia happy")
            lia "Thank you [povTitle] [povLastName]!"
            $ lia_points += 1

        "Anything for you Lia.":
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "*giggle* Such a smooth talker..."
            $ renpy.show(lia_outfit+"_lia smile")
            pov "Well a hard worker as you really deserves it. Only good girls get my praise."
            lia 'Jumping to conclusions are we? You barely know me and you still consider me a "good girl"?'
            pov "With face like yours I have no doubt it."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "*giggle* I'm sorry [povTitle] [povLastName], but I think I need to get back to my office."
            pov "I think I want you to stay."
            lia "Aww, maybe another time.\nBye bye principal!"
            "Hmm, she came by just to chat..?"
            $ lia_points += 2
    return


label lia_office1:
    scene bg office with fade
    "*knock knock*"
    pov "It's open, please come in."
    $ renpy.show(lia_outfit+"_lia smile")
    pov "Nurse Lia."
    lia "Principal [povFirstName]."
    menu:
        "So we are on first name basis now?":
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Are we not?"
            pov "Let's keep it professional shall we?"
            $ renpy.show(lia_outfit+"_lia sad")
            lia "Oh, you where serious?"
            pov "Indeed. So what did you have in mind?"
            lia "Nothing... Forgive me, duty is calling."
            $ lia_points -= 2

        "So what's on your mind?":
            lia "Nothing in particular, I just left some papers and decided to see if you where free."
            pov "A man is never truly free."
            lia "I'm happy to be a woman then, maybe I can free you? *giggle*"
            if [povGender] == "male":
                pov "Are you suggesting that I leave my wife for you?"
            elif [povGender] == "female":
                pov "Are you suggesting that I leave my husband for you?"
            else:
                pov "Are you suggesting that I leave my marriage for you?"
            $ renpy.show(lia_outfit+"_lia surprised")
            lia "First off are you married?! And in that case, yes! *giggle*"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            pov "Haha, I'm sorry, I can't do that. I have neither a wife nor husband."
            lia "Well, I have a {i}friend{/i} that's perfect for you. She happens to be single and has a weak point for people like you."
            pov "People {i}like me{/i}? Could her name be {i}Lia{/i}?"
            $ renpy.show(lia_outfit+"_lia happy")
            lia "Oh, do you hear that? Seems like they need me at the office."
            pov "I hear nothing..?"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Vibrate is a single girls best friend. Trust me on that.\nBye bye [povFirstName]!"
            $ lia_points += 2

        "Look at that eye candy!":
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "I could say the same about you [povTitle] [povLastName]."
            pov "Honestly, I would rather look at you then myself."
            lia "*giggle* I have noticed. It's the nurse outfit right?"
            pov "To be honest Lia, I am sure you would look great in any outfit."
            $ renpy.show(lia_outfit+"_lia happy")
            lia "I will make sure to always keep an \"outift\" on then. Shame, it's quite relaxing to slip out of it now and then."
            pov "Haha, Isn't birthday suit considered a \"outfit\"?"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Oh principal, are you trying to get me undressed?"
            pov "What if I am?"
            lia "*giggle* I guess i better get back to my office before this turns into something... More interesting...\nMhm, see you around principal."
            $ lia_points += 2

    return


label lia_office2:
    scene bg office with fade
    "*knock knock*"
    pov "Please come in Lia."
    $ renpy.show(lia_outfit+"_lia surprised")
    lia "How did you know it was me?"
    menu:
        "You are the only one who knocks on my door":
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Am I?\n..."
            pov "At least you are the only beautiful nurse that knocks on my door."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Do you want it to stay that way?"
            pov "Are you asking me if I want another beautiful nurse? Do you have a sister?"
            lia "*giggle* Nope, I will always be your beautiful nurse. And let's keep my sister out of this."
            pov "I fine with that. For now."
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Regarding a new nurse or my sister?"
            pov "Why not both?"
            $ renpy.show(lia_outfit+"_lia blink")
            lia "Why not nope?"
            $ lia_points += 1

        "So what's on your mind today?":
            lia "Oh, you wouldn't want to know *giggle*"
            pov "Is it that embarrassing?"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "I am sure you would love to know... but lets take that another time."
            pov "So what should I take today?"
            $ renpy.show(lia_outfit+"_lia happy")
            if [povGender] == "male":
                lia "You sir, are a flirty and handsome devil. That's a dangerous combination"
            elif [povGender] == "female":
                lia "Miss, for someone so flirty and beautiful as you I wonder where you hide all the men that fall for you."
            else:
                lia "[povFirstName], you are such a flirty smooth talker..."
            pov "I take that as a complement Lia."
            $ lia_points += 2

        "I'm psychic!":
            lia "*giggle* So you already know why I'm here?"
            pov "Indeed, after our last meeting you fell deeply in love with me and now you are trying to get closer to me."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Hmm, not that far from the truth *giggle*"
            pov "I know, so what can I do for the schools cutest nurse today?"
            $ renpy.show(lia_outfit+"_lia smile")
            lia "If Ashford actually had more then one nurse I might been happy to hear that."
            pov "Maybe I should employ some competition for you?"
            lia "Or you should employ other tactics when trying to complement me *giggle*"
            pov "Roses are red, violets are blue, your hot as hell"
            lia "Hahaha, that was horrible!"
            $ lia_points += 2

    "*Bzzzz*"
    lia "Ah, they need me at the office, talk to you later!\nBye bye!"
    return


label lia_test:
    scene bg office with fade
    $ renpy.show(lia_outfit+"_lia smile")
    lia "Hello [povName], did you miss me? "
    pov "Indeed I did."
    menu:
        "Casual":
            $ lia_outfit = 'casual'
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Like this?"

        "Undies":
            $ lia_outfit = 'undies'
            $ renpy.show(lia_outfit+"_lia blush")
            lia "Pervert..."

        "Nude":
            $ lia_outfit = 'nude'
            $ renpy.show(lia_outfit+"_lia blush")
            lia "As you wish..."
    return
