##############################################################################
# Buyables Menu
#
# Buy extra's with orbs.

screen buyables_screen:
    imagemap:
        ground "images/ui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                if sexy_uniform == 0:
                    ui.imagebutton("images/ui/sexy_uniform_idle.png", "images/ui/sexy_uniform_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "sexy_uniform"), SetVariable("buyable_cost", [3, 0, 0, 0])])
                elif nude_uniform == 0:
                    ui.imagebutton("images/ui/nude_uniform_idle.png", "images/ui/nude_uniform_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "nude_uniform"), SetVariable("buyable_cost", [8, 0, 0, 0])])
                if bdsm_detention == 0:
                    ui.imagebutton("images/ui/bdsm_detention_idle.png", "images/ui/bdsm_detention_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "bdsm_detention"), SetVariable("buyable_cost", [5, 0, 0, 0])])
                if magic_accounting == 0:
                    ui.imagebutton("images/ui/magic_accounting_idle.png", "images/ui/magic_accounting_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "magic_accounting"), SetVariable("buyable_cost", [0, 1, 1, 1])])
                if hyper_anatomic_body == 0:
                    ui.imagebutton("images/ui/anatomical_models_idle.png", "images/ui/anatomical_models_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "hyper_anatomic_body"), SetVariable("buyable_cost", [4, 0, 0, 0])])
                if lower_inhibition_level < 4:
                    ui.imagebutton("images/ui/lower_inhibition"+str(lower_inhibition_level)+"_idle.png", "images/ui/lower_inhibition"+str(lower_inhibition_level)+"_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "lower_inhibition_level"), SetVariable("buyable_cost", [2 + lower_inhibition_level, 0, 0, 0])])
                if no_detention == 0 and good_points > 0:
                    ui.imagebutton("images/ui/no_detention_idle.png", "images/ui/no_detention_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "no_detention"), SetVariable("buyable_cost", [0, 0, 2, 2])])
                #if sexy_uniform == 0:
                #    ui.imagebutton("images/ui/cheerleader_club_idle.png", "images/ui/cheerleader_club_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("buyable", "cheerleader_club"), SetVariable("buyable_cost", [3, 0, 0, 0])])
                    
                def _buy_buyable(buyable_cost):
                    if globals()['buyable'] == 'lower_inhibition_level':
                        update_stat_min('inhibition', get_stat_min('inhibition') - 25)
                    globals()[eval('buyable')] += 1             # Register the new buyable.
                    globals()['red_orb'] -= buyable_cost[0]     # Pay the price.
                    globals()['blue_orb'] -= buyable_cost[1]
                    globals()['green_orb'] -= buyable_cost[2]
                    globals()['yellow_orb'] -= buyable_cost[3]
                    globals()['buyable'] = 'unlocked'

                    renpy.restart_interaction()                 # Make sure we update the UI so you get feedback when you buy.
                    return

                buy = renpy.curry(_buy_buyable)                 # Curry is used to make sure _buy_buyables only gets activated once a click. (Think of it as a handler.)

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
            if buyable == "sexy_uniform":
                add "buildings/sexy_uniform1.jpg"
                text "All students are forced to wear a more revealing uniform.\nUnlocks sexy uniform dress code."

            elif buyable == "nude_uniform":
                add "buildings/nude_uniform.jpg"
                text "Students are forced to go to school nude or in lingerie.\nUnlocks nude uniform dress code."
                
            elif buyable == "cheerleader_club":
                add "buildings/cheerleader_club.jpg"
                text "Open up a cheerleader club for the students .\nAllows visiting the Cheerleader Club."

            elif buyable == "hyper_anatomic_body":
                add "buildings/classrooms.jpg"
                text "Anatomical models based on pornstars, since we all know that porn is {i}real{/i}. \nUnlocks hyper sexualized human models."

            elif buyable == "magic_accounting":
                add "buildings/classrooms.jpg"
                text "You don't know how, but it seems you can {i}always{/i} squeeze out some more cash from your budget. \nGives you 10% more money per month and level."

            elif buyable == "bdsm_detention":
                add "buildings/bdsm_detention.jpg"
                text "If they don't listen, spank them. If they don't behave, make them behave.\nUnlocks BDSM detention."

            elif buyable == "no_detention":
                add "buildings/classrooms.jpg"
                text "You know man, love is like the best thing, we should all spread love. \nUnlocks no detention."

            elif buyable == "lower_inhibition_level":
                add "buildings/sexy_uniform2.jpg"
                $ var = get_stat_min('inhibition') - 25
                text "Help the students become more relaxed in regards to their body. \nLowers minimum inhibition to [var]."

            elif buyable == "unlocked":
                text "Congratulations, you unlocked a new buyable!"

            else:
                null height 20
                text "Here you can buy special upgrades for your school. Most extras will be available directly except for new classes, they will be available the next day."

    hbox:
        xanchor 0
        yanchor 0
        xpos 0.53
        ypos 0.87
        spacing 5
        vbox:
            yalign 0.5
            text "{size=30}Cost:    {/size}"
            text "{size=25}Have:    {/size}"
        grid 7 2:
            yalign 0.5
            spacing 5
            $ ui.image(im.Scale("images/ui/orbs/orb_morale.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_morale]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_behavior.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_behavior]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_academics.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_academics]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_artistry.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_artistry]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_athletics.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_athletics]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_deviance.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_deviance]{/size}"

            $ ui.image(im.Scale("images/ui/orbs/orb_inhibition.png", small_orb_width, small_orb_height, bilinear=True))
            text "{size=25}[orb_inhibition]{/size}"


        vbox:
            spacing 5
            python:
                _can_buy = red_orb >= buyable_cost[0] and blue_orb >= buyable_cost[1] and green_orb >= buyable_cost[2] and yellow_orb >= buyable_cost[3] and globals()['buyable'] != 'unlocked'
                if _can_buy:
                    ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=buy(buyable_cost))
                else:
                    ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=None)
            $ ui.imagebutton("images/ui/return_button_idle.png", "images/ui/return_button_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=ui.returns(0))

