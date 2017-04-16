# This is a playground, trying out more dynamic and generic events.

label generic_class:

    scene classroom with fade

    if uniform == "nude_uniform" and inhibition > 50:
        $ renpy.show("female_student_1 "+uniform+" sad")
        "One of the girls is standing in a corner trying to cover up some of her body."
        "Well, sooner or later {i}she will accept{/i} the rules of our fine school."

    elif behavior < renpy.random.randint(0,35):
        $ renpy.show("female_student_1 "+uniform+" angry")
        "As you walk into a class room you hear the angry roar of a young girl."
        if deviance > 10 and inhibition > 90:
            girl "You can't touch me like that! Keep your filthy hands to yourself!"
        elif deviance > 25:
            "You did WHAT?! {w} AND WITH MY BEST FRIEND!?"
        else:
            "Just let me be you stupid piece of shit!"
        "At least I can be happy that it's not me she's angry with."

    elif morale > renpy.random.randint(10,100):
        $ renpy.show("female_student_1 "+uniform+" happy")
        "As you enter the classroom you hear a few girls giggle and joke with each other."
        girl "*giggle* You're sooo funny!"

    elif academics > renpy.random.randint(20,100):
        $ renpy.show("female_student_1 "+uniform+" normal")
        $ topic = random_topic("academics")
        "As you enter the classroom you hear some students discuss a class."
        girl "Yeah, so do any of you understand [topic]?"
        if behavior > renpy.random.randint(25,95):
            girl "I kinda get the big picture but yeah, I think I need to study some more, anyone wanna give me a hand?"
        elif deviance > renpy.random.randint(25,100):
            girl "Maybe I should just give it up and get down on my knees, if ya know what I mean *giggle*"
        else:
            girl "Maybe I should just give it up and take a break instead."

    else:
        $ renpy.show("female_student_1 "+uniform+" normal")
        if deviance > 90 and inhibition < 10:
            "A bunch of girls are talking loudly about their latest sexual experiences."
            if renpy.random.randint(1,2) == 1:
                girl "Yeah, I know, I got THREE at the same time, I didn't think they would fit at first, but Mhmm... It felt sooooo good, I tell ya!"
            else:
                girl "... and while his father was doing me he came in and saw everything! *giggle* I had to let him do both me and my BFF at the same time to make him forgive me."

        if deviance > 70 and inhibition < 30:
            "A few girls are talking loudly about their latest sexual experiences."
            if renpy.random.randint(1,2) == 1:
                girl "So I had to go a whole day with that vibrating inside me *giggle* I was sooo wet and actually came several times during class!"
            else:
                girl "... but my sister isn't into it at all. I really have tried to get her along but she's like sooo shy all the time, I just don't understand."

        elif deviance > 50 and inhibition < 50:
            "A few girls are talking about their latest sexual experiences."
            if renpy.random.randint(1,2) == 1:
                girl "Really?! That's like a whole class of girls doing it in the shower room!\n...But it sounds kinda hot."
            else:
                girl "You did it too?! Wow, it's crazy no one saw us doing it, it was just outside of school too!"

        elif deviance > 30 and inhibition < 70:
            "A few girls are talking about their latest sexual experiences."
            if renpy.random.randint(1,2) == 1:
                girl "After that he put it in my butt! It was kinda weird at first, but I really liked it!"
            else:
                girl "Yeah, I know... But he really appreciate it when I dress like that and I kinda like how all the guys tries to catch a glimpse..."

        elif deviance > 10 and inhibition < 90:
            "A few girls are talking about their latest sexual experiences."
            if renpy.random.randint(1,2) == 1:
                girl "Mhmm, yeah, it tasted a bit weird in the beginning, but after a while you kinda start liking it."
            else:
                girl "I know what you're saying, you have to, like, really really like him to let him do that!"
        else:
            "You hear some students chatting about boys and sports."

        "Girls these days..."
    return

label test:

    scene pool with fade
    show amane
    "<3"
    return
