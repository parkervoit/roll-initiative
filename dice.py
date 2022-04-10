import random 

def dice_roll(x = 20, y = 0, modifier = 0, numdice = 1, damage = False):
    ''' dice_roll(x, modifier, numdice)
        
        x = int n sides of the dice (default d20)
        y = int n sides of added die, granted from a spell,e.g. Guidance (default 0)
        modifier = int value of modifier for roll (default 0)
        numdice = int n number of dice (default 1)

        This function returns the final total for a roll in D&D
        Prints each dice roll, base sum, modifier, and the total roll value
        
        Returns None
    '''
    count = 1
    dice = 0
    add_dice = 0
    for i in range(numdice):
        count += 1
        roll = random.randint(1,x)
        print(f'd{x} #{count - 1} Base : {roll}')
        if y != 0:
            add_dice += random.randint(1,y)
            print(f'Bonus Dice Roll : {add_dice}')
        if damage == True:
            if roll == 20:
                dice += (roll * 2)
            else:
                dice += roll
        else:
            dice += roll
    print(f'\nBase Total : {dice + add_dice}')
    print(f'Modifier : +{modifier}')
    print('------------------------------')
    print(f'Total Roll : {dice + modifier + add_dice}')