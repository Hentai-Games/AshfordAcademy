#### FLAGON EVENT PACK 1 - Pool ####

## This event pack contains events for all original locations in the game, as well as new events for the monthly actions.
## This File is for the Pool.
## Pictures are located in the subdirectory \Flagon1\Pool
## All custom images, characters, variables... are prefixed with "fla_" (with the exception of temp variables) to avoid conflicts.
## Formatting shamelessly stolen from Goldo. All your Code are belong to us!
#### SETUP ####

#Define characters
#Characters go here if needed

#Init variables
#Variables go here if needed

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Declaring images

image bg fla_pool1 = "mods/Flagon1/Pool/fla_pool1.jpg"
image bg fla_pool2 = "mods/Flagon1/Pool/fla_pool2.jpg"
image bg fla_pool3 = "mods/Flagon1/Pool/fla_pool3.jpg"
image bg fla_pool4 = "mods/Flagon1/Pool/fla_pool4.jpg"
image bg fla_pool5 = "mods/Flagon1/Pool/fla_pool5.jpg"
image bg fla_pool6 = "mods/Flagon1/Pool/fla_pool6.jpg"
image bg fla_pool7 = "mods/Flagon1/Pool/fla_pool7.jpg"
image bg fla_pool8_1 = "mods/Flagon1/Pool/fla_pool8_1.jpg"
image bg fla_pool8_2 = "mods/Flagon1/Pool/fla_pool8_2.jpg"
image bg fla_pool9 = "mods/Flagon1/Pool/fla_pool9.jpg"
image bg fla_pool10 = "mods/Flagon1/Pool/fla_pool10.jpg"
image bg fla_pool13 = "mods/Flagon1/Pool/fla_pool13.jpg"
image bg fla_pool14 = "mods/Flagon1/Pool/fla_pool14.jpg"
image bg fla_pool15 = "mods/Flagon1/Pool/fla_pool15.jpg"
image bg fla_pool16 = "mods/Flagon1/Pool/fla_pool16.jpg"
image bg fla_pool17 = "mods/Flagon1/Pool/fla_pool17.jpg"
image bg fla_pool18 = "mods/Flagon1/Pool/fla_pool18.jpg"
image bg fla_pool19 = "mods/Flagon1/Pool/fla_pool19.jpg"
image bg fla_pool20 = "mods/Flagon1/Pool/fla_pool20.jpg"

#Setting up events and conditions

init:
    $ event("fla_pool1", "act == 'pool' and morale > 15", event.choose_one('pool'), priority=200)
    $ event("fla_pool2", "act == 'pool' and inhibition < 95", event.choose_one('pool'), priority=200)
    $ event("fla_pool3", "act == 'pool' and inhibition < 95", event.choose_one('pool'), priority=200)
    $ event("fla_pool4", "act == 'pool' and behavior > 15", event.choose_one('pool'), priority=200)
    $ event("fla_pool5", "act == 'pool' and morale > 15", event.choose_one('pool'), priority=200)
    $ event("fla_pool6", "act == 'pool' and behavior > 20", event.choose_one('pool'), priority=200)
    $ event("fla_pool7", "act == 'pool' and inhibition < 90", event.choose_one('pool'), priority=200)
    $ event("fla_pool8", "act == 'pool' and uniform == 'sexy_uniform'", event.choose_one('pool'), priority=200)
    $ event("fla_pool9", "act == 'pool' and athletics > 5", event.choose_one('pool'), priority=200)
    $ event("fla_pool10", "act == 'pool' and inhibition < 75 and athletics > 35", event.choose_one('pool'), priority=200)
    $ event("fla_pool11", "act == 'pool' and behavior > 40 and inhibition < 60", event.choose_one('pool'), priority=200)
    $ event("fla_pool13", "act == 'pool' and inhibition < 85", event.choose_one('pool'), priority=200)
    $ event("fla_pool14", "act == 'pool' and deviance > 25 and inhibition < 70", event.choose_one('pool'), priority=200)
    $ event("fla_pool15", "act == 'pool' and deviance > 50", event.choose_one('pool'), priority=200)
    $ event("fla_pool16", "act == 'pool' and deviance > 50", event.choose_one('pool'), priority=200)
    $ event("fla_pool17", "act == 'pool' and deviance > 60", event.choose_one('pool'), priority=200)
    $ event("fla_pool18", "act == 'pool' and inhibition < 75", event.choose_one('pool'), priority=200)
    $ event("fla_pool19", "act == 'pool' and inhibition < 75 and athletics > 25", event.choose_one('pool'), priority=200)
    $ event("fla_pool20", "act == 'pool' and deviance > 75 and inhibition < 25", event.choose_one('pool'), priority=200)

label fla_pool1:
    
    scene bg fla_pool1 with fade
    "The pool is full of happy students enjoying the water"
    if renpy.random.randint (1, 2) == 1:
        $ morale +=1
    else:
        $ athletics +=1
    return
    
label fla_pool2:
    
    scene bg fla_pool2 with fade
    "You spot a student lazily floating atop the water."
    return
    
label fla_pool3:
    
    scene bg fla_pool3 with fade
    "You cautiously peek into the girls changing room. Looks like these girls are... perky."
    return
    
label fla_pool4:
    
    scene bg fla_pool4 with fade
    "A group of students is cleaning the pool. Looks like their having fun!"
    $ behavior +=1
    return
    
label fla_pool5:
    
    scene bg fla_pool5 with fade
    pov "Enjoying the pool?"
    girl "Oh yes! It's great to have a place to swim!"
    return
    
label fla_pool6:
    
    scene bg fla_pool6 with fade
    "One of your students is helping her friend learn how to swim. It's always good to see your students helping each other out."
    $ behavior +=1
    return
    
label fla_pool7:
    
    scene bg fla_pool7 with fade
    girl "Is it just me or are these school swimsuits to small?"
    return
    
label fla_pool8:
    
    scene bg fla_pool8_1 with fade
    "As you enjoy a nice swim, a student walks up to the edge of the pool and strikes a sexy pose."
    girl "Hello [povTitle]. [povLastName]. Do you like my swimsuit?"
        
    if inhibition > 60:
        pov "Very nice indeed. It suits you well!"
        $ morale +=1
        $ inhibition -=1
    else:
        pov "Very nice indeed. But I think it would look even better if it were a bit more revealing don't you?"
        scene bg fla_pool8_2
        "The girl flashes you a naughty grin and rolls up her top with a wink"
        girl "How about now?"
        pov "Truly divine."
        $ deviance +=1
        $ inhibition -=1
    return
    
label fla_pool9:
    
    scene bg fla_pool9 with fade
    "This student is taking a well deserved rest after a hard workout"
    $ athletics +=1
    return
    
label fla_pool10:
    
    scene bg fla_pool10 with fade
    "Your not sure what impresses you more. How long she can hold her breath or her ability to apply suction without swallowing water."
    $ athletics +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
        $ deviance +=1
    return
    
label fla_pool11:
    
    $ r=renpy.random.randint(1, 2)
    image bg fla_pool11 = ConditionSwitch("r==1","mods/Flagon1/Pool/fla_pool11_1.jpg","r==2","mods/Flagon1/Pool/fla_pool11_2.jpg")
    
    scene bg fla_pool11 with fade
    "Your students have now begun teaching eachother more advanced lessons, like sex in the water."
    $ behavior +=2
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance+= 5
    return
    
label fla_pool13:
    
    scene bg fla_pool13 with fade
    "A suprised cry draws your attention. Looks like this students had a slight wardrobe malfunction."
    $ inhibition -=1
    return
    
label fla_pool14:
    
    scene bg fla_pool14 with fade
    "A senior is groping an underclassman in the pool, while his girlfriend watches with a flushed face."
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance+= 5
    return
    
label fla_pool15:
    
    scene bg fla_pool15 with fade
    "The girls of the swim team are putting on a show for the boys, as a reward for an excellent practice session."
    $ athletics +=1
    return
    
label fla_pool16:
    
    scene bg fla_pool16 with fade
    "These two girls do this everyday after swim class. They claim it helps to strech thier muscles after a hard workout."
    return
    
label fla_pool17:
    
    scene bg fla_pool17 with fade
    "You look into the changing room just in time to see a student removing her panties. A long string of semen is dripping from her pussy."
    pov "Make sure you have a shower before getting in the pool, we don't want the water contaminated!"
    girl "Will do [povTitle]. [povFirstName]!"
    return
    
label fla_pool18:
    
    scene bg fla_pool18 with fade
    "During free swim, students enjoy taking toys into the pool with them."
    $ deviance +=1
    return
    
label fla_pool19:
    
    scene bg fla_pool19 with fade
    "Swimming laps can be boring, so it's important to reward yourself. This girl has found a way that keeps her muscles moving as well as being fun!"
    $ athletics +=1
    return
    
label fla_pool20:
    
    scene bg fla_pool20 with doubleflash
    "You walk into the pool and are suddenly knocked to the ground. Before you know what's happening your pants have been removed and female flesh is being pressed against you."
    pov "Wha... WHAT ARE YOU DOING!?"
    girl1 "All the boys around here are pathetic! They weren't even able to last an hour!"
    girl2 "And we still NEED more. You can satisfy us right [povFirstName]?"
    "You can feel your body responding to the kisses and carresses of the girls. You hold out as long as you can, but these girls are insaitable, and after what feels like days of thrusting, licking and fingering you eventually pass out in a pool of cum and sweat."
    "As the blackness claims you, your last thought is that maybe your policies have been TOO effective."
    $behavior -=2
    $deviance +=2
    if renpy.random.randint(1, 2) == 1:
        $ deviance+= 5
        $reputation -=1
    return