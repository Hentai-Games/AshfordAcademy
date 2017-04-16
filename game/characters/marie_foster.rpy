##########################################################
#
#                       Marie Foster
#
# Nurse Lia's little sister.
#
##########################################################

init python:
    def update_marie_outfit(uniform, inhibition):
        if uniform == "nude_uniform":
            return "nude"
        elif uniform == "sexy_uniform":
            return "undies"
        elif uniform == "no_uniform":
            if inhibition > 75:
                return "casual"
            else:
                return "casual2"
        else:
            return "uniform"

define marie_outfit = 'uniform'          # This can be 'uniform', 'casual', 'undies' or 'nude'.
define marie_points = 0
define marie_last_choice = 0

define marie = Character('Marie', color="#5B3959")

# Sprites

# Sprites
image uniform_marie smile                  = "characters/marie_foster/uniform_marie_smile.png"
image uniform_marie smile_blush            = "characters/marie_foster/uniform_marie_smile_blush.png"
image uniform_marie happy                  = "characters/marie_foster/uniform_marie_happy.png"
image uniform_marie happy_blush            = "characters/marie_foster/uniform_marie_happy_blush.png"
image uniform_marie blush                  = "characters/marie_foster/uniform_marie_blush.png"
image uniform_marie angry                  = "characters/marie_foster/uniform_marie_angry.png"
image uniform_marie sad                    = "characters/marie_foster/uniform_marie_sad.png"
image uniform_marie surprised              = "characters/marie_foster/uniform_marie_surprised.png"
image uniform_marie surprised_blush        = "characters/marie_foster/uniform_marie_surprised_blush.png"

image casual_marie smile                   = "characters/marie_foster/casual_marie_smile.png"
image casual_marie smile_blush             = "characters/marie_foster/casual_marie_smile_blush.png"
image casual_marie happy                   = "characters/marie_foster/casual_marie_happy.png"
image casual_marie happy_blush             = "characters/marie_foster/casual_marie_happy_blush.png"
image casual_marie blush                   = "characters/marie_foster/casual_marie_blush.png"
image casual_marie angry                   = "characters/marie_foster/casual_marie_angry.png"
image casual_marie sad                     = "characters/marie_foster/casual_marie_sad.png"
image casual_marie surprised               = "characters/marie_foster/casual_marie_surprised.png"
image casual_marie surprised_blush         = "characters/marie_foster/casual_marie_surprised_blush.png"

image casual2_marie smile                  = "characters/marie_foster/casual2_marie_smile.png"
image casual2_marie smile_blush            = "characters/marie_foster/casual2_marie_smile_blush.png"
image casual2_marie happy                  = "characters/marie_foster/casual2_marie_happy.png"
image casual2_marie happy_blush            = "characters/marie_foster/casual2_marie_happy_blush.png"
image casual2_marie blush                  = "characters/marie_foster/casual2_marie_blush.png"
image casual2_marie angry                  = "characters/marie_foster/casual2_marie_angry.png"
image casual2_marie sad                    = "characters/marie_foster/casual2_marie_sad.png"
image casual2_marie surprised              = "characters/marie_foster/casual2_marie_surprised.png"
image casual2_marie surprised_blush        = "characters/marie_foster/casual2_marie_surprised_blush.png"

image undies_marie smile                   = "characters/marie_foster/undies_marie_smile.png"
image undies_marie smile_blush             = "characters/marie_foster/undies_marie_smile_blush.png"
image undies_marie happy                   = "characters/marie_foster/undies_marie_happy.png"
image undies_marie happy_blush             = "characters/marie_foster/undies_marie_happy_blush.png"
image undies_marie blush                   = "characters/marie_foster/undies_marie_blush.png"
image undies_marie angry                   = "characters/marie_foster/undies_marie_angry.png"
image undies_marie sad                     = "characters/marie_foster/undies_marie_sad.png"
image undies_marie surprised               = "characters/marie_foster/undies_marie_surprised.png"
image undies_marie surprised_blush         = "characters/marie_foster/undies_marie_surprised_blush.png"

image nude_marie smile                     = "characters/marie_foster/nude_marie_smile.png"
image nude_marie smile_blush               = "characters/marie_foster/nude_marie_smile_blush.png"
image nude_marie happy                     = "characters/marie_foster/nude_marie_happy.png"
image nude_marie happy_blush               = "characters/marie_foster/nude_marie_happy_blush.png"
image nude_marie blush                     = "characters/marie_foster/nude_marie_blush.png"
image nude_marie angry                     = "characters/marie_foster/nude_marie_angry.png"
image nude_marie sad                       = "characters/marie_foster/nude_marie_sad.png"
image nude_marie surprised                 = "characters/marie_foster/nude_marie_surprised.png"
image nude_marie surprised_blush           = "characters/marie_foster/nude_marie_surprised_blush.png"

init:
    $ event("marie_class", "act == 'classroom'", event.once(), event.only(), priority=900)

label marie_class:
    scene classroom with fade
    $ marie_outfit = update_marie_outfit(uniform,inhibition)
    $ renpy.show(marie_outfit+"_marie smile")
    "???" "Hello [povName]."
    menu:
        "Hello there!":
            pass

        "Yes?":
            pass

    "???" "I hear you are the new principal."
    pov "That's correct miss...?"
    marie "Marie."
    pov "That's correct Marie."
    marie "Thank you. That was all.\nBye."
    pov "Okay, bye Marie."
    $ marie_points += 1
    return

