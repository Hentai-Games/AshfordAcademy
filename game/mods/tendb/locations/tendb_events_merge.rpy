# Merge of tendb events for new structure in r5003

image bg tendb_bath151 = "mods/tendb/locations/bath/bath151.jpg"
image bg tendb_class151 = "mods/tendb/locations/class/class151.jpg"
image bg tendb_class152 = "mods/tendb/locations/class/class152.jpg"
image bg tendb_class153 = "mods/tendb/locations/class/class153.jpg"
image bg tendb_class154-1 = "mods/tendb/locations/class/class154-1.jpg"
image bg tendb_class154-2 = "mods/tendb/locations/class/class154-2.jpg"
image bg tendb_class154-3 = "mods/tendb/locations/class/class154-3.jpg"
image bg tendb_class154-4 = "mods/tendb/locations/class/class154-4.jpg"
image bg tendb_class154-5 = "mods/tendb/locations/class/class154-5.jpg"
image bg tendb_class154-6 = "mods/tendb/locations/class/class154-6.jpg"
image bg tendb_class155-1 = "mods/tendb/locations/class/class155-1.jpg"
image bg tendb_class155-2 = "mods/tendb/locations/class/class155-2.jpg"
image bg tendb_class156 = "mods/tendb/locations/class/class156.jpg"
image bg tendb_class157 = "mods/tendb/locations/class/class157.jpg"
image bg tendb_class158 = "mods/tendb/locations/class/class158.jpg"
image bg tendb_class159 = "mods/tendb/locations/class/class159.jpg"
image bg tendb_gym50 = "mods/tendb/locations/gym/gym50.jpg"
image bg tendb_office50-1 = "mods/tendb/locations/office/office50-1.jpg"
image bg tendb_office50-2 = "mods/tendb/locations/office/office50-2.jpg"
image bg tendb_office51 = "mods/tendb/locations/office/office51.jpg"
image bg tendb_office52 = "mods/tendb/locations/office/office52.jpg"
image bg tendb_office53-1 = "mods/tendb/locations/office/office53-1.jpg"
image bg tendb_office53-2 = "mods/tendb/locations/office/office53-2.jpg"
image bg tendb_office53-3 = "mods/tendb/locations/office/office53-3.jpg"
image bg tendb_office53-4 = "mods/tendb/locations/office/office53-4.jpg"
image bg tendb_pool151 = "mods/tendb/locations/pool/pool151.jpg"
image bg tendb_school_grounds150-1 = "mods/tendb/locations/school_grounds/school_grounds150-1.jpg"
image bg tendb_school_grounds150-2 = "mods/tendb/locations/school_grounds/school_grounds150-2.jpg"
image bg tendb_school_grounds150-3 = "mods/tendb/locations/school_grounds/school_grounds150-3.jpg"
image bg tendb_sports_field50-1 = "mods/tendb/locations/sports_field/sports_field50-1.jpg"
image bg tendb_sports_field50-2 = "mods/tendb/locations/sports_field/sports_field50-2.jpg"

#Also defined in Tina Lee script
#image bg tendb_showers = "locations/places/showers.jpg" 

init:
    $ event("tendb_bath151", "act == 'bath' and inhibition <= 50 and deviance > 35", event.choose_one('bath'), priority=160)
    $ event("tendb_class151", "act == 'class' and inhibition < 75 and deviance > 25", event.choose_one('class'), priority=170)
    $ event("tendb_class152", "act == 'class' and inhibition < 60 and deviance > 35", event.choose_one('class'), priority=170)
    $ event("tendb_class153", "act == 'class' and inhibition < 85 and deviance > 20", event.choose_one('class'), priority=170)
    $ event("tendb_class154", "act == 'class' and inhibition < 25 and deviance > 70", event.choose_one('class'), priority=170)
    $ event("tendb_class155", "act == 'class' and inhibition < 35 and deviance > 50", event.choose_one('class'), priority=170)
    $ event("tendb_class156", "act == 'class' and deviance >= 55 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=170)
    $ event("tendb_class157", "act == 'class' and deviance >= 65 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=170)
    $ event("tendb_class158", "act == 'class' and inhibition < 45 and deviance > 60", event.choose_one('class'), priority=170)
    $ event("tendb_class159", "act == 'class' and deviance >= 75 and pda_rules == 'pda_bdsm'", event.choose_one('class'), priority=170)
    $ event("tendb_gym50", "act == 'gym' and deviance > 25", event.choose_one('gym'), priority=150)
    $ event("tendb_office50", "act == 'office' and academics > 65 and inhibition < 60", event.choose_one('office'), priority=200)
    $ event("tendb_office51", "act == 'office' and behavior_rules == 'behavior_zero' and deviance > 40", event.choose_one('office'), priority=200)
    $ event("tendb_office52", "act == 'office' and deviance > 50", event.choose_one('office'), priority=200)
    $ event("tendb_office53", "act == 'office' and deviance > 65 and inhibition < 50", event.once(), event.choose_one('office'), priority=200)
    $ event("tendb_pool151", "act == 'pool' and athletics > 65 and inhibition > 50", event.choose_one('pool'), priority=180)
    $ event("tendb_school_grounds150", "act == 'school_grounds' and inhibition < 50 and deviance > 50", event.choose_one('school_grounds'), priority=160)
    $ event("tendb_sports_field50", "act == 'sports_field' and inhibition < 60", event.choose_one('sports_field'), priority=150)
  
    
label tendb_bath151:

    scene bg tendb_bath151 with fade
    "Some teachers and students get along together very well."
    $morale += 1
    $inhibition -=1
    return    
    
label tendb_class151:
    
    scene bg tendb_class151 with fade
    "There are other things that can be learned besides schoolwork."
    "Female Student" "Good! Riighht theree~ That's the spot!"
    $ academics -= 1
    $ morale += 1
    return

label tendb_class152:

    scene bg tendb_class152 with fade
    "Beautiful teamwork can spontaneously occur anywhere."
    $ academics -= 1
    $ inhibition -= 1
    $ deviance += 1
    return

label tendb_class153:
    
    scene bg tendb_class153 with fade
    "A little stimulation can help a girl stay awake in class."
    $ academics += 1
    $ behavior -= 1
    return

label tendb_class154:
    
    scene bg tendb_class154-1 with fade
    "You visit in classroom just in time to see a teacher give a special lesson."
    "Teacher" "Attention! I need your attention, please!"
    "All eyes focused on the teacher."
    "Today! We're going to be learning a special lesson on the female body!"
    "Student" "No need to shout Teacher."
    scene bg tendb_class154-2
    "Teacher" "Ah, yes. Sorry. You can see me spreading apart my pussy lips here, also known as the labia. Be sure to get a good look."
    "Drawings scribbled."
    scene bg tendb_class154-3
    "Teacher" "Ahh...and this is the nipple. This can be a very sensitive spot...like it is for me."
    "Student" "Teacher can you please smile?"
    scene bg tendb_class154-4
    "Teacher" "Of course. Thank you for reminding me. If you stimulate this enough, a girl can even lactate"
    "Scribble scribble."
    scene bg tendb_class154-5
    "Teacher" "Ahhhh....and this....is the clitoris...and extremely sensitive...mmmhmmm...so treat it well..."
    "Student" "Smile Teacher?"
    scene bg tendb_class154-6
    "Teacher" "Mhmm...anything for my students."
    
    $ academics +=1
    $ morale += 1
    $ behavior -= 1
    return

label tendb_class155:
    
    scene bg tendb_class155-1 with fade
    "You pass by a classroom and see a teacher telling another teacher how to relax in front of students."
    "Teacher 1" "Just give into it. Go with the flow. Let your body do what it needs to do."
    "Teacher 2" "Mhhmmm..I'm trying..."
    "Teacher 1" "Good. That's right, just listen to your body."
    "Teacher 2" "I'm listening!!!"
    scene bg tendb_class155-2
    "Teacher 1" "Great job! I think you're ready to go back to class."
    "Teacher 2" "Thank you for your guidance.."

    $ academics +=1
    $ behavior -=1
    return

label tendb_class156:
    
    scene bg tendb_class156 with fade
    "You're not sure what she did but she must have been a bad student."
    $ deviance += 2
    $ behavior += 1
    $ morale -= 1
    return

label tendb_class157:

    scene bg tendb_class157 with fade
    "For breaking school rules, she's being punished by being the female model in a health class."
    $ academics += 1
    $ behavior += 2
    $ inhibition -=1
    return

label tendb_class158:

    scene bg tendb_class158 with fade
    "Some of the female students volunteered themselves for the sake of art."
    "They look like they enjoy the attention."
    $ artistery += 1
    $ inhibition -= 2
    return
    
label tendb_class159:
    
    scene bg tendb_class159 with fade
    "Some of the girls join in to punish those who break school policy."
    $ morale += 1
    $ behavior += 2
    $ deviance +=1
    return  

label tendb_gym50:
    scene bg tendb_gym50 with fade
    "You find a girl in deep sleep and tied up in the storage shed."
    "Definitely one of the stranger pranks you've seen."
    $ behavior -= 1
    return

label tendb_office50:
    scene bg tendb_office50-1 with fade
    "Some parents come to your office and thank you personally for bringing Ashford Academy to a new level of academic prowress."
    "Parent" "Without you, my child wouldn't be having such an excellent education."
    "Parent" "Thank you so much."
    scene bg tendb_office50-2
    pov "You're welcome. If other like-minded parents like you would like to say thanks, please show them here."
    "Parent" "Of course I will."
    
    $inhibition -= 1
    $deviance +=1
    return

label tendb_office51:
    scene bg tendb_office51 with fade
    "Because teachers can't punish students, they instead decide to call the students' parents and punish them instead."
    "Parents of frequent offenders seem to like it."
    
    $inhibition -= 1
    $deviance += 1
    return

label tendb_office52:
    scene bg tendb_office52 with fade
    "You're not sure why she's in your office and neither does she."
    $ behavior -=1
    $ inhibition +=1
    return

label tendb_office53:
    scene bg tendb_office with fade
    pov "Darn reports. Why's there so many?"
    "Your phone receives a message and you take a look."
    scene bg tendb_office53-1 with fade
    pov "Damn! Who's this?"
    "You have no idea who the sender is."
    scene bg tendb_office53-2
    "Next."
    scene bg tendb_office53-3
    "Next."
    scene bg tendb_office53-4
    "These might've been sent to the wrong number, but you don't mind."
    return

label tendb_pool151:
    scene bg tendb_pool151 with fade
    "Some of the swimmers are trying out new training regimes to become more competitive."
    $ academics -= 1
    $ inhibition +=1
    $ athletics += 1
    return    
    
label tendb_school_grounds150:
    scene bg tendb_school_grounds with fade
    "You're walking through the courtyard when you stumble upon a competition."
    scene bg tendb_school_grounds150-1 with fade
    "Female Teacher" "You're a hundred years too young to compete against me."
    "Female Student" "You old hag. Your pussy is too loose to get anyone excited."
    "Male Teacher" "Show them the power of being a teacher!"
    "Male Student" "Come on! We can't lose to them!"
    scene bg tendb_school_grounds150-2
    "Female Teacher" "Hmm...you're pretty good."
    "Female Student" "Heh..who do you think you're talking to."
    scene bg tendb_school_grounds150-3
    "Female Teacher" "Yess!"
    "Female Student" "Ahhh!"
    "Male Student" "Looks like it was a tie."
    "Male Teacher" "What a shame I thought this would be the one. Tomorrow again?"
    "Male Student" "Sure. We might need something bigger than pens."
    $ morale +=1
    $ deviance +=1
    $ inhibition +=1
    return
    
label tendb_sports_field50:

    scene bg tendb_sports_field50-1 with fade
    "A cheer leader is doing squats in preparation for the local competition."
    "Male Cheer Leader" "Yosh! Let me help out."
    scene bg tendb_sports_field50-2 with vpunch
    "Female Cheer Leader" "Ah! Yes, thank you!"
    $ athletics +=1
    $ inhibition -=1
    return
    