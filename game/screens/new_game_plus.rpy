##############################################################################
# New game plus screen
#
# Screen that allows the user to set-up their initial settings
# such as name, title, gender et cetera.

screen new_game_plus:

    tag menu

    imagemap:
        ground persistent.mod_custom_title_screen_ground

    grid 3 1:
        style_group "prefs"
        xfill True

        vbox:
            style_group "pref"
            label _("{b}Gender settings{/b}")
            frame:
                vbox:
                    label _("Sex")
                    for gender in povGenders:
                        textbutton _(gender) action SetVariable("povGender", gender)
            frame:
                vbox:
                    label _("Title")
                    for title in povTitles:
                        textbutton _(title) action SetVariable("povTitle", title)
            frame:
                vbox:
                    label _("BDSM Title")
                    for bdsmTitle in povBdsmTitles:
                        textbutton _(bdsmTitle) action SetVariable("povBdsmTitle", bdsmTitle)
        vbox:
            label _("{b}Game settings{/b}")
            frame:
                style_group "pref"
                has vbox
                label _("Difficulty")
                for difficulty in difficulties:
                    textbutton _(difficulty) action SetVariable("game_mode", difficulty)

        vbox:
            label _("{b}Content settings{/b}")
            frame:
                style_group "pref"
                has vbox
                vbox:
                    label _("New game plus content")
                    textbutton _("Enabled") action SetVariable("new_game_plus", True)
                    textbutton _("Disabled") action SetVariable("new_game_plus", False)

            frame:
                textbutton _("Start") action Start("new_game_plus")

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
