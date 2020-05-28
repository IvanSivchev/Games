import random

EMPTY_MARK = 'x'
win_field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]

MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}

def shuffle_field():
    field = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, EMPTY_MARK]
    random.shuffle(field)
    return field


def print_field(field):
    print(field[0:4])
    print(field[4:8])
    print(field[8:12])
    print(field[12:16])


def is_game_finished(field):
    if field == win_field:
        return True
    else:
        return False


def perform_move(field, key):
    x_position = field.index(EMPTY_MARK)
    for move in MOVES.keys():
        if key == move:
            temp = field[x_position + MOVES[move]]
            field[field.index(temp)] = EMPTY_MARK
            field[x_position] = temp
            return field
    else:
        return IndexError


def handle_user_input():
    key = input("Choose your move! Up - w, Down - s, Left - a, Right - d: ")
    return key


def main():
    field = shuffle_field()
    while not is_game_finished(field):
        print_field(field)
        key = handle_user_input()
        perform_move(field, key)
    print("You win!")


if __name__ == '__main__':
    main()