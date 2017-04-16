##############################################################################
# Buildings Menu
#
# Build and upgrade your buildings.

screen buildings_screen:
    imagemap:
        ground "images/ui/menu_bg.png"

    python:
        building_level = globals()[eval('building_pick')]
        building_cost_array = eval(building_pick + '_price')
        building_cost = building_cost_array[building_level]

        def _buy_building(cost):
            globals()[eval('building_pick')] += 1               # Register the new building.
            globals()['cash'] -= cost                           # Pay the price.

            renpy.restart_interaction()                         # Make sure we update the UI so you get feedback when you buy.
            return

        buy = renpy.curry(_buy_building)                        # Curry is used to make sure buy only gets activated on click. (Think of it as a handler.)

    hbox:
        xfill True
        yfill True
        vbox:
            yfill True
            vbox:
                python:
                    for building in buildings:
                        if eval(building['requirement']) <= building['requirement_value']:
                            pass
                        else:
                            ui.imagebutton("images/ui/"+building['name']+"_idle.png", "images/ui/"+building['name']+"_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("building_pick", "building_"+building['name'])])
                    
            vbox:
                spacing 10
                xpos 0.1
                ypos 0.31
                text "{size=30}Money : [cash]{/size}"
                $ ui.imagebutton("images/ui/return_button_idle.png", "images/ui/return_button_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=ui.returns(0))

        vbox:
            xfill True
            xpos 0.003
            ypos 0.003
            for building in buildings:
                if  building_pick == "building_"+building['name']:
                    hbox:
                        spacing 5
                        add building['image']
                        text building['description']

            null height 30
            vbox:
                yfill True
                yalign 1.0
                hbox:
                    if building_level < len(building_cost_array) - 2:
                        $ building_next = building_level + 1
                    else:
                        $ building_next = 'Max'
                    spacing 10
                    xpos 0.02
                    ypos 0.37
                    hbox:
                        python:
                            _can_buy = cash >= building_cost                # Can you afford the building?
                            if _can_buy and building_cost > 0:
                                ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=buy(building_cost))
                            elif building_cost > 0:
                                ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=None)
                            else:
                                ui.imagebutton("images/ui/buy_button_idle.png", "images/ui/buy_button_hover.png", insensitive_image="images/ui/buy_button_disable.png", clicked=None)
                    grid 3 1:
                        xfill True
                        xalign 0.5
                        yalign 0.5
                        grid 2 1:
                            hbox:
                                text "{size=30}  Level :   {/size}"         # some space padding is used to avoid other grids becoming larger than this and cause a bit of moving around at certain occasions.
                            hbox:
                                if building_cost == 0:                      #checks if next level is the last one, based on the each building costs.
                                    text "{size=30}Max1{/size}"
                                else:
                                    text "{size=30}[building_level] -> [building_next]{/size}"
                        grid 2 1:
                            hbox:
                                if building_cost == 0:
                                    text "(Can't upgrade it further)"
                                else:
                                    text "{size=30}Cost : {/size}"
                            hbox:
                                if building_cost == 0:
                                    text ""
                                else:
                                    text "{size=30}[building_cost]{/size}"
                        grid 2 1:
                            if building_cost == 0:
                                hbox:
                                    text ""
                                hbox:
                                    text ""
                            else:
                                hbox:
                                    text "{size=30}Maintenance : {/size}"
                                hbox:
                                    text "{size=30}[building_cost]{/size}"

