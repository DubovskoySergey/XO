def welcome():
    print("Добро пожаловать в игру Крестики-Нолики")
    while True:
        figure_io = None
        figure_player = input("Выберите фигуру Х/О: ")
        if figure_player == "x":
            figure_io == "o"
            break
        elif figure_player == "o":
            figure_io == "x"
            break
        else:
            print("Неверная фигура.")
    first_step = input("Кто будет ходить первым? im/io: ")
    return figure_player, figure_io, first_step

def print_field(field):
        t = "|___|___|___|"
        print("_ _ _ _ _ _")
        for i in range(len(field)):
            for j in range(len(field[i])):
                print("_" +str(field[i][j]), end="_" + "|")
            print()

def game(field, step, sel = ""):
    if sel != "":
        for i in range(len(field)):
            for j in range(len(field[i])):
                if field[i][j] == sel:
                    field[i][j] = "X"
                    step.append(sel)
        return field, step
    return field, step

def step(first_step):
    if first_step.lower() == "im":
        while True:
            try:
                sel = int(input("select number: "))
                if sel in range(1,10):
                    break
            except ValueError:
                print("Выберите существующую ячейку.")
        return sel
    elif first_step.lower() == "io":
        io()


def io():
    pass

def check_win(player_step):
    win = 0
    win_comb = [[1,2,3], [4,5,6], [7,8,9],
            [1,4,7], [2,5,8], [3,6,9],
            [1,5,9], [3,5,7]]
    for i in win_comb:
        if sorted(player_step) == i:
            win = 1
    if win == 1:
        return win
    else:
        return win

def start():
    field = [[1,2,3],[4,5,6],[7,8,9]]
    player_step = []
    io_step = []
    win = None
    figure_player, figure_io, first_step = welcome()
    print_field(field)
    win =  check_win(player_step)
    while win == 0:
        sel = step(first_step)
        field, player_step = game(field, player_step, sel)
        print_field(field)
        win =  check_win(player_step)
    print("Player win")

start()
