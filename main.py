from random import randint

def print_field(field):
        t = "|___|___|___|"
        print("_ _ _ _ _ _")
        for i in range(len(field)):
            for j in range(len(field[i])):
                print("_" +str(field[i][j]), end="_" + "|")
            print()

def user_input():
    tap = None
    while True:
        try:
            tap = int(input('Выберите номер поля: '))
        except ValueError:
            continue
        else:
            return tap

def user_tap(u_tap, field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if u_tap == field[i][j]:
                field[i][j] = 'x'
    list_user.add(int(u_tap))
    return list_user, field

def io_tap(list_user, list_io, field):
    while True:
        io_t = randint(1,9)
        if io_t not in list_user and io_t not in list_io:
            break
    for i in range(len(field)):
        for j in range(len(field[i])):
            if io_t == field[i][j]:
                field[i][j] = '0'
                list_io.add(io_t)
    return list_io, field

def win(list_tap):
    win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,8],[1,5,9],[3,5,7]]
    for w in win_comb:
        result = all(x in list_tap for x in w)
        if result == True:
            return "win"
            break

list_user = set()
list_io = set()
field = [[1,2,3],[4,5,6],[7,8,9]]
print_field(field)
while True:
    u_tap = user_input()
    list_user, field = user_tap(u_tap, field)
    if win(list_user) == "win":
        print("Player win!")
        break
    list_io, field = io_tap(list_user, list_io, field)
    print_field(field)
    if win(list_io) == "win":
        print("IO win!")
        break
