import random
mistakes_allowed = 5

def rand_number():
    return random.randint(1,20)

def usr_input():
    return input('Please, input your number between 1 and 20: ')

def check(end,random, number, mistakes_counter):
    if number == random:
        print('You win!')
        return True
    if number > random:
        print('Your number is bigger then needed!')
    if number < random:
        print('Your number is less then needed!')
    if mistakes_counter == 4:
        return False

def game_over(end, mistakes_counter, mistakes_allowed):
    if end == 1:
        return True
    if mistakes_counter >= mistakes_allowed:
        print('You lose!')
        return True
    else:
        return False

def GAME():
    mistakes_counter = 0
    random = rand_number()
    end = 0
    while game_over(end, mistakes_counter, mistakes_allowed) == False:
        number = int(usr_input())
        chk = check(end, random, number, mistakes_counter)
        if not chk:
            mistakes_counter +=1
        else:
            end += 1

GAME()