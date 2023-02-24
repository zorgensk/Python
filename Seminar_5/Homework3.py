# Создайте программу для игры в ""Крестики-нолики"".



def draw_board(play_field):
    for i in range(3):
        print (play_field[0+i*3], play_field[1+i*3], play_field[2+i*3])

def move_play_field(step,symbol):
    ind = play_field.index(step)
    play_field[ind] = symbol

def check_win(play_field):
    win_result = ((0 , 1 , 2), (3 , 4 , 5), (6 , 7 , 8), (0 , 3 , 6) , (1 , 4 , 7), (2 , 5 , 8), (0 , 4 , 8), (2 , 4 , 6))
    for i in win_result:
        if play_field[i[0]] == play_field[i[1]] == play_field[i[2]]:
            return play_field[i[0]]
    return False

def chek_move():
    while True:
        try:
            n = int(input())
            if n < 1 or n > 9:
                raise  Exception
            return n
        except ValueError:
            print('Неверный формат')
        except Exception:
            print('Введите число от 1 до 9')

play_field = list(range(1, 10))
win = False
count = 0
while not win:
    draw_board(play_field)
    print("Ходит X: ")
    step_X = chek_move()
    symbol = 'X'
    count += 1
    move_play_field(step_X, symbol)
    temp = check_win(play_field)
    if temp:
        print("Победа Х !!!")
        win = True
        break
    draw_board(play_field)
    if count == 9:
        print("Ничья!!!")
        win = True
        break
    print("Ходит O: ")
    step_O = chek_move()
    symbol = 'O'
    count += 1   
    move_play_field(step_O, symbol)
    temp = check_win(play_field)
    if temp:
        print("Победа O !!!")
        win = True
        break
    
draw_board(play_field)
