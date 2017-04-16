# This contains code for the new day planner. You probably
# don't want to change this file, but it might make sense to
# change many of the variables or styles defined here from
# other files.

init -100 python:

    side_menu = [
        {"title": "Policy",             "menu": "policy",               "yoffset": 5,   "xoffset": 4,   "xminimum": 170},
        {"title": "Buildings",          "menu": "buildings",            "yoffset": 36,  "xoffset": 4,   "xminimum": 170},
        {"title": "Buyables",           "menu": "buyables",             "yoffset": 67,  "xoffset": 4,   "xminimum": 170},
        {"title": "Show budget",        "menu": "show_budget",          "yoffset": 98,  "xoffset": 4,   "xminimum": 170},
        {"title": "Achievements",       "menu": "achievement_summary",  "yoffset": 129, "xoffset": 4,   "xminimum": 170}
        ]

    # The frame containing the day planner.
    style.dp_frame = Style(style.frame)
    style.dp_vbox = Style(style.vbox)
    style.dp_hbox = Style(style.hbox)

    # The frame and vbox containing a single choice.
    style.dp_choices = Style(style.default)
    style.dp_choices_vbox = Style(style.vbox) 
    style.dp_choices.xalign = 0
    
    # Buttons.
    style.dp_choice_button = Style(style.button)
    style.dp_choice_button_text = Style(style.button_text)

    style.dp_done_button = Style(style.button)
    style.dp_done_button_text = Style(style.button_text)

    # Labels.
    style.dp_label = Style(style.label)
    style.dp_label_text = Style(style.label_text)

    # The title of the buttons.
    dp_done_title = "Done Planning"
    
    # A map from period name to the information we know about that period.
    __periods = { }

    # The period we're updating.
    __period = None
    
    class __Period(object):

        def __init__(self, name, var):
            self.name = name
            self.var = var
            self.acts = [ ]

    def dp_period(name, var):
        __periods[name] = store.__period = __Period(name, var)

    __None = object()
        
    def dp_choice(name, value=__None, enable="True", show="True"):

        if not __period:
            raise Exception("Choices must be part of a defined period.")

        if value is __None:
            value = name
        
        __period.acts.append((name, value, enable, show))

    def __set_noncurried(var, value):
        setattr(store, var, value)
        return True
        
    __set = renpy.curry(__set_noncurried)
        

label day_planner(periods):

    python hide:
        renpy.choice_for_skipping()
    
label day_planner_repeat:

    if renpy.has_label("dp_callback"):
        call dp_callback

    python hide:
    
        ui.window(style=style.dp_frame)
        ui.vbox(style=style.dp_vbox)
        ui.hbox(style=style.dp_hbox)

        can_continue = True

        for p in periods:

            if p not in __periods:
                raise Exception("Period %r was never defined." % p)

            ui.window(style=style.dp_choices)
            ui.vbox(style=style.dp_choices_vbox)
            
            p = __periods[p]
            v = getattr(store, p.var)

            layout.label(p.name, "dp")

            valid_choice = False
            
            for name, value, enable, show in p.acts:
                show = eval(show)
                enable = eval(enable)

                selected = (v == value)
                
                if show:
                    layout.button(name, "dp_choice", clicked=__set(p.var, value), selected=selected, enabled=enable,)

                if show and enable and selected:
                    valid_choice = True

            if not valid_choice:
                can_continue = False
            
            ui.close()
                    
        ui.close() # hbox.
        

        layout.button(
            dp_done_title,
            "dp_done",
            clicked=ui.returns(False),
            enabled=can_continue)
        
        ui.close() # vbox

        for item in side_menu:
            layout.button(item['title'], clicked=ShowMenu(item['menu']),yoffset=item['yoffset'],xoffset=item['xoffset'],xminimum=item['xminimum'])

        if povFirstName == 'debug':
            layout.button("Debug screen", clicked=ShowMenu('debug_screen'),yoffset=160,xoffset=5,xminimum=170)
            layout.button("Inventory", clicked=ShowMenu('inventory'),yoffset=191,xoffset=5,xminimum=170) 
            #layout.button("Office", clicked=ShowMenu('office_screen'),yoffset=222,xoffset=5,xminimum=170)
            layout.button("Mod List", clicked=ShowMenu('mod_list'),yoffset=253,xoffset=5,xminimum=170)
            layout.button("Notify", clicked=Notify('acad_gain'),yoffset=284,xoffset=5,xminimum=170)
        
        
        ## Removed until added functionality or merged with phone.
        if(new_messages > 0):
            layout.button("Notifications ({color=[notification_color]}[new_messages]{/color})", clicked=ShowMenu('mailbox'),xoffset=815,yoffset=4,xminimum=200)
        else:
            layout.button("Notifications ([new_messages])", clicked=ShowMenu('mailbox'),xoffset=815,yoffset=4,xminimum=200)

    if ui.interact():
        jump day_planner_repeat
    else:
        return

