# TODO: Relocate and sort variables and functions.

define school_name = "Ashford Academy"

define balancer = 1    # This variable is used to balance the building bonuses
define evil_points = 0
define good_points = 0

# Is "new game +" available?
define persistent.new_game_plus = False
define difficulties = {
    'easy':{
        'reputation':10,
        'monthy_event_bonus':1,
        'cash':500,
        'population':100,
        'balancer':1,
        'weekly_planning_focus_bonus':0.8,
        'weekly_planning_focus':2},
    'normal':{
        'reputation':10,
        'monthy_event_bonus':1,
        'cash':500,
        'population':100,
        'balancer':2,
        'weekly_planning_focus_bonus':0.6,
        'weekly_planning_focus':2},
    'hard':{
        'reputation':10,
        'monthy_event_bonus':1,
        'cash':250,
        'population':75,
        'balancer':3,
        'weekly_planning_focus_bonus':0.6,
        'weekly_planning_focus':1}
    }

init python:

    def starting_school(school):
        globals()['reputation'] = 10
        globals()['monthy_event_bonus'] = 1

        globals()['Morale_change'] = globals()['morale']
        globals()['Behavior_change'] = globals()['behavior']
        globals()['Academics_change'] = globals()['academics']
        globals()['Artistery_change'] = globals()['artistery']
        globals()['Athletics_change'] = globals()['athletics']
        globals()['Deviance_change'] = globals()['deviance']
        globals()['Inhibition_change'] = globals()['inhibition']

        globals()['cash_change'] = globals()['cash']
        globals()['population_change'] = globals()['population']
        globals()['reputation_change'] = globals()['reputation']

    def new_game(game_mode):
        globals()['reputation'] = 10
        globals()['monthy_event_bonus'] = 1

        # Multiply starting stats:
        if(game_mode=='easy'):
            globals()['cash'] = 500
            globals()['population'] = 100
            globals()['balancer'] = 1
            globals()['weekly_planning_focus_bonus'] = 0.8
            globals()['weekly_planning_focus'] = 2

        elif(game_mode=='normal'):
            globals()['cash'] = 500
            globals()['population'] = 100
            globals()['balancer'] = 2
            globals()['weekly_planning_focus_bonus'] = 0.6
            globals()['weekly_planning_focus'] = 2

        elif(game_mode=='hard'):
            globals()['cash'] = 250
            globals()['population'] = 75
            globals()['balancer'] = 3
            globals()['weekly_planning_focus_bonus'] = 0.6
            globals()['weekly_planning_focus'] = 1

        globals()['Morale_change'] = globals()['morale']
        globals()['Behavior_change'] = globals()['behavior']
        globals()['Academics_change'] = globals()['academics']
        globals()['Artistery_change'] = globals()['artistery']
        globals()['Athletics_change'] = globals()['athletics']
        globals()['Deviance_change'] = globals()['deviance']
        globals()['Inhibition_change'] = globals()['inhibition']

        globals()['cash_change'] = globals()['cash']
        globals()['population_change'] = globals()['population']
        globals()['reputation_change'] = globals()['reputation']

        # Send the first tutorial message - or not?

label new_game:
    scene black
    if povName == '':
        info "Please enter your name."
        if not renpy.variant('touch'):
            $ povFirstName = renpy.input("What is your first name?", length=16) or "Principal"
            $ povLastName = renpy.input("What is your last name?", length=16) or "Shinryu"

        elif renpy.variant('touch'):
            info "What is your first name? (leave blank for 'Principal')"
            $ input_header = 'First name:'
            call inputter from _call_inputter
            $ povFirstName = input_text or "Principal"
            info "What is your last name? (leave blank for 'Shinryu')"
            $ input_header = 'Last name:'
            $ text_group = 1
            $ input_text = ''
            call inputter from _call_inputter_1
            $ povLastName = input_text or "Shinryu"

        else:
            $ povFirstName = "Principal"
            $ povLastName = "Shinryu"

        if povFirstName == 'debug':
            python:
                side_menu += [
                    {"title": "Debug screen",       "menu": "debug_screen",         "yoffset": 160, "xoffset": 4,   "xminimum": 170},
                    {"title": "Inventory",          "menu": "inventory",            "yoffset": 191, "xoffset": 4,   "xminimum": 170},
                    {"title": "Mod List",           "menu": "mod_list",             "yoffset": 253, "xoffset": 4,   "xminimum": 170},
                    {"title": "Notify",             "menu": "acad_gain",            "yoffset": 284, "xoffset": 4,   "xminimum": 170}
                    ]
            #layout.button("Office", clicked=ShowMenu('office_screen'),yoffset=222,xoffset=5,xminimum=170)
        $ povName = povFirstName+" "+povLastName
    $ new_game(game_mode)
    jump new_game_story
