##############################################################################
# Policy Menu
#
# Show policy screen and options.

screen policy_screen:
    imagemap:
        ground "images/ui/menu_bg.png"

    hbox:
        xfill True
        yfill True
        vbox:
            python:
                ui.imagebutton("images/ui/student_rules_idle.png", "images/ui/student_rules_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("policy_screen", "student_rules")])
                ui.imagebutton("images/ui/learning_materials_idle.png", "images/ui/learning_materials_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=[SetVariable("policy_screen", "learning_materials")])

        vbox:
            xfill True
            xpos 0.008
            ypos 0.008
                        
            if policy_screen == "learning_materials":
                label _("Depiction of the human body")
                if(hyper_anatomic_body > 0 ):
                    textbutton _("Hyper sexualized - Use models based on porn stars.") action SetVariable("anatomic_body", 1.3) xminimum 800
                textbutton _("Normal - Usage of anatomical correct human models.") action SetVariable("anatomic_body", 0.7) xminimum 800
                textbutton _("Non sexual - Non sexualized versions of the human body.") action SetVariable("anatomic_body", 0) xminimum 800
                null height 25

                label _("Learning materials")
                textbutton _("New - Buy new materials for each and every class.") action SetVariable("learning_materials", 1.3) xminimum 800
                textbutton _("Normal - Reuse of materials and buy new when needed.") action SetVariable("learning_materials", 1) xminimum 800
                textbutton _("Old & Cheap - Reuse materials as long as possible.") action SetVariable("learning_materials", 0.7) xminimum 800
                null height 25

                label _("Salary - Here you can adjust the salary of your teachers.")
                textbutton _("High salary - Teachers get a significant salary boost.") action [SetVariable("salary", "salary_high"), SetVariable("salary_skill_multiplier", 1.7)] xminimum 800
                textbutton _("Normal salary - Normal teacher salary used at other schools.") action [SetVariable("salary", "salary_normal"), SetVariable("salary_skill_multiplier", 1.2)] xminimum 800
                textbutton _("Low salary - Teachers get paid a bit less then normal.") action [SetVariable("salary", "salary_low"), SetVariable("salary_skill_multiplier", 0.7)] xminimum 800

            elif policy_screen == "student_rules":
                label _("Entrance requirements - The requirements to be accepted to your school.")
                textbutton _("Perfect record - Perfect behaviour and academics.") action SetVariable("entrance_req", 5) xminimum 800
                textbutton _("Advanced requirements - Need to pass a special exam.") action SetVariable("entrance_req", 4) xminimum 800
                textbutton _("Standard requirements - Need to pass a normal exam.") action SetVariable("entrance_req", 3) xminimum 800
                textbutton _("Age requirements - You only need to be old enough.") action SetVariable("entrance_req", 2) xminimum 800
                textbutton _("No requirements - Everyone is welcome. Even you.") action SetVariable("entrance_req", 1) xminimum 800
                null height 25

                label _("Dress code - What sort of clothing will be required to wear at school. ")
                if nude_uniform > 0:
                    textbutton _("Nude - No clothing allowed during class.") action SetVariable("uniform", "nude_uniform") xminimum 800
                if sexy_uniform > 0:
                    textbutton _("Sexy uniform - A uniform showing more skin. ") action SetVariable("uniform", "sexy_uniform") xminimum 800
                textbutton _("No uniform - Students are allowed to wear anything.") action SetVariable("uniform", "no_uniform") xminimum 800
                textbutton _("Normal uniform - A basic school uniform.") action SetVariable("uniform", "normal_uniform") xminimum 800
                textbutton _("Conservative uniform - A uniform showing less skin.") action SetVariable("uniform", "conservative_uniform") xminimum 800
                null height 25

                label _("PDA Rules - Determines how you will punish public displays of affection.")
                if no_detention > 0:
                    textbutton _("Nothing - Make love, not war, man.") action [SetVariable("pda_rules", "pda_none"), SetVariable("pda_rule_level", 1)] xminimum 800
                textbutton _("Detention - A little lax, but more students will show off this way.") action [SetVariable("pda_rules", "pda_detention"), SetVariable("pda_rule_level", 2)] xminimum 800
                textbutton _("Suspension - Most schools follow this rule.") action [SetVariable("pda_rules", "pda_suspension"), SetVariable("pda_rule_level", 3)] xminimum 800
                textbutton _("Expulsion - Public display are not allowed at all.") action [SetVariable("pda_rules", "pda_expulsion"), SetVariable("pda_rule_level", 4)] xminimum 800
                if bdsm_detention > 0:
                    textbutton _("BDSM Detention - Taste the whip.") action [SetVariable("pda_rules", "pda_bdsm"), SetVariable("pda_rule_level", 5)] xminimum 800
                null height 25

                label _("Behavior - Amount of violence allowed to punish students.")
                textbutton _("Everything goes - Teachers are allowed to do whatever they feel like.") action [SetVariable("behavior_rules", "behavior_no_limit"), SetVariable("behavior_rules_multiplier", 2)] xminimum 800
                textbutton _("Physical abuse - Teachers are allowed to use moderate violence.") action [SetVariable("behavior_rules", "behavior_physical"), SetVariable("behavior_rules_multiplier", 1.5)] xminimum 800
                textbutton _("Verbal abuse - Verbal and non physical abuse are allowed.") action [SetVariable("behavior_rules", "behavior_verbal"), SetVariable("behavior_rules_multiplier", 1)] xminimum 800
                textbutton _("Zero tolerance - No kind of aggression towards students are allowed.") action [SetVariable("behavior_rules", "behavior_zero"), SetVariable("behavior_rules_multiplier", 0.6)] xminimum 800

            else:
                text "Here you choose what rules your students and teachers should follow."
    vbox:
        xalign 0.992
        yalign 0.992
        $ ui.imagebutton("images/ui/return_button_idle.png", "images/ui/return_button_hover.png", insensitive_image="images/ui/menubutton_disable.png", clicked=ui.returns(0))
