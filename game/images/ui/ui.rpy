init python:
    import datetime
    now = datetime.datetime.now()

init:
    # Colours used in the UI
    define color_increase       = '007F00'      # Green
    define color_decrease       = 'D50000'      # Red
    define notification_color   = 'FFF600'      # Yellow
    
    # For transition effect
    image circleiris    = "images/ui/transitions/circleiris.png"

    image splash        = "images/ui/splash.jpg"
    image main          = "images/ui/mm_ground.png"

    # Orbs
    define small_orb_width      = 32
    define small_orb_height     = 32
    define ui_orb_spacing       = 8
    
    image orb_academics  =  im.Scale("images/ui/orbs/orb_academics.png", 35, 35, bilinear=True)
    image orb_artistery  =  im.Scale("images/ui/orbs/orb_artistry.png", 35, 35, bilinear=True)
    image orb_athletics  =  im.Scale("images/ui/orbs/orb_athletics.png", 35, 35, bilinear=True)
    image orb_morale     =  im.Scale("images/ui/orbs/orb_morale.png", 35, 35, bilinear=True)
    image orb_behavior   =  im.Scale("images/ui/orbs/orb_behavior.png", 35, 35, bilinear=True)
    image orb_deviance   =  im.Scale("images/ui/orbs/orb_deviance.png", 35, 35, bilinear=True)
    image orb_inhibition =  im.Scale("images/ui/orbs/orb_inhibition.png", 35, 35, bilinear=True)


label splashscreen:
    scene black
    show text ""
    with Pause(0.5)
    
    show splash 
    with dissolve
    with Pause(2.0)
    
    scene black
    with dissolve
    with Pause(0.5)

    show main
    with dissolve

    # Christmas countdown!
    if (now.month == 12) and (now.day <= 27 or now.day == 31):
        "Christmas countdown featuring Jack Drake - Day [now.day]"
        $ renpy.jump("jack_drake_christmas"+str(now.day))
    return
