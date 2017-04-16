python:
    random_event_day = renpy.randomint(1, 6)     # Once a week, random day.
    random_event_level = renpy.randomint(1, random_event_max_level)
# At end of ever event?
# random_event_max_level =- random_event_level

#init:
    #$ event("morning_building_upgrade", "act == 'new_day' and 3 >= random_event_level", event.choose_one('new_day'),event.only(), priority=20)


label morning_building_upgrade:
    # Random building calc. Maybe from planning?
    if building_level > 0:
        "A wealthy businessman offers to upgrade [building].\nIt's a good offer but it might be bad for your reputation."
    else:
        "A wealthy businessman offers to build a [building].\nIt's a good offer but it might be bad for your reputation."
    menu:
        "Accept" if building_level > 0:
            "You accept the offer and [building] has been upgraded to [building_level].\n"

        "Accept" if building_level == 0:
            "You accept the offer and [building] has been built.\n"

        "Decline":
            "You politly decline the offer."


label morning_ruckus:
    "Your students have been making a ruckus by [calculate based on stats - Pop culture references?]. This results in bad reputation for [school_name]."

label morning_ruckus2:
    "Some students from other schools have came by and casused trouble by starting fights and flirting with the girls."

label morning_ruckus3:
    "Some of [school_name] students started a fight just outside school."
    if security > 2:
        "Security intervined and broke it up before anything bad happend."
    menu:
        "Give the students detention":
            pass
        "Ignore it":
            pass

label morning_student_letter:
    "Some students have written a letter to thank you for the work done to [school_name]. It also mentions their wish to do their best as well."


label morning_media:
    "[school_name] was mentioned in [media] due to [achievement/excellence/etc.] in [stat]. This have resulted in [population/reputation/etc.]."

label morning_other_school:
    "[A nearby school have been closed due to/A nearby school have been forced to close due to] [reason], this gives you the opportunity to welcome students to transfer to [school_name]. This might cause a stir while the new students settle in."
    menu:
        "Let everyone transfer":                                                                      # +population -morale
            pass
        "Let the most [random.choice(intelligent, sporty, arty (++))] transfer":                      #  +population +stat -morale -behaviour
            pass
        "Decline":
            "You decline the offer."

label morning_latest_thing:
    "Students have started [random thing] and it's becoming \"the latest thing\". As principal you decide to:"
    menu:
        "Support it":
            pass
        "Suppress it":
            pass
        "Ignore it":
            pass
