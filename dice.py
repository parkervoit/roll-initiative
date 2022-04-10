import random 

def dice_roll(x, modifier, numdice, damage = False):
    ''' dice_roll(x, modifier, numdice)

        x = int n sides of the dice 

        modifier = int value of modifier for roll

        numdice = int n number of dice 

        This function returns the final total for a roll in D&D
    '''
    count = 1
    dice = 0
    for i in range(numdice):
        count += 1
        roll = random.randint(1,x)
        print(f'd{x} #{count - 1} Base : {roll}')
        if damage == True:
            if roll == 20:
                dice += (roll * 2)
            else:
                dice += roll
        else:
            dice += roll
    print(f'\nBase Total : {dice}')
    print(f'Modifier : +{modifier}')
    print('------------------------------')
    print(f'Total Roll : {dice + modifier}')