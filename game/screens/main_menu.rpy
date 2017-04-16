##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

define menu2 = [
    {"text": "New Game +",  "action" : "GalleryManager.ShowMenu(), Show('new_game_plus')",  "xpos": 1066,   "ypos": 369,    "reverse": True,    "requirement" : "persistent.new_game_plus"},
    {"text": "Gallery",     "action" : "GalleryManager.ShowMenu(), Show('gallery_grid')",   "xpos": 1066,   "ypos": 322,    "reverse": False,   "requirement" : "persistent.new_game_plus"}
    ]

screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
            ground persistent.mod_custom_title_screen_ground

            # This is so that everything transparent is invisible to the cursor.
            alpha False

            #for menu in menu2:
            #   if eval(menu['requirement']):
            #   gallery.main_button(text=menu['text'], action=menu['action'],  xpos=menu['xpos'], ypos=menu['ypos'], reverse=menu['reverse'])
            $ xpos = 1066
            if persistent.new_game_plus:
                $ gallery.main_button(text='New Game +',    action=[GalleryManager.ShowMenu(), Show("new_game_plus")], xpos=xpos, ypos=369, reverse=True)
                $ gallery.main_button(text='Gallery',       action=[GalleryManager.ShowMenu(), Show("gallery_grid")],  xpos=xpos, ypos=322)

            $ gallery.base_button(text='New Game',      action=[Start()],  xpos=1066, ypos=417)
            $ gallery.main_button(text='Load Game',     action=[GalleryManager.ShowMenu(), ShowMenu("load")],  xpos=xpos, ypos=466)
            $ gallery.main_button(text='Preferences',   action=[GalleryManager.ShowMenu(), Show("preferences")],  xpos=xpos, ypos=514)
            $ gallery.main_button(text='Mod Manager',   action=[GalleryManager.ShowMenu(), Show("mod_manager")],  xpos=xpos, ypos=561)
            $ gallery.main_button(text='Help',          action=[Help()],  xpos=xpos, ypos=610)
            $ gallery.main_button(text='Quit',          action=[Quit(confirm=False)],  xpos=xpos, ypos=657)


init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"
