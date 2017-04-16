##########################################################
#
#                       Michèle Chandelier
#
# A exchange student first met in the office regarding
# a school transfer.
# French nationality with a tendency to use french phrases. 
# 
# Will be used as comic relief and most likely non-sexual
# character teasing with nudity.
#
##########################################################


# We use this variable to keep track on her feelings towards the player. 
define michele_chandelier_points = 0
define michele_chandelier_outfit = ''          # This can be '' (nothing), 'short_skirt_', 'cosplay_' or 'sexy_uniform_'.

# We load images to be shown and the variations.
image michele_chandelier normal         = "characters/hina_amagi/hina_amagi_normal.png"
image michele_chandelier happy          = "characters/hina_amagi/hina_amagi_normal.png"
image michele_chandelier blush          = "characters/hina_amagi/hina_amagi_normal.png"
image michele_chandelier angry          = "characters/hina_amagi/hina_amagi_normal.png"
image michele_chandelier surprised      = "characters/hina_amagi/hina_amagi_normal.png"
image michele_chandelier sad            = "characters/hina_amagi/hina_amagi_normal.png"



# TODO: V
define michele_chandelier = Character('Michèle Chandelier', color="#F8BA87")

# Events
init:
    $ event("hina_amagi_in_class1", "act == 'class' and hina_amagi_points > 0 and hina_amagi_points < 7 and planning_day > 2", event.choose_one('class'))



label michele_chandelier_transfer:
    
    "*Knock knock*"
    scene bg office with fade
    "Someone is knocking on the office door."
    menu:
        "It's open, come on in!":
            pass
        "...":
            pass
    "The door slowly opens and a young woman with a face filled with confusion walks in."
    pov "Hello Miss."
    if povGender == 'female':
        "???" "Allô! Can you be Mme. [povLastName]?"
    else:
        "???" "Allô! Can you be principal?"
    pov "Yes, indeed I am."
    "Her face lights up and are big smile covers her face."
    michele_chandelier "Ah, très bien! Je suis Michèle, Michèle Chandelier!"
    menu:
        "Sorry?":
            pass
        "Je ne parle pas français.":
            pass
        "J'aime française moi petit fille!" if new_game_plus == true:
            michele_chandelier "C'est merveilleux!"
            pov "A vrai dire je ne parle pas français."
            michele_chandelier "Vraiment?"
            pov "Yes, really."
    
    michele_chandelier "Ah, désolé! I am still not used to anglaise. I came here regarding a transfert."
    pov "A transfer? To Ashford Academy?"
    michele_chandelier "Oui oui! Could this be done?"
    pov "When did you send in the papers and who did you talk to?"
    michele_chandelier "I haven't sent any papers. Can we do it today?"
    pov "Miss Chandelier, you mus-"
    michele_chandelier "Michèle!"
    pov "Michèle, you must understand that these things take time. You can't just walk in and transfer to a new school."
    michele_chandelier "Très bien! Can I start next week?"
    pov "I don't think you understand. Transfer papers takes time. First we need grades and verification from your old school, a written request for a transfer signed by your legal guardian and then we need to review and approve."
    michele_chandelier "Si bien... Not next week?"
    menu:
        "No, I'm sorry.":
            michele_chandelier ":("
            return
        "We could have an interview ":
            pass
    
    pov "So you want to transfer to Ashford?"
    michele_chandelier "Mais oui!"
    
    
    ## Glossary ##
    # parfait    = perfect
    # Mme        = Mrs
    # Bonsoir!   = Good evening
    # C'est bon  = It's good
    # bon        = good, well
    # si bien    = so
    # Oui        = yes
    # aussi      = also
    # D'accord   = Okay!
    # Au viol!   = rape!
    # très       = very
    # arret      = stop
    # Vraiment?  = Really?
    # avec moi   = with me?
    # Bonne nuit = good night
    # modèle nue = nude model
    # toi et moi = you and me
    # petit file = little girl
    # écoute moi = listen to me
    # pauvre petit = poor little
    # a vrai dire = tell the truth
    # Ouvre la bouche = open your mouth
    # Mais non chérie = But not sweetheart
    # Mais il est joli! = But it is pretty!
    # Elles sont belles! = They are beautiful!
    # Merci à l'academie = Thank you to the Academy





