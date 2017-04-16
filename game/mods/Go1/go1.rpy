#### GOLDO EVENT PACK 1 ####

## This event pack contains events for all original locations in the game. Pictures are located in the subdirectory \Go1."
## All custom images, characters, variables... are prefixed with "go_" (with the exception of temp variables) to avoid conflicts.
## New transitions and screens are added, whitout prefix.
## Thank you for trying these out. Please report any problem back to me on the Ashford Academy forum (https://www.henthighschool.com/ashford-academy/)

#### TO DO LIST ####
#Correct use of good / evil points
#Tweak reputation changes
#Edit some images bg colors (pool 16 / gym 16 / grounds 11)

#### SETUP ####

#Define characters
define go_rina = Character('Rina', color="#0033FF")
define go_guys = Character('Guys', color="#1E90FF")
define go_miya = Character('Miya', color="#db7093")
define go_hinata = Character('Hinata', color="#FF1493")

#Init variables
define go_HwithRina = 0
define go_HwithMiya = 0
define go_SexwithHinata = 0
#These counters are used so that a certain event triggers only after a first H scene with the same girl has been seen by the player. 
#There must be a more elegant way to code this though (perhaps using 'event.depends()'?)"

#Define transitions
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define doubleflash = MultipleTransition([True, Fade(0.1, 0.0, 0.5, color="#fff"), True, Fade(0.1, 0.0, 0.5, color="#fff"),True])

#Define the screen used for scrolling a picture (background picture to be declared first as 'go_bg')
screen scroll_screen:
    viewport:
        edgescroll (200, 500)
        mousewheel True
        add go_bg


#Declaring images

image bg go_field = "mods/Go1/screens/go_field.jpg"
image bg go_gym = "mods/Go1/screens/go_gym.jpg"

image bg go_pool3_1 = "mods/Go1/screens/go_pool3_1.jpg"
image bg go_pool3_2 = "mods/Go1/screens/go_pool3_2.jpg"
image bg go_pool3_3 = "mods/Go1/screens/go_pool3_3.jpg"
image bg go_pool3_4 = "mods/Go1/screens/go_pool3_4.jpg"
image bg go_pool4 = "mods/Go1/screens/go_pool4.jpg"
image bg go_pool5 = "mods/Go1/screens/go_pool5.jpg"
image bg go_pool6 = "mods/Go1/screens/go_pool6.jpg"
image bg go_pool7 = "mods/Go1/screens/go_pool7.jpg"
image bg go_pool8_1 = "mods/Go1/screens/go_pool8_1.jpg"
image bg go_pool8_2 = "mods/Go1/screens/go_pool8_2.jpg"
image bg go_pool8_3 = "mods/Go1/screens/go_pool8_3.jpg"
image bg go_pool9 = "mods/Go1/screens/go_pool9.jpg"
image bg go_pool10_1 = "mods/Go1/screens/go_pool10_1.jpg"
image bg go_pool10_2 = "mods/Go1/screens/go_pool10_2.jpg"
image bg go_pool11_1 = "mods/Go1/screens/go_pool11_1.jpg"
image bg go_pool11_2 = "mods/Go1/screens/go_pool11_2.jpg"
image bg go_pool11_3 = "mods/Go1/screens/go_pool11_3.jpg"
image bg go_pool11_4 = "mods/Go1/screens/go_pool11_4.jpg"
image bg go_pool11_5 = "mods/Go1/screens/go_pool11_5.jpg"
image bg go_pool12_1 = "mods/Go1/screens/go_pool12_1.jpg"
image bg go_pool12_2 = "mods/Go1/screens/go_pool12_2.jpg"
image bg go_pool14 = "mods/Go1/screens/go_pool14.jpg"
image bg go_pool15_1 = "mods/Go1/screens/go_pool15_1.jpg"
image bg go_pool15_2 = "mods/Go1/screens/go_pool15_2.jpg"
image bg go_pool15_3 = "mods/Go1/screens/go_pool15_3.jpg"
image bg go_pool17 = "mods/Go1/screens/go_pool17.jpg"

image bg go_bath1_1 = "mods/Go1/screens/go_bath1_1.jpg"
image bg go_bath1_2 = "mods/Go1/screens/go_bath1_2.jpg"
image bg go_bath1_3 = "mods/Go1/screens/go_bath1_3.jpg"
image bg go_bath2_1 = "mods/Go1/screens/go_bath2_1.jpg"
image bg go_bath2_2 = "mods/Go1/screens/go_bath2_2.jpg"
image bg go_bath3 = "mods/Go1/screens/go_bath3.jpg"
image bg go_bath4 = "mods/Go1/screens/go_bath4.jpg"
image bg go_bath5_1 = "mods/Go1/screens/go_bath5_1.jpg"
image bg go_bath5_2 = "mods/Go1/screens/go_bath5_2.jpg"
image bg go_bath5_3 = "mods/Go1/screens/go_bath5_3.jpg"
image bg go_bath6_1 = "mods/Go1/screens/go_bath6_1.jpg"
image bg go_bath6_2 = "mods/Go1/screens/go_bath6_2.jpg"
image bg go_bath6_3 = "mods/Go1/screens/go_bath6_3.jpg"
image bg go_bath6_4 = "mods/Go1/screens/go_bath6_4.jpg"
image bg go_bath6_5 = "mods/Go1/screens/go_bath6_5.jpg"
image bg go_bath7 = "mods/Go1/screens/go_bath7.jpg"
image bg go_bath8 = "mods/Go1/screens/go_bath8.jpg"

image bg go_class1_1 = "mods/Go1/screens/go_class1_1.jpg"
image bg go_class1_2 = "mods/Go1/screens/go_class1_2.jpg"
image bg go_class3 = "mods/Go1/screens/go_class3.jpg"
image bg go_class4 = "mods/Go1/screens/go_class4.jpg"
image bg go_class5 = "mods/Go1/screens/go_class5.jpg"
image bg go_class6 = "mods/Go1/screens/go_class6.jpg"
image bg go_class7 = "mods/Go1/screens/go_class7.jpg"
image bg go_class8 = "mods/Go1/screens/go_class8.jpg"
image bg go_class9 = "mods/Go1/screens/go_class9.jpg"
image bg go_class10 = "mods/Go1/screens/go_class10.jpg"
image bg go_class11_1 = "mods/Go1/screens/go_class11_1.jpg"
image bg go_class11_2 = "mods/Go1/screens/go_class11_2.jpg"
image bg go_class11_3 = "mods/Go1/screens/go_class11_3.jpg"
image bg go_class12 = "mods/Go1/screens/go_class12.jpg"
image bg go_class13_1 = "mods/Go1/screens/go_class13_1.jpg"
image bg go_class13_2 = "mods/Go1/screens/go_class13_2.jpg"
image bg go_class13_3 = "mods/Go1/screens/go_class13_3.jpg"
image bg go_class13_4 = "mods/Go1/screens/go_class13_4.jpg"
image bg go_class13_5 = "mods/Go1/screens/go_class13_5.jpg"
image bg go_class13_6 = "mods/Go1/screens/go_class13_6.jpg"
image bg go_class14 = "mods/Go1/screens/go_class14.jpg"
image bg go_class15 = "mods/Go1/screens/go_class15.jpg"
image bg go_class16 = "mods/Go1/screens/go_class16.jpg"
image bg go_class18 = "mods/Go1/screens/go_class18.jpg"
image bg go_class19 = "mods/Go1/screens/go_class19.jpg"
image bg go_class20_1 = "mods/Go1/screens/go_class20_1.jpg"
image bg go_class20_2 = "mods/Go1/screens/go_class20_2.jpg"
image bg go_class21_1 = "mods/Go1/screens/go_class21_1.jpg"
image bg go_class21_2 = "mods/Go1/screens/go_class21_2.jpg"
image bg go_class22_1 = "mods/Go1/screens/go_class22_1.jpg"
image bg go_class22_2 = "mods/Go1/screens/go_class22_2.jpg"
image bg go_class24 = "mods/Go1/screens/go_class24.jpg"

image bg go_field1 = "mods/Go1/screens/go_field1.jpg"
image bg go_field2 = "mods/Go1/screens/go_field2.jpg"
image bg go_field3 = "mods/Go1/screens/go_field3.jpg"
image bg go_field4 = "mods/Go1/screens/go_field4.jpg"
image bg go_field5 = "mods/Go1/screens/go_field5.jpg"
image bg go_field6_1 = "mods/Go1/screens/go_field6_1.jpg"
image bg go_field6_2 = "mods/Go1/screens/go_field6_2.jpg"
image bg go_field6_3 = "mods/Go1/screens/go_field6_3.jpg"
image bg go_field7 = "mods/Go1/screens/go_field7.jpg"
image bg go_field8_1 = "mods/Go1/screens/go_field8_1.jpg"
image bg go_field8_2 = "mods/Go1/screens/go_field8_2.jpg"
image bg go_field8_3 = "mods/Go1/screens/go_field8_3.jpg"
image bg go_field9 = "mods/Go1/screens/go_field9.jpg"
image bg go_field10 = "mods/Go1/screens/go_field10.jpg"
image bg go_field11 = "mods/Go1/screens/go_field11.jpg"
image bg go_field12_1 = "mods/Go1/screens/go_field12_1.jpg"
image bg go_field12_2 = "mods/Go1/screens/go_field12_2.jpg"
image bg go_field12_3 = "mods/Go1/screens/go_field12_3.jpg"
image bg go_field13 = "mods/Go1/screens/go_field13.jpg"
image bg go_field14_1 = "mods/Go1/screens/go_field14_1.jpg"
image bg go_field14_2 = "mods/Go1/screens/go_field14_2.jpg"
image bg go_field14_3 = "mods/Go1/screens/go_field14_3.jpg"
image bg go_field15 = "mods/Go1/screens/go_field15.jpg"
image bg go_field16 = "mods/Go1/screens/go_field16.jpg"
image bg go_field17 = "mods/Go1/screens/go_field17.jpg"

image bg go_grounds1_1 = "mods/Go1/screens/go_grounds1_1.jpg"
image bg go_grounds1_2 = "mods/Go1/screens/go_grounds1_2.jpg"
image bg go_grounds1_3 = "mods/Go1/screens/go_grounds1_3.jpg"
image bg go_grounds2_1 = "mods/Go1/screens/go_grounds2_1.jpg"
image bg go_grounds2_2 = "mods/Go1/screens/go_grounds2_2.jpg"
image bg go_grounds3 = "mods/Go1/screens/go_grounds3.jpg"
image bg go_grounds4 = "mods/Go1/screens/go_grounds4.jpg"
image bg go_grounds5_1 = "mods/Go1/screens/go_grounds5_1.jpg"
image bg go_grounds5_2 = "mods/Go1/screens/go_grounds5_2.jpg"
image bg go_grounds6 = "mods/Go1/screens/go_grounds6.jpg"
image bg go_grounds7 = "mods/Go1/screens/go_grounds7.jpg"
image bg go_grounds8 = "mods/Go1/screens/go_grounds8.jpg"
image bg go_grounds9_1 = "mods/Go1/screens/go_grounds9_1.jpg"
image bg go_grounds9_2 = "mods/Go1/screens/go_grounds9_2.jpg"
image bg go_grounds10_1 = "mods/Go1/screens/go_grounds10_1.jpg"
image bg go_grounds10_2 = "mods/Go1/screens/go_grounds10_2.jpg"
image bg go_grounds11 = "mods/Go1/screens/go_grounds11.jpg"

image bg go_gym1 = "mods/Go1/screens/go_gym1.jpg"
image bg go_gym2 = "mods/Go1/screens/go_gym2.jpg"
image bg go_gym3 = "mods/Go1/screens/go_gym3.jpg"
image bg go_gym4 = "mods/Go1/screens/go_gym4.jpg"
image bg go_gym5 = "mods/Go1/screens/go_gym5.jpg"
image bg go_gym6_1 = "mods/Go1/screens/go_gym6_1.jpg"
image bg go_gym6_2 = "mods/Go1/screens/go_gym6_2.jpg"
image bg go_gym6_3 = "mods/Go1/screens/go_gym6_3.jpg"
image bg go_gym7_1 = "mods/Go1/screens/go_gym7_1.jpg"
image bg go_gym7_2 = "mods/Go1/screens/go_gym7_2.jpg"
image bg go_gym7_3 = "mods/Go1/screens/go_gym7_3.jpg"
image bg go_gym8_1 = "mods/Go1/screens/go_gym8_1.jpg"
image bg go_gym8_2 = "mods/Go1/screens/go_gym8_2.jpg"
image bg go_gym9 = "mods/Go1/screens/go_gym9.jpg"
image bg go_gym10 = "mods/Go1/screens/go_gym10.jpg"
image bg go_gym11 = "mods/Go1/screens/go_gym11.jpg"
image bg go_gym12 = "mods/Go1/screens/go_gym12.jpg"
image bg go_gym13 = "mods/Go1/screens/go_gym13.jpg"
image bg go_gym14 = "mods/Go1/screens/go_gym14.jpg"
image bg go_gym15_1 = "mods/Go1/screens/go_gym15_1.jpg"
image bg go_gym15_2 = "mods/Go1/screens/go_gym15_2.jpg"
image bg go_gym15_3 = "mods/Go1/screens/go_gym15_3.jpg"
image bg go_gym15_4 = "mods/Go1/screens/go_gym15_4.jpg"
image bg go_gym15_5 = "mods/Go1/screens/go_gym15_5.jpg"
image bg go_gym16 = "mods/Go1/screens/go_gym16.jpg"
image bg go_gym17 = "mods/Go1/screens/go_gym17.jpg"

image bg go_lib1_1 = "mods/Go1/screens/go_lib1_1.jpg"
image bg go_lib1_2 = "mods/Go1/screens/go_lib1_2.jpg"
image bg go_lib1_3 = "mods/Go1/screens/go_lib1_3.jpg"
image bg go_lib2 = "mods/Go1/screens/go_lib2.jpg"
image bg go_lib3_1 = "mods/Go1/screens/go_lib3_1.jpg"
image bg go_lib3_2 = "mods/Go1/screens/go_lib3_2.jpg"
image bg go_lib3_3 = "mods/Go1/screens/go_lib3_3.jpg"
image bg go_lib3_4 = "mods/Go1/screens/go_lib3_4.jpg"
image bg go_lib4 = "mods/Go1/screens/go_lib4.jpg"
image bg go_lib5 = "mods/Go1/screens/go_lib5.jpg"
image bg go_lib6_1 = "mods/Go1/screens/go_lib6_1.jpg"
image bg go_lib6_2 = "mods/Go1/screens/go_lib6_2.jpg"
image bg go_lib6_3 = "mods/Go1/screens/go_lib6_3.jpg"
image bg go_lib6_4 = "mods/Go1/screens/go_lib6_4.jpg"

image bg go_office1_1 = "mods/Go1/screens/go_office1_1.jpg"
image bg go_office1_2 = "mods/Go1/screens/go_office1_2.jpg"
image bg go_office1_3 = "mods/Go1/screens/go_office1_3.jpg"
image bg go_office2 = "mods/Go1/screens/go_office2.jpg"
image bg go_office3 = "mods/Go1/screens/go_office3.jpg"
image bg go_office4 = "mods/Go1/screens/go_office4.jpg"
image bg go_office5 = "mods/Go1/screens/go_office5.jpg"
image bg go_office6 = "mods/Go1/screens/go_office6.jpg"
image bg go_office7 = "mods/Go1/screens/go_office7.jpg"
image bg go_office8 = "mods/Go1/screens/go_office8.jpg"
image bg go_office9 = "mods/Go1/screens/go_office9.jpg"
image bg go_office10 = "mods/Go1/screens/go_office10.jpg"
image bg go_office11_1 = "mods/Go1/screens/go_office11_1.jpg"
image bg go_office11_2 = "mods/Go1/screens/go_office11_2.jpg"
image bg go_office11_3 = "mods/Go1/screens/go_office11_3.jpg"
image bg go_office11_4 = "mods/Go1/screens/go_office11_4.jpg"
image bg go_office12 = "mods/Go1/screens/go_office12.jpg"

image go_hinata normal = "mods/Go1/chars/go_hinata_normal.png"
image go_hinata smile = "mods/Go1/chars/go_hinata_smile.png"
image go_hinata sexy = "mods/Go1/chars/go_hinata_sexy.png"
image go_hinata surprised = "mods/Go1/chars/go_hinata_surprised.png"
image go_hinata thoughtful = "mods/Go1/chars/go_hinata_thoughtful.png"


#Setting up events and conditions

init:
    $ event("go_pool1", "act == 'pool' and deviance > 15", event.choose_one('pool'), priority=200)
    $ event("go_pool2", "act == 'pool' and deviance > 15 and inhibition <90", event.choose_one('pool'), priority=200)
    $ event("go_pool3", "act == 'pool' and deviance > 25 and inhibition <90", event.choose_one('pool'), priority=200)
    $ event("go_pool4", "act == 'pool' and deviance > 75 and inhibition < 15", event.choose_one('pool'), priority=200)
    $ event("go_pool5", "act == 'pool' and deviance > 85 and inhibition < 10", event.choose_one('pool'), priority=200)
    $ event("go_pool6", "act == 'pool' and deviance > 95 and inhibition < 5", event.choose_one('pool'), priority=200)
    $ event("go_pool7", "act == 'pool'", event.choose_one('pool'), priority=200)
    $ event("go_pool8", "act == 'pool' and inhibition < 90", event.choose_one('pool'), priority=200)
    $ event("go_pool9", "act == 'pool'", event.choose_one('pool'), priority=200)
    $ event("go_pool10", "act == 'pool' and inhibition < 90", event.choose_one('pool'), priority=200)
    $ event("go_pool11", "act == 'pool' and inhibition < 80", event.choose_one('pool'), priority=200)
    $ event("go_pool12", "act == 'pool' and deviance > 75 and inhibition < 10", event.choose_one('pool'), priority=200)
    $ event("go_pool13", "act == 'pool' and behavior > 20", event.choose_one('pool'), priority=200)
    $ event("go_pool14", "act == 'pool' and deviance > 50 and inhibition < 50", event.choose_one('pool'), priority=200)
    $ event("go_pool15", "act == 'pool' and deviance > 95 and inhibition < 5", event.choose_one('pool'), priority=200)
    $ event("go_pool16", "act == 'pool' and inhibition < 90", event.choose_one('pool'), priority=200)
    $ event("go_pool17", "act == 'pool' and deviance > 95 and inhibition < 5", event.choose_one('pool'), priority=200)
    
    $ event("go_bath1", "act == 'bath'", event.choose_one('bath'), priority=200)
    $ event("go_bath2", "act == 'bath' and deviance > 25 and inhibition <90", event.choose_one('bath'), priority=200)
    $ event("go_bath3", "act == 'bath' and deviance > 50 and inhibition <50", event.choose_one('bath'), priority=200)
    $ event("go_bath4", "act == 'bath' and deviance > 25 and inhibition <50", event.choose_one('bath'), priority=200)
    $ event("go_bath5", "act == 'bath' and deviance > 75 and go_HwithMiya > 0", event.choose_one('bath'), priority=200)
    $ event("go_bath6", "act == 'bath'", event.choose_one('bath'), priority=200)
    $ event("go_bath7", "act == 'bath' and inhibition < 90", event.choose_one('bath'), priority=200)
    $ event("go_bath8", "act == 'bath'", event.choose_one('bath'), priority=200)
    
    $ event("go_class1", "act == 'class' and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class2", "act == 'class' and deviance > 90 and inhibition < 10", event.choose_one('class'), priority=200)
    $ event("go_class3", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("go_class4", "act == 'class'", event.choose_one('class'), priority=200)
    $ event("go_class5", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("go_class6", "act == 'class' and deviance > 75 and inhibition < 70", event.choose_one('class'), priority=200)
    $ event("go_class7", "act == 'class' and artistery > 20 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class8", "act == 'class' and deviance > 95 and inhibition < 5 and academics > 50", event.choose_one('class'), priority=200)
    $ event("go_class9", "act == 'class' and uniform == 'nude_uniform'", event.choose_one('class'), priority=200)
    $ event("go_class10", "act == 'class' and deviance > 75 and inhibition < 5 and artistery > 20", event.choose_one('class'), priority=200)
    $ event("go_class11", "act == 'class' and deviance > 75 and inhibition < 50 and artistery > 20", event.choose_one('class'), priority=200)
    $ event("go_class12", "act == 'class' and inhibition < 90 and artistery > 20", event.choose_one('class'), priority=200)
    $ event("go_class13", "act == 'class'", event.choose_one('class'), priority=200) 
    $ event("go_class14", "act == 'class' and deviance > 25 and inhibition < 90", event.choose_one('class'), priority=200)
    $ event("go_class15", "act == 'class' and deviance > 75 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class16", "act == 'class' and deviance > 75 and inhibition < 5 and academics > 50", event.choose_one('class'), priority=200)
    $ event("go_class17", "act == 'class' and deviance > 95 and inhibition < 5 and academics > 50", event.choose_one('class'), priority=200)
    $ event("go_class18", "act == 'class' and uniform == 'sexy_uniform'", event.choose_one('class'), priority=200)
    $ event("go_class19", "act == 'class' and deviance > 25 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class20", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("go_class21", "act == 'class' and deviance > 85 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class22", "act == 'class' and deviance > 50 and inhibition < 50", event.choose_one('class'), priority=200)
    $ event("go_class23", "act == 'class' and deviance > 25 and inhibition < 20", event.choose_one('class'), priority=200)
    $ event("go_class24", "act == 'class' and deviance > 95 and inhibition < 5", event.choose_one('class'), priority=200)
    $ event("go_class25", "act == 'class' and deviance > 25 and inhibition < 50", event.choose_one('class'), priority=200)

    $ event("go_field1", "act == 'sports_field' and deviance > 50 and inhibition < 70", event.choose_one('sports_field'), priority=200)
    $ event("go_field2", "act == 'sports_field' and deviance > 50 and inhibition < 5", event.choose_one('sports_field'), priority=200)
    $ event("go_field3", "act == 'sports_field' and athletics > 20 and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("go_field4", "act == 'sports_field' and deviance > 75", event.choose_one('sports_field'), priority=200)
    $ event("go_field5", "act == 'sports_field' and athletics > 10", event.choose_one('sports_field'), priority=200)
    $ event("go_field6", "act == 'sports_field' and deviance > 75 and inhibition < 20", event.choose_one('sports_field'), priority=200)
    $ event("go_field7", "act == 'sports_field' and deviance > 5 and inhibition < 90", event.choose_one('sports_field'), priority=200)
    $ event("go_field8", "act == 'sports_field' and athletics > 20 and inhibition < 90", event.choose_one('sports_field'), priority=200)
    $ event("go_field9", "act == 'sports_field' and morale > 15 and uniform == ('sexy_uniform' or 'nude_uniform') and inhibition < 70", event.choose_one('sports_field'), priority=200)
    $ event("go_field10", "act == 'sports_field' and deviance > 15 and behavior < 50", event.choose_one('sports_field'), priority=200)
    $ event("go_field11", "act == 'sports_field' and deviance > 70 and inhibition < 90", event.choose_one('sports_field'), priority=200)
    $ event("go_field12", "act == 'sports_field' and deviance > 95 and inhibition < 5", event.once(), event.choose_one('sports_field'), priority=200)
    $ event("go_field13", "act == 'sports_field' and deviance > 75 and inhibition < 10", event.choose_one('sports_field'), priority=200)
    $ event("go_field14", "act == 'sports_field' and deviance > 50 and inhibition < 70 and go_HwithRina>=2", event.choose_one('sports_field'), priority=200)
    $ event("go_field15", "act == 'sports_field' and athletics > 50 and inhibition < 50", event.choose_one('sports_field'), priority=200)
    $ event("go_field16", "act == 'sports_field' and athletics > 70 and deviance > 50 and inhibition < 20", event.choose_one('sports_field'), priority=200)
    $ event("go_field17", "act == 'sports_field' and athletics > 70 and deviance > 75 and inhibition < 70", event.choose_one('sports_field'), priority=200)
    
    $ event("go_grounds1", "act == 'school_grounds' and deviance > 75", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds2", "act == 'school_grounds' and morale > 15", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds3", "act == 'school_grounds' and behavior < 75", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds4", "act == 'school_grounds' and athletics > 20 and inhibition < 50", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds5", "act == 'school_grounds' and deviance > 75 and inhibition < 15", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds6", "act == 'school_grounds' and artistery > 25 and deviance > 50 and inhibition < 20", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds7", "act == 'school_grounds' and deviance > 50 and inhibition < 5", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds8", "act == 'school_grounds' and deviance > 95 and inhibition < 5", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds9", "act == 'school_grounds' and deviance > 85 and inhibition < 50 and evil_points > 0", event.choose_one('school_grounds'), priority=200)
    $ event("go_grounds10", "act == 'school_grounds' and deviance > 50 and inhibition < 75", event.choose_one('school_grounds'), priority=200)    
    $ event("go_grounds11", "act == 'school_grounds' and artistery > 50 and inhibition < 70", event.choose_one('school_grounds'), priority=200)
    
    $ event("go_gym1", "act == 'gym' and deviance > 85 and inhibition < 20", event.choose_one('gym'), priority=200)
    $ event("go_gym2", "act == 'gym' and deviance > 95 and inhibition < 50", event.choose_one('gym'), priority=200)
    $ event("go_gym3", "act == 'gym' and deviance > 75 and inhibition < 20", event.choose_one('gym'), priority=200)
    $ event("go_gym4", "act == 'gym' and deviance > 85 and inhibition < 50", event.choose_one('gym'), priority=200)
    $ event("go_gym5", "act == 'gym' and deviance > 50 and inhibition < 20", event.choose_one('gym'), priority=200)
    $ event("go_gym6", "act == 'gym'", event.choose_one('gym'), priority=200)
    $ event("go_gym7", "act == 'gym'", event.choose_one('gym'), priority=200)
    $ event("go_gym8", "act == 'gym'", event.choose_one('gym'), priority=200)
    $ event("go_gym9", "act == 'gym' and athletics > 10", event.choose_one('gym'), priority=200)
    $ event("go_gym10", "act == 'gym' and deviance > 15 and inhibition < 50", event.choose_one('gym'), priority=200)
    $ event("go_gym11", "act == 'gym' and deviance > 15", event.choose_one('gym'), priority=200)
    $ event("go_gym12", "act == 'gym'", event.choose_one('gym'), priority=200)
    $ event("go_gym13", "act == 'gym' and deviance > 15 and inhibition < 50", event.choose_one('gym'), priority=200)
    $ event("go_gym14", "act == 'gym'", event.choose_one('gym'), priority=200)
    $ event("go_gym15", "act == 'gym' and deviance > 95 and inhibition < 5", event.choose_one('gym'), priority=200)
    $ event("go_gym16", "act == 'gym' and inhibition < 75", event.choose_one('gym'), priority=200)
    $ event("go_gym17", "act == 'gym' and inhibition < 50", event.choose_one('gym'), priority=200)
    
    $ event("go_lib1", "act == 'library' and deviance > 25 and inhibition < 90", event.choose_one('library'), priority=200)
    $ event("go_lib2", "act == 'library' and deviance > 10 and inhibition < 75", event.choose_one('library'), priority=200)
    $ event("go_lib3", "act == 'library' and academics > 20", event.choose_one('library'), priority=200)
    $ event("go_lib4", "act == 'library' and deviance > 25 and inhibition < 50", event.choose_one('library'), priority=200)
    $ event("go_lib5", "act == 'library'", event.choose_one('library'), priority=200)
    $ event("go_lib6", "act == 'library'", event.choose_one('library'), priority=200)
    
    $ event("go_office1", "act == 'office'", event.choose_one('office'), priority=200)
    $ event("go_office2", "act == 'office' and deviance > 75 and inhibition < 50", event.choose_one('office'), priority=200)
    $ event("go_office3", "act == 'office' and inhibition < 90", event.choose_one('office'), priority=200)
    $ event("go_office4", "act == 'office' and deviance > 75 and inhibition < 50 and go_SexwithHinata == 1", event.choose_one('office'), priority=200)
    $ event("go_office5", "act == 'office' and deviance > 50 and inhibition < 50", event.choose_one('office'), priority=200)
    $ event("go_office6", "act == 'office' and deviance > 95 and inhibition < 5", event.choose_one('office'), priority=200)
    $ event("go_office7", "act == 'office' and deviance > 15 and inhibition < 70", event.choose_one('office'), priority=200)
    $ event("go_office8", "act == 'office' and inhibition < 50 and uniform == ('nude_uniform')", event.choose_one('office'), priority=200)
    $ event("go_office9", "act == 'office' and deviance > 50 and inhibition < 50", event.choose_one('office'), priority=200)
    $ event("go_office10", "act == 'office' and deviance > 75 and go_HwithRina>=3", event.choose_one('office'), priority=200)
    $ event("go_office11", "act == 'office'", event.choose_one('office'), priority=50)
    $ event("go_office12", "act == 'office' and deviance > 15 and inhibition < 70", event.choose_one('office'), priority=200)
    
    
    
    

#### POOL EVENTS ####

label go_pool1:
    
    $ r=renpy.random.randint(1,2)
    image bg go_pool1 = ConditionSwitch("r==1","mods/Go1/screens/go_pool1_1.jpg","r==2","mods/Go1/screens/go_pool1_2.jpg")
    
    scene bg go_pool1 with fade
    pov "Those new water sprinklers might be a bit too powerful..."
    $ inhibition-=1
    return
    
    
label go_pool2:
    
    $ r=renpy.random.randint(1,3)
    image bg go_pool2 = ConditionSwitch("r==1","mods/Go1/screens/go_pool2_1.jpg","r==2","mods/Go1/screens/go_pool2_2.jpg","r==3","mods/Go1/screens/go_pool2_3.jpg")
    
    scene bg go_pool2 with fade
    "This poor girl is always the victim of silly pranks at the pool..."
    $ deviance +=1
    $ morale-=1
    return
    
    
label go_pool3:
    
    scene bg pool with fade
    "You come to the pool late in the day, expecting everyone to be gone.\n
     Instead, you hear some moans and decide to take a look."
    
    scene bg go_pool3_1 with fade
    go_hinata "Nooo wait, ahhnn, what do you think you are doing? Ahh..."
    
    if inhibition >=70:
        "The boy fondles her tits a little more, then reluctantly let her go."
        $ inhibition -=1
        return
    
    scene bg go_pool3_2
    "The boy keeps on fondling her."
    go_hinata "Aaaaah, aah... Someone will see us..."
    boy "Is that why your nipples are getting so stiff?"
    
    if deviance < 75 or inhibition > 50:
        "The boy fondles her tits and pussy a little more, then reluctantly let her go."
        $ deviance +=1
        return        
    
    boy "Come on, let's have a bit of fun."
    go_hinata "Wait, here? Stop it already!"
    scene bg go_pool3_3 with fade
    "The boy ignores her remarks and lifts her body, shoving his penis in her wet pussy."
    go_hinata "Aaaah, hhhnnn!!!"
    "He starts slamming inside her pussy rythmically."
    go_hinata "Aaaah, you bastard... You're being so rough... Aaah, oh, hhnnn..."
    "She moans uncontrollably, caught in the pleasure of the act."
    "While banging her, he pinches her nipples and fondles her ass."
    go_hinata "Aaaaw, aaah, mmmm, aaaah..."
    boy "Mmmh baby you're so tight, I can't hold it much longer..."
    go_hinata "Aaaaaaah, wait, noooo..."
    scene bg go_pool3_4 with doubleflash
    "The boy rams his shaft into her pussy and explodes within her."
    "He puts his boxers back on with a satisfied look and leaves the girl panting on the side of the pool."
    pov "Well, that was interesting..."
    $ inhibition -=1
    $ deviance +=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5
    return


label go_pool4:
    
    scene bg go_pool4 with fade
    "Guys are having fun with this girl at the pool."
    guy "Hmmpf, don't worry babe... If we keep doing it everyday, you'll have the best body in the swimming team in no time."
    girl "Aah, if you say so... Aah, aaah..."
    $ inhibition -=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return


label go_pool5:
    
    scene bg go_pool5 with fade
    "Guys are having fun with this girl at the pool."
    "Guy 1" "Oh yeah girl, keep this sexy pose, I'm about to..."
    with flash
    "Guy 2" "Oh, me too... Shake your boobs and ass more!" 
    "Guy 3" "Yes! Take this!!!"
    with flash
    girl "Whoah!!! There's so much! How long had you guys been saving up?"
    "Guy 1" "Shut up, here I come again!"
    with doubleflash
    "Hot cum spurts all over her body and suit."
    girl "Stop it already..."
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return


label go_pool6:
    
    "Swimsuits have always been a favorite fetish with the boys. Seeing hot girls at the swimming pool everyday really messes up with their hormones."
    
    scene bg go_pool6 with fade
    "It seems like they have decided to take out their frustration on this girl."
    girl "Hmmpf, mmmh, mmmh!!!"
    "Judging by how eager she is to service every cock around her, she looks like she can handle it."
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return


label go_pool7:
    
    scene bg go_pool7 with fade
    teacher "Woah, Rina Davies set up a new record again! What's her secret?"
    $ athletics +=1
    if renpy.random.randint(1, 4) == 1:
        $ athletics +=5
    return

label go_pool8:
    
    scene bg pool with fade
    "As you enter the pool, you notice a swimming competition is starting."
    "You join a crowd of other bystanders watching from the poolside. A pretty, athelic girl in a swimsuit is standing right in front of you."
    
    scene bg go_pool8_1 with fade
    go_rina "Oh, hi [povTitle] principal! Came here to see your students performance?"
    go_rina "I'm afraid they will disappoint you. It's a pity those girls have such bad techniques... Naomi is the best swimmer, but her body is too weak..."
    "She obviously thinks she is better than all of them. She is hot, but what a vain girl!"
    
    menu:
        "They are doing their best. You should respect that.":
            pov "Not everyone can be gifted at sports. What makes you think you are so much better than everyone else?"
            "She looks at you with a pained expression."
            go_rina "Don't you know who I am? I'm Rina Davies! The fastest swimmer in school!"
            go_rina "This school should be proud to have me in its swimming team!"
            go_rina "I wish you would show more appreciation for students who achieve, \
                    instead of supporting losers..."
            "She moves away from you, sulking."
            $ athletics -=1
            return
            
        "But you are not like them, are you?":
             pov "I guess you could show them a thing or two..."
             "The girl's mood brightens as you speak."
             go_rina "Why, of course! I'm Rina Davies, the best swimmer in the team. You've heard of my achievements haven't you?"
             pov "Ah, hem, sure..."
             go_rina "Comes competition time, I will be your best asset against all the other schools."
             $ morale +=1        
             "You watch and chat with Rina for a while."
             
             menu:
                 "Stay a bit.":
                     "As the crowd grows thicker, you find yourself getting closer and closer."
                     "Soon, your bodies are touching. You can smell her hair and feel her firm body pressing against yours."
                     "You concentrate really hard, but nature has the best of you."
                     "Against your efforts, your dick hardens and starts perking under your tracksuit, rubbing against her butt."
                     if deviance <15:
                         "The girl suddenly tenses up as she feels your boner."
                         go_rina "I... I really must go now. Good bye!"
                         "She leaves in a hurry, blushing. You feel ashamed of yourself, getting turned on by a student."
                         $ morale -=1
                         return
                         
                     elif deviance <50:
                         "It must be quite obvious to her by now that you are getting hard. Still, she doesn't move away."
                         "For a few minutes of torture and lust, you can feel her firm butt pressing against your dick."
                         "She seems to be doing this on purpose. You notice her cheeks are flushed, and her nipples are perking from under her suit."
                         go_rina "All right, it's time for me to go now. See you later principal... *wink*"
                         "She leaves you red faced and frustrated."
                         $ deviance +=1
                         return
                         
                     elif deviance<95:
                         "You are pretty sure the girl is feeling your boner. Still, she makes no attempt to move away."
                         "Instead, she leans back. Ever so slowly, she grinds her butt on your already hard shaft."
                         go_rina "I'll let you in on a little secret. Do you know what makes a great swimmer?"
                         pov "Mmmh... no... *sweating*"
                         go_rina "Your whole body must be strong, not only your arms... The strenght in your legs and buttocks also helps to increase your speed."
                         pov "But... buttocks?"
                         go_rina "Oh yes... I trained hard to make mine firm and powerful. You see?"
                         "As she says that, she contracts her buttocks around your dick, through your tracksuit. You feel a jolt of pleasure across your whole body as she does that."
                         go_rina "Let me show you just how strong they are..."
                         "She moves her ass up and down, wrapping your erect cock between her buttcheeks. Boy, does she have a strong grip!"
                         pov "Hmmmpf..."
                         go_rina "You like that, don't you [povTitle] principal?"
                         pov "..."
                         "As she continues her grinding, the bell rings, ending the competition."
                         go_rina "Well, that's it for now... Thanks for being such good company! *wink*"
                         $ deviance +=1     
                         $ athletics +=1
                         if go_HwithRina < 1:
                            $ go_HwithRina = 1
                         return
                         
                     else:
                         go_rina "*giggles* Oh my, principal, you sure seem like you have a lot of energy today!"
                         "There is no use in denying it, since your hard cock is already firmly lodged between her buttocks."
                         pov "Well, guilty as charged... How could a man resist a body as hot as yours!"
                         go_rina "I feel bad, it looks like you are in pain..."
                         "Her hand reaches for your crotch as she says that."
                         "Unzipping you, she takes out your hard, burning cock from your trousers."
                         go_rina "Wow... It's so hot..."
                         "Slowly, she massages your cock while grinding her butt against it."
                         "The fabric of her swimsuit and her skin rubbing against your dickhead feels very erotic."
                         pov "Ugh..."
                         "She places your dick between her buttocks, and starts sliding her ass up and down your shaft."
                         pov "Mmmh..."
                         go_rina "You know, I train hard to be a complete athlete. Let me show you another trick..."
                         
                         scene bg go_pool8_2
                         "Trapping your dick between her thighs, she starts moving back and forth."
                         go_rina "Can you feel the strenght in my thighs? That what it means to be a real athlete..."
                         "She grinds her thighs around your dick masterfully. You can feel her getting wet through the fabric of her swimsuit."
                         "The feeling of her soft skin walling in on your cock is overwhelming."
                         "You can feel your hard cock rubbing against her crack. Her juices flow through her swimsuit, lubricating your cock."
                         "She increases her pace and contracts her tighs even more. You feel that you will soon be at your limit."
                         pov "Ooooh..."
                         "As she brings you close to heaven, your instincts take over. You grab her tits fiercely, pinching her nipples through her swimsuit."
                         
                         scene bg go_pool8_3 with doubleflash
                         pov "Aaah!!!"
                         go_rina "Kyaaaai!!!"
                         "You come hard all over her legs. She looks at the gooey mess you left, panting."
                         go_rina "You came... Such a naughty man..."
                         "Some of your cum has spurted over the back and butt of a girl that was standing in front of you two."
                         girl "Uh? Who is splashing water on me?"
                         "You decide to hightail it before she realizes what has been going on."
                         go_rina "Good bye [povTitle] [povLastName]... See you next time..."
                         
                         $ deviance +=1
                         $ athletics +=1
                         if go_HwithRina < 1:
                            $ go_HwithRina = 1
                         if renpy.random.randint(1, 2) == 1:
                                $ deviance +=1
                         return
                         
                 "Time to go.":
                     "The crowd is getting thicker and noisier. You decide you have seen enought and politely say good bye to Rina."
                     go_rina "Good bye [povTitle] [povLastName]! Come back any time!"
                     return


label go_pool9:
    
    scene bg go_pool9 with fade
    "Waitresses from the cafetaria have come at the pool to serve drinks and ice cream to the thirsty students. Such a nice idea!"
    $ morale +=1
    return


label go_pool10:
    
    scene bg go_pool10_1 with fade
    "You see Rina, leader of the swimming team, doing warm-ups before practice."
    go_rina "Oh, hi [povTitle] [povLastName]!"
    "You decide to give her a word of encouragement."
    menu:
        "Great job!":
            pov "Great job, Rina! You are a very promising athlete."
            "Rina is beaming with pride."
            go_rina "Thank you, sir! I do my best!"
            "You watch her exercise for a while, finding it hard to concentrate on anything else."
            $ morale +=1
            return
        
        "Come on, you can go lower than that!":
            pov "Try harder, I'm sure you can go even lower!"
            go_rina "You think so? But I cannot bend my back anymore..."
            pov "Here, let me help you."
            "You grab her by the shoulders and start pushing her down."
            "You are doing this to help her improve, of course. Still, you can't help but appreciate the feeling of her smooth skin under your palms."
            if athletics < 50:
                go_rina "Aaah, *pant*, Awww, *pant*, no... It's too hard!"
                "She doesn't seem to be able to go any lower, and so you stop. You both look rather disappointed."
                $ morale -=1
                
            else:
                "You push her down, and, inch by inch, she manages to reach all the way to her toes."
                scene bg go_pool10_2
                go_rina "*panting* Han, han..."
                pov "You did it! Well done!"
                go_rina "Thanks... I couldn't have done it without your help!"
                $ athletics +=1
                if renpy.random.randint(1, 2) == 1:
                    $ athletics +=5
                "During her efforts, her swimsuit has slipped a little. You can now make out the shape of her crotch, outlined by the fabric of her swimsuit."
                if deviance < 15:
                    "Embarrassed, she quickly adjusts her bathing suit and rises up."
                    go_rina "Thank you [povTitle] [povLastName], I have to go practice now."
                    $ morale -= 1
                    
                elif deviance < 75:
                    "Feeling the intensity of your stare, she blushes."
                    "However, she keeps the pose for a little bit longer, giving you a nice view."
                    pov "..."
                    go_rina "I... I have to go practice now. Thanks for your help. It was... nice of you."
                    $ inhibition -= 1
                
                else:
                    "She notices you are staring at her, but makes no effort to hide herself."
                    go_rina "Here, let me see if I can still bend over a bit more..."
                    "She keeps bending her body, bouncing her boobs from left to right. She moans in an exagerated manner as she goes."
                    go_rina "Mmmh, aaah, mmmmh..."
                    "This is rather erotic..."
                    "Before your hungry eyes, she pulls up her swimsuit with one hand, outlining her crack and giving you a glimpse of her pussy lips. How lewd..."
                    go_rina "Do you like what you see, [povTitle] [povLastName]?"
                    pov "I... Ahem..."
                    go_rina "*giggle* Well, I have to go practice now. I'm glad that you enjoyed the show though *wink*"
                    $ deviance +=1
            return
      
label go_pool11:
    
    #Panning up and down
    scene bg go_pool11_1:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 1.0 xalign 1.0 yalign 1.0
        pause 1.0
        linear 1.0 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(5.0)
    $ go_bg=ImageReference("bg go_pool11_1")    
    show screen scroll_screen

    "You see Rina, the girl from the swimming team, standing there in a skimpy bikini."
    go_rina "Hi [povTitle] [povLastName]..."
    pov "Oh hi there! Is that swimsuit new?"
    go_rina "..."
    menu:
        "What's wrong? You look gorgeous in it.":
            if deviance < 15:
                pov "I think you look stunning..."
                go_rina "Oh, come on! Are you going to make that kind of comments too now? Leave me alone!"
                "She's pissed. You quickly back off..."
                $ morale -=1
                hide screen scroll_screen
                
            elif deviance < 50:
                go_rina "Ah, mmm, thanks. You don't think it's a bit too much for the public pool?"
                pov "No, of course not. Just wear whatever you're confortable with."
                "She lightens up a little."
                go_rina "Thanks, [povTitle] principal! I bought it because it's got a good design for swimming, but it is a bit revealing... I was \
                         afraid of what people would say..."
                pov "Never mind what they say. You look great in that swimsuit."
                go_rina "Why, thank you! Well, just don't stare so much, okay? *smile*"
                "You realize you've been checking her out the whole time. Reluctantly, you stop."
                pov "(I sure would like a piece of that...)"
                $ morale +=1
                hide screen scroll_screen
                
            elif deviance < 90 or inhibition > 10 or go_HwithRina == 0:
                go_rina "*smile* Oh, stop it [povTitle] principal..."
                pov "I mean it... All the boys around here are staring at you. You look amazing."
                go_rina "Gee, thanks... I bought it for the upcoming competition, you see..."
                go_rina "But well, I guess it can't be helped if it makes the boys stare..."
                go_rina "Should I make a sexy pose to impress them even more? *giggle*"
                "Looking into your eyes, she proceeds to take various poses, like a lingerie model on a catwalk. She walks around you, moving her hips 
                 sensually, showing off her gorgeous boobs and ass..."
                pov "(Damn, I wish I had my camera.)"
                "Boys around the pool go wild, whistling and making catcalls. She laughs, turns around and wink at you. Somehow, you know she is doing all of this because 
                 you're watching her."
                go_rina "Ahah, look at them! Anyway, I will go now before I cause a riot. I will see {i}you{/i} later, [povTitle] principal! *giggle*"
                $ inhibition -= 1
                hide screen scroll_screen
                
            else:
                pov "I must say, you are very sexy in this outfit."
                go_rina "Oh, principal, what a direct thing to say! You... You really think so? *smile*"
                "You look at her wonderful body, beautifully outlined by her sexy bikini."
                pov "(Great ass... Big, firm tits... And such a cute face...)"
                pov "(If I wasn't the principal...)"
                "As you shamelessly check her out, she giggles and gives you a daring look."
                go_rina "Oh, [povTitle] principal, you are looking at me with such hungry eyes... You wouldn't be forming any bad thoughts, now, would you?"
                "She pulls herself closer to you, her voice turning into a sexy whisper. You feel her hand lightly caress your boxers, brushing against your dick."
                go_rina "Are you getting hard just watching me..."
                pov "All right, that's it! Young lady, you are coming with me."
                "You grab her hand and lead her away from the pool. Your serious tone is giving her pause. Did she go too far? Is she about to be disciplined?"
                "She follows you into a corner of the pool, behing a large, decorative rock."
                go_rina "*worried* [povTitle] [povLastName]? Is it okay? What is this ab..."
                "Without a word, you grab her and forcefully kiss her. She moans in surprise, but you slip your tongue into her mouth, muffling her."
                go_rina "Mmmpf, aaaah, mmmh..."
                "She doesn't put on any struggle. After a few moments she is kissing you back passionately."
                "You use your hands to pull her against you, grabbing and squeezing her ass."
                go_rina "Ah! <3"
                "Pulling back for a moment, you see her looking back at you with lust and anticipation."
                pov "You've been teasing me for way too long... Now, you're gonna get what's coming to you!"
                
                hide screen scroll_screen
                
                scene bg go_pool11_2 with fade
                "You rip your boxers off and roughly push her down on the rock."
                go_rina "Oh, [povTitle] [povLastName]... You really got me pinned down this time... *blush*"
                "She looks into your eyes with desire, and whispers in your ear."
                go_rina "Just do anything you want to me, principal... I want you inside me, I want it so bad..."
                "She is grinding her hips, rubbing herself against your dick. You can feel her moistness spread through the fabric of her swimsuit."
                pov "All right babe. You better get ready, because here I come!"
                
                scene bg go_pool11_3
                "You pull her swimsuit to the side and enter her in one swift move."
                go_rina "Aaaah!!!"
                "She is already wet and you slide in her pussy with ease."
                "You start moving inside her, slipping in and out of her wet pussy."
                pov "You like that, don't you! Naughty girl..."
                go_rina "Yes!"
                "You ram your dick into her violently, making lewd slushing noise as you stretch her wet pussy."
                go_rina "Oooh, you're pounding me, I love it!"
                go_rina "*panting* Ahn, ahn, ahn..."
                "You rip off her top and bite one of her nipples. She cries out in a mix of pain and pleasure."
                go_rina "Aaaw, oooh..."
                "She uses her hips to fuck you back, contracting her pussy around your burning cock."
                go_rina "Fuck me... Fuck me hard..."
                pov "Oooh... This is too good..."
                "You fuck her furiously, increasing your speed and turning her moans into lustful cries."
                go_rina "Aah, aahhhahhhh!!!"
                pov "Now take that, aaarrrrh!!!"
                
                scene bg go_pool11_4 with doubleflash
                "You grab her butt and push your dick as deep as possible into her wet pussy, coming hard."
                pov "Hmmmpf!!!"
                "She moans sexily with every spurt of cum unloading inside her."
                go_rina "Aah, aaaah! Your hot cum... it's filling me... It feels so... good..."
                "You rest your sweaty body on top of her, breathing in her neck."
                
                scene bg go_pool11_5                
                "She hugs you tight, caressing your hair and neck."
                go_rina "Oh, [povTitle] principal, you have really spoiled me today..."
                "Unconsciously, she is still moving her hips back and forth. Your cock is still firmly lodged into her tight pussy."
                "The scents of her skin and sweat mix with the strong smell of your love juices. You feel her erect nipples rubbing against your chest, and her wet 
                 pussy contracting in spasms around your manhood."
                "After only a few moments, you feel your vigor return."
                go_rina "It's... it's getting hard again?"
                "You start licking her nipples and squeezing her ass once more. She moans in pleasure as your dick hardens and you slowly start moving in and out of her again."
                go_rina "Aaah... You still... Aaaah!!!"
                pov "Mmmh, hmmpf..."
                "Sucking on her nipple, you increase your pace and fuck her furiously."
                go_rina "Ah, oh, aaah, you're, aah... you're ripping me... aah... appart!"
                "Your dick is now harder than ever before. You nail her down with long, violent thrusts, while kneading her ass."
                "Her juice and your cum spurt out of her pussy with every movement, making dirty noises."
                "Rina grinds her hips like crazy and starts screaming."
                go_rina "Ah yes, YEEES! FUCK ME PRINCIPAL, AAH, FUCK ME HARDER!"
                "She is being so loud now that someone must have heard you, but you couldn't care less at this point."
                pov "Ohh..."
                "You moan as you ram your cock into her one last time, reaching an exploding orgasm."
                
                scene bg go_pool11_4 with doubleflash
                go_rina "AAAAAAAAAAAHH! YEEEEEEES, YES!!!"
                "Rina comes at the same time as you, her pussy twitching around your dick."
                pov "Hmmmmpf, AAaaaarrrrr!!!"
                "You burst into her pussy, filling her with loads and loads of cum."
                "Love juices come gushing out of her cunt, splashing on the floor with lewd noises."
                go_rina "I'm... so full... My pussy is filled up with your wonderful, hot cum..."
                
                scene bg go_pool11_5 with fade
                "She gives you a long, deep kiss, before she reluctantly lets you slide out of her."
                pov "We should probably go before someone comes to check on the noise..."
                "You fix your boxers and take a final look at her before leaving. She is panting, laying down in a pool of cum, her tits exposed and her legs spread appart."
                pov "What a sight..."
                
                $ deviance +=1
                if go_HwithRina < 2:
                    $ go_HwithRina = 2
                if renpy.random.randint(1, 2) == 1:
                    $ deviance +=1
            return
                
        "Anyway, I gotta go.":
            if inhibition > 30:
                "She seems uncomfortable, so you decide to leave her alone."
            else:
                "As you leave, you notice many boys are staring intensely at Rina. You even overhear some dirty jokes. Rina stands here blushing, even as \
                 a dozen boys undress her with their eyes."
                $ inhibition -= 1
            
            hide screen scroll_screen
            
            return

label go_pool12:
    
    scene bg go_pool12_1 with fade
    
    "What's this? A girl is by the pool, sitting down on her boyfriend. Upon closer inspection, you realize something is going on."
    girl "So annoying... Why do you insist on putting me in such an embarrassing position?"
    guy "Come on, you agreed to do this... You know how I am when I see you in your swimsuit... It makes me so horny..."
    girl "*sigh* All right, just one minute then, that's all that we agreed!"
    "The girl lowers herself between his legs. The guy takes his erect cock and slides it between her buttcheeks, under the fabric of her swimsuit."
    "The girl awkwardly moves back and forth, masturbating him with her ass."
    girl "Is this all right?"
    guy "...yes... it's good... Mmmh, keep going..."
    "She continues moving her hips and ass, grinding her butt on his cock. He seems totally lost in a world of pleasure."
    guy "Ah yes... That's perfect..."
    girl "Okay, that's enought. I think we should stop. You've had your..."
    
    scene bg go_pool12_2 with vpunch
    with flash
    guy "Hooaaah!!!"
    girl "Whaaat?"
    "Unable to resist the caress of her smooth butt, the guy comes fast and hard, spurting gooey cum all over her suit and ass."
    with doubleflash
    girl "Noooo! Look what you did... You're the worst!"
    
    $ inhibition -=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance +=1
    return
    
    
label go_pool13: #To be merged with vanilla event "pool3"?
    
    $ r=renpy.random.randint(1,2)
    image bg go_pool13 = ConditionSwitch("r==1","mods/Go1/screens/go_pool13_1.jpg","r==2","mods/Go1/screens/go_pool13_2.jpg")
    
    scene bg go_pool13 with fade
    "It's clean up day! Hurray!"
    pov "Keep up the good work girls!"
    $ behavior += 1
    return


label go_pool14:
    
    scene bg go_pool14 with fade
    
    "Those girls have lost a bet with the boys from the swim team..."
    go_guys "Come on, bitches! Show us more!"
    girl1 "This is so embarrassing..."
    go_guys "That's it! Now spread your legs appart! Hurry up or we will fuck you, right here, right now!"
    girl2 "*sob* Noooo! Let me out of here..."
    return
    
    
label go_pool15:
    
    "After practice, you hear voices coming out from the girls shower room. Hiding yourself, you take a peek."
    
    scene bg go_pool15_1 with fade
    
    girl "We can't do this here! Someone will come!"
    guy "Come on honey, I've been watching you, waiting for this all day... I'm on fire! I need to stick it in, right now."
    "The guy plays with her ass and releases her boobs from her swimsuit."
    "Pulling up the crotch of her swimsuit, he starts pressing his hard cock against her butthole."
    girl "Wait, what are you doing! Not there!"
    guy "Don't worry babe... The water will make it slip right in..."
    girl "Nooooooo!!!"
    "Ignoring her protests, he slides his rock-hard cock into her ass."
    "At first, it doesn't look like it's going to fit. Yet, slowly, he streches out her asshole and inches his dick deeper into her butt."
    "The girl moans in pain as he fucks her ass raw, pushing her face and tits against the wall."
    girl "Aaaah, aaaah, aaaah!"
    "After a while, pain disappears from her voice and her moans become more erotic. She starts masturbating with one hand while her ass is being abused."
    "It looks like she's beginning to like this."
    girl "Mmmh, aaah, mmmh..."
    guy "Urgh... I'm at my limit... Watch out!"
    
    scene bg go_pool15_2 with doubleflash
    "He slams his cock deep into her ass and cums hard inside her."
    guy "Aaaaaarrrrh!!!"
    girl "Aaaaaaaaaaah!!!"
    "She screams as he takes out his cock from her butt and unloads the rest of his cum all over her body."
    
    scene bg go_pool15_3 with flash
    "Her ass makes gross noises as thick cum comes gushing out of it, sliding down her slit and dripping on her thighs."
    guy "Hehe... I like you better when you're covered in jizz..."
    girl "...you jerk..."
    
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance +=1
    
    return
    
label go_pool16:
    
    image bg go_pool16 = ConditionSwitch("inhibition>50","mods/Go1/screens/go_pool16_1.jpg","inhibition<=50 and inhibition>20","mods/Go1/screens/go_pool16_2.jpg","inhibition<=20","mods/Go1/screens/go_pool16_3.jpg")

    #Panning up and down
    scene bg go_pool16:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 1.0 xalign 1.0 yalign 1.0
        pause 0.5
        linear 1.0 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(4.0)
    $ go_bg=ImageReference("bg go_pool16")    
    show screen scroll_screen
    
    if inhibition > 70:
        "When the locker room is full, some girls do not hesitate to change in plain sight."
    elif inhibition > 30:
        "Some girls now choose to go topless at the pool."
        girl "I feel a lot freer now..."
    else:
        "Why bother with a swimsuit at all? Some girls now go completely naked at the pool, unafraid to display their goods for all the world to see."
        girl "I love the feeling of liquid running all over my naked skin..."
    
    pov "Kinky..."
    
    $ inhibition -= 1
    hide screen scroll_screen
    
    return
    
    
label go_pool17:
    
    scene bg go_pool17 with fade
    
    "Relaxing by the poolside, being pleasured by twins... Your definition of a perfect day!"
    
    $ inhibition -=1
    $ deviance +=1
    if renpy.random.randint(1, 3) == 1:
        $ deviance +=1
    
    return


#### BATH EVENTS ####

label go_bath1:
    
    scene bg go_bath1_1 with fade
    "While walking around the baths, you hear a woman voice, humming... You decide to take a peek."
    go_hinata "Aaaah... A hot bath is so relaxing..."
    "What do you do?"
    
    menu:
        "Stay a bit longer to see what happens.":
            scene bg go_bath1_2
            go_hinata "Uh? Is someone there?"
            "After a few minutes, you accidentally make a noise and the girl realizes she's being watched."
                        
            if inhibition >= 90:
                $ morale -=1
                go_hinata "Whaaaat! Go away you pervert!!!"
                
            else:
                go_hinata "Oh, [povTitle] [povLastName]! What are you doing here?"
                "Feeling foolish, you mumble something about checking the towel supply and leave quickly."
                $ inhibition -=1
            return
            
        "Leave quietly before she notices you.":
            $ morale +=1
            return
        
        "Spoil her fun." if evil_points >= 1 and deviance > 15 and inhibition < 90:
            "You enter the room and close the door behind you."
            go_hinata "[povTitle] [povLastName]? What is this about?"
            pov "Well, I'm just looking for the bathroom."
            "Not giving her time to answer, you unzip your pants and take out your dick."
            "You start peeing in her bath."
            scene bg go_bath1_3
            pov "*whistle*"
            go_hinata "Wait, no!!!"
            if deviance > 80:
                go_hinata "..."
                go_hinata "It's so... warm..."
                $ deviance += 1
                return
            else:
                go_hinata "Nooo!!! You're so mean..."
                $ morale -= 1
                $ evil_points += 1
                return
        
        

label go_bath2:
    
    scene bg go_bath2_1 with fade
    "Entering the baths, you hear girls giggle."
    "Blonde girl" "Gee, honey, yours are so soft and smooth... No wonder the boys always stare at you!"
    "Blue haired girl" "That's... That's not..."
    "Redhead" "Heehee, look at your nipples! They're getting hard!"
    "You decide to make your presence known."
    menu:
        "Come on, girls, this is a public place, not a playground!":
            "The girls blush and excuse themselves. Frowning, they sink their bodies into the water and go quiet."
            pov "It's a pity to miss out on such hot bodies... But we gotta have some discipline."
            $ behavior +=1
            $ morale -=1
            return
        "Hello there, having fun?":
            if inhibition >60:
                girls "Oh, hi [povTitle] [povLastName]. Sorry, we didn't mean to be noisy!"
                "Seeing you, the girls blush and hide their bodies. Too bad you had to interrupt..."
                $ inhibition -=1
                return
            elif inhibition > 70 or deviance<15:
                girls "Hi [povTitle] [povLastName], nice of you to come by!"
                "The girls keep playing in the water, flaunting their luscious bodies and oblivious to your presence."
                "After a while you decide to go. You're quite sure one of the girls noticed your raging hard-on..."
                "Blonde girl" "Bye [povTitle] [povLastName]... Come back to see us sometime! <wink>"
                $ morale +=1
                $ inhibition -=1
                return
            else:
                "Blonde girl" "Oh, it's [povTitle] [povLastName] again!"
                "Blue haired girl" "Hi... [povTitle] [povLastName]..."
                "Redhead" "It's very good you're here! Come on, tell us, do you like my friend's tits?"
                menu:
                    "What! What kind of question is that!":
                        "The girls giggle and they resume their playing."
                        pov "Kids these days..."
                        $ behavior +=1
                        return
                    "Well, sure!":
                        pov "You have very nice breasts indeed, young lady."
                        "Redhead" "You hear that girl! The principal likes us... Show him more!"
                        "Blue haired girl" "I... Wait..."
                        "The other girl grabs her boobs and squeezes them while you watch. Ami cries out and makes feeble attempts at resisting her friend, \
                         but you can see her nipples getting quite erect as you watch her."
                        pov "Well girls, thanks for the show!"
                        $ deviance +=1
                        $ inhibition -=1
                        return
                    "Mmmh, I don't know, I'd have to see more..." if deviance>75: 
                        pov "But I have to see more to make up my mind..."
                        "Blonde girl" "You only need to ask..."
                        "She starts flaunting her boobs while pinching Ami's nipples."
                        "Blue haired girl" "Aaah..."
                        "Redhead" "Of course [povTitle] [povLastName], we'll put on a good show just for you!"
                        "She spreads her legs wide open, giving you a good view of her hot pussy and thighs."
                        "You are getting seriously aroused from watching this."
                        "Blonde girl" "[povTitle] [povLastName], you seem to be having a 'hard' time... Why don't you take it out and show some appreciation for our show?"
                        "Not needing any further encouragement, you take out your erect cock and start jerking off in pace with their bouncing breasts."
                        "The girls continue fondling and masturbating each other in abandon."
                        "Redhead" "Oh yes, [povTitle] [povLastName], keep going..."
                        "Blonde girl" "Aaah, principal, watching your hot cock is making me so horny!"
                        "Blue haired girl" "It's... swollen... so big..."
                        "As you watch the lewd girls grind against each other, you cannot endure it and longer, and cum with great force."
                        
                        scene bg go_bath2_2 with doubleflash
                        "Blonde girl" "Yes, yeeeeees!!!"
                        "Blue haired girl" "Oooooooooh!!!"
                        "Redhead" "Aaaaaaah!!!"
                        with flash
                        "Blue haired girl" "Aww... So sticky..."
                        $ deviance +=1
                        $ inhibition -=1
                        if renpy.random.randint(1, 2) == 1:
                            $ deviance +=1
                        return

label go_bath3:
    
    scene bg go_bath3 with fade
    "Looks like some girls are experimenting with their bodies..."
    "Blue haired girl" "Mmmh..."
    "Redhead" "Aaah, that's it, use more tongue!"
    "Blonde girl" "Aaah, I think I'm about to go..."
    "You don't have the heart to interrupt them."
    $ deviance +=1
    $ inhibition -=1
    return

label go_bath4:
    
    scene bg go_bath4 with fade
    "The bath helps students relax... and become closer."
    girl "You don't mind if I lean against you?"
    guy "Woah, senpai... No, I, ahem..."
    girl "Hey! Wait a minute..."
    girl "What's this I feel rubbing against my back?"
    guy "S-Sorry senpai... I'm not... I didn't mean to..."
    girl "*giggles*"
    $ deviance +=1
    return

label go_bath5:
    
    "While in the baths, you ran into Miya from the tennis club."
    
    scene bg go_bath5_1 with fade
    go_miya "Oh, [povTitle] principal, you are so naughty! *smiles*"
    pov "Come on, it's your own fault; how can a man resist such a sexy body?"
    go_miya "Is that so? I'm very sorry to be such a bother... Is there any way I could make it up to you?"
    pov "Well sweetie, I'm glad you asked..."
    
    scene bg go_bath5_2 with fade
    go_miya "Aah, [povTitle] principal, I feel it, aaaah, it's too big!"
    pov "Just relax, girl, I'm going to take it slow."
    "She's already very wet, and your cock starts sliding in and out of her with ease."
    go_miya "Mmmh, ah, mmh... Aaaaaah!"
    "Her moans get louder and louder."
    go_miya "Ooh yes, oh, harder, HARDER!!!"
    "Someone will definitely hear you, but none of you care."
    "You increase your pace. You can feel your shaft hit her womb hard everytime you slam into her."
    pov "...you like that you little slut, don't you?"
    go_miya "Oh, yes [povTitle] principal, keep going, rape me with your large cock!"
    "You feel close to climax. As you keep ramming into her, her vagina contracts strongly around your cock, making you feel fantastic."
    pov "So... tight... Hmmpf!"
    
    scene bg go_bath5_3 with flash
    "You explode your load into her."
    with doubleflash
    go_miya "Aaah, aah, ah..." 
    go_miya "You came a lot..."
    "She looks with dreamy eyes at your cum, leaking out from her wet pussy."
    pov "Thank you sweetie. That was heaps of fun!"
    go_miya "Thank you sir! Please, let me clean you up before you go. *wink*"
    "This school has really become a wonderful place."
    $ deviance +=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance +=5
    return

label go_bath6:
    
    scene bg go_bath6_1 with fade
    "This girl is too shy to go nude into the public baths."
    pov "Well, this is pity since she seems to have such a great body... Maybe I should say something to her?"
    menu:
        "That's fine, it's okay to be shy.":
            pov "Well, modesty is a virtue. You can wear anything in the baths, as long as you feel all right with it."
            girl "Thank you sir. I just don't like being stared at... *blushing*"
            $ morale +=1
            $ inhibition +=1
            return
            
        "What are you ashamed of?":
            pov "You're very pretty you know. Why do you hide your body like you are ashamed of it?"
            if deviance < 15:
                girl "Wh... What? But.. but Sir, you cannot talk to students like that!!!"
                "She is offended. You feel you might have gone a bit too far."
                $ morale -= 1
                return
            elif inhibition > 50:
                "She blushes and seems unhappy with your comment."
                $ morale -= 1
                return
            else:
                girl "Thank you, I... I know I should be more open-minded... But I'm not confortable being naked around others yet. Maybe in time..."
                $ inhibition -=1
                return
        
        "Unacceptable. This is a bath, not the swimming pool!":
            pov "Why are you wearing a bathing suit? Don't you have any hygiene? This is a public bath, and all clothing must be checked in the locker room!"
            girl "But... but sir!"
            menu:
                "Give her a break.":
                    pov "I'll let you off this time. But you've been warned."
                    girl "Thank you sir..."
                    $ behavior +=1
                    return
                "Punish her.":
                    if deviance <25:
                        pov "You are to leave the baths immediately. I can't accept unhygenic behavior in this school."
                        girl "..."
                        "She excuses herself, picks up her stuff and leaves, her eyes full of tears."
                        $ behavior +=1
                        $ morale -=1
                        return
                    else:
                        pov "Well young lady, it seems to me you need to learn more about hygiene."
                        girl "What... what do you mean?"
                        pov "As punishment for your disrespectful behavior, you shall have to wash my back."
                        girl "Wash your... WHAT?"
                        pov "You heard me. Or perhaps you would prefer to take off your swimsuit right now \
                        and conform with the rules?"
                        girl "...no... okay..."
                        scene bg go_bath6_2 with fade
                        girl "Aaah..."
                        pov "That's good, scrub it well."
                        girl "*sigh*"
                        pov "Good, good, put some more soap."
                        girl "Okay..."
                        pov "And do my chest too. I need to be perfectly clean."
                        "Reluctantly, she reaches around your shoulders and washes your chest as well."
                        "You take that opportunity to lean back against her. As a result, her tits start rubbing lightly against your \
                         back every time she moves."
                        "You can feel her getting tense, but she doesn't back off. She continues scrubbing your chest dutifuly, her boobs pressing against you. \
                         After a little while, you can actually feel her nipples perk against the fabric of her swimsuit."
                        if deviance <=75:
                            "This is fun, but you feel you have to stop, as you would rather not get caught. Even if she is a gullible one, \
                             other people might see through your little ploy and it would damage your reputation."
                            pov "All right, thank you. I hope you will remember this lesson well."
                            "She looks relieved that it is over, but a little flushed as well. Her nipples are still erect, and you \
                             notice she is slowly rubbing her thighs together."
                            girl "Thank you sir. I... I will."
                            $ inhibition -=1
                            $ deviance +=1
                            return
                        else:
                            "You wonder if you could push your luck further..."
                            pov "All right, come around. You need to clean the rest of my body."
                            girl "..."
                            "Obedient, she comes around and kneels in front of you."
                            pov "That's it, wash my legs now..."
                            "The feeling of her soft, soapy hands running on your legs and thighs quickly gives you a raging hard-on."
                            "The girl avoids staring directly at your boner, but you can see her giving side looks from time to time."
                            "Her cheeks are flushing. She is absent-mindedly biting her lips."
                            pov "Have you ever seen a man before?"
                            girl "..."
                            girl "Not... not this close..."
                            pov "You can look at it, don't be embarrassed. After all, you will need to clean it next."
                            "The girl blushes even more, but doesn't protest. Intead, she shyly looks at your erect cock."
                            "Slowly, she slides her soapy hands up your thighs and towards your crotch."
                            
                            scene bg go_bath6_3 with fade
                            "She starts lightly touching your balls and shaft."
                            girl "Is... is this okay?"
                            pov "Oh, yes. Make sure to clean it well."
                            "She starts caressing the rest of your cock softly, as well as the head and balls."
                            "After a while, her touch becomes firmer and less hesitant. She is looking at your cock intensely, as if detailing \
                             every inch of it and commiting it to memory."
                            "You feel ready to take it a little further."
                            pov "There is an even better way to clean it, you know. Perhaps you would like to learn it?"
                            girl "..."
                            pov "Here, take it in your mouth and lick it clean."
                            "You are pretty sure she was expecting this. With only a moment of hesitation, she opens her mouth wide and wraps \
                             your hard cock between her lips."
                            
                            scene bg go_bath6_4
                            "She seems unsure of what she is doing at first, merely sliding your cock into her mouth repeatedly." 
                            "But she quickly finds her own pace, making you feel really good. She starts using her tongue as well."
                            pov "Hmpf, you're good at this..."
                            "The girl doesn't say anything, but she looks pleased."
                            "Making dirty, slurping sounds, she sucks on your cock harder and harder. Sometimes she stops and licks your balls, or \
                             play with her tongue around the tip of your shaft."
                            girl "There's... there's something coming out..."
                            pov "Yes, it is called precum. Try and lick it, see if you like the taste."
                            "She obediently licks the head of your shaft clean. She frowns a little at the taste, but doesn't stop her sucking."
                            girl "Mmmh, mmmh..."
                            pov "I'm at my limit... Hmmmpf..."
                            pov "Here I come!!!"
                            
                            scene bg go_bath6_5 with flash
                            girl "Mmmmmmh!!!"
                            with flash
                            "She is surprised by your orgasm and attempts to move her head back, but you quickly grab her hair and force your cock \
                             down her throat."
                            pov "Don't spill it. You wouldn't want us to get dirty again now, would you?"
                            "She makes muffling sounds as your cum drips down her throat and mouth."
                            "After you're spent, you slowly take your dick out of her mouth, rubbing it against her lips and cheek."
                            "She is coughing, gasping for air. Cum drips from her lips and onto her boobs, staining her bathing suit. The scent floats heavily \
                             in the air."
                            pov "And this concludes our lessson for today. Now, go and clean up your face. You have got cum all over it."
                            girl "..."
                            $ deviance +=1
                            $ morale -=1
                            if renpy.random.randint(1, 2) == 1:
                                $ deviance +=5
                        return
    

label go_bath7:
    
    scene bg go_bath7 with fade
    "This girl likes that boy a lot. She follows him around everywhere... even in the baths!"
    guy "...and I was like, give me the freakin' ball, dude! And then..."
    "Will he ever notice?"
    $ inhibition -=1
    return

label go_bath8:
    
    scene bg go_bath8 with fade
    "The teachers too can enjoy the baths."
    $ r = renpy.random.randint(1,3)
    if r == 1:
        teacher "...and I caught him hiding an adult magazine in his textbook..."
    elif r==2:
        teacher "...he's handsome, but relationships at work are no good..."
    elif r==3:
        teacher "...these two are dating, I assure you..."
    $ morale +=1
    return


#### CLASS EVENTS ####

label go_class1:  #This event would go well with a 'no panties' policy
    
    scene bg go_class1_1 with hpunch
    "You accidentally bump into the girl who was collecting the tests."
    girl "Aaaw!"
    "She falls on all four and drops her papers."
    "While she crawls around picking up the tests, you notice that she is not wearing any underwear."
    pov "(Nice buttocks... I sure wouldn't mind a piece of that ass!)"
    scene bg go_class1_2
    girl "Aaaah, [povTitle] [povLastName], don't look!!!"
    "She quickly gathers the remaining papers and leaves, blushing redder than ever."
    $ inhibition -=1
    return
    
    
label go_class2:
    
    $ r=renpy.random.randint(1, 3)
    
    image bg go_class2_1 = ConditionSwitch("r==1","mods/Go1/screens/go_class2_1.jpg","r==2","mods/Go1/screens/go_class2_3.jpg","r==3","mods/Go1/screens/go_class2_5.jpg")
    image bg go_class2_2 = ConditionSwitch("r==1","mods/Go1/screens/go_class2_2.jpg","r==2","mods/Go1/screens/go_class2_4.jpg","r==3","mods/Go1/screens/go_class2_6.jpg")
    
    if r==3:
        $ msg= "in her mouth."
    else:
        $ msg= "on her face."
        
        
    scene bg go_class2_1 with fade
    "One of the senior girl you've met before offers to service you."
    girl "Well, [povTitle] [povFirstName], we are having a lot of fun in this school thanks to your guidance, it's only right that we repay you in kind!"
    "How nice of her! You smile as she takes your erect cock out of your pants, and into her mouth."
    "Students pass you by but no one seems to care. Some girls blush and some boys smirk."
    girl "Mmmh [povTitle] [povFirstName], you' shaft is so hot, it's like it's about to melt in my mouth... Aaah..."
    "Her skilled tonguework brings you to the limit in no time. You grab her hair and cum hard [msg]"
    
    scene bg go_class2_2 with flash
    girl "Aaaah! <3"
    pov "Thank you my dear, you ARE the embodiement of this school's spirit!"
    $ inhibition -=1
    $ deviance +=1
    $ behavior -=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance +=5
    return


label go_class3:

    scene bg go_class3 with fade
    "This school has turned so lewd, you can barely recognize it."
    girls "Aaaaaaaaaah!!!"
    "Congratulations on your handywork."
    $ deviance +=1
    $ inhibition -=1
    return


label go_class4:
    
    scene bg go_class4 with fade
    
    "This girl is staring at you. She looks rather intense."
    
    if deviance < 15:
        "You feel a bit embarrassed and clear your throat."
        pov "Well, I'll leave you to your studies..."
        return
        
    "You can't help but stare at her big pair of knockers."
    "She seems to notice your interest and makes no attempt to hide them. Instead, she leans forward."
    pov "Oh my..."
    $ deviance +=1
    
    if deviance > 50:
        "You stare at her a bit, getting a raging hard-on. She stares at your crotch, absent-mindedly licking her lips."
        "The class bell rings and startles you out of your naughty thoughts."
    return


label go_class5:
    
    scene bg go_class5 with fade
    "This school has become so lewd that students are having sex all over the classroom!"
    "There is nothing teachers can do to alleviate the chaos. Some of them just choose to give up and join in."
    $ deviance +=1
    $ behavior -=1
    return
    
    
label go_class6:
    
    #Panning up and down
    scene bg go_class6:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ go_bg=ImageReference("bg go_class6")    
    show screen scroll_screen
    
    "Students.{w=0.8} Having sex.{w=0.8} In class." 
    "Why doesn't that surprise you anymore?"
    $ deviance +=1
    hide screen scroll_screen
    return
   
   
label go_class7:
    
    scene bg go_class7 with fade
    
    "This girl has agreed to pose for the art class... Today's subject is 'Ecchi drawings'."
    go_guys "Come on doll, show us more skin!"
    girl "...okay..."
    $ inhibition -=1
    $ artistery +=1
    
    if renpy.random.randint(1, 2) == 1:
        $ artistery +=5
    return
        
        
label go_class8:
    
    scene bg go_class8 with fade
    
    "Instead of sending bad students to detention, this teacher has chosen a more 'hands-on' approach."
    with vpunch
    "*spank*{w=1.0}{nw}"
    girl "Aaaaw!"
    with vpunch
    "*spank*{w=1.0}{nw}"
    girl "Aaaah!"
    "Teacher" "I repeat my original question: Let x be a pseudo-locally Hermite monoid. Let us assume log(y) = m(0;1). 
             Further, suppose µ is co-pointwise separable and open. What is the resulting {i}i{/i} value?"
    girl "*sob* Please... *sob* I don't know... *sob* Let me go..."
    "Teacher" "I see. Young lady, you aren't putting any effort into this, are you? Could it be that you want to be punished further?"
    with vpunch
    "*spank*{w=1.0}{nw}"
    girl "*sob* Nooo... *sob* I don't want to..."
    "Teacher" "What does the class think? Should I give her the punishment she deserves?"
    class "Hell yeah!" 
    class "Give it to her!"
    class "The bitch has it coming!"
    girl "Noooo... *sob*"
    "Teacher" "Well, you heard them, my dear. Now, prepare yourself for a lesson you will not soon forget."
    "The teacher takes out his large, erect cock from his pants."
    girl "Please, no, AAAAAHHHH!"
    with vpunch
    "*spank*{w=0.5}{nw}"
    "The teacher forces his cock into her ass, making her cry out in pain."
    girl "Aaaah, aaaah, hnnnn, aaaahh!!!"
    "The class cheer on as the teacher fucks her ass harder and harder."
    "The girl is crying in pain and clenching her teeth, but at the same time, you can see that she is getting very wet."
    "Teacher" "My dear, your pussy is dripping wet... Look, it has even started leaking on the classroom floor. It's just as I thought, you {i}enjoy{/i} 
             being abused in front of the class, don't you?"
    girl "No... No, I don't..."
    with vpunch
    "*spank*{w=0.5}{nw}"
    "Teacher" "Do not lie to me!!!"
    with vpunch
    "*spank*{w=0.5}{nw}"
    girl "Aaah, aaaah..."
    "After each spanking, the girl gets wetter and wetter."
    "The teacher increases his thrusts into her gaping asshole, violently ramming his shaft into her. Her pussy is overflowing with her juices as he violates her."
    "After a few minutes, the teacher lets himself go, and comes hard inside her ass."
    with doubleflash
    girl "AAAAAAAHHH!!!"
    "The girl screams at the top of her lungs, as she orgasms from being humiliated and ass-fucked in front of the class."
    
    pov "Well, this teacher sure has some unorthodox methods... It seems to be working, though."

    $ inhibition -=1
    $ deviance +=1
    $ behavior +=1
    $ morale -=1
    if renpy.random.randint(1, 2) == 1:
        $ deviance +=5
    return

label go_class9: #This event goes with the 'nude uniform' policy
    
    scene bg go_class9 with fade
    
    "Since the school has done away with clothes and uniforms altogether, students are free to concentrate on their studies."
    
    $ academics += 1
    if renpy.random.randint(1, 4) == 1:
        $ academics += 5
    
    return

label go_class10:
    
    scene bg go_class10 with fade
    
    "These girls have agreed to star in a feature film for the cinema class."
    "The best actress will earn a scholarship from a prominent adult entertainement company."
    pov "They are both very serious about it... I wonder who's going to win?"
    
    $ inhibition -=1
    $ artistery +=1
    
    if renpy.random.randint(1, 3) == 1:
        $ artistery +=5
        
    return

label go_class11:
    
    scene bg hallway with fade
    with vpunch
    girl "Hiiiiiiiiiiiii!!!"

    "As you walk along the corridor, you hear a girl scream coming out from one of the rooms."
    
    "Alarmed, you rush to the source of the scream and open the door to the classroom."
    
    scene bg go_class11_1 with fade
    
    "A group of students is surrounding a girl, standing there completely naked."
    "A tall, strong-looking male student is holding her firmly and playing with her naked body."
    
    guy "Well, well... What should we do with you, you little slut? *grin*"
    guy "You must be a real horny bitch to come out in front of us all naked like that! Trying to turn us all on..."
    girl "What? No!!! You're... you're the one who asked me to be a nude model for... for your art project!"
    "Other girl" "Oh, what a stupid bitch you are! *giggle* Believing any lie a guy tells you... And showing off your stupid naked body to a bunch of horny boys! 
           You really need to be taught a lesson!"
    guy "Oh, I wasn't lying. *sneer* We {i}are{/i} making an art project. It's a short film featuring you being fucked senseless like the 
         cock-loving bitch you are..."
    girl "No! Nooooooooo!!!"
    "Suddenly, the struggling girl sees you standing there, and a glimmer of hope flashes on her face."
    girl "[povTitle] [povFirstName]! Oh please, Sir, help me!"
    "The guy holds her back and tightens his grip, making her squeal with pain."
    guy "Come on, man, we're just filming a scene here! It's an art project... for the good of the school, honest. *smirk* She's in character and all, 
         but she likes it when we play it rough. Don't pay attention to her!"

    menu:
        "Do you take me for a fool, you punk?":
            pov "You think I'm stupid, jerk? Let her go right now and come with me! You are all going to detention for this!"
            guy "Whoah, hold it right there, old man! Don't you know who the fuck I am?"
            guy "My dad owns 4 factories, 3 brothels and an executive jet. He's one of the big shots that keep your shitty school afloat. You think you 
                can just barge in here and tell me what to do? In MY OWN fucking school?"
            guy "Think about it. You wanna mess with me, just to protect this no-name bitch?"
            "Saying that, he starts playing with the girl's pussy."
            girl "Aaaaaaaaah!!!"
            guy "You see that? She's already horny from being naked in front of everyone... She's a whore..."
            "Clenching your fists, you come forward and say menacingly:"
            pov "Let.{w=0.6} Go.{w=0.6} Of.{w=0.6} Her.{w=0.6} NOW!"
            guy "..."
            guy "Nah, shove it old man! You want a piece of me? I'll show you!"
            "The guy pushes the girl to the side and throws a wild punch at your face."
            with hpunch
            "You block it just in time."
            guy "Come on! I'll..."
            with vpunch
            guy "Uh?"
            "The girl he just released grabs him by the leg, holding him back just as he is about to strike again."
            "You take advantage of this opportunity to make your counter-attack."
            with hpunch
            "*punch*{w=0.8}{nw}"
            guy "Ugh!"
            with hpunch
            "*punch*{w=0.8}{nw}"
            guy "Aaagh!"
            with vpunch
            "*kick*{w=0.8}{nw}"
            guy "UHAAAAR!!!"
            "Your roundhouse kick sends your opponent flying into the air, crashing down on a school table."
            "After all, it seems you aren't so worn out after your years of practicing karate in university."            
            "With their leader defeated, the rest of the molesters panick and start running away."
            class "He's crazy!!!"
            class "Help us!!!"
            "This one will not earn you any points with the PTA, but at least the girl is safe."
            girl "Oh, thank you, [povTitle] [povFirstName]... Thank you..."
            "You help her getting dressed, and escort her out of the school."
            
            $ morale +=1
            $ behavior +=1
            $ reputation -=1
            $ good_points +=1
                        
            return
            
            
        "Who am I to discourage love of the arts in my school...":
            pov "A film, you say? That sounds like a worthy project for an art class. Please, don't mind me and just continue where you left off."
            "The girl's eyes widen in shock as she understands the meaning of your words."
            girl "No, principal, please! Nooo!"
            class "Hurrah!!!"
            guy "Thanks [povTitle] [povLastName]! Now, we'll show this little bitch right here a good time!"
            "Other girl" "[povTitle] [povFirstName]! You're like, the coolest principal ever!"
            "The girl's eyes fill up with tears as the boys start closing in on her, feeling her body, grabbing her tits and ass, licking and sucking on her nipples..."
            girl "Aaaah! Noooo... *sob* *sob*"
            "The guy holding her brings his hand down to her pussy, and starts rubbing her clit. She cries in shame and humiliation, 
             but doesn't struggle anymore. After the shock of seeing you turn against her, she doesn't seem to have any fight left in her."
            "Holding a digital camera, the other girl is filming every detail of the scene while trying out different angles."
            "Other girl" "Look at this dirty slut... Being molested by half a dozen guys, I bet she loves every moment of it."
            "You watch as the boys keep fondling her body and playing with her ass and tits. She moans softly and shivers under their touch."
            "After a few minutes, the guy standing behind her gets bolder, and starts fingering her pussy. First, a finger. Then two. Then three."
            
            scene bg go_class11_2
            girl "Mmmmh, aaaah, aaaah..."
            "He seems to be able to slide into her pussy with ease."
            guy "Well, what do we have here? Our class whore is getting wet!"
            girl "That's not... mmmh..."
            "Indeed, you can see her pussy is glistenning with something more than sweat."
            "The guy stops his fondling for a moment and shoves his sticky fingers in her face. They are covered in her juices."
            guy "And what is this now, slut?"
            "He laughs as he wipes his hand over her face, covering her in her own juices."
            girl "Mmmh!!!"
            "The guy resumes fingering her. She moans as he violates her with his hand, and soon more juices start flowing out of her."
            girl "Aaah, mmmh, aaaaah..."
            "She has stopped crying and is now moaning sexily. Her mind seems to have wandered off, but her body is responding to 
             the feeling of being molested by so many lewd hands."
            "Other girl" "All right, enought playing around! Are you going to stick a cock into this dirty slut or what? Teach that bitch her rightful place!"
            guy "*snigger* You hear that, bitch? I'm going to stick it into your wet, slutty cunt. What do you say?"
            girl "..."
            "The guy takes you his erect cock from his pants. He starts rubbing his shaft against her slit."
            girl "Ah!"
            "The other guys stop fondling her and make a circle around them, cheering them on."
            "As the guy slides his hard cock along her slit, her pussy lips open up and her juices start flowing out, lubricating his cock."
            girl "Aaaah... aaaaaah..."
            "Other girl" "She's more than ready now... Do it! Fuck her cunt!!!"
            guy "Gee, do you really have to give me orders all the time like this?"
            "Other girl" "Shut the fuck up! I'm the director! Just do what I fucking say!"
            guy "..."
            "Abruptly, the guy pulls back his cock from between the girl's legs, and she lets out a little cry of surprise. She is very wet now, her hot juices running down 
             the lenght of her legs. She raises her ass in anticipation, her body moving of its own accord."
            "A split-second later, the guy plunges his shaft into her pussy in one hard, deep thrust."
            girl "Aaaaaaaaaaaaaaaaah!!!"
            "He starts fucking her from behind in long, deep strokes. Her pussy makes wet noises and she moans as she is being raped."
            "Other girl" "Oh that's good... Look at the expression on her face! She's enjoying this!"
            "Other girl" "Mmmmh... I'm beginning to feel a little jealous..."
            "The guy pinches her nipples and fondles her tits as he fucks her faster and harder."
            "She gives out little cries of pleasure with every thrust now, completely lost in the moment."
            girl "Ah, ah, ah, aah..."
            "The guy switches positions, lifting her legs up and sitting her down on his cock. He starts fucking her with her legs in the air, giving everyone a full view of her 
             wet, streched out pussy."
            "Other girl" "Oh, that's a good shot!"
            "She is dripping wet now and her love juices are splashing out as his cock reaches deep into her. She cries out with lust as he fucks her deep and hard."
            girl "Aaaah, aaaah, ooooooooooooooh!!!"
            guy "Ha, ha, ha..."
            guy "Ready, hmmpf, for the fireworks...?"
            
            scene bg go_class11_3 with doubleflash
            "The guy takes out his cock at the last moment and explodes his load onto her, spurting cum all over her body and face."  
            girl "Ahaaaaaaaaaa!!!"
            guy "Uhrrrrr!!!"
            "Other girl" "All right, that's it! CUT!!!"
            "Other girl" "You should be careful there! You almost put some on the camera! And... whaaaat? My hair! You jerk!"
            "The guys burst into applause as the lead actor negligently wipes his sticky cock on his co-star's ass, before letting her slip down to the floor."
            "Out of breath, she lies there panting, her body and face covered in cum."
            "She looks oblivious to the students around her as they pack up their things and leave."
            "You follow everyone outside. Before going out and turning off the light, the last girl turns around and smiles at her:"
            "Other girl" "You can find the footage on Youtube in a day or so. Just google your name, really. See you around... *laugh*"
            
            $ inhibition -=1
            $ deviance +=1
            $ morale -=1
            $ artistery +=1
            $ evil_points += 1
            $ r=renpy.random.randint(1, 4) 
            if r == 1:
                $ deviance +=5
            elif r == 2:
                $ artistery +=5
            
            return
     
     
label go_class12:
    
    scene bg go_class12 with fade
    "This girl models for the art class. Some students are busy drawing, but most just stare at her, drooling over their sketchbook."
    
    $ artistery +=1
    if renpy.random.randint(1, 3) == 1:
        $ artistery +=5
    
    return


label go_class13:
    
    "As you walk around the school during lunch break, you notice a pleasant smell coming from one of the classrooms."
    
    scene bg go_class13_1 with fade
    
    "A girl is having lunch by herself in the classroom."
    pov "Oh, hi there! What are you doing here, eating on your own?"
    girl "Oh, [povTitle] [povLastName]! Sorry I... I often eat by myself..."
    girl "I love cup ramen, you see... So I usually prepare one and do a bit of studying during lunchbreak. It does get a bit lonely though."
    pov "Well, I can sit down with you for a while, if you want. Tell me about your studies..."
    "You chat pleasantly while she is eating."
    "She eats her ramen in the traditional way, stopping to blow on her hot noodles, then swallowing them whole."
    "She makes obscene noises while slurping, and soup is running down the side of her mouth. It is erotic in a bizarre way. Watching her, you start to feel 
     strange urges."
    girl "*slurp* Mmmh, aah... *slurp*" 
    pov "..."
    "You run out of things to say as you watch her, thinking naughty thoughts."
    "The silence is becoming awkward. What do you do?"
    
    menu:
        "Excuse yourself.":
            pov "Well, young lady, thank you for the chat. I'll leave you to your meal then."
            girl "*slurp* Oh, sure [povTitle] [povLastName]! It was very nice of you to stop by."
            
            $ morale +=1
            return
        
        "Make a move on her.":
            "Slowly, you bring your hand down under the table, close to her knee."
            "She is wearing a short skirt, and her thighs are exposed. Her smooth, white flesh is tempting you..."
            "Holding your breath, you bring your hand closer and lightly caress her thigh."
            with vpunch
            girl "EEK!"
            "Surprised by your touch, she jumps up, bumping the table and sending her bowl of soup flying."
            "*splash*"
            with hpunch
            "*crack*"
            girl "Oh no!!!"
            "Soup has splashed everywhere, soaking her shirt. The bowl fell down on the floor, leaving a mess."
            pov "(Oops!)"
            "She looks upset. What do you tell her?"
            menu:
                "Don't worry, I'll take care of it.":
                    girl "You... You startled me..."
                    "She is looking at you with suspicion."
                    pov "I'm sorry, it was an accident. You can go and get changed, I will take care of the clean up."
                    "She is grateful for your offer."
                    girl "Thank you [povTitle] [povLastName]! I'm sorry I was so clumsy..."
                    if deviance <25:
                        "She leaves in a rush, not looking back."
                    elif deviance < 75:
                        "She blushes and look at you like she is on the verge of saying something... Then she bows, turns around and leaves."
                    else:
                        "She looks at you hesitantly."
                        girl "I'm... I'm sorry, I was startled earlier but... It's not against you or anything..."
                        pov "Hush now kid... Just go freshen up! We can always catch up later. *smile*"
                        "She blushes and gives you an intense look, holding her hands behind her back. Her wet shirt has become almost transparent, and you 
                         can make out the shape of her tits through the damp fabric."
                        "After a moment of indecision, she leans in and kiss your cheek, thanking you one last time before heading out."
                        $ inhibition -=1
                    return
                
                "Let's clean it together.":
                    pov "Well, it seems we made quite a mess."
                    girl "But you..."
                    pov "Anyway, we can't leave the classroom like that! Let's clean it up together before lunchbreak is over."
                    "You fetch a mop and some water and start scrubbing."
                    "The girl looks unhappy but resigned. She gets on all four and starts cleaning the floor."
                    "You get a good view of her panties as she is busy cleaning up."
                    pov "(Nice... I should press my advantage...)"
                    menu:
                        "Go for it!":
                            scene bg go_class13_2 with fade
                            girl "Ah!!!"
                            "Taking her by surprise, you start running your fingers lightly over her ass and panties."
                            if deviance <25:
                                girl"WHAAAAT? Don't touch me, you pervert!!!"
                                "She is yelling and red with anger."
                                pov "I... Ahem... Let me explain..."
                                "She throws the mop in your face, and the bucket soon follows. She storms out of the classroom looking mad as hell."
                                pov "This can't be good..."
                                $ morale -= 1
                                $ reputation -= 1
                                
                            else:
                                girl "What... wait..."
                                "Ignoring her, you continue feeling her through her panties."
                                "She shifts her ass, trying to evade your touch, but your inquisitive hand follows her everywhere, lightly caressing her above her panties."
                                girl "Aah, no, [povTitle]... Aaah..."
                                "Pushing her panties in, you see the shape of her crotch, nicely outlined by the fabric of her underwear. It is starting to feel a 
                                 little moist as well."
                                girl "What, aah... are you doing... Mmmh..."
                                "Emboldened by her lack of reaction, you start feeling her more. Soon, you are sliding a couple of fingers along her slit. She 
                                 has gotten unmistakably wet by now."
                                girl "We... you... shouldn't be doing this..."
                                "She sighs as you keep massaging her crotch through her underwear. You decide to take it a bit further and start running your 
                                 finger along the side of her panties, touching her naked skin."
                                "She shivers under your touch. Caressing her, you slip a finger under her panties and run it along her vulva."
                                if deviance < 50:
                                    girl "Aaah, no!!!"
                                    "As if awoken from a dream, she snaps out of her transe and covers up her pussy."
                                    "Rising quickly, she says:"
                                    girl "Sorry [povTitle] [povLastName], this isn't... We cannot do this..."
                                    "Blushing red, she apologizes with a quick bow and rushes out of the classroom."
                                    "You stand there a minute, feeling a little frustrated and confused. Your fingers are still sticky with some of her wetness."
                                    pov "That's just too bad..."
                                    $ deviance += 1
                                    
                                else:
                                    "She moans in pleasure as she feels your touch on her bare skin."
                                    "Pulling her panties, you squish them so that her pussy lips are exposed and only her slit is still covered."
                                    girl "Aaaaw..."
                                    "Caressing the sides of her pussy with your fingers, you hear her moans become sexier as her underwear becomes wet."
                                    "You fondle her ass and caress her pussy more, soon to be rewarded with more of her love juices flowing out."
                                    girl "Aaah, mmmh..."
                                    "Hungry for more, you use both hands to slowly slide her panties off, feeling the smooth skin of her ass and legs as you go."
                                    girl "Aaaah... [povTitle] [povLastName], no..."
                                    scene bg go_class13_3
                                    "Her naked pussy is now exposed in front of you, glistening with her love juices."
                                    girl "..."
                                    "She is raising her hips in anticipation, waiting for your next move."
                                    "Running your fingers directly along her slit, you feel her wetness as her pussy opens up like a blooming flower."
                                    "You slowly push your fingers in, and her pussy swallows them with a sucking sound."
                                    girl "Ahaaaa!!!."
                                    "You have no problem entering her with two fingers as she is already soaking wet. You start sliding your fingers in and out of her."
                                    "She cries in exctasy as more of your fingers penetrate her, stretching her cunt."
                                    "You grab her ass with your other hand and start playing with her butt."
                                    girl "Oh yes! [povTitle] [povLastName]..."
                                    "She seems to enjoy being fucked by your hand. You keep massaging her ass, giving her a little spank from time to time."
                                    girl "Aaah... Aah!!!"
                                    "Raising her hips to increase her sensations, she loves it as you fondle and fuck her with your hands."
                                    "You slowly increase your pace and her whines become louder and more intense."
                                    girl "Aaaaaah! Aaaaah! Ahaaaa..."
                                    "She is completely into it now, her body is very sensitive. You decide to go all the way."
                                    "Plunging your fingers into her in fast, deep strokes, you spank her harder, bringing her closer to extasy."
                                    with hpunch
                                    "*spank*{w=0.8}"
                                    girl "Aah! Yes!"
                                    "Your hand makes dirty, slushing noises as her juices leak out of her pussy and run down her inner thighs."
                                    girl "Oh yes! Oooh, yes I'm... I'm..."
                                    with doubleflash 
                                    girl "Aaaaaaahaaaaaaaaaa!!!"
                                    "She tenses up and reaches climax as you masturbate her hard and fast. Her juices spurt all over your hand and leak out, 
                                     forming a small poodle underneath her."
                                    girl "Aaah... Aaah..."
                                    pov "Good girl..."
                                    with hpunch
                                    "*Driiiiiiiiiing*"
                                    "The bell!"
                                    "You were so busy having fun that you completely forgot about the end of the break."
                                    "Reluctantly, you stop here and quickly wipe up the floor. It wouldn't do to be caught in this position by the whole class..."
                                    "A minute later, the teacher and students enter the classroom. Suddenly, you notice the girl's soaked 
                                     panties are still lying crumpled on the floor."
                                    "Noticing this as well, the girl blushes and pretends to look away. She sits down with her legs crossed and 
                                     prepares for class."
                                    "You have a few words with the professor and then leave class as if nothing happened. The girl looks at you go and you give 
                                     her a small wink. She blushes and quickly turns her head around."
                                    pov "Sweet little thing, that one..."
                                    $ deviance += 1
                                    $ inhibition -= 1
                                    if renpy.random.randint(1, 3) == 1:
                                        $ deviance += 5                                       
                            return
                                
                        "Forget it!":
                            pov "(What am I thinking? I can't assault a schoolgirl in class during lunchbreak! The PTA will have my head on a spike!)"
                            "After you're done cleaning, you apologize again to the girl and leave her to her studying."
                            
                            return
                            

                
                "You spilled hot soup on your shirt! Quick, take it off!":
                    if inhibition <70 and deviance >50:
                        girl "But... I can't..."
                        pov "Hurry up, there is no time for discussion! I won't let a student get harmed under my watch!"
                        "Reaching for her shirt, you reap it open in one swift move."
                        
                        scene bg go_class13_4 with fade
                        girl "Aaaah!"
                        pov "Wow!"
                        "Her boobs burst out of her shirt. She isn't wearing any bra. Her big, round tits are in plain view, her nipples a nice pink color."
                        pov "Such a nice pair of knockers... Didn't feel like wearing any bra today, did you?"
                        "The girl blushes and avoids looking you in the eye."
                        girl "I... I don't like bras, they're... constraining."
                        "You still haven't let go of her shirt, and your hand are framing her boobies. You don't seem to be able to take your eyes off them."
                        "After an awkward moment, the girl raises her eyes and notice the hungry look on your face. She blushes even further, but doesn't 
                         attempt to hide from your gaze."
                        girl "Do... do you like them, [povTitle] [povLastName]?"
                        pov "*gulp* I... They're... hem..."
                        girl "You... you can touch them a little if you want... I don't mind..."
                        "She guides your hands, placing them on top of her tits. Without thinking, you start softly massaging her boobs."
                        girl "Aah, mmh..."
                        "Her tits are so big that you cannot really wrap your hands around them. Instead, you squeeze the front of her boobs and roll your thumbs on her nipples."
                        girl "Aaahhhh..."
                        "She moans under your touch as her nipples become flushed and hard."
                        girl "Ah, oh, ah... [povTitle] [povLastName]..."
                        "She is completely submitting to your lewd hands rubbing and pinching her tits."
                        "Her boobs are still a little wet with soup, which lubricates your hands nicely."
                        pov "You seem to have some soup on your tits, dear... Here, let me help."
                        
                        scene bg go_class13_5
                        "Grabbing her ass, you sit her down on the table. You bring your mouth down on her tits and start licking and sucking her nipples."
                        girl "Aaaah!!!"
                        "Surprised at first, she is quick to enjoy the feeling and your tongue and lips on her tits."
                        girl "Mmmh... It feels... good..."
                        "You lick and suck hard on her horny tits. She is very sensitive and moans with pleasure as you increase in intensity, even biting her 
                         nipples lightly."
                        girl "Aaaah, [povTitle] [povLastName], don't bite me... Aaaah!"
                        "As you continue sucking on her hard nipples, she caresses your hair and face passionately."
                        girl "I'm... feeling strange [povTitle] [povLastName]... If you continue I... Aaaah..."
                        "You bring your hands to cup and massage her tits as your tongue continues licking and flicking her nipples."
                        girl "Aaah... Mmmh..."
                        "Her tits are now covered with sweat and saliva. She looks at her swollen nipples with dreamy eyes..."
                        "You increase the strength of your touch as you bite and lick her nipples more aggressively. She sighs and moans lustfully as you go."
                        girl "Aaaah... Mmmmh... Oh yes..."
                        "You can feel tension building up in her body. You realize she is about to come just from having her tits played with."
                        girl "Oh, oh... I'm... I..."
                        
                        scene bg go_class13_6 with doubleflash
                        "You increase the pace and pressure of your hands and tongue. Suddenly, she cries out and arches her back, reaching climax."
                        girl "Aaaaaaaaaaaaaaahaaaaaaaa!!!!!"
                        "Her loud cries echo in the classroom, covering the lewd sounds of your sucking and licking."
                        "Lewdly, you lick the liquid off her super-sensitive boobs as she moans with pleasure."                        
                        "Suddenly, you notice the clock: lunchbreak is about to end! Reluctantly you stop playing with her."
                        "Taking a step back, you see her orgasm receding. She is still laying on the table, her boobs exposed and her legs spread out. Her 
                         panties are drenched, leaving a small poodle of her love juices on the table."
                        pov "Thank you dear... We should have 'lunch' together more often. *grin*"
                        
                        $ deviance += 1
                        $ inhibition -= 1
                        if renpy.random.randint(1, 3) == 1:
                            $ deviance += 5
                    else:
                        girl "What??? I can't! You must be joking!"
                        pov "..."
                        pov "Ahah, yeah of course! That was a joke! Ahahaha!"
                        "Your laugh sounds nervous and exagerated. She is looking at you with suspicion."
                        girl "Well, that wasn't funny. I'm sorry, I have to go now."
                        "She rushes out, leaving you by yourself to clean the mess on the floor."
                        pov "Man, that sucks..."
                        $ morale -= 1
                    return
                
     
     

label go_class14:
    
    "Approaching the classroom after school is over, you overhear a girl giggle."
    
    scene bg go_class14 with fade
    "A girl and a boy are alone in the classroom. The boy is crouching behind her and is busy playing with her ass." 
    girl "Gee, what do you think you're doing? Didn't you say we should stay here a bit to study for the exam?"
    boy "*mumbling* Your sweet... ass... It's so... soft... and... squishy..."
    girl "Hey, snap out of it, aaaah... Are you even listening to me?"
    boy "Oh, my precious... My beautiful, sweet, gorgeous ass... You're going to be mine, all mine..."
    girl "Stop it! I'm not a soft toy! Aaaah!"
    "In spite of her protests, she is getting turned on by this. She leans on a table for support as he keeps feeling her butt and teasing her asshole."
    girl "Oh all right... Just do whatever you want... But after that, we really, aah, should, aaaah, study..."
    "You have a feeling there won't be any studying going on in this classroom tonight."
    
    $ deviance += 1
    $ academics -= 1
    
    return


label go_class15:
    
    scene bg go_class15 with fade
    
    "She agreed to make it up to him if he helped her cheat for the final exam. But she was in for more than she bargained for."
    
    $ deviance += 1
    $ academics -= 1
    
    return
     

label go_class16:
    
    scene bg go_class16 with fade
    
    "The biology teacher is in charge of sex ed as well, but she finds it difficult to explain things properly without showing a practical example."
    "Today, a student is helping her demonstrate a sure-fire contraception method."
    class "Whoaaah!!!"
    
    $ deviance += 1
    $ inhibition -= 1
    $ academics += 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


label go_class17:
    
    $ r=renpy.random.randint(1, 3)
    image bg go_class17 = ConditionSwitch("r==1","mods/Go1/screens/go_class17_1.jpg","r==2","mods/Go1/screens/go_class17_2.jpg", "r==3","mods/Go1/screens/go_class17_3.jpg")
    
    scene bg go_class17 with fade
    
    "Exams are fast approaching. This girl agreed to act as the class's \"{i}stress relief{/i}\" while everyone is studying in an all-night marathon."
    pov "Such selflessness is to be commended..."
    
    $ morale += 1
    $ deviance += 1
    $ academics += 1
    if renpy.random.randint(1, 2) == 1:
        $ academics += 5
    
    return


label go_class18: # Goes well with skimpy uniforms
    
    scene bg go_class18 with fade
    
    "Shorter dresses equals happier students... and faculty."
    girl "I received another love letter yesterday... Even kinkier than the one before! *giggle*"
    
    $ morale += 1
    $ inhibition -= 1
    
    return

label go_class19:
    
    scene bg go_class19 with fade
    
    girls "Now tell us, Key-kun... Which ones are better?"
    "When it comes to getting the boys' attention, some girls are awfully competitive." 
    
    $ inhibition -=1
    
    return

label go_class20:
    
    scene bg go_class20_1 with fade
    
    "This girl always comes to school without underwear to tease the boys. This time, her ploy worked a little too well."
    "Guy 1" "You are finally getting what you deserve, slut! Come on! Suck on my dick harder!"
    "Guy 2" "Her pussy is... so tight... Ah, it's really great..."
    "Guy 3" "Seems like her ass needs to be filled as well... Here I come!"
    girl "Mmmmmmmmmh!!!"
    "Her cries are muffled by the dick in her mouth as her pussy and ass are being fucked hard."
    "She is quite horny in spite of her situation, her body responding to the stimulation. Her pussy makes squishing sounds as her love juices spread. 
     Her tits bounce back and forth with every thrust, her nipples standing flushed and erect."
    "Guy 1" "If you keep using your tongue like this... I will..."
    "Guy 2" "Oh, her pussy is sucking me in... It's too much..."
    "Guy 3" "Her tight ass, it's squeezing my dick!"
    
    scene bg go_class20_2 with doubleflash
    
    "They all cum in her at the same time."
    girl "Mmmwaaaaahhh!!!"
    with flash
    "Guy 1" "Aaaaaah!"
    with flash
    "Guy 2" "Ooooh!"
    with flash
    "Guy 3" "Arrrh!"
    
    "Warm cum gushes out of her holes as she gets her mouth, ass and pussy filled up."
    "The boy she was jerking off cannot hold it and spits his cum on her belly and tits."
    with doubleflash
    "Guy 4" "Oh, yeaaah!!!"
        
    girl "Aaah, aah, ah..."
    "As she coughs and tries to recover her breath, other boys start lining up for the second round..."
    
    $ deviance +=1
    $ behavior -=1
    
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return
    

label go_class21:
    
    scene bg go_class21_1 with fade
    
    girl "Whaaat! Wait, [povTitle] [povLastName], what are you doing???"
    pov "Come on now, kitten, I thought you didn't want me to tell your parents how you got caught masturbating in class?"
    girl "It's true... but..."
    pov "Hush now, sweetie... Why don't you just relax and let yourself go?"
    "Not waiting for her answer, you press you hard cock against her pussy and slowly push it in."
    girl "Ah, you're, aaah! You're pushing it inside, ah... No wait, mmmh, it's too big!"
    girl "Ahahaaaa!!!"
    "It's kind of hard to get into her, but you force yourself in as she struggles to breathe."
    "Her exposed tits rub on the table as you slowly start fucking her."
    girl "Aaaah! Aaah!" 
    "You take it slow at first, giving her a moment to get used to the sensation of your dick."
    girl "Oooooh... Aaah, aaah..."
    "After a little while, she relaxes a little and you manage to slide in and out of her more easily."
    girl "Mmmh, mmmh, aaah..."
    "She moans as you increase your pace. You can feel the soft, wet sensation of her tight pussy gripping your cock."
    "Your shaft is now nicely lubed with her love juices."
    pov "How are we doing down there, little kitty? You seem to be enjoying this well enough..."
    girl "I'm, aah, I'm not..."
    "Her weak protests do little to hide the response of her body as she moans sexily with each of your thrusts."
    "You grab her ass forcefully and start shoving your cock even deeper inside her."
    girl "Aah, aah, it's going all the way! You're filling me, aah, completely!"
    "As you fuck her hard and deep, her pussy juices flow out and she screams in exctasy."
    girl "Oh, [povTitle] [povLastName], oh! Yes!!!"
    pov "Your pussy is too much fun, babe girl... Prepare yourself..."
    pov "Urrrrgh!!!"
    scene bg go_class21_2 with doubleflash
    "Your cock twiches inside her and you start spurting loads of cum in her pussy."
    girl "Aaaah! So warm, so strong! Aaaahaaaaaaaaaaa!!!"
    with flash
    "She arches backwards as she orgasms with great force. You withdraw your cock, unloading the rest of your seed all over her ass."
    pov "Well... You see, it wasn't so hard... Now, I am going to think upon your request. What should I tell your parents, I wonder? *wink*"
    girl "Awww, [povTitle] [povLastName]... you're such a meanie..."
    
    $ deviance +=1
    $ morale -=1
    
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5
    
    return    
    
    
label go_class22:
    
    scene bg hallway with fade
    "As you patrol around the classrooms during lunchtime, you hear whispers coming from around a corner, at the end of the corridor."
    "You approach cautiously, waiting to see what it is all about before making your presence known."
    
    scene bg go_class22_1 with fade
    
    "A young girl is sitting down on a half-naked guy. His cock is erect between her legs and she is sliding along in awkward movements."
    girl "Sen... senpai? Why is it growing so big?"
    guy "It's becoming bigger because... uh... it... it wants to be your friend?" 
    guy "Hush now baby, just keep going."
    girl "But... but it's becoming big, and swollen and... so very hot... It's going to burn my legs..."
    guy "Don't worry about that, babe, just keep working your thighs. If you make it big and hot enough, you will be rewarded."
    girl "Re... rewarded?"
    guy "Yes... A man's cock is full of cream, and you can get some if you work hard enough for it."
    girl "Cream?..."
    "She continues masturbating his hard cock between her legs. In spite of her inexperience, the guy seems to be enjoying himself."
    guy "Ah girl... You have such smooth skin... Your thighs feel like silk..."
    "The guy is now shaking his hips as well and humping, making her ass and tits bounce."
    girl "You're... ah... moving a lot..."
    guy "Mmmh, mmh, aah..."
    girl "Wait! It's... twitching?"
    guy "So.. so good..."
    girl "Aaah, it's... hot... What is... going on?"

    with flash
    guy "Uuuurh!!!"
    girl "Aaaah! It's... it's coming out!"
    scene bg go_class22_2 with doubleflash
    "The guy ejaculates and hot semen comes gushing out on her white skin."
    girl "Ooooh! Cream! So much... cream?"
    guy "Ah... Good job girl..."
    guy "Come on, you can taste it..."
    "Blushing, she scoops some of his cum with one hand, and cautiously bring it to her lips. She licks if off her hand and fingers."
    girl "..."
    girl "EEEW!!! That's disgusting!"
    guy "Ahah, well, some say it's an acquired taste... You'll come to like it in time."
    girl "Aaaw... This sucks... And you made my legs and uniform all sticky..."
    guy "Stop whining already... Remember, if you want us to date, I'll expect you to do this every day. Tomorrow, I will teach you about sixty-nine."
    girl "Sixty-nine? Are... are we going to study maths together?"
    guy "*sigh*"
    
    $ deviance +=1
    
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


label go_class23:
    
    if deviance < 98:
        $ r=renpy.random.randint(1, 3)
    else:
        $ r=renpy.random.randint(1, 5)
        
    image bg go_class23 = ConditionSwitch("r==1","mods/Go1/screens/go_class23_1.jpg","r==2","mods/Go1/screens/go_class23_2.jpg","r==3","mods/Go1/screens/go_class23_3.jpg",
        "r==4","mods/Go1/screens/go_class23_4.jpg","r==5","mods/Go1/screens/go_class23_5.jpg")
    
    scene bg go_class23 with fade
    "Everyone line up for the class picture!"
    pov "I think I will have to order reprints for this one..."
    
    $ inhibition -=1
    return


label go_class24:
    
    scene bg go_class24 with fade
    
    "Orgies in class have become common, sometimes involving teachers. Students are more interested in surrendering to their every carnal 
     desire than in doing any studying."
    "Your reputation as a 'unique' school grows, however."
    
    $ deviance +=1
    $ inhibition -=1
    $ behavior -=1
    $ academics -=1
    $ reputation +=1
    
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5
    return
    

label go_class25: #This event could be split to work with the 'nude uniform' policy
    
    if deviance < 100:
        $ r=renpy.random.randint(1, 2)
    else:
        $ r=renpy.random.randint(1, 3)
    
    image bg go_class25 = ConditionSwitch("r==1","mods/Go1/screens/go_class25_1.jpg","r==2","mods/Go1/screens/go_class25_2.jpg","r==3","mods/Go1/screens/go_class25_3.jpg")
    
    scene bg go_class25 with fade
    "Some guys have started to build their own harems."
    pov "Well, I suppose I cannot keep them all for myself."
    $ deviance +=1
    $ morale +=1
    
    return
    
    
    
#### SPORT FIELD EVENTS ####

label go_field1:
    
    scene bg go_field1 with fade

    "This girl from the tennis club found herself in an awkward positon... Everyone is looking."
    "You wonder if she isn't doing this on purpose, though..."
    
    $ deviance += 1
    return


label go_field2:
    
    scene bg go_field2 with fade

    "This girl only trains with the boys tracking team."
    "Word is she loves nothing more than sucking on a hard, sweaty dick after working out."
    
    $ deviance += 1
    
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return


label go_field3: # This event would go well with a 'no panties' policy

    scene bg go_field3 with fade

    "Some girls came to support the boys baseball team."
    "You find they offer a far more interesting spectacle than the game, though."
    
    $ inhibition += 1
    $ morale += 1
    return
    
    
label go_field4:
    
    scene bg go_field4 with fade
    
    "This girl is a serious student but she hates sports... She worked out an arrangement with the PE teacher and is now exempted from attending practice. 
     Sports practice, anyway."
    
    $ deviance += 1
    $ athletics -= 1
    
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


label go_field5:
    
    scene bg go_field5 with fade
    
    "Girls in the tennis club are fiercely competitive."
    go_miya "Take that! UWAH!"
    with hpunch
    
    $ athletics += 1
    
    if renpy.random.randint(1, 4) == 1:
        $ athletics += 5
    
    return


label go_field6:
    
    scene bg go_field with fade
    
    "The captain of the tennis team has requested a word with you after practice."
    
    scene bg go_field8_1 with fade
    
    "You admire her technique as she crushes her last opponent, sending her crying all the way to the locker-room."
    go_miya "Hi [povTitle] [povLastName]! Did you enjoy the match?"
    pov "Oh yes! You are truly an amazing player!"
    go_miya "*smile* Thank you, [povTitle] [povLastName]! That means a lot."
    pov "So... What did you want to talk about?"
    go_miya "Hmm... [povTitle] [povLastName], I noticed you've been coming to watch me play quite often lately."
    go_miya "Is it truly because you like sports, or... something else?"
    "She blushes and looks at you with inquisitive eyes, waiting for your answer."
    menu:
        "No, nothing special really. Why do you ask?":
            go_miya "Okay... I just thought..."
            go_miya "Well, never mind."
            "She talks to you a bit about the tennis club, and then she takes her leave, looking a bit dispirited."
            return
            
        "Well, guilty as charged: I love tennis!":
            pov "I love to watch a good match, that's why! I was quite the player myself in high school!"
            "(You are lying through your teeth.)"
            go_miya "Oh really? Yay, the principal is a worthy challenger! Let's play together then!"
            pov "Uh... Hem... Wait..."
            "She shoves a racket in your hands and takes her position before you can find an excuse to get out of it."
            "..."
            "You get your ass handed to you."
            go_miya "Uwah! Uwah! UWAH!"
            with vpunch
            "The last ball travels at shattering speed and hits you in the nuts."
            pov "Aaaaaaawooooohh... *crying*"
            "The girl stands above you, frowning."
            go_miya "Well, I thought you would be more of a challenge..."
            
            $ athletics += 1
            if renpy.random.randint(1, 3) == 1:
                $ athletics += 5
            return
             
        
        "Well, guilty as charged: I love your ass!":
            "She freezes for a moment, surprised by your answer."
            pov "(Wow, i think I should have kept my mouth shut... She's gonna kill me!!!)"
            "Suddenly, she burst out laughing."
            go_miya "Ahahaha! [povTitle] [povLastName], you're so honest!"
            go_miya "I knew you were interested in me... I can tell when men give me dirty looks. And you've been giving me plenty!"
            "She approaches you, lowering her voice seductively."
            go_miya "Well, since you love my ass so much..."
            
            scene bg go_field6_1 with fade
            go_miya "Well, [povTitle] [povLastName], is this alright? Can you feel it?"
            pov "Sure... *sweating*"
            "Miya is sitting over you, slowly rubbing her sexy ass over your crotch."
            "The feeling is amazing and soon, you can feel your body respond."
            go_miya "Ah! I feel... Something is getting hard..."
            "She lifts her skirt to give you a better view, and keeps using her butt to rub your dick through the tracksuit."
            pov "Mmh..."
            go_miya "I think you need some... breathing room..."
            scene bg go_field6_2
            "She pulls down your pants to free your big, hard cock. Placing it between her buttocks, she starts grinding against you harder..."
            pov "Ugh..."
            "Your cock is rock hard now and your pleasure increases with every movement of her ass. The pressure of your dick is shoving her panties in her crack, making it 
             look like she's wearing a thong."
            go_miya "Aah, [povTitle] [povLastName]! I feel... I feel you... You're burning hot!"
            "Your cock is on fire as you feel the soft skin of her exposed buttocks run against it."
            "She slides her ass and pussy harder along your dick. Your feel surrounded by walls of flesh as she contracts her athletic buttocks around your cock."
            go_miya "Do you like it, [povTitle] [povLastName]? Am I doing it... right?"
            pov "Oh yes, Miya... You're good..."
            "After a few minutes, watching her erotic ass massage your hard cock proves to be too much for you."
            pov "Oh, I'm... Aaaaah!!!"
            scene bg go_field6_3 with doubleflash
            "Your hot cum erupts everywhere, soiling her ass and panties."
            go_miya "Wow! So much... hot... cum... Mmmh...!"
            "As your orgams recedes, you watch your gooey cum drip down her round ass."
            go_miya "Ah, [povTitle] [povLastName] you're so naughty... Look how much you came..."
            go_miya "*sigh* Well, I guess I will have to go without underwear again for the rest of the day."
            "Rising up, she makes a great show of taking off her cum-stained panties, giving you a nice view of her pussy and asshole by spreading her buttcheeks for you."
            "Throwing her panties on the ground next to you, she blows you a kiss and says:"
            go_miya "Something to remember me by..."
            
            $ inhibition -= 1
            $ deviance += 1
            $ go_HwithMiya = 1
            if renpy.random.randint(1, 2) == 1:
                $ deviance += 5
            return
             

label go_field7:
    
    "Today's weather is perfect and you decide to take a little rest by the sports field."
    scene bg go_field7 with fade
    girl "Hi, [povTitle] principal! Taking a nap are you? *giggle*"
    "Just when you thought things couldn't get any better!"
    
    $ inhibition -= 1
    return


label go_field8: #Img3 Would go well with the no panties policy

    $ r=renpy.random.randint(1, 3)
    if r==3 and inhibition < 70:
        scene bg go_field8_3 with fade
        "Miya, captain of the tennis club, is playing today. She looks uncomfortable."
        "You realize the reason why as she is playing. Her skirt lifts up from time to time, just enough to let you see she isn't wearing any panties."
        "She notices your gaze and blushes, but she doesn't stop playing."
        $ athletics += 1
        $ inhibition -= 1
        
    else:        
        scene bg go_field8_1 with fade
        "Miya, captain of the tennis club, is playing today. She recognizes you."
        go_miya "Hi [povTitle] [povLastName]! *smile*"
        $ athletics += 1
        if deviance > 30 and inhibition < 70:
            "Her short skirt does nothing to hide her panties while she plays. You love how sexy her ass looks and decide to stay and watch for a while."
            scene bg go_field8_2
            "She seems to feel your gaze weighing on her. Instead of hiding herself though, she gives you an even better view."
            "After enjoying the view for a while, you decide to go before you get nosebleeds."
            $ inhibition -= 1
    return


label go_field9:
    
    #Panning left and right
    scene bg go_field9:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 2 xalign 1.0 yalign 1.0
        pause 1.0
        linear 2 xalign 0.0 yalign 0.0
    with fade
    "The cheerleader club came to support your football team!"
    "The opposing team was so distracted that they score an easy victory."
    girls "Go Ashford go!"
    
    $ inhibition -= 1
    $ athletics += 1
    if renpy.random.randint(1, 3) == 1:
        $ athletics += 5
    return


label go_field10:
    
    scene bg go_field10 with fade
    
    "While those two unsuspecting teachers were watching the soccer game, kids pulled a prank on them, activating the water sprinklers."
    pov "Well, I've done worse in my days..."
    
    $ behavior -= 1
    $ morale += 1
    return
    

label go_field11:
    
    scene bg go_field11 with fade
    
    "This girl never misses a game from the boy football team."
    "She spends a lot of time with them in the locker room after the match, too."
    
    $ deviance += 1
    $ athletics += 1
    return
    
    
label go_field12: #Make this event happen only once?
    
    scene bg go_field with fade
    "You heard that a temporary boxing ring has been set up near the sports field. It worries you that violent sports would be practiced in school: if 
     someone gets hurt, their parents will sue you to your last penny."
    "A very large crowd has gathered to witness the fight. You have to elbow your way through, finding it difficult to reach the ring."
    girl "Aaaah!"
    "As you approach, you hear a cry of pain, unmistakeably coming from a girl. What the hell is going on?"
    
    scene bg go_field12_1 with fade
    "On the ring, in front of the chanting crowd, a pretty young girl is riding a big, muscular boxer. You've seen the girl before, but you don't recognize the boy: 
     it seems he comes from another school."
    "A guy dressed as a referee is holding a mike and commenting the ongoing 'fight'."
    "Referee" "... and this particular battle pits our very own Saori, which some of you undoubtedly know well, against Stone, the star boxer from the rival school!"
    "Referee" "As you know, Ashford doesn't have a boxing team, so we worked out a little arrangement with Stone. Ladies and gentleman, I present to you a brand new 
         sport... CUNTBOXING!!!"
    "The crowd roars in approval."
    "Referee" "The rules of the game are simple: the last one to orgasm wins by K.O. The winning school will take home this season's boxing award, and the prize money for 
         a total of $5,000!"
    pov "(This is... outrageous!!! This is unacceptable behavior in school!!! This is...{w} Wait, how much money did he just say???)"
    "While you ponder the implications of it all, the girl is being fucked relentlessly by her opponent. He squeezes her tits hard with his strong hands."
    "Saori" "Aaaaaah, aaaah!!!"
    "She is moaning and wailing as her pussy is streched by his large, rock-hard cock. She moves her hips in rythm with his thrusts. Her screams are obviously 
     screams of pleasure, not pain as you first suspected."
    "Girls and boys in the crowd leer, make catcalls, and comment on the fighters' techniques and bodies."
    girl1 "This girl is fucked hard and rough in front of all her schoolmates, and look at her: she loves it! How lewd..."
    girl2 "Well, she is quite a slut... Although, I wouldn't mind riding that hunk! Look at the size of his..."
    pov "(Quick! I must do something about this!)"
    menu:
        "Stop this nonsense.":
            "Pushing your way through the crowd, you reach the ring and step on stage. Red faced, you rip the mike off the hands of the stunned referee-looking guy 
             and address the crowd."
            "Referee" "P-Principal..."
            pov "CUT IT OUT! CUT IT OUT!"
            "The chants stop, and a heavy silence falls on the crowd. People near the stage give you a dumbfounded look."
            pov "What the hell do you think you are all doing! This is a reputable school, not some open-air peep show!"
            pov "I am giving you all exactly {b}3 minutes{/b} to clear the field and go to class, or you will {b}ALL{/b} be placed in detention for a week. Do I make myself clear?"
            "You turn towards the offensive couple. They have stopped their humping, frozen in an embarrassing position. The girl is trying to hide herself and looks mortified."
            pov "As for you two exhibitionists..."
            "Before you say another word, though, the crowd starts booing and yelling at you. They are pissed that you spoiled their fun, and feel empowered by their number."
            guy "Fuck off!"
            girl "Yeah, get lost [povLastName]!!!"
            "You get booed, insulted and thrown all kinds of garbage as you forcefully disperse the crowd with the help of the security staff."
            "After a while, you manage to restore order, but it took all morning and you feel thoroughly spent. Everyone has deserted now, except the girl, who is left sobbing 
             in a corner of the ring."
            pov "And now Miss, wait until your parents hear about this..."
            
            $ behavior +=1
            $ morale -= 1
            $ deviance -= 1
            return
        
        "Chant with the crowd.":
            "Fascinated with the spectacle, you join the crowd and cheer them on."
            pov "(Well, this school badly needs the money! And she seems to be enjoying herself well enough...)"
            pov "Go girl! Ride him until he's spent!"
            girl1 "Ahah, even the principal has come to support our team!"
            girl2 "Hi, [povTitle] [povLastName]! Nice of you to come by..."
            "The girl on stage is being fucked roughly, her body bouncing with every thrust. Her pretty big tits are bizarrely deformed as her opponent squeezes them."
            "Saori" "Oooh yes! Do me harder!!!"
            "Watching this lewd act, you feel a familiar sensation arousing in your pants. The two girls next to you are watching your reaction with interest."
            "Referee" "Well, we haven't had a clear winner yet... Maybe it's time for a change of strategy! Let's see if Stone can resist Saori's secret weapon!"
            
            scene bg go_field12_2 with fade
            "Saori lifts herself, pulling out her opponent's dick from her dripping pussy. Using her love juices as lube, she starts playing with her butt and streching 
             her asshole."
            "Stone" "..."
            "You can see the boxer staring at her white, sexy ass, his mouth gaping in anticipation."
            "She grabs his dick and slowly inserts it in her wet ass, lowering herself on him."
            "Referee" "And here she goes! The secret technique of the Pink Moon School!"
            "Her ass swallows his dick surprisingly easily, and soon he is fucking her butthole even harder than he was doing her pussy."
            "Saori" "Aaaah! So big! Aaaah!!!"
            "She screams with a mix of pain and pleasure as his huge cock enters her ass. She seems to love this even more than being fucked in her pussy."
            pov "Wow..."
            "You sport a raging hard-on by now and the girls next to you cannot fail to notice."
            girl1 "Oh my, [povTitle] [povLastName], you're such a pervert! Does watching this slut being fucked in the ass turn you on?"
            girl2 "Wow, look at this! The principal's dick is almost as big as this guy's!"
            "Before you can say anything, the girl reaches for your groin and she frees your dick from your pants."
            "Grabbing your erect dick with her hand, she starts rubbing it. The feeling of her soft, skillful hand is very pleasant."
            girl2 "So hot... I can feel it bulge in my hand... Like it's got a life of its own! *giggle*"
            girl1 "Really? Let me see, I wanna touch it too!"
            "The girls start masturbating you in the middle of the crowd."
            "Meanwhile, the couple on stage are still fucking hard. The boxer is showing remarkable stamina, while the girl seems to be born for this type of things. 
             This could drag on forever."
            "Stone" "Raaaah, raaah..."
            "Saori" "Ahaaah, aaaaah..."
            "Referee" "Well, this match has been going on for 30 minutes now... Who will win and emerge as this year's champion?"
            "The boxer decides to sprint towards victory and increases his pace. He is now lighting fast, plunging his shaft in her ass all the way to his balls. She 
             screams and wails in passion as she feels ravaged by his cock."
            pov "..."
            "The girls in the public are taking good care of you, and you feel close to your limit."
            "As he keeps pounding the girl's ass, the boxer starts moaning and grunting louder."
            "Stone" "Ooooh!!!"
            scene bg go_field12_3 with doubleflash
            "Suddenly, the boxer guy arches his back and reaches climax, spurting loads of thick cum deep in the girl's ass."
            "'Adriaaaaaaan!!!', he screams, as he shoots his load."
            with doubleflash
            "Referee" "3... {w=0.8}2... {w=0.8}1... {w=0.8}K.O!!!"
            "He is cumming so hard that semen gushes out of her, dripping all over her pussy and butt. She cums only a few seconds after him, screaming in intense 
             pleasure as he dumps his last load into her."
            "Saori" "AAAAAAAAAH!!!"
            "Watching this is too much for you and you cum hard under the sweet, skillful touch of the girls hands..."
            with doubleflash
            girl1 "Aaah!!!"
            girl2 "Oh!!!"
            girl1 "There's so much..."
            girl2 "Our hands are covered in your hot cum, principal..."
            girl1 "Some of it even landed on my skirt and legs..."
            girl2 "It's all over my hands, so sticky... Here girl, do you wanna taste?"
            girl1 "*licking* Yummy... Here, clean my fingers too."
            girl2 "Mmmh..."
            "Thanking the girls for their help, you step on the ring to congratulate the champion."
            pov "Well done, kid!"
            "Saori" "Thank, ah... you..."
            pov "You really {i}did{/i} work your ass off to achieve this result!"
            "You decide that she deserves the largest share of the reward. The remainder will help your finance, which is also nice."
            pov "Well, I hope next year's competition will be as exciting as this one!"
            
            $ behavior -= 1
            $ deviance += 1
            $ reputation += 1
            $ cash += 500
            $ r = renpy.random.randint(1, 3)
            if r == 1:
                $ deviance += 5
            elif r == 2:
                $ athletics += 5
            return            
             
            
label go_field13:
    
    scene bg go_field13 with fade
    
    "This girl has skipped practice to meet up with her boyfriend from another school."
    guy "Oh yes... I love it when you wear your sports uniform..."
    girl "Mmmh... Just be careful this time, okay? I don't want any more cum stains..."
    
    $ deviance +=  1
    $ inhibition -= 1
    $ athletics -= 1
    $ behavior -= 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5    
    return


label go_field14:
    
    "Rina from the swimclub left you a message, asking you to meet up with her behind the running track."
    
    scene bg go_field14_1 with fade
    go_rina "*giggle* oh, [povTitle] [povLastName], I didn't know you had such a perverted mind..."
    pov "Come on, baby, you're the one who is always teasing me in your sexy swimsuit..."
    go_rina "All right, I think we can agree that I am a bad girl... Will you punish me for my insolence?"
    "You grind against her for a while, taking out your cock and working it on her crotch. Through her swimsuit, you can feel becoming very wet as your shaft 
     rubs against her clit."
    go_rina "Oh [povTitle] [povLastName]... Maybe we should... Ahhh... stop..."
    pov "Not a chance, kitten, this has already gone too far... Aahhhh!!!"
    
    scene bg go_field14_2 with flash
    "You cum with great force, surprising her."
    with doubleflash
    pov "Aaaarrrrrhhhhhh!!!"
    
    scene bg go_field14_3
    go_rina "Aaaah, [povTitle] [povLastName]!!! Aaaaaahhh!!!"
    go_rina "*annoyed* Look at the mess you've made... Even my boobs are covered in cum... What am I supposed to do now?"
    pov "Well, we could take this to the shower room..."
    go_rina "*giggle* That's not a bad idea at all..."

    $ deviance +=  1
    $ inhibition -= 1
    if go_HwithRina < 3:
        $ go_HwithRina = 3    
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5    
    return


label go_field15: # This would go well with a 'no underwear' policy
    
    #Panning up and down
    scene bg go_field15:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 4.0 xalign 1.0 yalign 1.0
        pause 1.0
        linear 4.0 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(10.0)
    $ go_bg=ImageReference("bg go_field15")    
    show screen scroll_screen
    
    "It's important for tennis players always to strech out before a match. Incidentally, this is also your favorite part."
    
    $ inhibition -= 1
    $ athletics += 1
    hide screen scroll_screen
    return
    

label go_field16:

    #Panning up and down
    scene bg go_field16:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 4.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 4.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(11.0)
    $ go_bg=ImageReference("bg go_field16")    
    show screen scroll_screen
    
    "Rivals on the field can become great friends off it. Sometimes even more than friends..."
    
    $ inhibition -= 1
    $ athletics += 1
    hide screen scroll_screen
    return


label go_field17:
    
    scene bg go_field17 with fade
    
    "The best players in the baseball team have many hardcore fans. Only a handful are privileged enough to get really close to them, though."
    
    $ deviance += 1
    $ morale += 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


#### SCHOOL GROUNDS EVENTS ####

label go_grounds1: # Would go well with a 'no panties' policy
    
    scene bg go_grounds1_1 with fade
    "A young girl confronts you in the schoolyard."
    girl "[povTitle] [povLastName]! I am a first year student, and I want to complain about your style of management!"
    girl "This school is a dump! Girls and boys keep fooling around instead of studying, sexual harassement is everywhere..."
    girl "...and your policies aren't helping one bit!"
    girl "This is outrageous, given the enormous tuition my parents have to pay, I expected much higher educational standards from this establishment!"
    "She looks really pissed. You don't really know what to say."
    pov "I... Ahem... Well..."
    if inhibition < 50:
        "Suddenly, a gush of wing blows across the yard."
        scene bg go_grounds1_2
        girl "Aaaaah!!!"
        "Wait a minute... She isn't wearing any panties!"
        pov "Fufufu... You came to complain about this school's lewdness, yet you aren't wearing underwear???"
        scene bg go_grounds1_3
        girl "No I... Uh..."
        pov "*laugh* What a perverted little girl you are! I bet you're getting off from yelling at me while naked under your skirt..."
        pov "Is that it? Does it make you horny? Are you wet?"
        pov "Come on! Tell your principal the truth!"
        girl "No!!! I... No!!!"
        "The girl is red with embarrassement. She is struggling for words..."
        "She gives you a furious look and for a second, you are unsure if she's going to cry or burst with anger. Instead, she suddenly turns back and runs away."
        girl "Buwaaaahaaa!!!"
        pov "Ha! Can you believe this girl?"
        
        $ deviance += 1
        $ behavior += 1
        
    else:
        "Your pathetic excuses don't even register with her."
        girl "You better turn this ship around, quickly! I didn't go through school with straight A's to end up in a ditch full of sleazy bums!"
        "She storms out and you heave a sigh of relief."
        
        $ deviance -= 1
        $ morale -= 1
        
    return
    
        
label go_grounds2:
    
    scene bg go_grounds2_1 with fade
    
    "As you prepare to leave school, a girls recognizes you."
    girl "Hi [povTitle] [povLastName]! Keep up the good work!"
    
    menu:
        "Thank you, I will do my best!":
            pov "Thanks, I'm trying!"
            girl "Good luck, [povTitle] [povLastName]!"
            
            $ morale += 1
            return
            
        "It's a privilege to work with friendly students like you!":
            pov "It's nice to be able to help nice, bright students like yourself to grow."
            scene bg go_grounds2_2
            girl "*giggle* Thank you Sir!"
            
            $ morale += 1
            return
            
        "It's a privilege to work around hotties like you!":
            pov "Well, working here is great. I get to see cute, hot babes like you all day! *wink*"
            if deviance < 15:
                "She looks shocked by your answer."
                girl "Hey! Stay away from me!!!"
                
                $ morale -= 1
                
            elif deviance <50:
                "She blushes."
                girl "Oh, [povTitle] [povLastName]... What are you saying..."
                      
                $ deviance += 1
                      
            else:
                scene bg go_grounds2_2
                "You compliment her on her boobs. She laughs."
                girl "Oh principal, you're so naughty! *giggle*"
                girl "Well, perhaps I'll let you touch them one day! *wink*"
                
                $ deviance += 1
                $ morale += 1
            
            return
        
        "Did I give you permission to address me?" if evil_points >= 1:
            pov "Go away."
            "She looks shocked by your rudeness. You walk past her, ignoring her pained look."
            
            $ morale -= 1
            return


label go_grounds3:
    
    scene bg grounds
    
    "Kids are playing in the fountain, fighting and jumping around."
    
    with vpunch
    "*splash*"
    scene bg go_grounds3 with fade
    girl "Oh no! I'm all wet now..."
    
    $ behavior -= 1
    $ inhibition -= 1
    return
        

label go_grounds4: # Would go well with a 'no panties' policy
    
    scene bg go_grounds4 with fade
    
    "Many students come to school by bike. That's a good, healthy habit."
    pov "It's amazing how skin-tight cycling shorts have become these days..."
    
    $ inhibition -= 1
    $ athletics += 1
    return


label go_grounds5:
    
    "Some lovebirds use the yard behind the school for romantic meetings."
    
    scene bg go_grounds5_1 with fade
    girl "Aaah, you said, aaah, that we'd meet here so you can declare your true love..."
    guy "Of course baby, just bear with it... You're about to feel the intensity of my love."
    girl "Ohhh, ahhh, you're too big! You're tearing me appart! Aaaah!"
    guy "Hush babe... Bear with it... Ohhhh!"
    scene bg go_grounds5_2 with doubleflash
    guy "Uaaaah!!!"
    girl "Aaaaaah!!!"
    "Loads of his cum splash in her pussy and out, staining her panties and uniform."
    guy "Ooohhhh yes... That's it baby! Do you feel my liquid love warming your pure cunt, er, heart?"
    girl "You jerk..."
    
    $ deviance += 1
    $ inhibition -= 1
        
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return
    
    
label go_grounds6:
    
    #Panning up and down
    scene bg go_grounds6:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 2.0 xalign 1.0 yalign 1.0
        pause 1.0
        linear 2.0 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(6.0)
    $ go_bg=ImageReference("bg go_grounds6")    
    show screen scroll_screen
    
    "The art club is taking risqué photos outside today for the school magazine."
    guy "Come on baby, give me a lustful look... That's it..."
    with flash
    guy "Show me some more... That's right, open it up for the camera."
    with doubleflash
    girl "It's... it's embarrassing..."
    with flash
    guy "This is really good... Keep going and you will become a professional model in no time!"
    
    $ artistery += 1
    $ inhibition -= 1
    if renpy.random.randint(1, 2) == 1:
        $ artistery += 5
    hide screen scroll_screen
    return
    

label go_grounds7:
    
    scene bg go_grounds7 with fade
    
    "This girl has just transfered from an all girls school"
    "She likes to show her classmates some of the tricks she learnt."
    
    $ deviance += 1
    $ inhibition -= 1
    return
    

label go_grounds8:
    
    scene bg go_grounds8 with fade

    "Everyone enjoys a treat after a hard day's work."
    girl "Mmmhhh..."
    guy "Come on girl, didn't your daddy teach you not to talk with your mouth full?"
    
    $ deviance += 1
    $ inhibition -= 1
    $ morale += 1
    return


label go_grounds9:
    
    scene bg go_grounds9_1 with fade
    
    girl "Aaah [povTitle] Principal, aah, aaah! This is too much! Aaaaaaah!!!"
    pov "Shut up kid, this is your punishment and you're going to take it all the way."
    pov "How dare you tease me by flashing your naked pussy in the schoolyard!"
    girl "Aah, ah, mmhhh! I'm sorry sir, I only meant it as a joke... It was a bet with my friends... Let me go, aaahh!"
    pov "Well, the joke's on you now... You awoke the beast, and it's going to fuck you like the dirty slut you are."
    girl "Aah, no, principal, I'm sorry, aaaaaah! Cars are coming, please, let's stop!"
    pov "Well, it's even better, everyone will see your true nature then."
    girl "Nooo!"
    pov "Oh my, you are so wet... You love being fucked in public like a street whore, don't you?"
    girl "I don't, aaah! This is... Oooohhhhh..."
    pov "You can say that, but your body is more honest... You're screaming so loud I bet all the neighbors are watching us from their windows right now."
    girl "Don't say that, aaaaaaahhh... I'm so embarrassed..."
    "Even as she says that, her pussy is dripping wet. You push her hard against the lamppost and fuck her even faster."
    pov "Ready? I'm going to pump loads of cum into your dirty pussy..."
    girl "Nooo, ah, don't... Not inside... Aaaaahhhh!!!"
    
    scene bg go_grounds9_2 with doubleflash
    pov "Uuuuurrrhhhh!!!"
    girl "Aaaaaaahhh!!!"
    "She climaxes as you cum hard into her tight pussy. Her cries are enough to alert half the block, but she doesn't seem to care anymore."
    girl "OOOOH, YES!!! AAAAAH!!!"
    pov "Fufufu... You really are a horny bitch, cumming from being fucked in the street..."
    "Pulling back, you stop holding her and she slips down to the ground. You spurt the last of your cum on her face."
    "She's half passed out after orgasming. Her clothes are ripped open and hot, sticky cum is gushing out of her pussy with dirty sounds."
    "You stride over her and leave her there, walking back home with a smile on your face."
    
    $ deviance += 1
    $ inhibition -= 1
    $ morale -= 1
    return


label go_grounds10:

    if deviance == 100 and inhibition == 0:
        scene bg go_grounds10_2 with fade
        $ deviance += 1
        $ inhibition -= 1
        if renpy.random.randint(1, 3) == 1:
            $ deviance += 5
    else:
        scene bg go_grounds10_1 with fade
        $ deviance += 1

    "Looks like he got himself a 'ride' home!"
    
    return
    

label go_grounds11:

    #Panning up and down
    scene bg go_grounds11:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 4.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 4.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(11.0)
    $ go_bg=ImageReference("bg go_grounds11")    
    show screen scroll_screen

    "This girl is modeling outside for the art club. She wants to be an idol one day."
    "You feel like she has {b}a lot{/b} of potential."
    
    $ artistery += 1
    $ inhibition -= 1   
    if renpy.random.randint(1, 3) == 1:
        $ artistery += 5
    hide screen scroll_screen
    return




#### GYM EVENTS ####

## This section contains events that could go with the cheerleading club as well.

label go_gym1:
    
    scene bg go_gym1 with fade
    
    "Stretching before practice is key."
    girl1 "Are you really sure this exercise will improve our flexibility?"
    girl2 "Aaahhh! I feel strange..."
    guy "Shut up and trust me. With a coach like me to help you, you will be on top in no time."
    
    $ deviance += 1
    $ inhibition -= 1
    return


label go_gym2: # This one is a bit over the top: only on new game+?
    
    scene bg go_gym2 with fade
    
    "The girls invited you to come in the locker room with them. You obliged."
    girl "Oooh yes [povTitle] [povLastName]! Cover us with dirty cum!!!"
    
    $ deviance += 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5    
    return    
    
    
label go_gym3:
    
    scene bg go_gym3 with fade
    
    girl "Aaaah, [povTitle] [povLastName], you're so big! I feel your hot dick inside me!"
    pov "Mmmh, baby you are tight..."
    pov "Who would have thought the volleyball team captain was such a horny slut?"
    girl "*blushing* Don't say such things... You're the one who brought me here!"
    pov "Well, originally I only wanted to congratulate you on your victory... but I kind of lost track."
    girl "You played with my ass, put your fingers in me..."
    pov "... and you sucked my dick off after that! Don't pretend you don't enjoy this *smirk*"
    girl "Mmmhhh, aahhh... It's true..."
    pov "Come on honey, get ready, I'm at my limit..."
    girl "Aaaah yes! Pump your hot cum inside me! I want it!!!"
    with doubleflash
    pov "Whoaaah!!!"
    "You enjoy playing with her hot, horny body all morning."
    
    $ deviance += 1
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5     
    return


label go_gym4:
    
    #Panning up and down
    scene bg go_gym4:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 1.5 xalign 1.0 yalign 1.0
        pause 1.0
        linear 1.5 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(5.0)
    $ go_bg=ImageReference("bg go_gym4")    
    show screen scroll_screen
    
    "Cheerleaders perform all kinds of useful services to maintain high morale within the sports teams."
    
    girl "So baby, did you reach a decision about the scholarship that other school is offering you?"
    guy "Ah, yes... Fuck them! I'm never leaving Ashford!!!"
    girl "That's what I wanted to hear! *giggle*"
    
    $ deviance += 1
    $ athletics += 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    hide screen scroll_screen
    return


label go_gym5:
    
    scene bg go_gym5 with fade
    
    girl "[povTitle] Principal... Am I doing this right?"
    pov "Mmmh... Yes..."
    girl "I'm sorry watching us practice has made you so hard... It looks painful..."
    pov "..."
    pov "Oh, yes! So painful... It needs your help..."
    girl "I'm glad you agreed to let me give you a hand. Oh, it's swelling!"
    pov "Good girl... Now, try and use your tongue on it..."
    girl "Okay..."
    
    $ deviance += 1
    $ inhibition -= 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


label go_gym6:
    
    scene bg go_gym with fade
    
    "A girl is asking you to help her stretch out before the gym competition."
    menu:
        
        "Accept.":
            
            scene bg go_gym6_1 with fade
            pov "Come on, girl, you can do it!"
            girl "Uhhh... Ahhh..."
            
            if athletics > 50:
                scene bg go_gym6_2 with fade
                pov "You did it!!!"
                girl "*giggle* Yes, of course! Thank you [povTitle] Principal!"
                "You notice her huge tits are pressing against the floor now."
                pov "(And here I thought gymnasts were all flat-chested, underage girls...)"
                girl "I'm sorry, did you say something?"
                pov "Ahah, ahem, not at all!"
                
                $ inhibition -= 1
                $ athletics += 1
            
            else:
                "You help her for a few moments. After she has properly stretched out, she thanks you with a smile."
                
                $ athletics += 1
            
            if renpy.random.randint(1, 2) == 1:
                scene bg go_gym6_3 with fade
                
                "Later, you learn she aced the competition."
                $ athletics += 5
            
            return
                
                
            
        "Decline.":
            
            girl "I see, of course you're too busy for this kind of things. Sorry for my silly request."
            
            $ morale -= 1
            return
        
    
label go_gym7:
    
    scene bg go_gym7_1 with fade
    
    "As you walk towards the gym, you see a girl sitting down by herself, looking sad."
    pov "Hi there. Is something wrong?"
    girl "..."
    girl "The other girls from the gym class... They laugh at me and tell me that I'm too fat to be a proper gymnast..."
    menu:
        "You're not fat at all!":
            pov "You, fat? That's not true at all!"
            girl "But, I... They say my chest is too big, and that it looks ugly..."
            
            menu:
                "Success is in your mind, your body shape doesn't matter.":
                    pov "You don't have to conform to what they think a gymnast should look like."
                    pov "Just practice hard, do  your best, and you will get results!"
                    scene bg go_gym7_2
                    "She listens to you and thinks upon your words. She smiles."
                    girl "Yes, of course you're right. My body may be a handicap, but it won't hold me back from reaching the top!"
                    girl "All right, I'm going to try even harder from now on!"
                    
                    $ morale += 1
                    $ good_points += 1
                    return
                    
                "What a load of bull. Big boobs are great!":
                    pov "Come on, everyone loves big boobs. They are just jealous because you have such nice tits."
                    if deviance < 20:
                        "Your words don't seem to make her feel better."
                        girl "No... I don't want people to look at me that way..."
                        "You made her uncomfortable. You decide to continue on your way, hoping someone else will find the words to cheer her up."
                        
                        $ morale -= 1
                        
                    else:
                        scene bg go_gym7_2
                        "She laughs."
                        girl "Principal! You are not supposed to look at your students that way!"
                        "She blushes, but you managed to make her smile again."
                        
                        scene bg go_gym7_3 with fade
                        
                        "Later, you see her at gym practice. She is moving freely, not embarrassed by her body anymore."
                        
                        $ morale += 1
                        $ inhibition -= 1
                        
                    return
            
        "Ignore them, they're stupid.":
            pov "Whatever people say, don't let it get to you. People who judge others on their appearance are just idiots."
            girl "I know you're right... but... Those remarks still hurt..."
            pov "Well, you will just have to grow thicker skin. In the sports world you will meet a lot of competitive, aggressive people like them."
            girl "..."
            "She looks resolved. Picking herself up, she heads towards the gym."
            girl "All right, I'll just ignore them from now on."
            
            $ morale -= 1
            $ athletics += 1
            return
           
        "Oh come on, grow the fuck up.":
            pov "What are you, in kindergarten? People are mean to each other all the time, get over it."
            girl "But... but I hate it!"
            pov "Oh please... Just learn how to beat them at their own game!"
            girl "Beat them... at their own game? What do you mean?"
            pov "Next time a girl makes this kind of remark, just shoot back."
            pov "You can say something like: \"I don't take dietary advice from anorexic bitches like you. You're flat as an ironing board.\"."
            pov "...or: \"I hear you get fucked all day by the baseball team in the men's room, is that why your hair always smells like cum and piss?\"."
            "The girl is shocked by your offensive langage. At the same time, she reflects upon your suggestion."
            girl "Well... Maybe I should try it... At least I could get back at the motherfuckers..."
            "She gets up with new found resolve. Clenching her teeth, she heads for the gym."
            pov "Oh, this is good..."
            "You decide to follow her. Wouldn't want to miss a catfight!"
            
            $ behavior -= 1
            $ evil_points += 1
            return
            
    

label go_gym8:
    
    scene bg go_gym8_1 with fade
    "You walk in on a girl changing to her gym outfit."
    
    if inhibition >= 90:
        girl "Hey! Please go!"
        pov "Ah, ahem, sorry."
        
        $ morale -= 1
        
    elif inhibition >= 70 or deviance < 15:
        girl "Oh, [povTitle] [povLastName]! I'm getting changed, please wait a bit outside."
    
    else:
        girl "Hi, [povTitle] [povLastName]! I'm getting changed."
        pov "I see, I'll just go then..."
        girl "Not at all, stay! I don't mind."
        scene bg go_gym8_2
        "You sit down and chat with her about the weather while she undresses."
        "She blushes as she feels your gaze on her exposed body, but she makes no effort to hide it."
        
        $ inhibition -= 1
    
    return


label go_gym9:
    
    scene bg go_gym9 with fade
    
    "Cheerleaders! Fueling everyone's sex fantasies since 1873..."
    
    $ morale += 1
    return

    
label go_gym10:
    
    scene bg go_gym10 with fade
    
    "This girl lost a bet with her friends, and was forced to expose her goods to the players during basketball practice."
    "You've never seen as many missed shots and players running into each other."
    
    $ inhibition -= 1
    $ athletics -= 1
    return


label go_gym11:
    
    scene bg go_gym11 with fade
    
    "When this girl came back to the locker room, she found out that someone stole her panties!"
    "She has no choice but to spend all day without underwear."
    
    $ morale -= 1
    $ deviance += 1
    $ inhibition -= 1
    return


label go_gym12:
    
    scene bg go_gym12 with fade
    
    "This girl has spilled her energy drink all over the floor. She is cleaning up her mess."
    
    if inhibition >= 90:
        "She realizes you have been staring at her, and blushes. Ashamed, you quickly look away and leave."
        
        if renpy.random.randint(1,2)==1:
            $ morale -= 1
        else:
            $ inhibition -= 1
        
    else:
        "You admire the shape of her athletic legs and round ass. She feels your gaze upon her and blushes."
        
        $ inhibition -= 1
        
    return


label go_gym13:
    
    scene bg go_gym with fade
    
    "A girl is standing in the sports hall. A bunch of boys are crouching in front of her."
        
    scene bg go_gym13 with fade
    
    girl "So, this is what it looks like. Watch carefully!"
    go_guys "Woaaah!"
    "Guy 1" "It looks tight..."
    "Guy 2" "Such a nice pink color..."
    "Guy 3" "Open it up more!"
    girl "Okay guys, the two minutes are up... You will have to pay me again if you want to see any more!"
    go_guys "No, wait!"
    "They scramble for their wallets."
    pov "Virgins..."
    
    $ deviance += 1
    $ inhibition -= 1
    
    return

label go_gym14:
    
    scene bg go_gym14 with fade
    
    "That was close!"
    
    $ athletics += 1
    
    if renpy.random.randint(1, 2) == 1:
        $ athletics += 5

    return


label go_gym15: 

    scene bg go_gym15_1 with fade

    pov "..."
    with vpunch
    "How the hell did you end up like this???"
    girl1 "He's coming back to his senses..."
    girl2 "[povTitle] [povLastName], can you hear us?"
    girl1 "I think he fell on his head pretty hard..."
    pov "What... What the hell happened?"
    girl1 "We heard a big thud from outside the locker room."
    girl2 "When we rushed here, you were passed out on the floor..."
    girl1 "...we didn't know what to do, so we started undressing you..."
    girl2 "...to take you to the shower room and make you take a cold shower."
    girl1 "But it's good though, you woke up!"
    pov "(I remember now... I was peeking on the girls and then I slipped...)"
    girl1 "We were alarmed when we got here... There was a big bump under your pants. We thought it must be where you hurt yourself."
    girl2 "Look at it, it's all swollen... Let me feel it, to see if there is a broken bone..."
    "She runs her small, soft hand along your erect cock, squeezing it. It feels amazing."
    pov "Uhhhh..."
    pov "Don't... don't worry, there's no bone in it..."
    girl1 "But isn't that what the guys call a 'boner'?"
    girl2 "It doesn't seem to get better... Look, it's getting even bigger now... Perhaps I should give it a kiss so that it will heal?"
    girl1 "Good idea, do it!"
    
    scene bg go_gym15_2
    girl2 "Mmmh..."
    "She brushes the tip of your dick with her lips. She kisses it a few times, then starts flicking her tongue around it."
    "Precum is already coming out and she licks it off your cock."
    girl2 "Mmmh... I think something is coming out... [povTitle] [povLastName], are you feeling any better?"
    pov "Hmmm yes... It's good, you should continue..."
    girl1 "Oh that's a relief! Is there anything that I can do to help?"
    pov "Well, I... I smacked my ass on the floor when I fell... Perhaps you could massage it a little?"
    girl1 "Of course! Leave it to me!"
    "The twin girls play along nicely." 
    "The first girl is massaging your ass with her soft, skillfull hands. She sucks on one of her fingers to lubricate it and starts teasing your asshole with it."
    "The other girl is licking and sucking on your swollen dick, making dirty, slurping sounds as she covers your shaft with her saliva."
    "Between the three of you, you don't think there is any doubt as to what is going on here..."
    pov "All right girls, I feel a lot better now, but I must get up to patch myself."
    "Surprising the girls, you push them over. Grabbing their clothes, you rip off pieces of garment."
    pov "There, this will be useful for bandages."
    
    scene bg go_gym15_3 with fade
    girl1 "Ah!"
    girl2 "Hii!"
    pov "Good, I feel better now! Say, girls, you helped me a lot... Should I help you in return?"
    girl1 "Oh, [povTitle] [povLastName]..."
    girl2 "Don't tease us..."
    "Ignoring their weak protests, you shove aside their panties and expose their naked pussies. As you expected, they are both already very wet."
    pov "Come on girls, spread your legs and let me see... I looks like you both have gaping wounds in need of healing, don't you?"
    girl1 "Yes [povTitle] [povLastName]... Please help us..."
    girl2 "Do something about it, please... I can't hold it..."
    pov "That's my girls."
    
    scene bg go_gym15_4 with fade
    "You shove your erect cock in the first girl's pussy."
    girl1 "Ooh! Aaaah!!!"
    "She screams as you plunge your shaft deep inside her."
    "Your dick makes wet sounds as it pumps in and out of her wet, tight pussy."
    "Using your hand, your start fingering the other girl. Her horny pussy swallows your finger whole."
    girl2 "Aaahhhh..."
    "She moans with pleasure as you stick more fingers into her cunt."
    "Her love juices are flowing out and soon, you are able to shove one of your lubed fingers in her ass as well."
    girl2 "Aaahhh yes!!!"
    "You fuck the twins for a while, increasing your pace and slowly bringing them to their limit."
    girl1 "Your dick, aaah!!! It's incredible!!!"
    girl2 "Touch me more! I want it!!! AAAAAHHHH!!!"
    
    scene bg go_gym15_5 with flash
    "The look of rapture on their cute faces brings you to your limit."
    "You cum hard in the first girl while shoving your hand deep in the other girl's pussy. All three of you orgasm at the same time."
    with doubleflash
    pov "Uhaaaaaarrrrrhhh!!!!"
    girl1 "YEEEEEES!!!"
    girl2 "AAAAAAHHH!!!"
    "Twins, Basil. Twins."
       
    $ deviance += 1
    $ inhibition -= 1
    
    if renpy.random.randint(1, 2) == 1:
        $ deviance += 5
    return
    

label go_gym16: 
    
    scene bg go_gym16 with fade
    
    "Whether you're thirteen or 30, peeking in the girl's locker room never gets old."
    
    return


label go_gym17: #Would go well with a 'no panties' policy
    
    #Panning up and down
    scene bg go_gym17:
        xpos 0 ypos 0 xanchor 0 yanchor 0
        pause 1.5
        linear 3.0 xalign 1.0 yalign 1.0
        pause 1.0
        linear 3.0 xalign 0.0 yalign 0.0
    with fade
    
    #These lines of code allow for scrolling with the mousewheel after panning is done
    pause(8.0)
    $ go_bg=ImageReference("bg go_gym17")    
    show screen scroll_screen
    
    "Cheerleader" "Go, Ashford, go, go!!!"
    "The efforts of this girl do wonders for your team."
    
    $ morale += 1
    $ athletics += 1
    if renpy.random.randint(1, 4) == 1:
        $ athletics += 5
    
    hide screen scroll_screen
    return



#### LIBRARY EVENTS ####
    
label go_lib1:
    
    "As you browse the library for books on sex education, you hear muffled sounds coming from behind the shelves."
    
    scene bg go_lib1_1 with fade
    
    girl "Wait, what are you doing!"
    guy "I like your sexy underwear... Were you wearing this in anticipation of our little study session?"
    girl "Nooo! You said we were going to study grammar together... Aahhh..."
    guy "Come on baby, you know you want it. I can feel your pussy is already so wet..."
    girl "Don't say such things... This isn't right..."
    guy "And yet, look how easy it is to push my finger in you..."
    girl "Ahaaahhh!"
    guy "Your hungry cunt is swallowing my finger... You're spreading love juices all over your panties!"
    girl "Stop it already... Aaah!!!"  
    guy "Look at this, your cunt is twitching! Your body doesn't lie... You want a dick right now, don't you?"
    if deviance > 75 and inhibition < 50:
        girl "..."
        guy "Come on, tell me the truth!"
        girl "I... Yes..."
        girl "I need it now... I need a hot dick in my pussy!"
        guy "*laugh* Ahah, you are so honest all of a sudden!"
        girl "Hurry up... Put it in..."
        
        scene bg go_lib1_2
        "The guy pulls out his erect cock. Grabbing her boobs from behind, he starts fucking her doggy-style."
        girl "Oooh yes, aaaah!!!"
        girl "I... I feel your dick inside me, it's so good!"
        guy "Hehe, your pussy is gripping my cock so nicely..."
        girl "Shut up and fuck me... Fuck me harder!"
        "He continues ramming her for a while, his balls slapping her cunt every time he shoves it in."
        guy "Oh baby... I'm about to come..."
        girl "Don't, ahhh... come inside... Today is bad, aahhh..."
        guy "All right... Aaaaah!!!"
        
        scene bg go_lib1_3 with doubleflash
        "The guy shoots loads of cum on her, spraying her ass, uniform, even her face and hair."
        girl "Watch it!!!"
        guy "Hehe... What a mess..."
        girl "Aaah... You made me all sticky... YOU IDIOT!"
        "You leave discretely while they're fighting."
        
        $ deviance += 1
        $ inhibition -= 1
        if renpy.random.randint(1, 3) == 1:
            $ deviance += 5
            
    else:
        girl "No... We can't do that here..."
        guy "*annoyed* Ok then... Let's go to my place!"
        girl "Ahhhh, you are so persistent!"
        girl "*blush* Well... Since we're not going to manage to study tonight anyhow..."
        guy "Good girl! Just wait until we get home, and I'll..."
        girl "But tommorow, we ARE going to study! PROMISE ME!!!"
        guy "All right, all right..."
        
        $ deviance += 1
    
    return
        

label go_lib2:
    
    "You hear a girl giggle from the back of the library."
    
    scene bg go_lib2 with fade
    
    girl "All right, onii-san, enough studying already... Whe are we going to have {i}fun{/i}!"
    guy "*glups*"
    girl "You like these, don't you you? Tee hee hee!"
    "Ignoring his protests, she continues teasing him."
    
    $ inhibition -=1
    
    return


label go_lib3:
    
    scene bg library with fade
    
    "You are looking for a rare book about the history of Ashford Academy."
    "A girl from the reading club is helping you look for it."
    
    scene bg go_lib3_1 with fade
    
    girl "I'm sorry [povTitle] [povLastName]... I can't find it anywhere!"
    pov "Uh, well, stay up there and look once more!"
    girl "Okay..."
    pov "(The view from down here is just too good...)"
    
    menu:
        "Look, don't touch.":

            "After getting an eyeful, you help her get back down."
            girl "I'm really sorry we couldn't find what you were looking for, [povTitle] [povLastName]."
            pov "Oh well, don't be sorry. Sometimes looking is its own reward..."
            "She gives you a puzzled look. You smile and say good bye to her before leaving the library."
            
            $ academics += 1
            
            return
            
    
        "Take advantage of the situation.":
            "You have a perfect view of her white ass and laced panties while she browses the bookshelf."
            girl "[povTitle] [povLastName], I really can't find it..."
            pov "Keep looking, my dear, it must be somewhere around here..."
            "Watching under her skirt is fun, but now you feel you want more."
            if deviance < 50 or inhibition > 50:
                "Bringing your hands up, you grab her ass."
                girl "W-What are you doing!"
                pov "Here, let me push you up so you can reach the top shelf!"
                
                if deviance < 15:
                    girl "B-but, you're touching... Let me go!!!"
                    "She slaps your hands off and gets down the ladder."
                    girl "This behavior is unacceptable! I will write to the board!"
                    "She's mad..."
                    $ morale -= 1
                    $ reputation -= 1
                else:
                    girl "I-Is this really necessary?"
                    pov "Of course! We have to look everywhere! Come on, don't waste time, look for that book."
                    "You give her a little encouraging squeeze."
                    girl "Ahaah!!!"
                    $ morale -= 1
            
            else:
                
                "Your dick is rock hard and you feel like you're loosing control over yourself."
                "Your hands move of their own accord. Before you know it, they are grabbing her sexy ass."
                girl "Aaaah! [povTitle] [povLastName]! What are you doing???"
                "She wriggles her ass to try and escape your grasp, but she can't do anything else than cling to the ladder in order not to fall."
                girl "Ah, ah, ah... [povTitle] [povLastName], this is wrong! Aaah!"
                "Ignoring her, you massage her ass, kneading her buttocks between your hands. Her skin is smooth and soft to the touch."
                girl "[povTitle] [povLastName], if you don't stop now, I will report this... Ahaaaa!"
                "Bringing your face only inches from her crotch, you pull her panties out of the way."
                
                scene bg go_lib3_2
                girl "[povTitle] [povLastName]! No!"
                "Her beautiful, shaven pussy is right here in front of your eyes. It's got a nice pink color. You can smell the faint, sweet scent emanating from it."
                "You breathe out softly on her exposed pussy. She is very sensitive and shivers when she feels your breath."
                pov "Relax, baby girl... I'm going to take good care of you..."
                "Leaning in, you softly kiss her pussy lips. She yelps in surprise and tries to avoid you, but you hold her ass firmly in place with both hands."
                girl "Not there, aaah!!!"
                "You starts licking her outer lips and her clit while continuing to massage her ass. Her body trembles under your touch."
                "Her body is responding and soon you feel a sweet, familiar taste on your tongue. Your tongue teasing her sex is too much for her, and her love juices 
                 have started flowing."
                girl "Mmmh, mmmh..."
                "Her body reacts despite herself and she starts moving her hips back and forth slightly. You push your tongue inside of her pussy."
                girl "Ahaaaah!!!"
                "Sucking and licking her skillfully, you can feel desire building up in her body. She is grinding her pussy against your face."
                girl "Oh, aah..."
                "She doesn't resist as you lift up the top of her uniform to reveal her small, beautiful tits."
                girl "Mmmh..."
                "She moans sexily as you rub her tits and pinch her nipples."
                "Her pussy is drenched by now, love juices and saliva flowing out and running down her thighs."
                pov "All right baby girl, I think now you're ready for this..."
                "You take out your cock from your pants. Her eyes widen as she sees your erect shaft, oozing with pre-cum."
                
                if deviance < 75:
                    girl "Ah, no! [povTitle] [povLastName]!"
                    "She resists as you pull her down towards your dick."
                    girl "I'm sorry [povTitle] Principal... I... I can't go any further."
                    "Freeing herself from your grip, she fixes her clothing and runs off."
                    pov "Damn... I was so close!"
                    
                    $ deviance += 1
                    $ inhibition -= 1 

                else: 
                
                    girl "[povTitle] [povLastName]! This is... so big! Are you going to put this in me?"
                    "She spoke with a mix of apprehension and lust."
                    pov "Would you like that?"
                    girl "..."
                    girl "I... Okay..."
                    scene bg go_lib3_3
                    "Although it looks like your shaft is too big for her fragile pussy, she is so wet that you can enter her tight hole without difficulty."
                    girl "Ooooh!!!"
                    "Grabbing her ass, you pull her down on your cock and fuck her sweet pussy as she clings to the ladder the best she can."
                    girl "Aah, aaah, aaaaaah!!!"
                    "Her pussy is tight and hot, gripping your dick in a sweet cocoon of flesh. A feeling of pure bliss washes over you."
                    "You increase your thrusts and the girl starts moaning wildly, overwhelmed by lust and sexual pleasure."
                    girl "AAAAAAH, AAH, AAAAAAAAAAH!!!"
                    "You are both reaching your limit. Pulling her down , you shove your cock deep inside of her just as you are about to come."
                    
                    scene bg go_lib3_4 with doubleflash
                    "You explode into her, spurting load after load of hot jizz in her pussy."
                    pov "Aaaaaaaaaaaah!!!"
                    "She climaxes loudly too as she feels your warm cum gushing insied of her."
                    girl "AAAAAAAAHHH!!! AAAAAAAAAAAAAAHHH!!!"
                    "Her screams echo into the library as you both revel in your orgasm."
                    "Gently, you help her down the ladder and hold her in your arms as her climax recedes. She is looking at your with dreamy eyes."
                    with vpunch
                    "Suddenly, something falls from the top of the shelf and lands on the floor next to you."
                    girl "Oh, look... Isn't that the book you were looking for?"
                    pov "Indeed! Well done, my dear, we made it!"
                    "She giggles and rests her head on your chest. You both stay like this for a while, loosing track of time. When you finally come out of the library, 
                     it's already dark outside."
                    
                    $ deviance += 1
                    $ inhibition -= 1
                    $ academics +=1
                    
                    $ r = renpy.random.randint(1,3)
                    
                    if r == 1:
                        $ deviance += 5
                    elif r == 2:
                        $ academics += 5
        
            return
    
        
label go_lib4:
    
    scene bg go_lib4 with fade
    
    "There are rumors of a secret room in the library, where girls from the book club surrender themselves to their lowest instincts..."
    "People have a lot of imagination. But sometimes, when alone in the library, you could swear you heard some muffled moans coming from behind the walls..."
    
    $ deviance += 1
    
    return
    
    
label go_lib5:
    
    scene bg go_lib5 with fade
    
    girl "Aaaw, the air con is out of order again..."
    pov "Yes, it's getting really hot in here... *glups*"
    
    $ inhibition -= 1
    
    return
    
label go_lib6:
    
    if inhibition >= 50:
        
        scene bg go_lib6_1 with fade
        
        "This girl is busy studying for next week's exam."
        pov "Hi there! How is the studying going?"
        girl "This exercise is really tough..."
        pov "Let me see..."
        
        if deviance > 15:
            scene bg go_lib6_2
            "As you look over her shoulder, she plays with her jersey, giving you a glimpse of her cleavage."
            girl "It's hot in here..."
            pov "Indeed... *sweating*"
            
            $ inhibition -= 1
            $ academics += 1
        
        else:
            pov "Why don't you try this?"
            girl "Oh, i see it now. Thanks, [povTitle] [povLastName]!"
            
            $ academics += 1
    
    else:
        scene bg go_lib6_3 with fade
        
        "This girl is studying for her next exam."
        "She is wearing a sexy top. It's obvious she doesn't have any bra."
        "You approach and greet her."
        
        if deviance <=75:
            pov "Hi there! How is the studying going?"
            girl "Oh, hi [povTitle] [povLastName]! I think I have trouble with this section..."
            pov "Well, let me see..."
            "Wow, what a nice view..."
            
            $ inhibition -= 1
            $ academics += 1
        
        else:
            scene bg go_lib6_4
            pov "How's my little kitten going today..."
            girl "Ah, [povTitle] [povLastName], it's you..."
            pov "Meet me after school, at the usual spot. I've been saving myself for you, I hope you're ready for it."
            girl "Mmmh, [povTitle] [povLastName]... I cannot wait to suck on your dirty cock..."
            
            $ inhibition -= 1
            $ deviance +=1
            $ academics += 1            
    return
    

#### OFFICE EVENTS ####

label go_office1:
    
    if deviance <= 25 or inhibition >= 90:
        scene bg go_office1_1 with fade
    elif deviance <= 50 or inhibition >= 70:
        scene bg go_office1_2 with fade
    elif deviance < 100 or inhibition > 0:
        scene bg go_office1_1 with fade
    else:
        scene bg go_office1_2 with fade
    
    "A girl rushes in your office without knocking or announcing herself. She's the editor of the school's newspaper."
    girl "Get your brand new issue of the Ashford Gazette, Principal! Breaking news and shocking investigations by your favorite reporter!"
    "Instead of breaking news, what this rag really focusses on is gossip, urban legends and cheap fan fiction. The problem page is pretty popular with 
     heartbroken students, though."
    pov "*sigh* What's on the front page this time..."
    
    if deviance <= 25 or inhibition >= 90:
        girl "Shocking news! Students have been seen kissing in school! On the mouth! We got this from a reliable source..."
        pov "Allright, whatever..."
              
    elif deviance <= 50 or inhibition >= 70:
        girl "Scandal! Learn all about the perverted cook who puts aphrodisiacs in the students meals! Our science team contributed to this edition..."
        pov "Can you believe this? I can't..."
        
        $ academics += 1
        
        
    elif deviance <= 80 or inhibition >= 50:
        
        girl "Amazing! Rumors abour students doing perverted things near the sports field are true! Our special investigator reports after a week undercover..."
        pov "Oh come on, give me a break... Haven't you got better things to do?"
        
        $ athletics += 1
    
    else:
        if deviance < 100 or inhibition > 0:
            girl "Unbelievable! Ashford has been ranked the most perverted school in Japan! Students are having sex everywhere on campus, even the principal is 
                  rumored to sleep with the students..."
            pov "Whaaat!?! Now that's going too far!"
            pov "Give me this! That's it, I've had enough! I am shutting this stupid rag down!"
            girl "Nooo! please sir, no! This newspaper is my life... Things just started looking up, and this edition's sales are going through the roof..."
            pov "You are not talking your way out of this!"
            girl "Please, [povTitle] [povLastName], please! I'll do anything you ask, I'll be a really good girl, just don't shut down the Gazette, please..."
            "She is begging you now, her eyes are full of tears."
            pov "Aw, all right... *sigh* Maybe we can work something out..."
            
        else:
            girl "Shattering news! Meet the girl who eats food with cum for lunch! Don't miss out on our exclusive interview, where she talks about the health benefits of 
                  her unorthodox diet!"
            pov "Goddamnit! Is there any way to shut you up?!?"
        
        scene bg go_office1_3 with fade
        girl "Mmmh... mmm..."
        pov "I supppose this is one way to silence the media."
        
        $ deviance += 1
        
        if renpy.random.randint(1, 3) == 1:
            $ deviance += 5
        
    return
        

label go_office2:
    
    scene bg go_office2 with fade
    
    "This teaching assistant has no academic knowledge or teaching skills to speak of, but she has a way of making sure you never fire her."
    
    $ deviance += 1
    $ academics -= 1
        
    if renpy.random.randint(1, 4) == 1:
        $ deviance += 5    
    return
    
    
label go_office3:    
    
    scene bg go_office3 with fade
    
    "Male students always line up to enroll in this teacher's class. You think you know why."
    
    $ inhibition -= 1
    $ academics += 1
    $ morale += 1
    
    return
    
    
label go_office4: 
    
    scene bg go_office4 with fade
    
    "Hinata has come to visit you this morning."
    go_hinata "Aaaaah, mmmh! [povTitle] Principal, you came all over my face..."
    pov "Well, be a good girl and lick it off..."
    go_hinata "Okay..."
    "What a nice way to start the day!"
    
    $ deviance += 1
    
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    
    return


label go_office5: 
    
    scene bg go_office5 with fade
    
    girl1 "Ah, [povTitle] [povLastName]! Why are you doing this..."
    pov "This is your punishment, child, remember? Just play along, or I {i}will{/i} tell your parents that you were caught smoking in the mensroom..."
    girl1 "She made me do it..."
    girl2 "Oh come on, stop whining... Let the perverted principal have his fun, and we're getting off easy!"
    girl1 "But it feels... strange..."
    "You run your fingers along their sensitive pussies, lightly caressing their clits and outer lips. The girls shiver under your touch."
    girl2 "Mmmpf, hurry up and get it over with, pervert."
    "Defiant as she is, her body is reacting to your touch. You can feel their pussies getting wetter as you continue your playing."
    "Slowly, you insert a finger into each girl's pussy."
    girl1 "Aaaaaah! It's coming in!!!"
    girl2 "Hey! Stop... stop it!"
    pov "Hush now girls. This only the beginning..."
    
    $ deviance += 1
    $ behavior += 1
    $ morale -= 1
    
    return


label go_office6: 
    
    scene bg go_office6 with fade
    
    "One of the professor made this student his personnal pet."
    "She submits to his every whim now, meeting him in his office every morning for 'training'."
    
    $ deviance += 1
    $ behavior += 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return
    
    
label go_office7: 
    
    scene bg go_office7 with fade
    
    girl1 "[povTitle] [povLastName], how long do we have to stand like this?"
    girl2 "This is too embarrassing..."
    "Girl 3" "[povTitle] [povLastName], can we get our bra back now? Please?"
    pov "You've been told many times not to talk during class... It is disrespectful to your teachers."
    pov "So your punishment is to stand in the faculty's office like this for 15 minutes, hopefully this will make you more respectful."
    pov "And if not... I will post this on the schoolboard."
    with flash
    "*click*"
    girls "Hiiiiiiii!!!"
    
    $ behavior += 1
    $ inhibition -= 1
    $ morale -= 1
    
    return
    

label go_office8: 
    
    scene bg go_office8 with fade
    
    "Since you adopted the nude uniform policy, some teachers have decided to follow the same dress code to be on par with their students."
    pov "Hello, ladies..."
    "Teachers" "Hello, [povTitle] [povLastName]! We still have time before class, would you like to hang around with us while we are waiting? *giggle*"
    pov "Well of course... It {i}is{/i} my duty to look after the well being of my employees, after all."
    
    $ deviance += 1
    $ inhibition -= 1
    
    return


label go_office9: 
    
    scene bg go_office9 with fade
     
    girl "[povTitle] Principal, aaah! Stop, why are you touching me there!!!"
    pov "Well, how can I resist touching you when you are taking such a lewd pose?"
    girl "B-but... you made me do it! You said... you just wanted a look and..."
    pov "... and I won't expel your boyfriend from the school. And that's true"
    pov "Now, behave, or I {i}will{/i} kick him out. Is that what you want?"
    girl "..."
    girl "No..."
    pov "Good... Now let me play with your ass a bit."
    girl "Aaaaaahaaa!!!"
    pov "Mmmh, you're quite the sensitive one, aren't you? I just started playing with your ass, and your love juices are already flowing..."
    girl "That's not, aaah... no..."
    pov "Your asshole is your weakness, isn't it? You and I are gonna have fun..."
    girl "Wait... Aaahh!"
    
    $ deviance += 1
    $ inhibition -= 1
    $ morale -= 1
    
    return


label go_office10: 
    
    scene bg go_office10 with fade
    
    "Rina from the school club has paid you a visit this morning."
    
    go_rina "Mmmmh!!!"
    pov "Aaaaaahhh!!!"
    go_rina "Gee, Principal, you're so naughty... Cumming so much in a young girl's mouth! Maybe you like my new swimsuit?"
    pov "Ahhh... Your mouth is the best, Rina-chan... So warm, and wet..."
    go_rina "*giggle* I'm glad you like it... Here, let me clean you up... Yum..."
    
    $ deviance += 1
    $ inhibition -= 1
    if renpy.random.randint(1, 3) == 1:
        $ deviance += 5
    return
    

label go_office11: 
    
    scene bg office with fade
    
    "You are working quietly in your office when someone knocks on the door."
    
    show go_hinata normal at center with fade
    
    go_hinata "Hi, [povTitle] [povLastName]!"
    
    "It's Hinata, from Class B. A very friendly student, if a bit frivolous."
    "She often comes to your office to say hi. This is a pleasant break from your hard work."
    pov "Hi Hinata-chan! How are you doing today?"

    "She seems eager to chat with you. What topic are you going to talk about?"
    
    menu:
        "Classes.": ## could be revised later to allow for random dialogue
            
            "Hinata has never been brillant in class, but you're sure she can progress if properly encouraged."
            pov "How are you doing in class lately?"
            
            if behavior < 10:
                show go_hinata thoughtful
                go_hinata "It's hard to hear anything the teacher says really... The boys always make a racket when she tries to speak."
            elif academics < 10:
                show go_hinata thoughtful
                go_hinata "I'm not really good in class... I always drift off, I can't help it."
            elif deviance == 100 and inhibition == 0 and behavior > 90:
                show go_hinata surprised
                go_hinata "The teacher made me blow him during an exam! He said that was part of the test..."
            elif deviance > 95 and inhibition < 5:
                show go_hinata thoughtful
                go_hinata "It's hard to concentrate on class when there are people fucking all around you..."
            elif deviance > 75 and inhibition < 20:
                show go_hinata surprised
                go_hinata "The biology teacher taught us about human reproduction the other day. She insisted that we see a live experiment to get a better idea..."
            elif deviance > 50 and inhibition < 50:
                show go_hinata thoughtful
                go_hinata "One day I saw the boy next to me in class masturbating while looking at my legs... Gross!"
            elif inhibition < 50:
                show go_hinata smile
                go_hinata "The English teacher didn't have any panties on the other day. She was wearing a mini-skirt, all the boys could see it."
            elif deviance > 50:
                go_hinata "Some weird stuff is going on..."
                show go_hinata surprised
                go_hinata "A girl from my class told me she gives blowjobs to older guys for money... Unbelievable!"
            elif academics > 50:
                show go_hinata smile
                go_hinata "Professor Drake is funny... He spends half the time daydreaming in class but his lectures are the best!"
            elif artistery > 25:
                show go_hinata surprised
                go_hinata "Guys from the art class said they wanted to take pictures of me naked... Is this really considered art?"
            elif academics > 25:
                go_hinata "My grades have improved lately. I really don't want to fail in the finals!"
            elif morale > 20:
                go_hinata "I get bored in class, but I'm doing my best to study harder. It's good that you've always encouraged me!"
            elif deviance > 25:
                "This girl in my class does perverted things with her pen during class... I'm sure the teacher sees her, but he doesn't say anything..."
            else:
                show go_hinata thoughtful
                go_hinata "Classes are boring..."
            
            $ academics += 1
                        
            return
                
        "Life in school.":
            
            "Hinata is very popular in school, her good nature and good looks have won her a lot of friends and admirers."
            pov "How are things in school?"
            
            if deviance == 100 and inhibition == 0:
                show go_hinata sexy
                go_hinata "The other day, boys wouldn't let us leave school until we serviced all of them..." 
                show go_hinata thoughtful
                go_hinata "It was fun, but I had to wash my hair 3 times to get rid of all the cum!"
            
            elif deviance > 95 and inhibition < 5:
                show go_hinata thoughtful
                go_hinata "I don't even use the school's bathrooms any more... There's always a couple having sex, or worse."
            
            elif deviance > 75 and inhibition < 20:
                show go_hinata surprised
                go_hinata "I walked in on a couple having sex in class! Can you believe it?"
            
            elif deviance > 50 and inhibition < 50:
                show go_hinata sexy
                go_hinata "I heard there's a special place in the woods near the racing track where girls meet boys to give them oral sex... Do you think it's true?"
                
            elif inhibition < 50:
                go_hinata "It's good that the school has a very relaxed atmosphere... People can wear anything they want..."
                show go_hinata sexy
                go_hinata "Or nothing, if that's what they want... *giggle*"
            
            elif deviance > 50:
                go_hinata "Mako says she did it with her boyfriend on the roof of the school."
                show go_hinata sexy
                go_hinata "It's a popular place to meet for couples."
            
            elif morale > 50:
                show go_hinata smile
                go_hinata "The atmosphere of the school is really great! Everyone is so nice!"
                show go_hinata sexy
                go_hinata "Especially you, [povTitle] principal! *giggle*"
            
            elif deviance > 25 and inhibition < 70:
                show go_hinata thoughtful
                go_hinata "Boys peeked on me the other day while I was naked in the baths... They even took a picture!"
            
            elif morale > 25 and deviance > 15:
                go_hinata "I like this school. I have a lot of friends there."
                show go_hinata thoughtful
                go_hinata "I just wish boys didn't make so many lewd comments at me..."
            
            elif athletics > 20:
                show go_hinata smile
                go_hinata "It's nice that we have good sports facilities! I want to cultivate my body and mind..."
                show go_hinata thoughtful
                go_hinata "People compliment me a lot more about my body, though."
            
            elif morale < 10:
                show go_hinata thoughtful
                go_hinata "This school is too serious for me... It looks like we can never take time to have fun!"
            
            else:
                go_hinata "The school is nothing special, but it's my school, so I like it!"
                
            $ morale += 1
                        
            return
        
        "Relationships.":
            
            if inhibition > 90:
                "So Hinata-chan, how is your romantic life going?"
                show go_hinata surprised
                "She is surprised by your question."
                go_hinata "I... That's..."
                show go_hinata thoughtful
                go_hinata "That's not a proper subject to talk about..."
                
                $ morale -= 1
                return
                         
            elif inhibition > 70:
                pov "So, tell me Hinata-chan... Is there any boy you like?"
                show go_hinata surprised
                go_hinata "Me??? I... Well..."
                
                if deviance > 25:
                    show go_hinata thoughtful
                    go_hinata "I used to like this boy, but... He always tries to do perverted things with me..."

                else:
                    show go_hinata normal
                    go_hinata "I don't know... I receive a lot of love letters lately..."
                
                $ inhibition -= 1
                return
                    
            else:
                pov "So, tell me Hinata-chan... Do you have a boyfriend?"
                show go_hinata surprised
                go_hinata "Me? Er... No..."
                show go_hinata thoughtful
                go_hinata "Too many guys try to take advantage of me... I'm waiting for the right person."
                
                menu:
                    "Really? How would you describe him?":
                        
                        pov "So, what's your ideal boyfriend like?"
                        
                        if deviance < 50:
                            show go_hinata smile
                            go_hinata "Well... Kind, attentionate, smart... Good looking? Rich?"
                            pov "Yep... That doesn't sound like one of our students all right."
                        else:
                            show go_hinata normal
                            "She blushes."
                            go_hinata "Well, maybe... I'd like a kind, good looking, older man... More mature, more experienced..."
                            "She gives you a strange look as she says that."
                            
                            if deviance > 90 and inhibition < 20:
                                show go_hinata sexy
                                go_hinata "I'll let him do anything to me..."
                                "She licks her lips and gives you a provocative look. The temperature in the room has just become unbearable."
                                
                        $ inhibition -= 1
                        
                        return
                            
                            
                    "What a pity... You are such a nice girl!":
                        pov "What a terrible loss for the boys in school! You are such a sweet girl, they must be unconsolable."
                        show go_hinata smile
                        go_hinata "Ahah, thank you [povTitle] [povLastName]! You are very kind."
                        
                        if deviance > 50 and inhibition < 50:
                            show go_hinata sexy
                            go_hinata "I appreciate the compliment, especially since it comes from such a handsome, sexy man..."
                            pov "(Control yourself, [povFirstName]...)"
                        
                        elif deviance > 15 and inhibition < 70:
                            show go_hinata normal
                            go_hinata "What about you Sir? Do you have a wife or girlfriend?"
                            pov "Well... not at the moment, no."
                            go_hinata "I see..."
                            
                        $ morale += 1
                        $ inhibition -= 1
                        
                        return
                    
                    "What a pity... You have such a nice body!":
                        
                        if deviance <= 15:
                            
                            "She looks shocked."
                            show go_hinata surprised
                            go_hinata "Uh, what, Sir??? Don't even say such things as a joke!!!"
                            show go_hinata thoughtful
                            "You managed to upset her. You and your big mouth..."
                            
                            $ morale -= 1
                            $ inhibition += 1
                            
                        elif deviance <= 25 or inhibition >= 70:
                            show go_hinata smile
                            "She laughs."
                            go_hinata "Ahahaha! That's funny Sir!"
                            show go_hinata surprised
                            go_hinata "You... You didn't mean anything by that did you?"
                            pov "Ahah no, of course not..."
                            
                        elif deviance <= 75 or inhibition >= 25:
                            show go_hinata smile
                            "She laughs."
                            go_hinata "Haha! Well, a compliment is a compliment... I'll accept it if it comes from you. *wink*"
                            show go_hinata sexy
                            go_hinata "Perhaps I should be more careful around you... *giggle*"
                            
                            $ inhibition -= 1
                            
                        else:
                            show go_hinata sexy
                            "She smiles flirtatiously."
                            go_hinata "So, you think so? I don't mind if you look at me that way..."
                            go_hinata "You only have to ask, and I can show you more... *giggle*"
                            "She lifts her skirt on the side, giving you a glimpse of her white ass and thighs... You can briefly see that she isn't wearing any 
                             panties."
                            go_hinata "I have to go now... See you later, [povTitle] [povLastName]..."
                            "She blows you a kiss and runs off, leaving you with a huge bulge in your pants."
                            
                            $ inhibition -= 1
                            $ deviance += 1
                            $ morale += 1
                            
                        return
        
        "Sex." if deviance > 50 and inhibition < 70:
            
            pov "So, Hinata-chan, how's your sex life?"
            show go_hinata surprised
            go_hinata "Whaaat??? What kind of question is that?"
            pov "Oh, come on... Don't act so innocent... A pretty girl like you must have a lot of admirers..."
            go_hinata "Me...? Pretty?"
            pov "Yes, of course... You are very attractive. The boys must be all over you."
            "She blushes."
            show go_hinata thoughtful
            if deviance <= 75:
                go_hinata "Well, no... It's not like that..."
            elif deviance <= 95:
                go_hinata "Well, I spend some time with boys... but..."
            else:
                go_hinata "Well, It's true I've been having sex with a lot of guys lately... but..."
            "You come closer to her."
            pov "So... You haven't found anyone who can satisfy you yet?"
            if deviance <= 75:
                go_hinata "[povTitle] [povLastName]... I'm not sure what you..."
                show go_hinata surprised
                go_hinata "Aaah!"
                "You place your hands around her waist and pull her close to you."
                go_hinata "[povTitle] [povLastName], what are you doing, aahh!"
                "You kiss her neck and bring your hands under her skirt, caressing her ass."
                                                                              
            elif deviance <= 90:
                "She laughs"
                show go_hinata smile
                go_hinata "You could say that..."
                show go_hinata sexy
                go_hinata "[povTitle] [povLastName], are you suggesting something...?"
                pov "Hell yeah!"
                "You leap over her like a hungry wolf."
            
            else:
                show go_hinata sexy
                "She gives you a flirtatious look."
                go_hinata "Well, I AM a naughty girl... But I think there is one man who can really teach me a lesson..."
                "She comes closer to you. Putting her arms around your neck, she whispers in your ear."
                go_hinata "I'm a bad girl, Principal. I need to be disciplined..." 
                go_hinata "You know what I want... Give it to me, please..."
            
            scene bg go_office11_1 with fade
            
            go_hinata "Ah, [povTitle] [povLastName], aaah!"
            "You push her down on your desk and start fondling her tits."
            "You play with her tits roughly, squeezing them through her uniform."
            "She moans as if in pain, but her sensitive body is responding. You can feel her nipples harden under her top."
            go_hinata "Mmmh, ha, ahaaa..."
            
            scene bg go_office11_2
            "Lifting up her uniform, you start pinching her erect nipples."
            pov "You never wear any bra, do you? What a slut..."
            go_hinata "Oh, [povTitle] [povLastName]..."
            "Her beautiful round tits stand to attention as you pinch and pull on her nipples."
            go_hinata "Aaah, [povTitle] [povLastName], not so hard... Aaaah!!!"
            "You place yourself between her legs. Your hard-on is pressing against her panties and you start rubbing yourself against her."
            "She moans immediately as she feels your horny dick pushing against her crotch."
            
            if deviance <= 75:
                "She looks deep into your eyes with a mix of apprehension and expectation."
                go_hinata "[povTitle] [povLastName]... I..."
                with hpunch
                "*driiiiing*"
                "The bell is ringing, classes are about to start."
                "The sudden noise makes her snap out of her dreamy state."
                go_hinata "Ah, I'm gonna be late!!! So... sorry Sir, I must go!"
                "She seems very shy all of a sudden. Pulling her top back down, she stands up and rushes to the door."
                "You let her go, feeling a bit puzzled by her sudden change of mood."
                "Just before exiting your office, she turns around and gives you a brief look. It looks as if she'd rather stay."
                "Her hesitation lasts only for a second, then she bows lightly and leaves."
                pov "I'll get her next time..."
                
                $ inhibition -= 1
                $ deviance += 1
            
            else:
                "She looks at you with dreamy eyes. She whispers with a sultry voice."
                go_hinata "[povTitle] [povLastName]... I want it..."
                "You continue fondling her tits, rubbing yourself against her pussy."
                pov "Well Hinata-chan... Tell me what you want..."
                go_hinata "I want... you know..."
                "You push yourself harder against her, grinding your cock against her clit. She moans with pleasure under your assaults."
                pov "Say it."
                go_hinata "..."
                "Ever through your clothes, you can feel how wet she is."
                pov "Say it, slut!"
                go_hinata "I want, ah... I want your hard dick, [povTitle] [povLastName]... I want it in my wet pussy..."
                go_hinata "Fuck me hard, [povTitle] [povLastName]! Please!"
                "You laugh."
                pov "Ok, ok! I get it... *smile*"
                pov "Let me fulfill your wish, then, little girl..."
                
                scene bg go_office11_3 with fade
                
                go_hinata "Aaaaaah!!!"
                "Pulling her soaked panties down, you take out your erect cock and start rubbing it between her thighs."
                go_hinata "Oh, [povTitle] [povLastName], aaaah!!!"
                "Her love juices are flowing non-stop from her pussy, oozing all over your cock."
                "She moans and grinds her hips in anticipation. Full of lust, she waits for your cock to penetrate her."
                go_hinata "Please, [povTitle] [povLastName], I beg you... Put it in, now..."
                "You feel you have kept her waiting for long enough. Slowly, you push the lenght of your shaft inside her, going all the way in."
                go_hinata "Ahahaaaaa! Oh, yes... yes!!!"
                "You start fucking her rythmically, her tight pussy squeezing your dick and lubricating it with love juices."
                go_hinata "Oooh, [povTitle] [povLastName], it's so good! Ooooh..."
                "She loves being fucked from behind. She pushes her ass against you, challenging you to go deeper and deeper inside of her."
                go_hinata "I'm a dirty girl, [povTitle] [povLastName]... Fuck me! Fuck me harder!"
                "You fuck her relentlessly, her pussy making wet, naughty noises every time you slap your body against hers."
                go_hinata "[povTitle] [povLastName], this is too good, aahhhhhh!"
                "You can feel your own climax is near. Before you go, though, you decide to give it everything you have."
                go_hinata "[povTitle] [povLastName], aahh!!! Ooooh... Yes!!!"
                "You fuck her faster and faster, slamming your cock all the way inside her with every thrust."
                pov "Do you... like this, ha... bitch?"
                go_hinata "Oooh! Yes! Oooh! Yeees!"
                "You increase your speed until you are fucking her as fast as you possibly can."
                go_hinata "My, aaah... My pussy's gonna melt... Aaaahh!!!"
                "You both reach your limit as you shove your dick deep into her cunt one last time."
                
                scene bg go_office11_4 with doubleflash
                go_hinata "[povTitle] [povLastName]... AAHAAAAAAAAAAHHHH!!!"
                pov "UUUURRRRHHHH!!!"
                
                with doubleflash
                "You come hard into her, filling her belly up with your dirty cum."
                go_hinata "Oooh, it's so warm, aaah!!!"
                "As you withdraw your dick, hot jizz starts flowing out of her pussy, dripping on her panties and legs."
                go_hinata "[povTitle] [povLastName]... I came so hard..."
                go_hinata "It was unbelievable..."
                "You hold her gently as she tries to find her breath. Kissing her ear and neck."
                "After resting with you for a few moments, Hinata suddenly realizes the time."
                go_hinata "..."
                go_hinata "AAAAH!!! My class! It's already started!!!"
                go_hinata "I'm fifteen minutes laaaaate!!!"
                "She rushes out of your office, half-naked, trying to fix her clothing as she goes."
                go_hinata "Sorry Sir!!! I... See you!!!"
                "You can hear her running down the corridor, no easy task with her panties still half down."
                pov "Silly girl..."
                
                $ inhibition -= 1
                $ deviance += 1
                if renpy.random.randint(1, 2) == 1:
                    $ deviance += 5
                $ go_SexwithHinata = 1
                
            return
            
    
label go_office12:
    
    scene bg go_office12 with fade
    
    "You have been getting a lot of attention from the female teachers lately."
    
    "Teacher1" "Ne, [povFirstName]-sama, do you have a girlfriend?"
    "Teacher2" "You never talk to us about your private life..."
    pov "Ladies..."
    "Teacher1" "Is it true you like that Marceline woman? From class C?"
    "Teacher2" "She is from Class C, but she ain't classy, I'll tell you that."
    "Teacher1" "Or perhaps you like younger girls... like those pretty cheerleaders?"
    "Teacher2" "*sexily* I could show you things those young brats have never dreamt about..."
    "Teacher1" "*sluttily* We know the way you look at us! Yes, those are real, you can touch them if you want..."
    pov "Ladies, please!"
    "It's getting harder and harder to concentrate on work these days."
    
    $ deviance += 1
    
    return


    
    
    
    
         
