# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
from random import randint

def pvp():
    candy_nums = int(input("Введите количество конфет: "))
    first_player = input("Введите имя первого игрока: ")
    second_player = input("Введите имя второго игрока: ")
    first_move = randint(0, 1)
    if first_move == 0:
        while (candy_nums > 0):
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break
            print(f'Ходит {second_player}')
            move2 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {second_player} !!! ')
                break
    else:
        while (candy_nums > 0):
            print(f'Ходит {second_player}')
            move2 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {second_player} !!! ')
                break
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break


def smart_enemy():
    candy_nums = int(input("Введите количество конфет: "))
    first_player = input("Введите  игрока: ")
    comp_player = 'Bot'
    first_move = randint(0, 1)
    if first_move == 0:
        while (candy_nums > 0):
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break
            print(f'Ходит {comp_player}', end=': ')
            move2 = candy_nums % 29 if candy_nums % 29 != 0 else randint(1, 28)
            print(move2)
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {comp_player} !!! ')
                break
    else:
        while (candy_nums > 0):
            print(f'Ходит {comp_player}', end=': ')
            move2 = candy_nums % 29 if candy_nums % 29 != 0 else randint(1, 28)
            print(move2)
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {comp_player} !!! ')
                break
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break


def pve():
    candy_nums = int(input("Введите количество конфет: "))
    first_player = input("Введите  игрока: ")
    comp_player = 'Bot'
    first_move = randint(0, 1)
    if first_move == 0:
        while(candy_nums > 0):
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break
            print(f'Ходит {comp_player}', end = ': ')
            if candy_nums < 29:
                move2 = candy_nums
            else:
                move2 = randint(1, 28)
            print(move2)
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {comp_player} !!! ')
                break
    else:
        while(candy_nums > 0):
            print(f'Ходит {comp_player}', end = ': ')
            if candy_nums < 29:
                move2 = candy_nums
            else:
                move2 = randint(1, 28)
            print(move2)
            candy_nums -= move2
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {comp_player} !!! ')
                break
            print(f'Ходит {first_player}')
            move1 = int(input("Введите число от 1 до 28: "))
            candy_nums -= move1
            print(f'осталось {candy_nums} конфет ')
            if candy_nums == 0:
                print(f'Победил {first_player} !!! ')
                break  
   


menu = int(input('Выбор соперника :\n1 для игры с другим игроком \n2 для игры с ботом\n3 для игры с умным ботом\n'))

if menu == 1:
    pvp()
elif menu == 2:
    pve()
else:
    smart_enemy()