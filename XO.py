import random

def make_field():
    field = ['[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]', '[ ]']
    return field

def print_field(field):
    for i in range(0, 9, 3):
        print(field[i:i+3])
        print('\n)')

def make_move(field):
    move = int(input('Input cordinates to place X, first number for row, second for column: '))
    if move == 11 and field[0] == '[ ]':
        field[0] = '[X]'
    elif move == 12 and field[1] == '[ ]':
        field[1] = '[X]'
    elif move == 13 and field[2] == '[ ]':
        field[2] = '[X]'
    elif move == 21 and field[3] == '[ ]':
        field[3] = '[X]'
    elif move == 22 and field[4] == '[ ]':
        field[4] = '[X]'
    elif move == 23 and field[5] == '[ ]':
        field[5] = '[X]'
    elif move == 31 and field[6] == '[ ]':
        field[6] = '[X]'
    elif move == 32 and field[7] == '[ ]':
        field[7] = '[X]'
    elif move == 33 and field[8] == '[ ]':
        field[8] = '[X]'
    else:
        print('Cant do that! Try again')
        make_move(field)
    return field

def is_game_over(field, turns):
    if field[0] == field[1] == field[2] != '[ ]':
        return True
    elif field[3] == field[4] == field[5] != '[ ]':
        return True
    elif field[6] == field[7] == field[8] != '[ ]':
        return True
    elif field[0] == field[3] == field[6] != '[ ]':
        return True
    elif field[1] == field[4] == field[7] != '[ ]':
        return True
    elif field[2] == field[5] == field[8] != '[ ]':
        return True
    elif field[0] == field[4] == field[8] != '[ ]':
        return True
    elif field[2] == field[4] == field[6] != '[ ]':
        return True
    if turns == 10:
        return True
    else:
        return False

def computer_turn(field, turns):
    comp_move = random.choice(range(0, 9))
    if turns <= 8:
        if field[comp_move] == '[X]':
            computer_turn(field, turns)
        elif field[comp_move] == '[O]':
            computer_turn(field, turns)
        else:
            field[comp_move] = '[O]'
    return field

def main():
    turns = 0
    field = make_field()
    while not is_game_over(field, turns):
        print_field(field)
        field = make_move(field)
        turns += 1
        player = 'x'
        if not is_game_over(field, turns):
            field = computer_turn(field, turns)
            print_field(field)
            player = 'o'
            turns += 1
    if turns == 10:
        print('Its a tie!')
    else:
        if player == 'x':
            print('You win!')
        elif player == 'o':
            print('Computer wins!')
    if input('Play again? (1 - YES, 0 - NO): ') == '1':
        main()

main()