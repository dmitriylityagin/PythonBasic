def space():
    print('                                       ')


def nyan1():
    print(' ▄▄▄▄▄  █      ▀    ▀█  ▀▄     █▀▀ ██  ')
    print(' ██▄▀██▄█   ▄       ██    ▀▀▀▀▀    ██  ')


def nyan2():
    print('        █  ▄    ▄              █       ')
    print('        █            ▄█▄▄  ▄   █ ▄▄▄   ')


def nyan3():
    print('       ▀█    ▄     ██    ▄   ▄  ▄   ██ ')
    print('       ▄█▄           ▀▄  ▀▀▀▀▀▀▀▀  ▄▀  ')


def nyan4():
    print('  ▀██▄▀██        ▀ ██▀             ▀██ ')
    print('    ▀████ ▀    ▄   ██   ▄█    ▄ ▄█  ██ ')


def nyan5():
    print('          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         ')
    print('        ▄▀            ▄       ▀▄       ')


def nyan6():
    print('      █▀▀█████████▀▀▀▀████████████▀    ')
    print('      ████▀  ███▀      ▀███  ▀██▀      ')
space()
nyan5()
nyan2()
nyan1()
nyan4()
nyan3()
nyan6()
space()

import random

min_number = 0
max_number = 255
attempt = 0
#input_number = 0

def start_game():
    global input_number
    input_number = 0
    print(f"Я загадал число от {min_number} to {max_number}")

def game_loop():
    global input_number, attempt

    case = random.randint(min_number, max_number)
    while input_number != case:
        input_number = int(input("Guess a number: "))
        attempt += 1
        if input_number < case:
            print("Your number is too small")
        elif input_number > case:
            print("Your number is too big")
        else:
            print("Right!")
def end_game():
    print(f"You made {attempt} attempts.")


start_game()
game_loop()
end_game()

