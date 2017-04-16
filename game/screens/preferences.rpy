##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("{b}Toggle content{/b}")
                grid 1 7:
                    vbox:
                        label _("Googirls")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "googirls", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "googirls", False)
                    vbox:
                        label _("Tentacles")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "tentacles", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "tentacles", False)
                    vbox:
                        label _("Catgirls")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "catgirls", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "catgirls", False)
                    vbox:
                        label _("Loli")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 1")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 2")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)
                    vbox:
                        label _("Placeholder 3")
                        textbutton _("Enabled") action SetDict(persistent.content_list, "loli", True)
                        textbutton _("Disabled") action SetDict(persistent.content_list, "loli", False)


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display - Window")
                textbutton _("640 x 360") action Preference("display", 0.5)
                textbutton _("960 x 540") action Preference("display", 0.75)
                textbutton _("1280 x 720") action Preference("display", 1)
                label _("Display - Fullscreen")
                textbutton _("1280 x 720") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

        vbox:
            frame:
                style_group "pref"
                has vbox
                #label _("{b}Advanced{/b}")
                #label _("Image cache size")
                #textbutton _("4") action SetVariable(config.image_cache_size, 4)
                #textbutton _("8") action SetVariable(config.image_cache_size, 8)
                #textbutton _("16") action SetVariable(config.image_cache_size, 16)


init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 1.0

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0
