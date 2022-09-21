# This function create a big cube with size X,Y,Z 
def Make_build(base_block, size_floor, material, amount_floors):
    text_function = []
    i = 1
    while i <= int(amount_floors):
        # Make floor with capasity
        stroka = ''
        stroka = 'fill ' + str(base_block['X']) + ' ' + str(base_block['Y']) + ' ' + str(base_block['Z']) + ' '
        stroka = stroka + str(base_block['X'] + size_floor['Length_floor']) + ' '
        stroka = stroka + str(base_block['Y'] + size_floor['Width_floor']) + ' '
        stroka = stroka + str(base_block['Z'] + size_floor['Hight_floor']) + ' '
        stroka = stroka + material + '\n'
        text_function.append(stroka)
        # Make floor with empty space inside
        stroka2 = ''
        stroka2 = 'fill ' + str(base_block['X'] + 1) + ' ' + str(base_block['Y'] + 1) + ' ' + str(base_block['Z'] + 1) + ' '
        stroka2 = stroka2 + str(base_block['X'] + size_floor['Length_floor'] - 1) + ' '
        stroka2 = stroka2 + str(base_block['Y'] + size_floor['Width_floor'] - 1) + ' '
        stroka2 = stroka2 + str(base_block['Z'] + size_floor['Hight_floor'] - 1) + ' '
        stroka2 = stroka2 + 'air\n'
        text_function.append(stroka2)
        #Change Z level of floor
        base_block['Y'] = base_block['Y'] + size_floor['Width_floor']
        i += 1
    text_function.append('say We created a new building!\n')
    return text_function