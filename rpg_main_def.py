# password = int(input("Введите пароль: "))
# login = int(input("Введите ваш логин: "))
# while not (len(login) > 5) and password[0:len(password)].isdigit() and (len(password) > 5):
#     print("Логин или пароль неверен")
# print("Все верно")
import random
import os
import time
from colorama import init
from colorama import Fore, Back, Style
# a = []
# for i in range(10000):
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)




# turtle.forward(100)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(100)

# Шестиугольник
# turtle.forward(50)
# turtle.left(60)
# turtle.forward(50)
# turtle.left(60)
# turtle.forward(50)
# turtle.left(60)
# turtle.forward(50)
# turtle.left(60)
# turtle.forward(50)
# turtle.left(60)
# turtle.forward(50)

# 4 Шестиугольника
# for i in range(6):
#     turtle.forward(50)
#     turtle.left(60)
# turtle.right(50)
# for i in range(6):
#     turtle.forward(50)
#     turtle.right(60)
# turtle.left(90)
# for i in range(6):
#     turtle.forward(50)
#     turtle.right(60)
# turtle.left(60)
# for i in range(6):
#     turtle.forward(50)
#     turtle.left(60)

# Черный квадрат
# turtle.shape("turtle")
# turtle.color("black")
# turtle.begin_fill()
# for i in range(4):
#     turtle.forward(50)
#     turtle.left(90)
# turtle.goto(10, 10)
# turtle.end_fill()

# turtle.shape("turtle")
# turtle.color("turquoise")
# turtle.dot(300, "turquoise")
# turtle.dot(30, "blue")
# turtle.up()
# turtle.goto(50, 0)
# turtle.down()
# turtle.color("black")
# turtle.circle(300, -30)
# turtle.up()
# turtle.goto(-80, 70)
# turtle.down()
# turtle.dot(30, "green")
# turtle.up()
# turtle.goto(80, 70)
# turtle.down()
# turtle.dot(30, "green")


# import turtle
# turtle.setup(500, 500)
# turtle.color("black")
# turtle.up()
# turtle.goto(-100, -200)
# turtle.down()
# turtle.begin_fill()
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(80)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(80)
# turtle.right(180)
# turtle.forward(80)
# turtle.end_fill()
# turtle.right(50)
# turtle.forward(100)
# turtle.right(81)
# turtle.forward(100)
# turtle.up()
# turtle.goto(-56, -175)
# turtle.end_fill()
# turtle.goto(100, 200)
# turtle.dot(100, "yellow")
# turtle.up()
# turtle.goto(-210, -240)
# turtle.color("green")
# turtle.left(120)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-180, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-150, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-120, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-90, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-60, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(-30, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(0, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(30, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(60, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(90, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(120, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(150, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(180, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)
# turtle.up()
# turtle.goto(210, -240)
# turtle.down()
# turtle.right(-30)
# turtle.forward(30)
# turtle.right(30)
# turtle.forward(10)

#import turtle
#import random

# c = ["black", "blue", "yellow", "pink", "red", "brown"]
# y = 150
# for i in range(15):
#     turtle.up()
#     turtle.goto(-50, y)
#     turtle.down()
#     a = random.randint(0, len(c) - 1)
#     turtle.color(c[a])
#     turtle.forward(100)
#     y = y - 20
# turtle.mainloop()


# s = f + a + d
# numbers = [a, f, d]
# a = input("Введите число: ")
# while a != "exit":
#     f = input("Введите число: ")
# if numbers == "exit":
#     print(s)
#     v = numbers.reverse()
#     print(v)

# c = ["black", "blue", "yellow", "pink", "red", "brown"]
# y = -100
# x = -100
# for i in range(14):
#     turtle.up()
#     turtle.goto(x, y)
#     turtle.down()
#     a = random.randint(0, len(c) - 1)
#     turtle.color(c[a])
#     turtle.dot(50)
#     y = y + 30
#     x = x + 30
# turtle.mainloop()


# import turtle
# import random
# f = []
# y = -100
# x = -100
# a = input("Введите цвет: ")
# while a != "exit":
#     f.append(a)
#     a = input("Введите цвет: ")
#     if a == "exit":
#         for i in range(14):
#             turtle.up()
#             turtle.goto(x, y)
#             turtle.down()
#             g = random.randint(0, len(f) - 1)
#             turtle.color(f[g])
#             y = y + 35
#             x = x + 35
#             for i in range(4):
#                 turtle.forward(30)
#                 turtle.left(90)
#         turtle.mainloop()



# n = []
# while True:
#     a = int(input("Введите число: "))
#     n.append(a)
#     if a != exit:
#         f = int(input("Введите число: "))
#         n.append(f)
#     elif a == exit:
#         print(sum(n))
#         v = n.reverse()
#         print(v)
#         print(n[-1])

# while a != exit:
#     n.append(a)
#     f = input("Введите число: ")
#     if f == exit:
#        break
#        print(sum(n))
#        v = n.reverse()
#        print(n)
#        print(n[-1])


# import turtle
# v = []
# x = ""
# y = ""
# x_list = []
# y_list = []
# while x != "exit" and y != "exit":
#     x = input("Введите координату x: ")
#     y = input("Введите координату y: ")
#     xsign = 1
#     ysign = 1
#     if x[0] == "-":
#         x = x[1:]
#         xsign = -1
#     if y[0] == "-":
#         y = y[1:]
#         ysign = -1
#     if x.isdigit() and y.isdigit():
#         x_list.append(int(x) * xsign)
#         y_list.append(int(y) * ysign)
# for i in range(len(x_list)):
#     turtle.goto(x_list[i], y_list[i])
# turtle.mainloop()

# k = {"Возраст": "1 год", "порода": "овчарка", "масса": "5 кг"}
# while True:
#     a = input("Что вывести? ")
#     print(k[a])


# k = {'ключ 1':"значение 1", 'ключ 2':"значение 2", 'ключ 3':"значение 3",
#      'ключ 4':"значение 4", 'ключ 5':"значение 5", 'ключ 6':"значение 6",}
# f = k.keys()
# print(f)

# import turtle
# import random
# c = ["blue", "green", "pink", "purple", "yellow", "grey", "brown"]
# x = -100
# y = 50
# turtle.up()
# turtle.goto(x, y)
# turtle.down()
# while True:
     #a = random.randint(160, 180)
    # g = random.randint(0, len(c) - 1)
    # turtle.color(c[g])
    # turtle.left(90)
    # turtle.forward(100)
    # turtle.right(170)



# turtle.pensize(5)
# def create_rect():
#     for i in range(4):
#         turtle.forward(50)
#         turtle.left(90)
# create_rect()
#
# def create_tr():
#     for i in range(2):
#         turtle.left(60)
#         turtle.forward(100)
#     turtle.left(60)
#     turtle.left(90)
#     turtle.forward(200)
#
# def create_circle():
#     turtle.dot(60, "black")
#
#
# turtle.up()
# turtle.goto(100, 100)
# turtle.down()
# create_tr()
#
#
# turtle.up()
# turtle.goto(-100, -100)
# turtle.down()
# create_circle()
#
# turtle.mainloop()


# import requests
# from bs4 import BeautifulSoup as b
# import random
# import telebot
# API_KEY = "6231784412:AAHnlhkskD0aPBe1OnjV7l1qvTKhO6Q-U_E"
# URL = "https://www.anekdot.ru/last/good/"
# def parser(url):
#     r = requests.get(url)
#     soup = b(r.text, 'html.parser')
#     anekdots = soup.find_all("div",class_ = 'text')
#     return [c.text for c in anekdots]
#
# list_of_jokes = parser(URL)
# random.shuffle(list_of_jokes)
#
# bot = telebot.TeleBot(API_KEY)
# @bot.message_handler(commands=['начать'])
#
# def hello(message):
#     bot.send_message(message.chat.id, "Привет, хочешь посмеяться введите цифру!")
# @bot.message_handler(content_types=["text"])
# def jokes(message):
#     if message.text.lower() in "123456789":
#         bot.send_message(message.chat.id, list_of_jokes[0])
#         del list_of_jokes[0]
#     else:
#         bot.send_message(message.chat.id, "Введите любую цифру!")
#
# bot.polling()

# def sq(a,b):
#     p = 2 * (a + b)
#     pl = a * b
#     print("Периметр:",p, "\nПлощадь:", pl)
#
# a = int(input("Введите сторону a: "))
# b = int(input("Введите сторону b: "))
# sq(a,b)
# def top_bread():
#     print("/￣￣￣\\")
#
# def bottom_bread():
#     print("\_____/")
#
# def tomato():
#     print("◯◯◯◯")
#
# def meat_and_cheese():
#     print("⋁ΞΞΞΞΞ⋁")
# top_bread()
# tomato()
# meat_and_cheese()
# bottom_bread()

# board = list(range(0,9))
# cells = 3
# dashes = 13
# spaces = 14
# counter = 0
# is_win = False
# tictoken = ''
#
#
# def check_win():
#     win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coords:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
# def make_step(count):
#     if count % 2 == 0:
#         token = take_input('X')
#     else:
#         token = take_input('0')
#     return token
#
#
# def draw_board():
#     for i in range(cells):
#        print(' ' * spaces, end="")
#        print('-' * dashes)
#        print(' ' * spaces, end="")
#        print(f'! {board[0 + i * 3]} ! {board[1 + i * 3]} ! {board[2 + i * 3]} !')
#        print(' ' * spaces, end="")
#        print("-" * dashes)
#
# def take_input(player_token):
#     player_answer = input(f'Where we put a {player_token}?: ')
#     if player_answer == "":
#         return 1
#     elif int(player_answer) >= len(board):
#         print("this area is not available")
#         return 1
#     player_answer = int(player_answer)
#     if str(board[player_answer]) not in 'XO':
#         board[player_answer] = player_token
#     else:
#         print("This cell is already taken!")
#         return 1
#     return player_token
#
# def main():
#     counter = 0
#     is_win = False
#
#     while not is_win:
#         draw_board()
#
#         tictoken = make_step(counter)
#
#         counter+=1
#
#         if counter > 4:
#             winner = check_win()
#             if winner:
#                 is_win = True
#                 print(f'{tictoken} is win!')
#             elif counter == 9:
#                 print("Draw! You're amazing!")
#                 return 1
#     draw_board()
#     input('Press enter to exit.')
#
# main()



# d = {"cat": "котик", "dog": "собака"}
# for i in d:
#     print(i, d[i])
#     print(d[i])

#
# # 1. Добавить перевод слова horse
# # 2. возможность удалить элемент по желанию пользователя
#
# print(d['cat'])


# translate = {"cat": "кошка"}
# translate["horse"] = "лошадь"
# s = input("Что хотите удалить? ")
# if s =="leave": print("Досвидания")
# else: del translate[s]
# rwarrior = {'здоровье': 100, 'атака': 30, 'защита': 25, 'навыки': {'щит': 10 }}
# archer = {'здоровье': 50, 'атака': 40, 'защита': 20, 'навыки': {'убежать': 10}, 'инвентарь': ['стрелы', 'меч', 'еда']}
# wizard = {'здоровье': 30, 'атака': 50, 'защита': 15, 'навыки': {'магический щит': 10, 'лечение': 5}}
#
# def print_dict():
#   for i in rwarrior:
#      print(i, rwarrior[i], sep=": ")
#   for a in archer:
#       print(a,archer[a], sep=": ")
#   for n in wizard:
#       print(n, wizard[n], sep=": ")



#print_dict()


# rwarrior = {'здоровье': 100, 'атака': 30, 'защита': 25, 'навыки': {'щит': 10 }}
# archer = {'здоровье': 50, 'атака': 40, 'защита': 20, 'навыки': {'убежать': 10}, 'инвентарь': ['стрелы', 'меч', 'еда']}
# wizard = {'здоровье': 30, 'атака': 50, 'защита': 15, 'навыки': {'магический щит': 10, 'лечение': 5}}
#
# def print_dict(item):
#     a = rwarrior.get()
#     s = archer.get()
#     d = wizard.get()
#     for i in item:
#         print(i,a,s,d)
# for item in [rwarrior, archer, wizard]:
#     print_dict(item)


# def space():
#     print('                                       ')
#
#
# def nyan1():
#     print(' ▄▄▄▄▄  █      ▀    ▀█  ▀▄     █▀▀ ██  ')
#     print(' ██▄▀██▄█   ▄       ██    ▀▀▀▀▀    ██  ')
#
#
# def nyan2():
#     print('        █  ▄    ▄              █       ')
#     print('        █            ▄█▄▄  ▄   █ ▄▄▄   ')
#
#
# def nyan3():
#     print('       ▀█    ▄     ██    ▄   ▄  ▄   ██ ')
#     print('       ▄█▄           ▀▄  ▀▀▀▀▀▀▀▀  ▄▀  ')
#
#
# def nyan4():
#     print('  ▀██▄▀██        ▀ ██▀             ▀██ ')
#     print('    ▀████ ▀    ▄   ██   ▄█    ▄ ▄█  ██ ')
#
#
# def nyan5():
#     print('          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄         ')
#     print('        ▄▀            ▄       ▀▄       ')
#
#
# def nyan6():
#     print('      █▀▀█████████▀▀▀▀████████████▀    ')
#     print('      ████▀  ███▀      ▀███  ▀██▀      ')
#
#
#
# nyan5()
# nyan2()
# nyan3()
# nyan4()
# nyan6()
# space()

#import random

# # def check():
# #         try:
# #             input_number = int(input("Угадай число: "))
# #         except:
# #             print("Введите правильное значение!")#
# min_number = 0
# max_number = 255
# attempt = 0
#
# def start_game():
#     print(f'Я загадал число от {min_number} до {max_number}')
#
# def game_loop():
#     global attempt
#     case = random.randint(min_number, max_number)
#     # try:
#     #     input_number =input("Угадай число: ")
#     # except:
#     #     print("Введите правильное значение!")
#     while 1:
#         attempt += 1
#         input_number = input("Введите число: ")
#         if input_number.isdigit():
#             if int(input_number) < case:
#                 print("Число слишком маленькое!")
#                 continue
#             elif int(input_number) > case:
#                 print("Число слишком большое!")
#                 continue
#             else:
#                 print("Угадал!")
#                 break
#         else:
#             print("Введите  числовое значение!")
#             continue
#
#
# def end_game():
#     print(f"Ты сделал попыток: {attempt}")
#
# start_game()
# game_loop()
# end_game()
# #
#
# def countdown(name, seconds):
#     import time
#
# for sec in range(seconds, -1, -1):
#     if sec > 0:
#         print(f"the rocket {name} will start by {sec} seconds")
#     else:
#         print("Lift off")
#     time.sleep(1)
# countdown(seconds=5, name="Falcon 3000")



# def count(N):
#     print("-" * int(N))
#
# N = int(input())
# for i in range(2):
#     count(N)

# def numsum(N:float, a: float):
#     print(N + a)
#
#
#
#
#
# N = float(input())
# a = float(input())
# numsum(N, a)


# def count(n):
#     e = n
#     m = 0
#     for i in range(n):
#         if n == 0:
#             return 0
#         elif n % e == 0:
#             m = m + 1
#             e = e - 1
#         else:
#             e = e - 1
#     return m
#
#
#
# n = int(input("Введите число: "))
#
# print(count(n))

# def numberOfOnes(N):
#     a = 0
#     while N != 0:
#         a += N % 2
#         N //= 2
#     print(a)
#
# N = int(input())
# numberOfOnes(N)

# board = list(range(0,9))
# cells = 3
# dashes = 13
# spaces = 14
# counter = 0
# is_win = False
# tictoken = ''
#
#
# def check_win():
#     win_coords = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coords:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False
#
# def make_step(count):
#     if count % 2 == 0:
#         token = take_input('X')
#     else:
#         token = take_input('0')
#     return token
#
#
# def draw_board():
#     for i in range(cells):
#        print(' ' * spaces, end="")
#        print('-' * dashes)
#        print(' ' * spaces, end="")
#        print(f'! {board[0 + i * 3]} ! {board[1 + i * 3]} ! {board[2 + i * 3]} !')
#        print(' ' * spaces, end="")
#        print("-" * dashes)
#
# def take_input(player_token):
#     player_answer = input(f'Where we put a {player_token}?: ')
#     if player_answer == "":
#         return 1
#     elif int(player_answer) >= len(board):
#         print("this area is not available")
#         return 1
#     player_answer = int(player_answer)
#     if str(board[player_answer]) not in 'XO':
#         board[player_answer] = player_token
#     else:
#         print("This cell is already taken!")
#         return 1
#     return player_token
#
# def main():
#     counter = 0
#     is_win = False
#
#     while not is_win:
#         draw_board()
#
#         tictoken = make_step(counter)
#
#         counter+=1
#
#         if counter > 4:
#             winner = check_win()
#             if winner:
#                 is_win = True
#                 print(f'{tictoken} is win!')
#             elif counter == 9:
#                 print("Draw! You're amazing!")
#                 return 1
#     draw_board()
#     input('Press enter to exit.')
#
# main()


# def strint(N: int, s: str):
#     print(s * N)
# s  = input()
# N = int(input())
# for i in range(3):
#     strint(N, s)






# def string(s:str):
#     wordMax =''
#     max = 0
#     s = s + ' '
#     while len(s) > 0:
#         n = s.find(' ')
#         word = s[:n]
#         print(word)
#         if len(word) > max:
#             max = len(word)
#             wordMax = word
#         s = s[n+1:]
#
#     print(wordMax)
#
# s1 = input()
# string(s1)
# s2 = input()
# string(s2)
# word = "m"
# def printTriangle(N):
#     for i in range(N + 1):
#         print(word * i)
#
#
#
#
# N = int(input())
# printTriangle(N)

# def fact(n):
#     if n == 1:
#         return 1
#     return fact(n-1) * n
#
# fact(5)




# def recursion(n):
#     if n == 1:
#       print(n)
#       return 1
#     elif n > 1:
#         print(n)
#         return recursion(n - 1)
#
# recursion(int(input('Число: ')))
# def numsum(N:float, a: float):
#     print(N + a)
#
#
#
#
#
# N = float(input())
# a = float(input())
# numsum(N, a)

from  random import choice
# list = []
# n = int(input("Введите число: "))
# k = r.randint(0, n)
# l = r.randint(0, n)
# a = r.randint(0, n)
# for i in range(3):
#     list.append(a)
#     a = k
#     k = l
# def get_random_list():
#     start = min(list)
#     end = max(list)
#     length = len(list)
#     print(f'Начало диапозона {start}: \nКонец диапозона {end}: \nКоличество элементов {length}:')
#
# get_random_list()

import random
import os
import time
from colorama import init
from colorama import Fore, Back, Style

role = {

        '1': 'Воин',
        '2': 'Лучник',
        '3': 'Маг'
    }

classes = {
    'Воин': {
        'здоровье': 100,
        'атака': 50,
        'защита': 40,
        'навыки': {
            'щит': 20
        }
    },
    'Лучник': {
        'здоровье': 70,
        'атака': 80,
        'защита': 25,
        'навыки': {
            'убежать': 10
        }
    },
    'Маг': {
        'здоровье': 50,
        'атака': 90,
        'защита': 15,
        'навыки': {
            'магический щит': 45,
            'лечение': 20
        }
    }
}

def init_person(name: str, is_enemy: bool  = False) -> dict[str,str | dict[str, int|dict]]:
    if is_enemy:
        person = {'класс':role[random.choice(list(role.keys()))] }
    else:
        while True:
           choice =  input(Fore.CYAN + 'Введите класс: 1 - Воин, 2 - Лучник, 3 - Маг\n')
           if is_valid(text=choice, is_role=True):
                break
        person = {"класс": role[choice]}
    person.update({'харастеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(Fore.YELLOW + f"{person['имя']} - {person['класс']}, имеет харастеристики: {person['харастеристики']}")
    return person

def is_valid(text: str, is_role: bool = False) -> True :
    if len(text) == 0:
        print(Fore.RED + 'Ошибка ввода. Вы ввели пустую строку.')
        return False
    elif text not in '123' and is_role == True:
        print(Fore.RED + 'Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
    else:
        return True
player_name = input(Fore.GREEN + "Введите ваше имя: ")
def get_player_name() -> str:
    if len(player_name) == 0 or player_name in "^%*@#!":
        print(Fore.YELLOW + f'В вашем имени: {player_name} найдены некоректные значения!')
    else:

        return player_name
get_player_name()


def get_random_name() -> str:
    list2 = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
    list1 = ['Лечащий', 'Летающий', 'Интересный', 'Скучный', 'Большой', 'Железный', 'Голодный','Умный', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'Восхитительный', 'Непобедимый']
    r1 = random.choice(list1)
    r2 = random.choice(list2)
    return r1, r2
get_random_name()

def enemy_atack(enemy1:dict [ str,str | dict],enemy2: dict[str,str|dict]):
    print(Fore.GREEN + f'{enemy1["имя"]} атакует {enemy2["имя"]}')
    damage = enemy1['харастеристики']['атака'] - enemy2['харастеристики']['защита']
    time.sleep(2)
    if damage < 0:
        damage = 1
    enemy2['харастеристики']['здоровье'] -= damage
    print(Fore.BLUE + f"{enemy1['имя']} наносит {damage}  урона и у {enemy2['имя']} остается {enemy2['харастеристики']['здоровье']} здоровья! ")


player = init_person(name=get_player_name())
enemy = init_person(get_random_name(), is_enemy=True)
enemy_atack(player, enemy)


def apply_skill(enemy):
    rand = random.randint(1,10)
    if rand > 6:
        skill = random.choice(list(enemy['характеристики']['навыки'].keys())) # Выбирает случайный навык
        enemy['характеристики']['здоровье'] += enemy['характеристики']['навыки'][skill]


        print(f"{enemy['имя']} применяет способность {skill}!")
apply_skill(enemy)

def clear():
    return os.system('cls')

def enter_to_continue():input("Введите Enter: ")


def fight_for_the_win(atacker:dict[str, str| dict], defender:dict[str,str| dict])-> bool:
    while True:
        time.sleep(2)
        clear()

        if atacker['харастеристики']['здоровье'] > 0:
            enemy_atack(atacker,defender)
        else:
            print(f'{atacker["имя"]} потерпел поражение!')
            return False
        if defender['харастеристики']["здоровье"] > 0:
            enemy_atack(atacker,defender)
        else:
            print(f'{defender["имя"]} потерпел поражение!')
            return True
        enter_to_continue()


clear()
fight_for_the_win(player,enemy)


