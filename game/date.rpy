# Count the days, months and years as well as name of the day.

init -100 python:
    total_days = 0
    day = 1
    month = 0
    year = 1
    planning_day = 0

    weekday_name = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    month_name = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month_length = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_now = month_name[month]

    def new_day():
        globals()['planning_day'] += 1
        globals()['total_days'] += 1
        globals()['day'] += 1
        if(globals()['day'] > month_length[month]):
            globals()['day'] = 1
            globals()['month'] += 1

            if(globals()['month'] > 11):
                globals()['year'] += 1
                globals()['month'] = 0
            globals()['month_now'] = month_name[month]

    def pay_day(pop,rep):               # 1st of every month this get called, pop = population, rep = reputation
        if globals()['magic_accounting'] > 0:
            income = pop * ((1 +(globals()['building_cafeteria'] / 10 ) ) + rep / 10) * (1 + (globals()['magic_accounting'] / 10 ) )
        else:
            income = pop * ((1 +(globals()['building_cafeteria'] / 10 ) ) + rep / 10)
        globals()['cash'] += int(income - ((income / 10) * salary_skill_multiplier ) )
        globals()['population'] += int(math.sqrt(rep / globals()['entrance_req'] ) * renpy.random.random() * 10 )


