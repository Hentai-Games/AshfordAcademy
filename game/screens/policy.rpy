##############################################################################
# Policy Menu
#
# Show policy screen and options.

define policy_screen = policy_screens[0]['name']

screen policy_screen:
    imagemap:
        ground "images/ui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                for screen in policy_screens:
                    ui.imagebutton("images/ui/"+screen['name']+"_idle.png", "images/ui/"+screen['name']+"_hover.png", clicked=[SetVariable("policy_screen", screen['name'])])

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
            
            
            $ runs = 0
            for label in policy_labels:
                if label['screen'] == policy_screen:
                    if runs >=1:
                        null height 25
                    label label['text']
                    for choice in policy_choices:
                        if choice['label'] == label['name']:
                            $ req = eval(choice['requirement'])
                            if req:
                                textbutton choice['text'] action eval(choice['action']) xminimum 800
                    $ runs += 1
            $ runs = 0
    vbox:
        xalign 0.992
        yalign 0.992
        $ ui.imagebutton("images/ui/return_button_idle.png", "images/ui/return_button_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=ui.returns(0))
