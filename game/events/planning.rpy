image sports_tourney1 = "images/special_events/sports_tourney1.jpg"         # Win
image sports_tourney2 = "images/special_events/sports_tourney2.jpg"         # Loss
image sports_tourney3 = "images/special_events/sports_tourney3.jpg"         # Win
image sports_tourney4 = "images/special_events/sports_tourney4.jpg"         # Great victory
image sports_tourney5 = "images/special_events/sports_tourney5.jpg"         # Bad loss

image fitness_training1 = "images/special_events/fitness_training1.jpg"
#image fitness_training2 = "images/special_events/fitness_training2.jpg"
#image fitness_training3 = "images/special_events/fitness_training3.jpg"
#image fitness_training4 = "images/special_events/fitness_training4.jpg"
#image fitness_training5 = "images/special_events/fitness_training5.jpg"

image standard_test1 = "images/special_events/standard_test1.jpg"

image art_exhibit1 = "images/special_events/art_exhibit1.jpg"

image school_trip1 = "images/special_events/school_trip1.jpg"
image school_trip2 = "images/special_events/school_trip2.jpg"
image school_trip3 = "images/special_events/school_trip3.jpg"
image school_trip4 = "images/special_events/school_trip4.jpg"
image school_trip5 = "images/special_events/school_trip5.jpg"
image school_trip6 = "images/special_events/school_trip6.jpg"

# Raise money options
image raise_money clean_the_streets = "images/special_events/raise_money_clean_the_streets.jpg"
image raise_money sell_their_services= "mods/litemod_events/raise_money_sell_their_services.jpg"
image raise_money pose_nude= "mods/litemod_events/raise_money_pose_nude.jpg"
image raise_money car_wash= "mods/litemod_events/raise_money_car_wash.jpg"
image bake_sale1= "mods/litemod_events/raise_money_bake_sale.jpg"
image bake_sale2= "mods/litemod_events/raise_money_bake_sale_2.jpeg"
image bake_sale3= "mods/litemod_events/raise_money_bake_sale_3.jpg"
image sexy_bake_sale1= "mods/litemod_events/raise_money_sexy_bake_sale.jpeg"
image sexy_bake_sale2= "mods/litemod_events/raise_money_sexy_bake_sale2.jpg"
init python:
    def WeightedPick(d):
        r = random.uniform(0, sum(d.itervalues()))
        s = 0.0
        for pick, value in d.iteritems():
            s += value
            if r < s: return pick
        return pick

    # FUNCTION OF THE MONTH - Why is this here?
    def generateList():
        if 't' in globals():
            t += 1
        else:
            t = 1

define weekly_planning_options = {
    "Make them behave.": {
        "requirement": "1 == 1",
        "stat": "behavior",
    },
    "We should create the next generation of great minds!": {
        "requirement": "1 == 1",
        "stat": "academics"
    },
    "Let's create the art and culture of tomorrow!": {
        "requirement": "1 == 1",
        "stat": "artistery"
    },
    "Our students shall become the next Olympic champions!": {
        "requirement": "1 == 1",
        "stat": "athletics"
    },
    "We should encourage them to... Explore their bodies.": {
        "requirement": "deviance > 5",
        "stat": "deviance"
    },
}

# eval(raise_money_options[0]['requirement'])


define raise_money_options = {
"prostitution": {"requirement": "deviance > 75",
    "results":[
        {"chance":10,    "text": "They got raped.",          "image":                "sexy_sluts.jpg"},
        {"chance":10,    "text": "They raped and robbed.",   "image":                "sexy_sluts.jpg"},
        {"chance":10,    "text": "They got robbed.",         "image":                "sexy_sluts.jpg"}]}}


init python:

    event("weekly_planning", "act == 'new_day' and planning_day >= 7 and persistent.mod_disable_weekly_planning == False", event.solo(), priority=-10)
    event("monthly_planning", "act == 'new_day' and day == 1 and persistent.mod_disable_monthly_planning == False", event.only(), priority=-20)

    first_sexual_weekly = False
    first_monthly_goal = False

    behavior_focus = 0
    academics_focus = 0
    artistry_focus = 0
    artistery_focus = 0
    athletics_focus = 0
    deviance_focus = 0

    weekly_planning = []

    def calculate_weekly_planning(stat):
        globals()[stat] += weekly_planning_focus + eval(stat+'_focus')
        globals()[stat+'_focus'] += weekly_planning_focus_bonus
        return

    monthly_goal = ""
    monthly_goal_type = ""
    monthly_goal_value = ""

    def monthly_goal_check(monthly_goal_type, monthly_goal_value):
        if monthly_goal_type == "building":
            return globals()[eval('goal_building')] >= monthly_goal_value

        elif monthly_goal_type == "stat":
            return globals()[eval('monthly_goal')] >= monthly_goal_value

        elif monthly_goal_type == "skip":
            return True

        else:
            return True

    def monthly_goal_menu(buildings):
        skip_stat_goal = False
        skip_building_goal = False
        goal_list_buildings = []
        for building in buildings:
            building_level = eval("building_"+building['name'])
            building_cost = building['cost'][building_level]
            if building_cost > 0:
                goal_list_buildings.append(building['name'])

        if not goal_list_buildings:
            skip_building_goal = True

        if goal_list_buildings:
            globals()['goal_building'] = "building_"+renpy.random.choice(goal_list_buildings)
            globals()['goal_building_name'] = goal_building.replace("_", " ")

        # Stats

        goal_list_stats = []
        normal_stats = ['Morale', 'Behavior', 'Academics', 'Artistery', 'Athletics']
        extra_stats = ['Inhibition', 'Deviance', 'Money']
        extras = ['reputation']
        for stat in normal_stats:
            stat = stat.lower()
            stat_num = eval(stat)
            if stat_num < 90:
                goal_list_stats.append(stat)


        if goal_list_stats:
            globals()['goal_stat'] = renpy.random.choice(goal_list_stats)
            globals()['goal_stat_num'] = globals()[eval('goal_stat')]
        elif not goal_list_stats and  globals()['reputation'] < 80:
            goal_list_stats.append ("reputation")
        else:
            globals()['goal_stat'] = "skip"
            skip_stat_goal = True

        # NOTE: Will be removed and replaced with "policy combinations", but need a system to keep track of daily policies first.
        if not skip_stat_goal:
            globals()['goal_stat2'] = renpy.random.choice(goal_list_stats)

        if not skip_building_goal and not skip_stat_goal:
            goal = renpy.display_menu([
                (goal_building_name.capitalize(), "goal_building"),
                (goal_stat.capitalize(), "goal_stat"),
                (goal_stat2.capitalize(), "goal_stat2")
                ])
        elif skip_building_goal and not skip_stat_goal:
            goal = renpy.display_menu([
                (goal_stat.capitalize(), "goal_stat"),
                (goal_stat2.capitalize(), "goal_stat2")
                ])
        elif not skip_building_goal and skip_stat_goal:
            goal = renpy.display_menu([
                (goal_building_name.capitalize(), "goal_building")])
        else:
            return "skip"


        if goal == "goal_building":
            globals()['monthly_goal'] = goal_building
            globals()['monthly_goal_value'] = building_level + 1
            globals()['monthly_goal_difficulty'] = 2
            return "building"

        elif goal == "goal_stat":
            globals()['monthly_goal'] = goal_stat

            globals()['goal_difficulty3'] = min(int(eval(goal_stat) + 20), 100)
            globals()['goal_difficulty2'] = min(int(eval(goal_stat) + 15), 100)
            globals()['goal_difficulty1'] = min(int(eval(goal_stat) + 10), 100)

            globals()['monthly_goal_value'] = renpy.display_menu([
                ("[goal_stat]: [goal_difficulty3]" , goal_difficulty3),
                ("[goal_stat]: [goal_difficulty2]" , goal_difficulty2),
                ("[goal_stat]: [goal_difficulty1]" , goal_difficulty1)
                ])
            return "stat"

        elif goal == "goal_stat2":
            globals()['monthly_goal'] = goal_stat2

            globals()['goal_difficulty3'] = min(int(eval(goal_stat2) + 20), 100)
            globals()['goal_difficulty2'] = min(int(eval(goal_stat2) + 15), 100)
            globals()['goal_difficulty1'] = min(int(eval(goal_stat2) + 10), 100)

            globals()['monthly_goal_value'] = renpy.display_menu([
                ("[goal_stat2]: [goal_difficulty3]" , goal_difficulty3),
                ("[goal_stat2]: [goal_difficulty2]" , goal_difficulty2),
                ("[goal_stat2]: [goal_difficulty1]" , goal_difficulty1)
                ])
            return "stat"

        else:
            "Error: No goal selected."
        return

# Weekly planning - Part 1
label weekly_planning:
    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] - Weekly planning"
    else:
        centered "[month_now] %(day)d: [today] - Weekly planning"
    scene office with fade
    if extroduce_jennifer_adriano == True and susan_returns == False:
        show teacher_susan sad at center
        pov "I'm glad you stayed around. I really have no idea what I would have done if you hadn't."
        teacher_susan "I - I don't know what to say. That poor girl..."
        pov "I know, feels surreal."
        teacher_susan "Well, I'll be staying for as long as you need me."
        pov "That's good to know, thank you."
        teacher_susan "..."
        pov "Well, as the song says, the show must go on. We must focus on the work at hand."
        teacher_susan "I guess so."
        pov "Thank you Susan."
        teacher_susan "Well Ashford, here we go again."
        $ susan_returns = True
    else:
        show teacher_susan normal at center
        teacher_susan "Today we need to plan what to focus on for the next week. Remember, every week you can change your plan."
    python:
        weekly_planning[:] = []
        for option in weekly_planning_options:
            if eval(weekly_planning_options[option]['requirement']):
                weekly_planning.append( (option, weekly_planning_options[option]) )

        weekly_plan = renpy.display_menu(weekly_planning)
        calculate_weekly_planning(weekly_plan['stat'])

    if weekly_plan['stat'] == 'deviance' and first_sexual_weekly == False and inhibition > 50:
        $ first_sexual_weekly = True
        teacher_susan "Sorry?"
        show teacher_susan surprised
        teacher_susan "Did you say... Explore their bodies?"
        menu:
            "Indeed, they need to be more comfortable with their bodies.":
                teacher_susan "I... see..."
                teacher_susan "But [povTitle] [povLastName] do you really think this is appropriate?"
                pov "You see Susan there is only one way for students to learn about this and since we are responsible for their future we have to do this."
                teacher_susan "I understand [povTitle] [povLastName]."

            "It's important for psychosexual development.":
                teacher_susan "I'm not sure I follow [povTitle] [povLastName]."
                pov "Don't you know your psychology?"
                show teacher_susan sad
                teacher_susan "Well it's not my field, Jack Drake usually covers that part."
                pov "The point is that humans are born polymorphously perverse and if you deny the sexual development, such as getting to know your own body, your mental health will suffer."
                show teacher_susan closed_eyes
                teacher_susan "I'm not really sure about this [povTitle] [povLastName], but its up to you."
                pov "It is and this is how we will do it."

            "Hell yeah! Why do you think I work here?" if new_game_plus == True:
                show teacher_susan angry
                teacher_susan "..."
                teacher_susan "You are a very, very disturbing person."
                pov "Susan?"
                teacher_susan "[povTitle] [povLastName]?"
                pov "Maybe we should explore your body as well?"
                teacher_susan "..."

    show teacher_susan normal at center
    if first_week == False:
        teacher_susan "Very well, I will inform the rest of the teachers."
    else:
        teacher_susan "Well [povTitle] [povLastName], I just talked to the board. They said that the Agency sends their best wishes, and they wanted me to tell you that the new secretary will arrive on monday morning."
        pov "The new secretary?"
        teacher_susan "Oh, it must have slipped my mind. Since I was assigned by the old administration, the board thought it would be better for you to mold your own team."
        menu:
            "What about you?":
                pov "Sounds a bit unfair, don't you think?"
                teacher_susan "Oh, don't worry about me, I'll have enough to do as it is. Sweet of you to care though."

            "Sounds fair.":
                pov "If that's what they want, I guess I'll move along accordingly."
                teacher_susan "I really think it's for the best. With all the recent events still fresh in mind, the board wants to make a clean slate."

            "But- but, I thought I was gonna score!" if new_game_plus == True:
                teacher_susan "..."
                pov "Ahaha, sometimes I just want to kill myself!"
                teacher_susan "If only..."


    # Weekly planning - Part 2
    scene office with fade
    $ renpy.show(lia_outfit+"_lia smile")
    if first_week:
        lia "Hello [povTitle] [povLastName]. My name is Lia Foster but please call me Lia.\nI'm the school nurse and I keep track of student health."
        $ renpy.show(lia_outfit+"_lia blink")
        menu:
            "Nice meeting you Lia.":
                lia "Same to you [povTitle] [povLastName]."

            "Nurse, I suddenly feel a bit feverish..":
                $ renpy.show(lia_outfit+"_lia happy")
                lia "*giggle* I get that a lot [povTitle] [povLastName]."
                pov "I fully understand why."
        lia "Anyhow, this week only one student have reported in sick."
        pov "Thank you nurse, I look forward meeting you again."
        lia "*giggle* "
    else:
        $ called_in_sick = renpy.random.randint(0, int((population - behavior)/20))
        $ renpy.show(lia_outfit+"_lia smile")
        if called_in_sick > 1:
            if lia_points < -5:
                lia "Hello [povBdsmTitle].\nYour lowly dirty whore just want to inform you that [called_in_sick] students have called in sick this week."
            elif lia_points < 0:
                lia "Hello [povBdsmTitle].\nThis week [called_in_sick] students have called in sick."
            elif lia_points < 5:
                lia "Hello principal.\nThis week [called_in_sick] students have called in sick."
            elif lia_points < 10 and lia_points > 5:
                lia "Hello [povTitle] [povFirstName].\nThis week [called_in_sick] students have called in sick."
            else:
                lia "Hello [povFirstName].\nThis week [called_in_sick] students have called in sick."
            pov "Thank you Lia. Keep up the good work."
        else:
            if lia_points < -5:
                lia "Hello [povBdsmTitle].\nThis lowly dirty whore just want to inform you that no students have called in sick this week."
            elif lia_points < 0:
                lia "Hello [povBdsmTitle].\nNo students have called in sick this week."
            elif lia_points < 5:
                lia "Hello principal.\nNo students have called in sick this week."
            elif lia_points < 15 and lia_points > 5:
                lia "Hello [povTitle] [povFirstName].\nNo students have called in sick this week."
            else:
                lia "Hello [povFirstName].\nNo students have called in sick this week."
                pov "Does that mean I you have some free time with me?"
                $ renpy.show(lia_outfit+"_lia smile_blush")
                lia "*giggle* Stop it [povFirstName], always flirty like that..."

            pov "Great work Lia. Keep up the good work."
        if lia_points < 0:
            lia  "Yes [povBdsmTitle]."
        else:
            lia  "My pleasure [povTitle] [povLastName]."


    # Weekly planning - Part 3
    scene office with fade
    if first_week:
        show teacher_susan normal at center
        pov "Thank you for getting me up to speed with school administration and all. It sure is a long road ahead, but at least now I know a little about which direction to take."
        teacher_susan "Glad to be of assistance. Hope your new secretary settles in smoothly."
        pov "I'm sure she will."
        teacher_susan "Well, goodbye [povTitle] [povLastName]. And good luck to you."
        pov "Thank you."
        $ first_week = False
    else:
        info "You think to yourself..."
        python:
            if min(academics, artistery, athletics) < max(20 + month + year, 100):
                pov("I think we should focus a bit more on basic education.")
            elif behavior < max(20 + month + year, 100):
                pov("It would be good if we could get the students to behave better.")
            elif morale < max(20 + month + year, 100):
                pov("I wonder what we could do to make the students happier?")
            elif inhibition > 85 - month:
                pov("I think it would be good for all of us if the students would be a bit more relaxed.")
            elif deviance > inhibition:
                pov("This school is becoming quite a interesting place to work at..")
            else:
                pov("A job well done.")
    $ planning_day = 0
    $ building_bonus()
    $ policy_bonus()
    call events_skip_period from _call_events_skip_period
    return


# Monthly planning - Part 1
label monthly_planning:

    scene black with fade
    if(year > 1):
        centered "Year: %(year)d [month_now] %(day)d: [today] - Monthly planning"
    else:
        centered "[month_now] %(day)d: [today] - Monthly planning"
    $ pay_day(population,reputation)

    scene office with fade
    show teacher_susan normal at center
    teacher_susan "The first of every month we organize something special for the students. What would you like us to do?"
    menu:
        "Science fair":
            teacher_susan "I will organize this [povLastName]."
            $ academics += monthy_event_bonus

        "Standard tests" if academics > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < academics:
                    renpy.scene()
                    standard_test_win = renpy.random.choice(["standard_test1"])
                    renpy.show(""+standard_test_win)
                    teacher_susan("Our score was so high that Ashford Academy is rated one of the best in the nation.")
                    academics += 1
                    reputation += 1

                elif renpy.random.randint(1, 101) > academics:
                    renpy.scene()
                    renpy.show("standard_test1")
                    teacher_susan("Our students got some of the worst grades in the country.")
                    academics += 1
                    reputation -= 1

                else:
                    renpy.scene()
                    renpy.show("standard_test1")
                    teacher_susan("School results where in the midrange with most other schools.")
                    academics += 1

        "Fitness training":
            scene fitness_training1 with fade
            teacher_susan "We made great progress with the Ashford Volleyball Team."
            $ athletics += monthy_event_bonus

        "Sports Tourney" if athletics > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < athletics:
                    renpy.scene()
                    sports_tourney_win = renpy.random.choice(["sports_tourney1", "sports_tourney3", "sports_tourney4"])
                    renpy.show(""+sports_tourney_win)
                    teacher_susan("The Ashford Volleyball Team did great and won every match including the finals!")
                    athletics += 1
                    reputation += 1

                elif renpy.random.randint(1, 101) > athletics:
                    renpy.scene()
                    renpy.show("sports_tourney5")
                    teacher_susan("Our team was utterly destroyed and had nothing against the other teams.")
                    athletics += 1
                    reputation -= 1

                else:
                    renpy.scene()
                    renpy.show("sports_tourney2")
                    teacher_susan("Our Volleyball Team had a good start but lost against some of the better national teams.")
                    athletics += 1

        "Visit museum":
            teacher_susan "I will organize this [povLastName]."

            $ artistery += monthy_event_bonus

        "Art Exhibit" if artistery > 45:
            python:
                renpy.transition(fade, None, False)
                if renpy.random.randint(1, 101) < artistery:
                    renpy.scene()
                    renpy.show("art_exhibit1")
                    teacher_susan("Our exhibit got a lot of attention and some students even sold some of their art!")
                    artistery += 1
                    reputation += 1

                elif renpy.random.randint(1, 101) > artistery:
                    renpy.scene()
                    renpy.show("art_exhibit1")
                    teacher_susan("We didn't get much attention and the few who came thought it was a joke.")
                    artistery += 1
                    reputation -= 1

                else:
                    renpy.scene()
                    renpy.show("art_exhibit1")
                    teacher_susan("We got some attention although mostly from parents and family.")
                    artistery += 1

        "Raise money":
            teacher_susan "This is what we can do to raise money."
            menu:
                "Clean the streets":
                    python:
                        renpy.scene()
                        renpy.show("raise_money clean_the_streets")
                        raise_money = int(renpy.random.randint(1, 2) * population )
                        cash += raise_money
                        morale -= 2
                        teacher_susan("Our students raised [raise_money]$ but didn't enjoy the task.")
                "Pose Nude" if deviance >= 25 and inhibition <= 70 and anatomic_body == 1.3 and artistery >= 50:
                    python:
                        renpy.scene()
                        renpy.show("raise_money pose_nude")
                        raise_money6 = int(renpy.random.randint(3, 4) * artistery )
                        cash += raise_money6
                        inhibition -= 2
                        deviance += 2
                        artistery += 3
                        teacher_susan("Our students raised [raise_money6]$ by posing tastefully nude.")

                "Sell their services" if deviance >= 50 and inhibition <= 50 and anatomic_body == 1.3:
                    python:
                        renpy.scene()
                        renpy.show("raise_money sell_their_services")
                        raise_money2 = int(renpy.random.randint(3, 4) * population )
                        cash += raise_money2
                        inhibition -= 2
                        deviance += 2
                        teacher_susan("Our students raised [raise_money2]$ using the... unique... 'talents' they've learned in school.")

                "Car wash" if morale >=30 and inhibition <80 and uniform == 'sexy_uniform':
                    python:
                        renpy.scene()
                        renpy.show("raise_money car_wash")
                        raise_money3 = int(renpy.random.randint(1, 2) * population )
                        cash += raise_money3
                        morale += 2
                        reputation += 1
                        teacher_susan("Our students raised [raise_money3]$ cleaning cars. The students' antics earned them a bit of a reputation, but both the students and car owners enjoyed themselves.")

                "Bake sale" if reputation > 15 and building_cafeteria > 0:
                    if deviance > 50 and uniform == 'nude_uniform':
                        python:
                            renpy.transition(fade, None, False)
                            renpy.scene()
                            sexy_bake_sale = renpy.random.choice(["sexy_bake_sale1", "sexy_bake_sale2"])

                            raise_money5 = int(renpy.random.randint(3, 4) * deviance + reputation )
                            renpy.show(sexy_bake_sale)
                            cash += raise_money5
                            deviance += 5
                            reputation += 1
                            teacher_susan("The students put on a bake sale, raising [raise_money5]$. More than cakes and bread were on offer, much to the delight of the customers.")
                    else:
                        python:
                            renpy.transition(fade, None, False)

                            renpy.scene()
                            bake_sale = renpy.random.choice(["bake_sale1", "bake_sale2", "bake_sale3"])

                            raise_money4 = int(renpy.random.randint(3, 4) * reputation )

                            raise_population = int(reputation / 4 )
                            renpy.show(bake_sale)
                            cash += raise_money4
                            population += raise_population

                            reputation += 1
                            teacher_susan("The students put on a bake sale, raising [raise_money4]$. Some customers were so impressed they've decided to enrol at Ashford.")
                "Cancel":
                    jump monthly_planning

        "School trip" if cash >= population:
            teacher_susan "This is usually a good boost to morale and will cost [population] $.\nIs this ok?"
            menu:
                "Yes":
                    python:
                        cash -= population
                        renpy.transition(fade, None, False)
                        if renpy.random.randint(1, 3) == 1:
                            renpy.scene()
                            school_trip = renpy.random.choice(["school_trip1", "school_trip2", "school_trip3", "school_trip4", "school_trip5"])
                            renpy.show(""+school_trip)
                            teacher_susan("Everyone had a great time with lots of fun.")
                            morale += 2
                            reputation += 1

                        elif renpy.random.randint(1, 5) == 1:
                            renpy.scene()
                            renpy.show("school_trip6")
                            teacher_susan("The school trip went ok, not everyone enjoyed it.")
                            morale += 1
                            reputation -= 1

                        else:
                            renpy.scene()
                            renpy.show("school_trip1")

                            teacher_susan("They had a good time.")
                            morale += 1

                "No":
                    jump monthly_planning

    # Monthly planning - Part 2
    scene office with fade
    $ tmp = renpy.random.choice([
        "And this months paperwork is done.",
        "Always additional work needed to be done...",
        "...and sign there.\nAh, all paperwork done for today.",
        "A job well done."])
    pov "[tmp]"

    # Monthly planning - Part 3 - Set up a goal for the next month.
    scene office with fade
    show teacher_susan normal at center
    if first_monthly_goal == False:
        susan_marina "[povTitle] [povLastName] every month we receive feedback from students, teachers and parents organizations. We use this feedback to set up a list of goals for our academy to strive for."
        susan_marina "I try to order all the feedback and create a list where we choose one goal to focus on every month. Failing to achieve the set goal will result in negative publicity and hurt the schools reputation."
        susan_marina "Please also keep in mind that you can influence how high we set each and every goal."
        $ first_monthly_goal = True
    else:
        if monthly_goal_check(monthly_goal_type, monthly_goal_value):
            show teacher_susan happy
            if globals()['monthly_goal_type'] != "skip":
                susan_marina "Good work with last months goal I am sure this will boost Ashfords reputation."
                $ reputation += 3
            else:
                susan_marina "Since we had no goal this month, I have nothing to report."
        else:
            show teacher_susan sad
            susan_marina "Your failure resulted in negative publicity and hurt the schools reputation."
            $ reputation -= 5

    show teacher_susan normal
    susan_marina "So [povTitle] [povLastName], what goal will we have for this month?"
    $ monthly_goal_type = monthly_goal_menu(buildings)

    if monthly_goal_type == "building":
        if monthly_goal_value == 1:
            susan_marina "Our goal for the next month is to build a [goal_building_name]."
        else:
            susan_marina "Our goal for the next month is to upgrade our [goal_building_name] to level [monthly_goal_value]."

    elif monthly_goal_type == "stat":
        susan_marina "Our goal for the next month is for [monthly_goal] to reach [monthly_goal_value]."

    elif monthly_goal_type == "skip":
        susan_marina "Congratulations, you have achieved every monthly goal available."

    else:
        susan_marina "You obviously have no goal in life. So sad..."

    call events_skip_period from _call_events_skip_period_1
    return

