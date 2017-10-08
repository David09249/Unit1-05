# Created by: David Wang
# Created on: 26-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit1-05
# This program displays the cost of the pizza, given the diameter

import ui

def calculate_button_touch_up_inside(sender):
    # calculate circumference
    
    # constants
    PI = 3.14
    LABOUR_COST = 0.75
    RENT_COST = 1.00
    MATERIAL_COST = 0.50
    HST = 0.13
    
    # input
    diameter = float(view['diameter_textbox'].text)
    
    # process
    sub_total = LABOUR_COST + RENT_COST + (MATERIAL_COST * diameter) 
    cost = sub_total + (sub_total * HST)
    
    # output
    # got currency format from here:
    # http://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
    view['answer_label'].text = 'The cost is: ' + '${:,.2f}'.format(cost)

view = ui.load_view()
view.present('full_screen')
