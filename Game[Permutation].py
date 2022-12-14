#Main idea of the game is elements permitation with empty element
#until the sequence is not restored

#[1][ ][3]             [1][2][3]             [1][2][3]             [1][2][3]     sequence
#[4][2][5] -> [2]^ ->  [4][ ][5] -> [5]< ->  [4][5][ ] -> [6]^ ->  [4][5][6] ->     is     -> end game
#[7][8][3]             [7][8][6]             [7][8][6]             [7][8][ ]     restored



from os import system
from random import shuffle


#---------------------------------------------------------------------------------------------------------------------------------------------------------------
def is_valid(field,size):
    if size % 2 == 0:
        return (len(list(filter(None,[field[i] > a for i in range(len(field)) for a in field[i+1:] if a != 0]))) + (1 + (field.index(0) // size))) % 2 == 0
    else:
        return (len(list(filter(None,[field[i] > a for i in range(len(field)) for a in field[i+1:] if a != 0]))) + 2 * (1 + (field.index(0) // size))) % 2 == 0
#---------------------------------------------------------------------------------------------------------------------------------------------(*collection check)

#---------------------------------------------------------------------------------
def field(range_set, selected_element_index, size):
    system('cls||clear')                    # <- clear console
    print('\n' + '  ' * (size - 1) + '>PYATNASHKI<' + '\n')
    for i in range(0, size**2, size):       # <- jumping over elements with a step equal to the size of the field (0,2) or (0,3,6) or (0,4,8,12)
        output_string = ' '
        for j in range(size):               # <- jumping over elements with a step equal to one [(0,1),(2,3)] or [(0,1,2),(3,4,5),(6,7,8)] and so on
            if range_set.index(range_set[i + j]) == selected_element_index[0]: # <- if the element is selected, then draw "> <" on it
                output_string += '>' + range_set[i + j] + '<'
            else:
                output_string += ' ' + range_set[i + j] + ' '
        print(output_string + '\n')
#-------------------------------------------(field render with selected element)

#----------------------------------------------------------------------------------------------------------------------------------------------------
def action(range_set, selected_element_index, size):
    key = input('wasd e: ')
    #______________________________________________________
    while key not in ['w', 'a', 's', 'd', 'e', '']:
        key = input('wasd e: ')
    #_______________________________________(input check)
    #_____________________________________________________________________
    if key == 'd' and selected_element_index[0] not in range(size - 1, size**2, size):
        return [selected_element_index[0] + 1, 0]
    elif key == 'a' and selected_element_index[0] not in range(0, size**2, size):
        return [selected_element_index[0] - 1, 0]
    elif key == 'w' and selected_element_index[0] not in range(size):
        return [selected_element_index[0] - size, 0]
    elif key == 's' and selected_element_index[0] not in range(size**2 - size, size**2, 1):
        return [selected_element_index[0] + size, 0]
    elif key == 'e' and range_set.index('[  ]') in range((selected_element_index[0] // size) * size, (selected_element_index[0] // size) * size + size):
        return [selected_element_index[0], 'row']
    elif key == 'e' and range_set.index('[  ]') in range(selected_element_index[0] % size, size**2, size):
        return [selected_element_index[0], 'column']
    else:
        return selected_element_index
    #_____________________________________(actions under various inputs)
#-----------------------------------------------------------------------------------(moving across the field, also permutation check)

#--------------------------------------------------------------------------------------------------
def swap(range_set, selected_element_index, size):
    a = range_set.index('[  ]')             # <- empty index
    b = selected_element_index[0]           # <- selected index

    if selected_element_index[1] == 'row' and a < b:
        for i in range(b - a):
            range_set[a + i], range_set[a + i + 1] = range_set[a + i + 1], range_set[a + i]
        return [range_set, b - 1]
    elif selected_element_index[1] == 'row' and a > b:
        for j in range(a - b):
            range_set[a - j], range_set[a - j - 1] = range_set[a - j - 1], range_set[a - j]
        return [range_set, b + 1]
    elif selected_element_index[1] == 'column' and a < b:
        for m in range(0, b - a, size):
            range_set[a + m], range_set[a + m + size] = range_set[a + m + size], range_set[a + m]
        return [range_set, b - size]
    elif selected_element_index[1] == 'column' and a > b:
        for n in range(0, a - b, size):
            range_set[a - n], range_set[a - n - size] = range_set[a - n - size], range_set[a - n]
        return [range_set, b + size]
    else:
        return [range_set, b]
#------------------------------------------------------------------------------------(permutation)

#---------------------------------------------------------------------------------------------------------------------------------------
size = int(input('Field size: '))          # <- set of the field size

end_set = [('[ ' + str(i) + ']') if i < 10 else ('[' + str(i) + ']') for i in range(1, size**2)]
end_set.append('[  ]')                      # <- completed **cell list represented like: ['[ 1]', '[ 2]', ..., '[15]', '[  ]'] - end game condition

element_id_swap = [0, 0]                    # <- selected top left element
start_set = [i for i in range(1, size**2)]
start_set.append(0)                         # <-  start ***num list represented like: [1, 2, ..., 15, 0]

shuffle(start_set)                          # <- first shuffle

while is_valid(start_set,size) != True:     # <- shuffling until the ***list become *collect
	shuffle(start_set)

game_set = ['[ ' + str(i) + ']' if i < 10 else '[' + str(i) + ']' for i in start_set]
game_set[game_set.index('[ 0]')] = '[  ]'   # <- turning the ***num list into the **cell list
#------------------------------------------------------------------------------------------------------------------(start settings)

#----------------------------------------------------------------
while game_set != end_set:
    field(game_set, element_id_swap, size)
    element_id_swap = action(game_set, element_id_swap, size)
    lst_el = swap(game_set, element_id_swap, size)
    game_set = lst_el[0]
    element_id_swap = [lst_el[1], 0]
else:
	system('cls||clear')
	print('\nYou WIN!')
	input()
#-----------------------------------------------------------(the game)