##########################################################
#
#                       Nurse Lia
#
# The school nurse, she's free-spoken, upbeat and flirty.
# She cares deeply for her little sister Marie who's a
# student at Ashford.
#
##########################################################

define lia_outfit = 'nurse'          # This can be 'nurse', 'casual', 'undies' or 'nude'.
define lia_points = 0
define lia_last_choice = 0

define lia = Character('Nurse Lia', color="#AF90A4")

# Sprites
image nurse_lia smile                  = "characters/lia_foster/nurse_lia_smile.png"
image nurse_lia smile_blush            = "characters/lia_foster/nurse_lia_smile_blush.png"
image nurse_lia happy                  = "characters/lia_foster/nurse_lia_happy.png"
image nurse_lia happy_blush            = "characters/lia_foster/nurse_lia_happy_blush.png"
image nurse_lia blush                  = "characters/lia_foster/nurse_lia_blush.png"
image nurse_lia blink                  = "characters/lia_foster/nurse_lia_blink.png"
image nurse_lia angry                  = "characters/lia_foster/nurse_lia_angry.png"
image nurse_lia sad                    = "characters/lia_foster/nurse_lia_sad.png"
image nurse_lia surprised              = "characters/lia_foster/nurse_lia_surprised.png"
image nurse_lia surprised_blush        = "characters/lia_foster/nurse_lia_surprised_blush.png"

image casual_lia smile                 = "characters/lia_foster/casual_lia_smile.png"
image casual_lia smile_blush           = "characters/lia_foster/casual_lia_smile_blush.png"
image casual_lia happy                 = "characters/lia_foster/casual_lia_happy.png"
image casual_lia happy_blush           = "characters/lia_foster/casual_lia_happy_blush.png"
image casual_lia blush                 = "characters/lia_foster/casual_lia_blush.png"
image casual_lia blink                 = "characters/lia_foster/casual_lia_blink.png"
image casual_lia angry                 = "characters/lia_foster/casual_lia_angry.png"
image casual_lia sad                   = "characters/lia_foster/casual_lia_sad.png"
image casual_lia surprised             = "characters/lia_foster/casual_lia_surprised.png"
image casual_lia surprised_blush       = "characters/lia_foster/casual_lia_surprised_blush.png"

image undies_lia smile                 = "characters/lia_foster/undies_lia_smile.png"
image undies_lia smile_blush           = "characters/lia_foster/undies_lia_smile_blush.png"
image undies_lia happy                 = "characters/lia_foster/undies_lia_happy.png"
image undies_lia happy_blush           = "characters/lia_foster/undies_lia_happy_blush.png"
image undies_lia blush                 = "characters/lia_foster/undies_lia_blush.png"
image undies_lia blink                 = "characters/lia_foster/undies_lia_blink.png"
image undies_lia angry                 = "characters/lia_foster/undies_lia_angry.png"
image undies_lia sad                   = "characters/lia_foster/undies_lia_sad.png"
image undies_lia surprised             = "characters/lia_foster/undies_lia_surprised.png"
image undies_lia surprised_blush       = "characters/lia_foster/undies_lia_surprised_blush.png"

image nude_lia smile                   = "characters/lia_foster/nude_lia_smile.png"
image nude_lia smile_blush             = "characters/lia_foster/nude_lia_smile_blush.png"
image nude_lia happy                   = "characters/lia_foster/nude_lia_happy.png"
image nude_lia happy_blush             = "characters/lia_foster/nude_lia_happy_blush.png"
image nude_lia blush                   = "characters/lia_foster/nude_lia_blush.png"
image nude_lia blink                   = "characters/lia_foster/nude_lia_blink.png"
image nude_lia angry                   = "characters/lia_foster/nude_lia_angry.png"
image nude_lia sad                     = "characters/lia_foster/nude_lia_sad.png"
image nude_lia surprised               = "characters/lia_foster/nude_lia_surprised.png"
image nude_lia surprised_blush         = "characters/lia_foster/nude_lia_surprised_blush.png"

# Events
image lia_office1                      = "characters/lia_foster/events/lia_office1.png"
image lia_office2                      = "characters/lia_foster/events/lia_office2.png"
image lia_office3                      = "characters/lia_foster/events/lia_office3.png"
image lia_office4                      = "characters/lia_foster/events/lia_office4.png"

init:
    $ event("lia_office_medical_supplies", "act == 'office' and not first_week", event.once(), event.only(), priority=1)
    $ event("lia_office1", "act == 'office' and lia_points >= 0 and lia_points < 5", event.choose_one('office'), event.depends("lia_office_medical_supplies"))
    $ event("lia_office2", "act == 'office' and lia_points >= 5 and lia_points < 10", event.choose_one('office'), event.depends("lia_office1"))
    $ event("lia_office3", "act == 'office' and lia_points >= 10 and lia_points < 20", event.once(), event.depends("lia_office2"))
    $ event("lia_office4", "act == 'office' and lia_points >= 10 and lia_points < 20", event.once(), event.depends("lia_office3"))
    $ event("lia_night1", "act == 'night' and lia_points >= 5", event.once(), priority=90)
    $ event("lia_night2", "act == 'night' and lia_points >= 15", event.once(), event.depends("lia_night1"), priority=90)
    $ event("lia_night3", "act == 'night' and lia_points >= 20", event.once(), event.depends("lia_night2"), priority=90)

    #The povGender == 'female' ones:
    #$ event("office_introduction_female", "act == 'office' and povGender == 'female'", event.once(), event.only(), priority=1)


label lia_office_medical_supplies:
    scene office with fade
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
            pov "With face like yours I have no doubt about it."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "*giggle* I'm sorry [povTitle] [povLastName], but I think I need to get back to my office."
            pov "I think I want you to stay."
            lia "Aww, maybe another time.\nBye bye principal!"
            "Hmm, she came by just to chat..?"
            $ lia_points += 2
    return


label lia_office1:
    scene office with fade
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

        "So what's on your mind?" if lia_last_choice != 1:
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
            pov "Haha, I'm sorry, I can't do that. I have neither wife nor husband."
            lia "Well, I have a {i}friend{/i} that's perfect for you. She happens to be single and has a weak point for people like you."
            pov "People {i}like me{/i}? Could her name be {i}Lia{/i}?"
            $ renpy.show(lia_outfit+"_lia happy")
            lia "Oh, do you hear that? Seems like they need me at the office."
            pov "I hear nothing..?"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Vibrate is a single girls best friend. Trust me on that.\nBye bye [povFirstName]!"
            $ lia_points += 2
            $ lia_last_choice = 1

        "Look at that eye candy!" if lia_last_choice != 2:
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "I could say the same about you [povTitle] [povLastName]."
            pov "Honestly, I would rather look at you than myself."
            lia "*giggle* I have noticed. It's the nurse outfit right?"
            pov "To be honest Lia, I am sure you would look great in any outfit."
            $ renpy.show(lia_outfit+"_lia happy")
            lia "I will make sure to always keep an \"outift\" on then. Shame, it's quite relaxing to slip out of it now and then."
            pov "Haha, Isn't birthday suit considered an \"outfit\"?"
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Oh principal, are you trying to get me undressed?"
            pov "What if I am?"
            lia "*giggle* I guess I better get back to my office before this turns into something... More interesting...\nMhm, see you around principal."
            $ lia_points += 2
            $ lia_last_choice = 2

    return


label lia_office2:
    scene office with fade
    "*knock knock*"
    pov "Please come in Lia."
    $ renpy.show(lia_outfit+"_lia surprised")
    lia "How did you know it was me?"
    menu:
        "You are the only one who knocks on my door" if lia_last_choice != 'a':
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Am I?\n..."
            pov "At least you are the only beautiful nurse that knocks on my door."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Do you want it to stay that way?"
            pov "Are you asking me if I want another beautiful nurse? Do you have a sister?"
            lia "*giggle* Nope, I will always be your beautiful nurse. And let's keep my sister out of this."
            pov "I'm fine with that. For now."
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Regarding a new nurse or my sister?"
            pov "Why not both?"
            $ renpy.show(lia_outfit+"_lia blink")
            lia "Why not nope?"
            $ lia_points += 1
            $ lia_last_choice = 'a'

        "So what's on your mind today?" if lia_last_choice != 'b':
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
            $ lia_last_choice = 'b'

        "I'm psychic!" if lia_last_choice != 'c':
            lia "*giggle* So you already know why I'm here?"
            pov "Indeed, after our last meeting you fell deeply in love with me and now you are trying to get closer to me."
            $ renpy.show(lia_outfit+"_lia smile_blush")
            lia "Hmm, not that far from the truth *giggle*"
            pov "I know, so what can I do for the schools cutest nurse today?"
            $ renpy.show(lia_outfit+"_lia smile")
            lia "If Ashford actually had more then one nurse I might been happy to hear that."
            pov "Maybe I should employ some competition for you?"
            lia "Or you should employ other tactics when trying to complement me *giggle*"
            pov "Roses are red, violets are blue, you're hot as hell"
            lia "Hahaha, that was horrible!"
            $ lia_points += 2
            $ lia_last_choice = 'c'

    "*Bzzzz*"
    lia "Ah, they need me at the office, talk to you later!\nBye bye!"
    return


label lia_office3:
    scene office with fade
    "Your door smashes open and you see..."
    $ renpy.show(lia_outfit+"_lia sad")
    lia "Hey [povFirstName]!"
    pov "Um, hey Lia, what's--"
    lia "Sorry, but can you do me a favor?\nI really-"
    if new_game_plus:
        menu:
            "Let her finish":
                pass

            "I'm gonna let you finish...":
                pov "Yo Lia, I’m really happy for you and Imma let you finish, but I am the best principal of all time. OF ALL TIME."
                $ renpy.show(lia_outfit+"_lia surprised")
                lia "Huh?"
                pov "Word."
                lia "Erhm, eh..."
                pov "So... what brings you to my door?"
                lia "Eh, yeah... Oh, yeah."
                pov "... Yeah?"

    $ renpy.show(lia_outfit+"_lia sad")
    lia "I really need to get away from work for a few hours, would that be ok?"
    menu:
        "Sure":
            pov "No problem Lia, "
            $ renpy.show(lia_outfit+"_lia smile")
            lia "Thanks [povFirstName], you're a real lifesaver!\nI got to go directly, see you later!"

        "Calm down, what's the problem?":
            lia "The hospital called, m-my sister..."
            pov "Your sister is at the hospital?\nWhat happend?"
            "You can see Lia's eyes starting to tear up."
            lia "I-I don't know, I'm next of kin... S-so they called me b-but they didn't say what it was all about, so I really need to get to the hospital!"
            menu:
                "Call a cab for Lia":
                    "You pick up your phone quickly calling the number for a cab."
                    lia "[povFirstName] what are you-"
                    pov "Give me a second Lia, I'm calling a cab for you."
                    $ renpy.show(lia_outfit+"_lia smile")
                    "???" "Welcome to Quick Cabs, how can I help you?"
                    pov "This is principal [povName] of Ashford Academy, we have a emergency and I need a cab here as soon as possible."
                    "Phone" "I could have one there in 25 minutes, is that okay?"
                    pov "No sir, I am sorry but that isn't quick.\n{b}I need a cab within the next five minutes or Ashford Academy will revoke the current contract with Quick Cabs.{/b}"
                    "Phone" "Oh, y-yes, I see, we just got a cab free, I will send it over."
                    pov "Good. Thank you."
                    $ renpy.show(lia_outfit+"_lia smile_blush")
                    lia "Oh, thanks [povFirstName], really, thank you!"
                    pov "Don't worry and tell the driver to put it on the school tab.\nNow Lia, go check up on your sister."
                    lia "You're a hero [povFirstName], thanks again!"

                "I understand, you're free to go.":
                    $ renpy.show(lia_outfit+"_lia smile")
                    lia "Thanks for understanding.\nI gotta go directly, see you later [povFirstName]!"
                    pov "See you Lia and good luck."

                "I'm sorry, but we need you here.":
                    $ renpy.show(lia_outfit+"_lia angry")
                    lia "You can't seriously do this [povFirstName], it's my sister for fuck's sake!"
                    pov "I understand that you're upset, but-"
                    lia "But fuck you, I'm leaving."
                    pov "Lia, calm-"
                    lia "Don't you tell me to calm down, get the fuck out of my way."
                    menu:
                        "Leave her be":
                            "You watch Lia storm out of your office."
                            $ lia_points = 0

                        "Hit her":
                            $ renpy.hide(lia_outfit+"_lia")
                            with vpunch
                            "*slap*"
                            "You watch Lia fall to the floor."
                            lia "Ah...\n*sob*...*sob*...\nW-why...*sob*"
                            "Lia lays on the floor in tears."
                            pov "Don't talk back to me Lia."
                            lia "*sob* *sob*"
                            menu:
                                "Give her a lesson":
                                    pov "I'm sorry Lia, but you have to know your place.\nNow, how should we do this..?"
                                    menu:
                                        "Rape her" if povGender == "male":
                                            "You walk over to the still sobbing Lia."
                                            pov "Here, give me your hands."
                                            lia "Fuck you [povFirstName] *sob*\nI-I'm leav-"
                                            "As Lia tries to stand up you grab her hand and pull her back to the ground."
                                            pov "Stay dow-"
                                            lia "Fuck off and get your filthy hands off me!"
                                            "You put your hand around her neck and force her down."
                                            lia "A-hh... Nugh...\nArgh..."
                                            pov "Take it easy Lia, I know you want this..."
                                            "She continues her feisty struggle until she gets out of breath.\nAs soon as her body starts to dwindle you release your grip and tie her hands to your table-leg."
                                            lia "*gasp*\nW-what..?"
                                            "You look her deep in the eyes as you remove both her clothes and yours."
                                            pov "That's some sexy black lingerie Lia.\nI like it."
                                            scene lia_office1
                                            lia "Stop it... You fucking pervert!"
                                            pov "You have a better body then I expected, you sure keep in shape Lia."
                                            lia "No, no, [povFirstName]! Stop it!\nGet your disgusting dick away from me!"
                                            pov "It feels nice just grinding it against your pussy like this, don't you agree?"
                                            lia "Don't you dare, I'll fucking kill you"
                                            "You slowly try to push your dick into her pussy.\nShe's tight, as expected by someone getting raped.\nBut there is some moisture... So you decide to force it in."
                                            scene lia_office2
                                            lia "Ahh..!\nNo... Why?!\nFuc-ah..."
                                            pov "You have a nice and tight little pussy Lia. If you keep this up I might forgive you for storming into my office..."
                                            lia "F-ahh... Fuck you!\nMhm... N-no-oh..."
                                            pov "Aww, you really are getting into to this huh?\nLet me take a picture, smile!"
                                            lia "Noo..! P-please...\n[povFirstName]... Ah!"
                                            pov "You got really tight, maybe I should take some more photos, might be a good gift for your sister at the hospital!"
                                            lia "Noo, no, please!\nAh, s-stop it!"
                                            pov "Mhm, here comes the first load!"
                                            scene lia_office3
                                            lia "Ah! Noo, not inside!\nAhh... *sob*"
                                            pov "Don't worry, there's more what that came from, I'll make sure to enjoy your body as much as possible."
                                            "You continue to fuck Lia and fill her up until she's barely consious."
                                            scene lia_office4
                                            pov "Ah, great work Lia... Your pussy really sucked out every last dropp.\nGood girl."
                                            lia "..."

                                        "Let Jack rape her" if not hit_the_road_jack:
                                            "You walk over to your phone and call Jack."
                                            jack_drake "Hiya, s'up?"
                                            pov "I need you to get over here Jack, I have... A present for you."
                                            jack_drake "Sweet, I'll be over in a jiffy."
                                            "You walk over to the still sobbing Lia."
                                            pov "Here, give me your hands."
                                            lia "Fuck you [povFirstName] *sob*\nI-I'm leav-"
                                            "As Lia tries to stand up you grab her hand and pull her back to the ground."
                                            pov "Stay dow-"
                                            lia "Fuck off and get your filthy hands off me!"
                                            "You put your hand around her neck and force her down."
                                            lia "A-hh... Nugh...\nArgh..."
                                            pov "Behave.\nOkay, Lia?"
                                            "She continues her feisty struggle until she gets out of breath.\nAs soon as her body starts to dwindle you release your grip and tie her hands to your table-leg."


                                        "Let a student rape her" if hit_the_road_jack:
                                            "You walk over to your phone and call Jack"

                                    scene black
                                    "You take some additional photos before you untie Lia and help her up..."
                                    scene office
                                    show nude_lia sad
                                    pov "You did a good job Lia.\nLet's keep this our secret and I will keep these photos a secret as well."
                                    lia "..."
                                    pov "Good girl, now go clean yourself up and get back to work and I promise you your sister will never have to see her sister like this."
                                    $ lia_points = -1

                                "Leave for lunch":
                                    pov "I'll leave for lunch now, when I'm back I expect you to be back at work."
                                    lia "..."
                                    pov "Good girl."
                                    "You pat Lia's head and leave."
                                    $ lia_points = 0
    return


label lia_office4:
    scene office with fade
    "Knock knock."
    pov "Please come in."
    $ renpy.show(lia_outfit+"_lia happy")
    lia "Hey [povFirstName]!"
    pov "Hey there Lia, how's your sister?"
    $ renpy.show(lia_outfit+"_lia blink")
    lia "Ah, yes, she's great!\nShe apparently hurt her ankle and fell, so nothing serious."
    pov "That's good news, you where really worried about her last time."
    $ renpy.show(lia_outfit+"_lia blush")
    lia "Yeah, yeah, she's my sister after all. It's horrible how the hospital couldn't say anything when they called.\nGot me all worried over nothing..."
    pov ""
    return

label lia_night1:
    scene park_evening with fade
    show casual_lia surprised at center
    lia "Oh, hello there [povLastName]!"
    pov "Hey there Lia, on your way home?"
    show casual_lia smile_blush
    lia "*giggle* Yeah, something like that..."
    menu:
        "Oh, mysterious!":
            show casual_lia happy
            lia "A girl has to have secrets you know..."
            pov "I sure do, but I'd love to find them out!"
            show casual_lia smile
            lia "Careful or one day you might *giggle*"
            pov "I wouldn't mind finding out more about you Lia."
            show casual_lia smile_blush
            lia "Do I want to know what you had in mind? *giggle*\n"
            pov "Anyhow, where are you heading?"
            show casual_lia blink
            lia "...\nI am meeting someone..."
            pov "Oh! Do I have competition?"
            show casual_lia smile_blush
            lia "*giggle* Obviously, a young woman as attractive as me have {i}sooo{/i} many men falling for me."
            pov "I wouldn't be surprised if you had."
            show casual_lia blush
            lia "You are kind [povFirstName]...\nI am actually meeting my sister... Oh, I should get going!"
            pov "I don't mind if you stay."
            show casual_lia smile
            lia "Ah, but my sister would!\n See you around!"

        "Unusual seeing you in casual clothing":
            lia "So [povFirstName], what outfit do you prefer? *giggle*"
            menu:
                "Nurse outfit" if povGender == "male":
                    show casual_lia smile_blush
                    lia "Haha, you're just like the students, I never knew grown men had the same thing for nurses."
                    pov "You can't meet many men then."
                    lia "I meet you, Isn't that enough? *giggle*"
                    pov "Obviously, I am {i}the{/i} alpha male!"
                    show casual_lia happy
                    lia "...\nAlpha {i}mail{/i}?"
                    pov "Yes, obviously {i}mail{/i}, by no account male."
                    show casual_lia smile_blush
                    lia "*giggle* I'm not so sure you're alpha, you have to prove that... Sometime..."
                    pov "Well... What are you doing tonight?"
                    lia "Oh! Damn, I got to go!\nSee you around [povFirstName]!"

                "Nurse outfit" if povGender == "female":
                    show casual_lia smile_blush
                    lia "Haha, your just like the male students, I never an adult woman like you would prefer a nurse outfit."
                    pov "Is there something wrong with that?"
                    show casual_lia happy
                    lia "No, no, no, not at all-hahaha"
                    pov "It feels like you are making fun of me."
                    show casual_lia smile_blush
                    lia "Would it be better if I made fun with you? *giggle*"
                    pov "Depends on what kind of fun."
                    lia "I think that you know what kind of fun I'm talking about."
                    pov "Maybe I do, maybe I don't."
                    lia "Aww, oh well..\nIt was nice talking to you [povFirstName], but I have to go, see you around!"
                    pov "Bye bye Lia."

                "Neither":
                    show casual_lia sad
                    lia "Naaw, you're no fun [povLastName], has it been a tough day?"
                    pov "You wouldn't know..."
                    lia "I am all ears if you need to talk [povFirstName]."
                    show casual_lia smile
                    pov "Thank you for that."
                    lia "...\nI need to go, see you around [povFirstName]!"
                    $ lia_points -= 2

                "This one":
                    show casual_lia smile_blush
                    lia "*giggle* Now I know what to wear when you ask me out [povFirstName]!"
                    pov "Haha, don't ruin the surprise Lia!"
                    show casual_lia happy_blush
                    lia "Regarding you asking me out or what I would wear?"
                    pov "Both!"
                    show casual_lia smile_blush
                    lia "If you keep this up it could get both messy and awkward at work."
                    pov "Do I seem to mind?"
                    lia "*giggle* I better get going...\nBye bye principal!"
    $ lia_points += 1
    return


label lia_night2:
    scene park_evening with fade
    "???" "Hey, [povFirstName]!"
    show casual_lia happy at center
    lia "*pant* Ah, hey there!"
    menu:
        "Have you become my personal stalker?":
            show casual_lia smile
            lia "*giggle* Maybe I have...\nAnyhow what are you up to [povFirstName]?"
            pov "The usual, tricking my stalkers into the park to... take care of them!"
            lia "Wow, that sound scary...\nDoes that mean you will {i}take care{/i} of me?"
            pov "Who knows, a professional wouldn't tell you!"
            show casual_lia smile_blush
            lia "Well [povTitle] [povFirstName], maybe I wouldn't mind if you {i}took care{/i} of me."
            pov "Do you say that to all men you run into in the park?"
            show casual_lia sad
            lia "...\n....\nNo..."
            pov "Hey, dont take it so serious Lia."
            lia "No...\nDon't worry, but I have to go now...\nI'll see you at work [povLastName]."

        "Fancy meeting you here!" if povGender != "female":
            show casual_lia smile
            lia "Same to you [povTitle]!"
            pov "So what is a beautiful woman doing in the park so late?"
            lia "The usual, looking for a handsome stranger."
            pov "And then you ran into your boss?"
            lia "You call it boss, I call it a handsome acquaintance."
            pov "I hope that's better than a stranger then."
            lia "Mom always told me to stay clear of strangers, especially those who try to give you candy."
            pov "So Lia, you want some candy?"
            show casual_lia happy
            lia "*giggle* Oh, please [povTitle] [povLastName], please give me some candy!"
            pov "I think you better listen to your mom more!"
            show casual_lia smile
            lia "*giggle* Or what will happen? You will drag me into a bush and rape me?"
            menu:
                "That does sound tempting!":
                    show casual_lia smile_blush
                    lia "*giggle* I better... watch out then...\n[povTitle] [povFirstName], {i}I wouldn't want something like that to happen.{/i}"
                    pov "You sure get my blood pumping Lia."
                    lia "Maybe I should leave you before both of us...\nEnd up in the bushes over there..."
                    pov "Well Lia, I still have candy."
                    "You can see Lia licking her lips..."
                    lia "*giggle* It sounds tempting as well, but I need to meet my sister..."
                    pov "Another time then?"
                    lia "Maybe another time...\nI'll see you around [povFirstName]..."
                    pov "Bye bye Lia."
                    $ lia_points += 1

                "Don't joke about that!":
                    show casual_lia sad
                    lia "Always so serious..."
                    pov "You shouldn't joke about such things."
                    lia "Ah, okay..."
                    pov "Good."
                    show casual_lia smile
                    lia "I guess I better get going, I got stuff to do [povLastName].\nSee you."
                    $ lia_points -= 1

        "Fancy meeting you here!" if povGender == "female":
            lia "Same to you [povTitle]!"
            pov "So what is a beautiful woman doing in the park so late?"
            show casual_lia smile_blush
            lia "I could ask you the same!"
            pov "Haha, always so flirty."
            lia "I guess that goes for both of us!"
            pov "Is it really safe for a girl like you to wander the park so late?"
            show casual_lia sad
            "You can feel how Lia is moving in closer to you."
            lia "I think so, have anything happend here recently?"
            pov "Don't worry, I was just asking Lia."
            show casual_lia blush
            lia "Don't scare me like that!"
            pov "Sorry, sorry!"
            lia "...\nHmm, maybe sis shoudln't walk here after school..."
            pov "Hey, I said sorry, I am sure it's perfectly safe here."
            show casual_lia smile
            lia "Thanks, but still...\nIf anything would happen to my sister..."
            pov "Hey It was just a question, is your sister a student at Ashford?"
            lia "Yeah..."
            pov "I'll talk to school security to take a extra walk towards the park and you can feel safe."
            show casual_lia happy
            lia "Really? Will you do that for me?"
            pov "Maybe not for {i}you{/i}, but for {i}you{/i} and the students."
            show casual_lia smile_blush
            lia "*giggle* thanks [povFirstName]!"
            pov "Well, I scared you to begin with..."
            lia "I'm sorry, but I'll have to run, I don't want my sister to wait for me in the dark!"
            pov "I understand Lia, I will see you at school!"
            lia "Thanks again!\nBye bye!"
            $ lia_points += 1
    return


label lia_night3:
    scene park_evening with fade
    if marie_points < 1:
        "You see Lia happily talking and gesturing with a younger girl."
    else:
        "You see Lia and Marie happily talking and gesturing."
    show casual_lia happy at center
    show casual_marie smile at right
    lia "Oh hey, [povFirstName]!\nOn your way home?"
    pov "Yepp, work is all done for today."
    show casual_lia smile
    lia "By the way, this is my sister Marie, I don't think you have met?"
    if marie_points > 0:
        "You see a faint smile and a glimmer in Marie's eyes."
    menu:
        "Nice meeting you Marie":
            marie "Nice meeting you [povTitle] [povLastName]."
            pov "A student at Ashford I presume?"
            marie "That's correct [povTitle] Principal."
            lia "Hey, relax Marie, we're out of school right now so there's no need to be so formal."
            show casual_marie smile_blush
            marie "..."
            pov "Don't worry about it.\nSo what are you girls up to?"
            show casual_lia smile
            lia "We where just meeting up before heading home, Marie is living with me you know."
            pov "Oh, I didn't know that, so how is that working out for you?"
            show casual_lia happy
            lia "Well, I'll let Marie answer that one *giggle*"
            show casual_marie blush
            marie "Umm, [povTitle] [povLastName] it's working out quite good, we both behave and..."
            lia "*giggle* Marie, relax, [povFirstName] isn't interrogating you!"
            pov "No no, I was just curious, you're not in trouble or anything.\nWell, Lia might be, but not you Marie."
            show casual_marie surprised
            marie "W-what? What did she do?\n...\nOh, you're joking?"
            pov "Haha, yes I am. Sorry about that."
            show casual_marie sad
            show casual_lia smile
            lia "Hey there sis, don't get so down over a joke. [povFirstName] is just pulling your leg."
            show casual_marie smile
            marie "Right...\nBack to your question, it's nice living with sis."
            lia "See, who's the best sister in the whole wide world?"
            marie "I only have one sister so it have to be that one."
            lia "And the name of that, single best sister in the whole wide world is..?"
            show casual_lia happy_blush
            marie "It's you, Lia.\nHappy?"
            lia "Aww, I love you too sis!\nYou're sooo cute Marie!"
            menu:
                "I concur.":
                    show casual_marie smile_blush
                    lia "On the loving or cute part?"
                    marie "Argh!\nStop joking around about me!"
                    show casual_lia smile
                    pov "Well, I guess you'll never hear the answer on that then."
                    marie "...\nMaybe I don't want to hear the answer..."

                "I love you too!" if new_game_plus:
                    lia "That escalated quickly! What about me [povFirstName]?!"
                    marie "Argh!\nStop joking around about me!"
                    show casual_lia smile

                "I love you too!" if not new_game_plus:
                    lia "Aww, don't fall madly in love with your students, you could get in trouble for that [povFirstName]!"
                    marie "Argh!\nStop joking around about me!"
                    show casual_lia smile

                "You're sooo cute!":
                    show casual_lia happy_blush
                    lia "Isn't she! Just like her big sister!"
                    marie "Argh!\nStop joking around about me!"
                    show casual_lia smile

            lia "Aww, my cute little sister, want me to tell [povFirstName] to be nice to you?"
            marie "Come'on Lia, cut it...\nShouldn't we be heading home?"
            show casual_lia happy
            lia "Oh, look at the time! I guess we should.\nNice meeting you here [povFirstName], see you around!"
            marie "...\nBye principal."
            pov "Bye bye girls."

        "Beautiful just like your sister":
            show casual_marie smile_blush
            marie "Oh, *giggle* I... Um-"
            show casual_lia blink
            lia "Hey, be nice [povFirstName], it's my sister."
            show casual_lia smile
            pov "Don't worry I'm not going after your sister Lia, I have you, right?"
            show casual_marie surprised
            marie "Wh-what!? Are you, like dating?"
            show casual_lia smile_blush
            menu:
                "Yepp":
                    show casual_marie smile_blush
                    show casual_lia happy_blush
                    lia "Cut it out...\nMarie is innocent and will belive anything you tell her..."
                    pov "Are we not dating?"
                    show casual_lia smile_blush
                    lia "That's not-!\nAh, stop joking around [povFirstName]..."
                    show casual_marie smile
                    marie "Well you two sure seem to know each other, maybe I should go home and give you some space?"
                    lia "No, no, don't listen to everything he says! [povFirstName] is just..."
                    pov "Confessing his unreplied love?"
                    lia "Oh my! Look at the time, we need to go home! Marie let's go."
                    show casual_marie smile_blush
                    marie "But, eh, what? *giggle* Sis, take it easy!"
                    lia "No, no, let's go, it's getting late!"
                    pov "I guess I'll see you girls at school, good night!"
                    lia "No, I mean, yeah, nice meeting you, bye bye Principal..."
                    marie "Nice meeting you [povTitle] [povLastName]!"
                    $ lia_points += 2

                "Maybe":
                    show casual_marie happy
                    pov "Well, I've tried getting closer to your sister Marie, but she can be a tricky cookie you know."
                    marie "Haha, I sure know, but don't you worry [povTitle] [povLastName], I can tell you all about Lia and she'll be yours in no time!"
                    show casual_lia happy_blush
                    lia "Hey guys, I'm here, cut it out!"
                    show casual_marie smile
                    marie "Come on sis, you need someone like [povLastName]!"
                    show casual_lia smile_blush
                    lia "*giggle* Need? You're not talking about yourself now?"
                    show casual_marie smile_blush
                    marie "I-um-eh, no, no! I couldn't, [povTitle] [povLastName] is the Principal of Ashford!"
                    show casual_lia smile
                    lia "*giggle* I know Marie, and I'm just kidding with you."
                    pov "You girls are cute getting all worked up like that."
                    show casual_marie smile_blush
                    if povGender == "male":
                        marie "W-well, hrm, I'm not getting worked up at all, it's my sister who goes for older men, not me!"
                    else:
                        marie "W-well, hrm, I'm not getting worked up at all, it's my sister who goes for someone older, not me!\nAnd I'm interested in guys!"
                    show casual_lia surprised
                    lia "*giggle* Sorry sis? Who said \"I want someone older and more mature\"?"
                    show casual_marie blush
                    marie "N-no, no, you must have misheard sis *giggle* I wouldn't say that!"
                    pov "Don't worry girls, there's enough of me for both of you."
                    show casual_lia smile_blush
                    lia "But maybe one of us want's you for herself? *giggle*"
                    marie "That \"one of us\" would not be me, s-sorry [povTitle] [povLastName]..."
                    pov "Anyhow, thanks for today girls, but I need to get home. Work tomorrow you know."
                    show casual_lia smile
                    lia "Yeah, same here actucally.\nOh well, bye bye [povFirstName]!"
                    marie "Um, bye bye [povTitle] [povLastName]!"
                    $ lia_points += 1

                "Nope":
                    show casual_lia sad
                    lia "..."
                    show casual_marie sad
                    marie "I'm sorry [povTitle] [povLastName], I shouldn't have asked that."
                    pov "No worries, right Lia?"
                    lia "Yeah, there's no worry at all."
                    show casual_lia smile
                    marie "I see, well it would make sense that you are already be married and have a family."
                    pov "I'm sorry?"
                    marie "Oh, your not married and have a family?"
                    pov "No I am not."
                    marie "Oh, I am terribly sorry [povTitle] [povLastName]!"
                    show casual_marie smile
                    lia "*giggle* You're to cute Marie, but I think we need to head home."
                    marie "It was nice meeting you [povTitle] [povLastName]."
                    pov "Same to you both, good night girls."
                    lia "Night Principal."
                    $ lia_points -= 1

            $ marie_points += 1

        # TODO: Marie + Lia stuff
        "I've met Marie before" if marie_points > 0:
            show casual_marie blush
            lia "Oh, really? Why didn't you tell me Marie?"
            marie "Eh, ah, we just ran into each other at school...\nRight [povTitle] [povLastName]?"
            pov "Yeah, something like that."
    return


label lia_test:
    scene office with fade
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
