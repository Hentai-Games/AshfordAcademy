# Buildings and starting level. 0 equals to not built.
define building_bath = 0
define building_classrooms = 1
define building_grounds = 1
define building_gym = 1
define building_library = 0
define building_pool = 0
define building_security = 0
define building_sports_field = 0
define building_dormitory = 0
define building_cafeteria = 0
define building_club_rooms = 0

# TODO: Move into clubs.rpy
define building_cheerleader_club = 0


# Buildings and prices for each level, we put prices in an list and let the level indicate the index for the price. All buildings are upgradeable until the price reaches "0".
# "requirement": "1 == 1" is due to the fact that "True" and "False" are global variables in python. //Ash: all python should work if you set True = False... This game don't...
define buildings = [
{"name": "bath",            "cost" : [325, 400, 475, 550, 700, 0],      "requirement": "1 == 1",        "image": "buildings/bath.jpg",          "description": "Open hot water baths for students to relax in. Also known as an onsen. \n\nA great way for students to unwind, but can lead to some naughty hijinx. \n\nBuying this will give a tiny increase to {b}morale{/b} every week, and allow you to visit the baths."},
{"name": "classrooms",      "cost" : [275, 350, 425, 550, 675, 0],      "requirement": "1 == 1",        "image": "buildings/classrooms.jpg",    "description": "Quality and state of classrooms, and the value of the educational materials available to teachers. \n\nIncreasing this will randomly add to your academic stats every month. \n\nThe next upgrade will add a tiny amount to all of your {b}academics{/b} each week."},
{"name": "grounds",         "cost" : [510, 620, 730, 840, 950, 0],      "requirement": "1 == 1",        "image": "buildings/grounds.jpg",       "description": "This building represents the quality and upkeep of the school. \n\nUpgrading it makes the whole school more beautiful, and students happier. \n\nThe next upgrade will add a small amount of {b}morale{/b} each week."},
{"name": "gym",             "cost" : [250, 400, 550, 700, 875, 0],      "requirement": "1 == 1",        "image": "buildings/gym.jpg",           "description": "Building where students can practice indoor athletic training. \nFirst level allows gym events and gym class, and higher levels give a bonus to {b}athletics{/b}. \n\nBuying this will open up the gym class, and allow you to visit the gym."},
{"name": "library",         "cost" : [250, 300, 375, 450, 575, 0],      "requirement": "1 == 1",        "image": "buildings/library.jpg",       "description": "A library to store the school's collection of books, as well as allow monitored internet access. \n\nBuying this will give a tiny increase to {b}intelligence{/b} every week."},
{"name": "pool",            "cost" : [350, 450, 550, 675, 800, 0],      "requirement": "1 == 1",        "image": "buildings/pool.jpg",          "description": "This is a swimming pool. \n\nLower levels only allow for visits.  Higher levels allow for bonuses to {b}athletics{/b}. Buying this will allow you to visit the pool."},
{"name": "security",        "cost" : [275, 325, 400, 525, 700, 0],      "requirement": "1 == 1",        "image": "buildings/security.jpg",      "description": "This is the level of quality of security for the entire school. \n\nWalls, cameras, guards, and all such things that protect from bad behavior. \n\nThe next upgrade will improve {b}school behavior{/b} a small amount each week."},
{"name": "sports_field",    "cost" : [225, 350, 475, 625, 750, 0],      "requirement": "1 == 1",        "image": "buildings/sports_field.jpg",  "description": "Large open fields where students can play, arrange games, practice sports, and generally exercise to their hearts' content. \n\nBuying this will allow fields visits."},
{"name": "dormitory",       "cost" : [650, 775, 900, 1125, 1300, 0],    "requirement": "1 == 1",        "image": "buildings/dormitory.jpg",    "description": "Build a dormitory to allow students to live on campus. \n\nBuilding this will allow you to visit the dormitory."},
{"name": "cafeteria",       "cost" : [725, 880, 1000, 1200, 0],         "requirement": "1 == 1",        "image": "buildings/cafeteria.jpg",    "description": "Open a cafeteria to allow students to buy snacks and socialize. \n\nBuilding this will allow you to visit the cafeteria and will give you some extra money each month."},
{"name": "club_rooms",      "cost" : [500, 700, 900, 1200, 0],          "requirement": "1 == 2",        "image": "buildings/classrooms.jpg",    "description": "Rebuilds old classrooms into club rooms. \n\nBuilding this will allow you to open clubs and visit them."}
]
#TODO: Update text and image for dorm and cafeteria.

# Since the buy building menu uses active pick we need to define a "normal state".
define building_pick = 'building_'+buildings[0]['name']
define building_level = eval(building_pick)
define building_cost_array = buildings[0]['cost']
define building_cost = building_cost_array[building_level]

init -100 python:

    # NOTE: New buildings might need rebalance.
    # TODO: Add "building_dormitory". Maybe dorms give bonus to population instead of stats?
    def building_bonus():
        globals()['morale'] += ((building_bath + building_grounds + building_pool + (building_cheerleader_club /2)) / 3) - ((building_security / 2 ) + balancer)
        globals()['behavior'] += building_security - balancer
        globals()['academics'] += ((building_library + building_classrooms) / 2) - balancer
        globals()['artistery'] += ((building_library + building_classrooms) / 2) - balancer
        globals()['athletics'] += ((building_pool + building_gym + building_sports_field) / 3) - ((building_cafeteria / 2) + balancer)
        globals()['deviance'] += (building_bath / 2) - balancer
        globals()['inhibition'] -= ((building_bath / 2) + (building_pool / 4)) - balancer
        globals()['reputation'] += good_points - evil_points
