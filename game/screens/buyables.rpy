##############################################################################
# Buyables Menu
#
# Buy extra's by using the schools stats.
define buyable = ""
define buyable_pick = ""
define buyable_cost = [float('inf'), 0, 0, 0, 0, 0, 0]

##  Name: [M,B,A,A,A,D,I] + Reputation?
# "cost": [0,0,0,0,0,0,0]
define buyables = [
{"name": "sexy_uniform",                "requirement": "sexy_uniform == 0",                             "cost": [25,10,0,0,0,0,0],      "image": "buildings/sexy_uniform1.jpg",         "description": "All students are forced to wear a more revealing uniform.\n\nUnlocks sexy uniform dress code."},
{"name": "nude_uniform",                "requirement": "sexy_uniform > 0 and nude_uniform == 0",        "cost": [25,10,0,0,0,0,0],      "image": "buildings/nude_uniform.jpg",          "description": "Students are forced to go to school nude or in lingerie.\n\nUnlocks nude uniform dress code."},
{"name": "cheerleader_club",            "requirement": "False",                                         "cost": [0,0,0,0,0,0,0],        "image": "buildings/cheerleader_club.jpg",      "description": "Opens a cheerleader club for the students .\n\nAllows visiting the Cheerleader Club."},
{"name": "hyper_anatomic_body",           "requirement": "hyper_anatomic_body == 0",                      "cost": [0,0,0,0,0,3,0],        "image": "buildings/classrooms.jpg",            "description": "Anatomical models based on pornstars, since we all know that porn is {i}real{/i}. \n\nUnlocks hyper sexualized human models."},
{"name": "magic_accounting",            "requirement": "magic_accounting == 0",                         "cost": [5,5,5,5,5,0,0],        "image": "buildings/classrooms.jpg",            "description": "You don't know how, but it seems you can {i}always{/i} squeeze out some more cash from your budget. \n\nGives you 10% more money per month and level."},
{"name": "bdsm_detention",              "requirement": "bdsm_detention == 0",                           "cost": [0,0,0,0,0,30,0],       "image": "buildings/bdsm_detention.jpg",        "description": "If they don't listen, spank them. If they don't behave, make them behave.\n\nUnlocks BDSM detention."},
{"name": "no_detention",                "requirement": "no_detention == 0 and good_points > 0",         "cost": [0,0,0,0,0,0,0],        "image": "buildings/classrooms.jpg",            "description": "You know man, love is like the best thing, we should all spread love. \n\nUnlocks no detention."},
{"name": "lower_inhibition_level",      "requirement": "False",                                         "cost": [0,0,0,0,0,lower_inhibition_level*10,0], "image": "buildings/sexy_uniform2.jpg",         "description": "Help the students become more relaxed in regards to their body. \n\nLowers minimum inhibition to [var]."},
{"name": "unlocked",                    "requirement": "False",                                         "cost": [0,0,0,0,0,0,0],        "image": "",                                    "description": "Congratulations, you unlocked a new buyable!"},
{"name": "",                            "requirement": "False",                                         "cost": [0,0,0,0,0,0,0],        "image": "",                                    "description": "Here you can buy special upgrades for your school. Most extras will be available directly except for new classes, they will be available the next day."},
]

screen buyables_screen:
    imagemap:
        ground "images/ui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                for buyable in buyables:
                    if eval(buyable['requirement']):
                        ui.imagebutton("images/ui/"+buyable['name']+"_idle.png", "images/ui/"+buyable['name']+"_hover.png", clicked=[SetVariable("buyable_pick", buyable['name'])])
                if lower_inhibition_level < 4:
                    ui.imagebutton("images/ui/lower_inhibition"+str(lower_inhibition_level)+"_idle.png", "images/ui/lower_inhibition"+str(lower_inhibition_level)+"_hover.png", clicked=[SetVariable("buyable_pick", "lower_inhibition_level")])

                def can_afford(cost, stats):
                    if len(cost) != len(stats):
                        return False

                    for i in range(len(cost)):
                        if not 100 >= (stats[i] - cost[i]) >= 0:                # Instead of "cost[i] > stats[i]" to calculate inhibition
                            return False
                    return True

                def _buy_buyable(buyable_cost):
                    if globals()['buyable_pick'] == 'lower_inhibition_level':
                        update_stat_min('inhibition', get_stat_min('inhibition') - 25)
                    globals()[eval('buyable_pick')] += 1                        # Register the new buyable.

                    globals()['morale']         -= buyable_cost[0]              # Pay the price.
                    globals()['behavior']       -= buyable_cost[1]
                    globals()['academics']      -= buyable_cost[2]
                    globals()['artistery']      -= buyable_cost[3]
                    globals()['athletics']      -= buyable_cost[4]
                    globals()['deviance']       -= buyable_cost[5]
                    globals()['inhibition']     -= buyable_cost[6]
                    globals()['buyable_pick']    = 'unlocked'

                    renpy.restart_interaction()                 # Make sure we update the UI so you get feedback when you buy.
                    return

                buy = renpy.curry(_buy_buyable)                 # Curry is used to make sure _buy_buyables only gets activated once a click. (Think of it as a handler.)

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
            $ var = get_stat_min('inhibition') - 25             # Used for lower inhibition
            for buyable in buyables:
                if buyable_pick == buyable['name']:
                    hbox:
                        spacing 5
                        if buyable['image'] != "":
                            add buyable['image']
                        else:
                            null height 20
                        text buyable['description']
                        $ buyable_cost = buyable['cost']
    hbox:
        xanchor 0
        yanchor 0
        xpos 0.17
        ypos 0.90
        spacing 5
        vbox:
            text "{size=30}Cost:   [buyable_cost]{/size}"
            text "{size=25}Have:    [morale], [behavior], [academics], [artistery], [athletics], [deviance], [inhibition]{/size}"

    vbox:
        xpos 0.85
        ypos 0.87
        spacing 5
        python:
            if can_afford(buyable_cost, [morale,behavior,academics,artistery,athletics,deviance,inhibition]) and buyable_pick != 'unlocked':
                ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=buy(buyable_cost))
            else:
                ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=None)
            ui.imagebutton("images/ui/return_button_idle.png", "images/ui/return_button_hover.png", clicked=ui.returns(0))
