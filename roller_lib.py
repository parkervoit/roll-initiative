import random
import json
import re

'''
Developed by Parker Voit, Aug 2022
'''

# base dice rolling function
def dice_roll(x = 20, addl_dice = 0, ability = '', numdice = 1, crit = False, show_output = False, roll_type = 'ability'):
    ''' dice_roll(x, modifier, numdice)
        
        x = int n sides of the dice (default d20)
        addl_dice = int n sides of added die, granted from a spell like Guidance (default 0)
        modifier = int value of modifier for roll (default 0)
        numdice = int n number of dice (default 1)
        crit = whether or not the hit roll was a critical hit (default False)
        

        This function returns the final total for a roll in D&D
        Prints each dice roll, base sum, modifier, and the total roll value
        This function handles critical hits by duplicating the damage die, then adding the ability modifier.
        
        
        Returns dice, additional_dice, modifier
    '''
    count = 1
    dice = 0
    add_dice = 0
    output = ''
    try:
        modifier = char_sheet['abilities'][ability]['mod']
    except Exception:
        char_lookup = skill_sheet[ability]
        modifier = char_sheet['abilities'][char_lookup]['mod']
    for i in range(numdice):
        count += 1
        roll = random.randint(1,x)
        output += f'<|>  d{x} #{count - 1} Dice Roll :  {roll}  <|>\n'
        dice += roll
    if crit == True:
        dice *= 2
    if addl_dice != 0:
            add_dice += random.randint(1,addl_dice)
            output += f'<|>  d{addl_dice} Bonus Roll   :  {add_dice}  <|>\n'
    output += f'''\n\n Dice Total          :  {dice + add_dice}\n Modifier            :  {modifier:{"+" if modifier else ""}}\n-----------------------------\n Total Roll          :  {dice + modifier + add_dice}'''
    if show_output:
        print(output)
    return dice, add_dice, modifier

def dice_to_roll(str):
    ''' Parses a roll string with modifier and extracts the type of dice, how many, and what modifier'''
    split = tuple(str.split('d', maxsplit = 1))
    number_of_dice = split[0]
    dice_type = split[1].split()[0]
    modifier = split[1].split()[1]
    roll_type = split[1].split()[-1]
    return number_of_dice, dice_type, modifier, roll_type

def crit_handler(roll_type, roll, dice_type):
    ''' checks an attack roll to see if the result matches dice type. If it does, then it returns true'''
    if roll_type == 'hit' and roll == dice_type:
        crit = True
    else:
        crit = False
    return crit

def import_char_json(filepath):
    with open(filepath) as file:
        char_sheet = json.load(file)
    return char_sheet