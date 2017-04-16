# Used in Policy screen
define policy_screen = ''

define policies = [
{"policy": "learning_materials",        "lable": "Depiction of the human body",     "options":
    {"text":"Hyper sexualized - Use models based on porn stars.",       "variable":"anatomic_body",     "variable_modifier":1.3, "requirement":"hyper_anatomic_body",   "":""}
},
{"name": "classrooms",      "requirement": "population",                                                "requirement_value": "0",       "image": "buildings/classrooms.jpg",    "description": "Quality and state of classrooms, and the value of the educational materials available to teachers. \n\nIncreasing this will randomly add to your academic stats every month. \n\nThe next upgrade will add a tiny amount to all of your {b}academics{/b} each week."},
{"name": "cafeteria",       "requirement": "persistent.we_dont_need_no_education_achievement_trigger",  "requirement_value": "True",    "image": "buildings/classrooms.jpg",    "description": "Build a cafeteria to allow students to buy some snacks. \n\nBuilding this will allow you to visit the cafeteria and will give you some extra money each month."}
]

# Defines the available policy screens
define policy_screens = [
{"name": "learning_materials"},
{"name": "student_rules"}
]

# Defines the menu labels in the available policy screens
define policy_labels = [
{"name": "body_models","screen":"learning_materials","text":"Depiction of the human body"},
{"name": "materials","screen":"learning_materials","text":"Learning materials"},
{"name": "salaries","screen":"learning_materials","text":"Salary - Here you can adjust the salary of your teachers."},
{"name": "entrance_req","screen":"student_rules","text":"Entrance requirements - The requirements to be accepted to your school."},
{"name": "dresscode","screen":"student_rules","text":"Dress code - What sort of clothing will be required to wear at school. "},
{"name": "pda_rules","screen":"student_rules","text":"PDA Rules - Determines how you will punish public displays of affection."},
{"name": "behavior","screen":"student_rules","text":"Behavior - Amount of violence allowed to punish students."}
]

# Defines the available policy choices for labels
define policy_choices = [
{"label":"body_models","text":"Hyper sexualized - Use models based on porn stars.","requirement":"hyper_anatomic_body > 0","action":"SetVariable('anatomic_body', 1.3)"},
{"label":"body_models","text":"Normal - Usage of anatomical correct human models.","requirement":"1 == 1","action":"SetVariable('anatomic_body', 0.7)"},
{"label":"body_models","text":"Non sexual - Non sexualized versions of the human body.","requirement":"1 == 1","action":"SetVariable('anatomic_body', 0)"},
{"label":"materials","text":"New - Buy new materials for each and every class.","requirement":"1 == 1","action":"SetVariable('learning_materials', 1.3)"},
{"label":"materials","text":"Normal - Reuse of materials and buy new when needed.","requirement":"1 == 1","action":"SetVariable('learning_materials', 1)"},
{"label":"materials","text":"Old & Cheap - Reuse materials as long as possible.","requirement":"1 == 1","action":"SetVariable('learning_materials', 0.7)"},
{"label":"salaries","text":"High salary - Teachers get a significant salary boost.","requirement":"1 == 1","action":"[SetVariable('salary', 'salary_high'), SetVariable('salary_skill_multiplier', 1.7)]"},
{"label":"salaries","text":"Normal salary - Normal teacher salary used at other schools.","requirement":"1 == 1","action":"[SetVariable('salary', 'salary_normal'), SetVariable('salary_skill_multiplier', 1.2)]"},
{"label":"salaries","text":"Low salary - Teachers get paid less then normal.","requirement":"1 == 1","action":"[SetVariable('salary', 'salary_low'), SetVariable('salary_skill_multiplier', 0.7)]"},
{"label":"entrance_req","text":"Perfect record - Perfect behaviour and academics.","requirement":"1 == 1","action":"SetVariable('entrance_req', 5)"},
{"label":"entrance_req","text":"Advanced requirements - Need to pass a special exam.","requirement":"1 == 1","action":"SetVariable('entrance_req', 4)"},
{"label":"entrance_req","text":"Standard requirements - Need to pass a normal exam.","requirement":"1 == 1","action":"SetVariable('entrance_req', 3)"},
{"label":"entrance_req","text":"Age requirements - You only need to be old enough.","requirement":"1 == 1","action":"SetVariable('entrance_req', 2)"},
{"label":"entrance_req","text":"No requirements - Everyone is welcome. Even you.","requirement":"1 == 1","action":"SetVariable('entrance_req', 1)"},
{"label":"dresscode","text":"Nude - No clothing allowed during class.","requirement":"nude_uniform > 0","action":"SetVariable('uniform', 'nude_uniform')"},
{"label":"dresscode","text":"Sexy uniform - A uniform showing more skin. ","requirement":"sexy_uniform > 0","action":"SetVariable('uniform', 'sexy_uniform')"},
{"label":"dresscode","text":"No uniform - Students are allowed to wear anything.","requirement":"1 == 1","action":"SetVariable('uniform', 'no_uniform')"},
{"label":"dresscode","text":"Normal uniform - A basic school uniform.","requirement":"1 == 1","action":"SetVariable('uniform', 'normal_uniform')"},
{"label":"dresscode","text":"Conservative uniform - A uniform showing less skin.","requirement":"1 == 1","action":"SetVariable('uniform', 'conservative_uniform')"},
{"label":"pda_rules","text":"Nothing - Make love, not war, man.","requirement":"no_detention > 0","action":"[SetVariable('pda_rules', 'pda_none'), SetVariable('pda_rule_level', 1)]"},
{"label":"pda_rules","text":"Detention - A little lax, but more students will show off this way.","requirement":"1 == 1","action":"[SetVariable('pda_rules', 'pda_detention'), SetVariable('pda_rule_level', 2)]"},
{"label":"pda_rules","text":"Suspension - Most schools follow this rule.","requirement":"1 == 1","action":"[SetVariable('pda_rules', 'pda_suspension'), SetVariable('pda_rule_level', 3)]"},
{"label":"pda_rules","text":"Expulsion - Public display are not allowed at all.","requirement":"1 == 1","action":"[SetVariable('pda_rules', 'pda_expulsion'), SetVariable('pda_rule_level', 4)]"},
{"label":"pda_rules","text":"BDSM Detention - Taste the whip.","requirement":"bdsm_detention > 0","action":"[SetVariable('pda_rules', 'pda_bdsm'), SetVariable('pda_rule_level', 5)]"},
{"label":"behavior","text":"Everything goes - Teachers are allowed to do whatever they feel like.","requirement":"1 == 1","action":"[SetVariable('behavior_rules', 'behavior_no_limit'), SetVariable('behavior_rules_multiplier', 2)]"},
{"label":"behavior","text":"Physical abuse - Teachers are allowed to use moderate violence.","requirement":"1 == 1","action":"[SetVariable('behavior_rules', 'behavior_physical'), SetVariable('behavior_rules_multiplier', 1.5)]"},
{"label":"behavior","text":"Verbal abuse - Verbal and non physical abuse are allowed.","requirement":"1 == 1","action":"[SetVariable('behavior_rules', 'behavior_verbal'), SetVariable('behavior_rules_multiplier', 1)]"},
{"label":"behavior","text":"Zero tolerance - No kind of aggression towards students are allowed.","requirement":"1 == 1","action":"[SetVariable('behavior_rules', 'behavior_zero'), SetVariable('behavior_rules_multiplier', 0.6)]"}
]



# Buyables
define buyable_cost = [0, 0, 0, 0]
define magic_accounting = 0

# Standard variables for school policy
define uniform = 'normal_uniform'               # nude_uniform, sexy_uniform, no_uniform, normal_uniform, conservative_uniform
define entrance_req = 3                         # 1 easy -- 5 hard +sexy?
define pda_rules = 'pda_suspension'             # pda_bdsm (5), pda_expulsion (4), pda_suspension (3), pda_normal (2), pda_none (1)
define pda_rule_level = 3

# Unlockables
define nude_uniform = 0
define sexy_uniform = 0
define bdsm_detention = 0
define no_detention = 0
define hyper_anatomic_body = 0
define tentacles = 0

# Variables for Teachers
define salary = 'salary_normal'                 # salary_high, salary_normal, salary_low
define salary_skill_multiplier = 1.2            # 0.7, 1.2, 1.7
define behavior_rules = 'behavior_verbal'       # behavior_no_limit (2), behavior_physical (1.5), behavior_verbal (1), behavior_zero(0.7)
define behavior_rules_multiplier = 1
define anatomic_body = 0                        # anatomic_body_non_sex (0), anatomic_body_normal (1), anatomic_body_sex (2)
define learning_materials = 0.7                 # old (0.7), normal (1.0), new (1.3)

init -100 python:

    def policy_bonus():
        globals()['academics'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['artistery'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['athletics'] += (learning_materials * salary_skill_multiplier) * (entrance_req / 3 )
        globals()['behavior'] += (behavior_rules_multiplier * (pda_rule_level / 2) ) - 2
        globals()['morale'] -= (behavior_rules_multiplier * (pda_rule_level / 2) ) - 2
        globals()['deviance'] -= (pda_rule_level / 2 ) - anatomic_body
        globals()['inhibition'] += (pda_rule_level / 2 ) - anatomic_body


        # Behavior data #
        if(behavior_rules == 'behavior_no_limit'):
            globals()['reputation'] -= 1

        elif(behavior_rules == 'behavior_zero'):
            globals()['reputation'] += 1

        # Uniform data #
        if(uniform == 'nude_uniform'):
            globals()['morale'] -= 2
            globals()['deviance'] += 3
            globals()['inhibition'] -= 3
            globals()['reputation'] -= 1

        elif(uniform == 'sexy_uniform'):
            globals()['morale'] -= 1
            globals()['behavior'] += 1
            globals()['inhibition'] -= 1
            globals()['deviance'] += 1

        elif(uniform == 'normal_uniform'):
            globals()['morale'] -= 1
            globals()['behavior'] += 1

        elif(uniform == 'no_uniform'):
            globals()['morale'] += 1
            globals()['behavior'] -= 1
            globals()['inhibition'] -= 1

        elif(uniform == 'conservative_uniform'):
            globals()['morale'] -= 2
            globals()['behavior'] += 2
            globals()['deviance'] -= 2
            globals()['inhibition'] += 2