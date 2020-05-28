import random

MAX_MISTAKES = 6

words = ["жопа", ]

def get_random_word(words):
    return random.choice(words)

def get_statuses(word):
    statuses = []
    for letter in word:
        statuses.append(False)
    return statuses

def print_word(word, statuses):
    for index, l in enumerate(word):
        if statuses[index]:
            print(l, end=" ")
        else:
            print("_", end=" ")

def game_over(statuses, mistakes):
    if mistakes >= MAX_MISTAKES:
        return True
    for status in statuses:
        if not status:
            return False
    return True

def user_input():
    return input("Please, input letter: ")

def check(statuses, word, typed_letter):
    if typed_letter not in word:
        return False

    for index, letter in enumerate(word):
        if typed_letter == letter:
            statuses[index] = True
    return True


def game():
    word = get_random_word(words)
    statuses = get_statuses(word)
    mistakes = 0
    while not game_over(statuses, mistakes):
        print_word(word, statuses)
        print(f" You have {MAX_MISTAKES - mistakes} more try(es)!")
        typed_letter = user_input()
        result = check(statuses, word, typed_letter)

        if not result:
            mistakes += 1

    if mistakes < MAX_MISTAKES:

        print("You win! :)")
    else:
        print("You lose! :(")


game()