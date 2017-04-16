init -1 python hide:
###############################################
#               Ashford Academy
#               Version:
    config.version = "15.05.09"
    config.developer = True
    config.rollback_enabled = False
#
#
###############################################

# The variable we store for the entered name of the main char and a DynamicCharacter that has the same stored in povName.
define povFirstName = ""
define povLastName = ""
define povName = ""                             # povName = povFirstName + povLastName
define povGenders = ["male", "female", "futa"]
define povGender = "male"
define povTitles = ["Mr.", "Mrs."]
define povTitle = "Mr."
define povBdsmTitles = ["Master", "Mistress"]
define povBdsmTitle = "Master"
define pov = DynamicCharacter("povName", color=(150, 0, 32, 255))
define game_mode = "normal"

init python:
    # Library "Math", it's used in some calculations such as "pay_day" and the "gallery".
    # Library "Time" is used in the "gallery".
    # Library "datetime" is used for christmas countdown events.
    import math
    import time
    import datetime

    # For mods - How to add new Gender & Title
    #povGenders.append("Alien")
    #povTitles.append("President")

    # Variables for unlockable scenes
    new_game_plus = False
    start_day_with_gin = False

    # TODO: How we handle stat/inhibition minimum/maximum should be changed.
    inhibition_min = 75
    lower_inhibition_level = 1

    # Notification system
    new_messages = 0
    mail = []
    reply_screen = False

    if persistent.mod_disable_original_stats == False:
        # Stats that will be shown on the GUI, all stats will also need a *_change stat. TODO: There is a better way to handle/auto generate these.
        register_stat("Morale",     "morale",       0, 5, 100)
        register_stat("Behavior",   "behavior",     5, 0, 100)
        register_stat("Academics",  "academics",    10, 0, 100)
        register_stat("Artistery",  "artistery",    10, 0, 100)
        register_stat("Athletics",  "athletics",    10, 0, 100)
        register_stat("Deviance",   "deviance",     0, 0, 100)
        register_stat("Inhibition", "inhibition",   75, 100, 100)

    # Here we set up the default values for the day planner.
    morning_act     = None
    afternoon_act   = None
    evening_act     = None

########################################################
#   This will most likely be moved at some point in time

    # Image dissolve Transitions.
    circleirisout   = ImageDissolve("images/ui/transitions/circleiris.png", 1.0, 8)
    circleirisin    = ImageDissolve("images/ui/transitions/circleiris.png", 1.0, 8, reverse=True)
    flash           = Fade(.25, 0, .75, color="#fff")
    # Content options - can be changed in the options screen. Will be used mostly for third-party content.
    persistent.content_list = dict(googirls=False, tentacles=False, catgirls=False, loli=False)

########################################################
#   Sets the choices of the daily planner.
#   @returns nothing
    def setDayPlannerChoices():
        dp_period("Morning", "morning_act")
        dp_choice("Office", "office")
        if (building_sports_field > 0):
            dp_choice("Sports field", "sports_field")
        if (building_gym > 0):
            dp_choice("Gym", "gym")
        if (building_library > 0):
            dp_choice("Library", "library")

        dp_period("Afternoon", "afternoon_act")
        dp_choice("Class", "class",)
        if (building_pool > 0):
            dp_choice("Pool", "pool")
        if (building_cafeteria > 0):
            dp_choice("Cafeteria", "cafeteria")

        dp_period("Evening", "evening_act")
        dp_choice("School grounds", "school_grounds")
        if (building_dormitory > 0):
            dp_choice("Dormitory", "dormitory")
        if (building_bath > 0):
            dp_choice("Bath", "bath")
        if (building_club_rooms > 0):
            dp_choice("After school Clubs", "club_rooms")
        return


########################################################
#
#  Game start
#  The script here is run as soon as you press new game.
#
########################################################

label new_game_plus:
    if renpy.has_label(persistent.mod_custom_new_game_plus):
        $ renpy.jump(persistent.mod_custom_new_game_plus)
    else:
        scene black
        if new_game_plus:
            "New game plus content unlocked."
        if povGender == "":
            "Please choose your gender:"
            menu:
                "Male":
                    $ povGender = 'Male'
                    $ povTitle = "Mr."
                    $ povBdsmTitle = "Master"
                "Female":
                    $ povGender = 'Female'
                    $ povTitle = "Ms."
                    $ povBdsmTitle = "Mistress"

# This is the entry point into the game. Find more info in story.rpy.
label start:
    if renpy.has_label(persistent.mod_custom_new_game):
        $ renpy.jump(persistent.mod_custom_new_game)
    else:
        jump new_game

# This is the label that is jumped to at the start of a day. Also, check available classes.
label day:

    # Increment the day and add any new buildings to the list.
    $ new_day()


##############################################################################
# Here's some story triggers and game over stuff
#
# See game_over.py in /screens for more information.

    # Default school background.
    scene Ashford_Academy with circleirisout


    $ act = 'new_day'
    $ today = weekday_name[total_days%7]
    $ normalize_stats()
    call events_run_period from _call_events_run_period

#
# Here ends the story and game over stuff.
#
##############################################################################


    # It's possible that we will be skipping the day, if one
    # of the events in the new_day jumped to skip_next_period. If
    # so, we should skip the day.
    if check_skip_period():
        jump night


    # See what classes we have and what needs to be done to access them. Every 7th day is planning day with weekly bonus.
    # The 1st of every month we have monthly extra planning.
    # Remember, at least one class in each period is req. to actually "play/plan" each day.

    $ setDayPlannerChoices()

    # Now, we call the day planner, which may set the act variables
    # to new values. We call it with a list of periods that we want
    # to compute the values for.
    call day_planner(["Morning", "Afternoon", "Evening"]) from _call_day_planner


    # We process each of the three periods of the day, in turn.
label morning:

    $ normalize_stats()
    # We set the "change" value so we can visualize the change as in red/green numbers on the UI.
    python:
        Morale_change = morale
        Behavior_change = behavior
        Academics_change = academics
        Artistery_change = artistery
        Athletics_change = athletics
        Deviance_change = deviance
        Inhibition_change = inhibition

        cash_change = cash
        reputation_change = reputation
        population_change = population

    # Tell the user what period it is.
    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] morning"
    else:
        centered "[month_now] %(day)d: [today] morning"

    # Set these variables to appropriate values, so they can be
    # picked up by the expression in the various events defined below.
    $ period = "morning"
    $ act = morning_act

    # Ensure that the stats are in the proper range. (0-var.max)
    $ normalize_stats()

    # Execute the events for the morning.
    call events_run_period from _call_events_run_period_1

    # That's it for the morning, so we fall through to the afternoon.

label afternoon:

    # It's possible that we will be skipping the afternoon, if one
    # of the events in the morning jumped to skip_next_period. If
    # so, we should skip the afternoon.
    if check_skip_period():
        jump evening

    # The rest of this is the same as for the morning.
    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] afternoon"
    else:
        centered "[month_now] %(day)d: [today] afternoon"

    $ period = "afternoon"
    $ act = afternoon_act

    $ normalize_stats()

    call events_run_period from _call_events_run_period_2


label evening:

    # The evening is the same as the afternoon.
    if check_skip_period():
        jump night

    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] evening"
    else:
        centered "[month_now] %(day)d: [today] evening"

    $ period = "evening"
    $ act = evening_act

    $ normalize_stats()

    call events_run_period from _call_events_run_period_3


label night:

    # This is now the end of the day, and not a period in which normal events
    # can be run. We put some boilerplate end-of-day text in here.

    scene black with circleirisin
    centered "Night"

    $ act = 'night'
    call events_run_period from _call_events_run_period_4
    call events_end_day from _call_events_end_day
    $ normalize_stats()

    # And we jump back to day to start the next day. This goes
    # on forever, until an event ends the game.
    jump day


# This is a callback that is called by the day planner. One of the
# uses of this is to show the statistics to the user.
label dp_callback:

    $ display_stats()
    $ display_extra_stats()
    return


label after_load:
    # TODO: Make sure mail get loaded here as well.
    python:
        update_stat_min('inhibition', 100 - (lower_inhibition_level * 25))
    $ setDayPlannerChoices()

    return
