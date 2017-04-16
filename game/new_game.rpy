# TODO: Relocate and sort variables and functions.

# Initialize the default values of some of the variables used in the game.
define cash = 0
define cash_change = 0
define population = 0
define population_change = 0
define reputation = 0
define reputation_change = 0

# "Hidden" variables for planning
define beh_focus = 0
define academics_focus = 0
define art_focus = 0
define ath_focus = 0
define sex_focus = 0

define evil_points = 0
define good_points = 0

define buyable = ''
define buyable_cost = [ ]

# Is "new game +" available?
$ persistent.new_game_plus = False

define difficulties = ['normal', 'normalOld', 'hard']

# Define game_mode = 'normal' -- TODO: Remove and replace.
init python:

    def new_game(game_mode):
        globals()['reputation'] = 10

        # Starting stats:
        if(game_mode=='normal'):
            globals()['cash'] = 500
            globals()['population'] = 100
            globals()['balancer'] = 1

        elif(game_mode=='normalOld'):
            globals()['cash'] = 500
            globals()['population'] = 100
            globals()['balancer'] = 2

        elif(game_mode=='hard'):
            globals()['cash'] = 250
            globals()['population'] = 75
            globals()['balancer'] = 3

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
            call inputter
            $ povFirstName = input_text or "Principal"
            info "What is your last name? (leave blank for 'Shinryu')"
            $ input_header = 'Last name:'
            $ text_group = 1
            $ input_text = ''
            call inputter
            $ povLastName = input_text or "Shinryu"

        else:
            $ povFirstName = "Principal"
            $ povLastName = "Shinryu"
        
        $ povName = povFirstName +" "+povLastName
    $ new_game(game_mode)
    jump new_game_story
