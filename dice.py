import random
import json

with open('roll-initiative/char_sheet.json') as file:
    char_sheet = json.load(file)

def dice_roll(x = 20, addl_dice = 0, ability = '', numdice = 1, crit = False):
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
    modifier = char_sheet['abilities'][ability]['mod']
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
    return dice, add_dice, modifier, output

def roll_d20(addl_dice = 0, ability = ''):
    ''' addl_dice = int n sides of bonus dice
        modifier = int ability modifier

        returns base sum of dice, bonus dice, modifier, and an output 
            string with total. '''
    return dice_roll(20, addl_dice, ability, 1, False)
