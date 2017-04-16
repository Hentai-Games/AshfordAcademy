##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
            ground persistent.mod_custom_title_screen_ground
            idle persistent.mod_custom_title_screen_idle
            hover persistent.mod_custom_title_screen_hoover
                
            # This is so that everything transparent is invisible to the cursor.
            alpha False

            if persistent.new_game_plus:
                hotspot (1066, 369, 176, 39) action ShowMenu("new_game_plus")
                # NOTE: Transform is broken in Renpy 6.18.0
                # $ gallery.main_button(xpos=1066, ypos=322)
            else:
                hotspot (0, 0, 0, 0) action Start("new_game_plus")

            hotspot (1066, 417, 176, 39) action Start()
            hotspot (1066, 466, 176, 39) action ShowMenu("load")
            hotspot (1066, 514, 176, 39) action ShowMenu("preferences")
            hotspot (1066, 561, 176, 39) action ShowMenu("mod_manager")
            hotspot (1066, 610, 176, 39) action Help()
            hotspot (1066, 657, 176, 39) action Quit(confirm=False)


init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"

