import random 

def dice_roll(x = 20, y = 0, modifier = 0, numdice = 1, damage = False):
    ''' dice_roll(x, modifier, numdice)
        
        x = int n sides of the dice (default d20)
        y = int n sides of added die, granted from a spell like Guidance (default 0)
        modifier = int value of modifier for roll (default 0)
        numdice = int n number of dice (default 1)

        This function returns the final total for a roll in D&D
        Prints each dice roll, base sum, modifier, and the total roll value
        
        Returns dice, additional_dice, modifier
    '''
    count = 1
    dice = 0
    add_dice = 0
    for i in range(numdice):
        count += 1
        roll = random.randint(1,x)
        print(f'<|>  d{x} #{count - 1} Base      :  {roll}  <|>')
        if y != 0:
            add_dice += random.randint(1,y)
            print(f'<|>  Bonus Dice Roll  :  {add_dice}  <|>')
        if damage == True:
            if roll == 20:
                dice += (roll * 2)
            else:
                dice += roll
        else:
            dice += roll
    output = f'\n\n Base Total       :  {dice + add_dice}\n Modifier         :  {modifier:{"+" if modifier else ""}}\n-----------------------------\n Total Roll       :  {dice + modifier + add_dice}'
    return dice, add_dice, modifier, output

def roll_d20(addl_dice = 0, modifier = 0):
    ''' addl_dice = int n sides of bonus dice
        modifier = int ability modifier

        returns base sum of dice, bonus dice, modifier, and an output 
            string with total. '''
    return dice_roll(20, addl_dice, modifier, 1, False)
    