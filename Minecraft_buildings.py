import Make_build

base_block = {'X':0, 'Y':0, 'Z':0}
size_floor = {'Length_floor':0, 'Width_floor':0, 'Hight_floor':0}
material = 'air'
amount_floors = 0
text_function = []

base_block['X'] = int(input('Enter X = '))
base_block['Y'] = int(input('Enter Y = '))
base_block['Z'] = int(input('Enter Z = '))

size_floor['Length_floor'] = int(input('Enter Length of floor = '))
size_floor['Width_floor'] = int(input('Enter Width of floor = '))
size_floor['Hight_floor'] = int(input('Enter Hight of floor = '))

material = input('Material of floor = ')
amount_floors = int(input('Amount of the floors = '))

text_function = Make_build.Make_build(base_block, size_floor, material, amount_floors)

for i in text_function:
    print(i)


# Make file with functions
name_of_file = 'create_building.mcfunction'
way_file = 'c:\\Users\\Atopus\\first\\pythonProject\\Minecraft\\'

write_file = 1
if write_file == 1:
    nefile = open(way_file + '\\' + name_of_file, 'w')
    # Add double cpase for the first Block
    i = 0
    while i < len(text_function):
        nefile.write(text_function[i])
        i += 1
    nefile.close()






