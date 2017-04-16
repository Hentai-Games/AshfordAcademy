##############################################################################
# Budget Menu
#
# A screen that shows income and expenditure.

screen show_budget_screen:

    # Calculate total sum of cash flow
    python:
        #Income
        student_pay = population * ( 1 + reputation / 10)
        cafeteria_income = int(population * (building_cafeteria / 10 ) )
        cafeteria = cafeteria_income / population
        magic_accounting_boost = int(((student_pay + cafeteria_income) * magic_accounting) / 10)
        multiplier = magic_accounting * 10
        each_student_pay = student_pay / population
        total_income = student_pay + cafeteria_income + magic_accounting_boost
        #Expend~
        teacher_salary = int((student_pay / 10 ) * salary_skill_multiplier )
        total_cost_buildings = 0
        total_expend = total_cost_buildings + teacher_salary
        #Total
        sum_total = total_income - total_expend

    frame:
        xpadding 10
        ypadding 10

    grid 3 14: # X columns & Y rows
        ycenter 0.5
        xcenter 0.5
        spacing 3

        text ""
        label "  {b}Ashford Academy budget:{/b}"
        text ""
        
        text ""
        label "{i}All values in thousands of dollars{/i}"
        text ""
        
        text "Income:"
        text ""
        text ""

        text "State funding:"
        text ""
        text "50 $"

        text "Students"
        text "[population] x [each_student_pay] $"
        text "[student_pay] $"

        text "Cafeteria income"
        text "[population] x [cafeteria]"
        text "[cafeteria_income] $"

        text "Magic accounting boost"
        text "[multiplier]%"
        text "[magic_accounting_boost] $"

        text "{b}Total income:{/b}"
        text ""
        text "{b}[total_income] ${/b}"

        text ""
        text ""
        text ""

        text "Expenditures:"
        text ""
        text ""

        text "[povTitle] [povLastName] salary:"
        text ""
        text "50 $"

        text "Teacher salary:"
        text ""
        text "[teacher_salary] $"

        text ""
        text "{b}Total:{/b}"
        text "{b}[sum_total] ${/b}"

        text ""
        text ""

        textbutton _("Return") action Return()

