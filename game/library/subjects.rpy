init python:
    def random_topic(topic):
        if topic == "academics":
            if academics >= 100:
                return renpy.random.choice(["Jungian psychology", "astrophysics", "quorum sensing", "recursive cortical networks"])
            if academics >= 75:
                return renpy.random.choice(["differential equations", "Freudian psychology", "linguistics", "particle physics"])
            if academics >= 50:
                return renpy.random.choice(["linear algebra", "sociology", "organic chemistry", "environmental science", "political science"])
            if academics >= 25:
                return renpy.random.choice(["history", "languages", "literature", "math", "art", "physics"])
            else:
                return renpy.random.choice(["the alphabet", "reading", "plus and minus"])

    def random_fact(topic):
        if topic == "academics":
            if True:
                return renpy.random.choice([
                    "The first central bank was established in Sweden in 1668 followed by England in 1694.",
                    "plus and minus"
                    ])
            else:
                return renpy.random.choice(["the alphabet", "reading", "plus and minus"])

    def haiku(topic):
        if True:
            return renpy.random.choice([
                "I drop on my knees\nHe commands me to suck it\nAnything for him.",
                "You control my head\nand I will control my tongue\nplease shove it deeper.",
                "I look up at him\nMy lips wrapped around his cock\nNeed your cum so bad.",
                'I’ve been good today\n"Please master let me taste it\nbegging like a slut."',
                '"Just for my princess"\ntender words making her cum\nwhile she sucks your cock.',
                'He forces his cock\nchocking the little cum slut\ntaking every drop.',
                'Head tickling the throat\nagile lips licking the shaft\ntake it like a champ.',
                'This is her first cock\ntake her mouth virginity\nconquer her cunt next.'
                ])

    def random_quote():
        if True:
            answer = "John Quincy Adams"
            question = "If your actions inspire others to dream more, learn more, do more and become more, you are a leader."
        elif True:
            answer = "Millard Fillmore"
            question = "An honorable defeat is better than a dishonorable victory."
        elif True:
            answer = "James Garfield"
            question = "Be fit for more than the thing you are now doing. Let everyone know that you have a reserve in yourself; that you have more power than you are now using. If you are not too large for the place you occupy, you are too small for it."
        elif True:
            answer = "Teddy Roosevelt"
            question = "We must dare to be great; and we must realize that greatness is the fruit of toil and sacrifice and high courage."
        elif True:
            answer = "William Taft"
            question = "Don't write so that you can be understood, write so that you can't be misunderstood."
        elif True:
            answer = "Calvin Coolidge"
            question = "Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb ... Persistence and determination alone are omnipotent."
        elif True:
            answer = "Franklin D. Roosevelt"
            question = "Yours is not the task of making your way in the world, but the task of remaking the world which you will find before you."
        elif True:
            answer = "Mahatma Gandhi"
            question = "You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty."
        elif True:
            answer = "Mahatma Gandhi"
            question = "It is unwise to be too sure of one's own wisdom. It is healthy to be reminded that the strongest might weaken and the wisest might err."
        elif True:
            answer = "Mahatma Gandhi"
            question = "In reality there are as many religions as there are individuals."
        elif True:
            answer = "Bob Dylan"
            question = "What's money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do."
        elif True:
            answer = "Herbert Simon"
            question = "A wealth of information creates a poverty of attention."
        elif True:
            answer = "Stephen Hawking"
            question = "I have noticed that even people who claim everything is predetermined and that we can do nothing to change it, look before they cross the road."
        elif True:
            answer = "Albert Einstein"
            question = "I am by heritage a Jew, by citizenship a Swiss, and by makeup a human being, and only a human being, without any special attachment to any state or national entity whatsoever."
        elif True:
            answer = "Albert Einstein"
            question = "Nationalism is an infantile sickness. It is the measles of the human race."
        elif True:
            answer = "Albert Einstein"
            question = "My passionate sense of social justice and social responsibility has always contrasted oddly with my pronounced lack of need for direct contact with other human beings and human communities. I am truly a 'lone traveler' and have never belonged to my country, my home, my friends, or even my immediate family, with my whole heart; in the face of all these ties, I have never lost a sense of distance and a need for solitude..."
        elif True:
            answer = "Albert Camus"
            question = "There will be no lasting peace either in the heart of individuals or in social customs until death is outlawed"
        elif True:
            answer = "George Bernard Shaw"
            question = "The reasonable man adapts himself to the world; the unreasonable one persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable man."
        elif True:
            answer = "Isaac Asimov"
            question = 'There is a cult of ignorance in the United States, and there always has been. The strain of anti-intellectualism has been a constant thread winding its way through our political and cultural life, nurtured by the false notion that democracy means that "my ignorance is just as good as your knowledge.'
        elif True:
            answer = "W.C. Fields"
            question = "A man's got to believe in something. I believe I'll have another drink."
        elif True:
            answer = "Thomas Jefferson"
            question = "A lady who has been seen as a sloven or slut in the morning will never efface the impression she has made, with all dress and pageantry she can afterwards involve herself in…"
        elif True:
            answer = "Friedrich Nietzsche"
            question = "That which does not kill us makes us stronger."