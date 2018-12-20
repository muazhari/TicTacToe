def nested(x, ys):
    return any(x in nested for nested in ys)


def check(board, player):
    if nested(' ', board):
        diag1 = [board[i][i] for i in range(0, len(board))]
        diag2 = [board[i][-i - 1] for i in range(0, len(board))]
        for i in range(0, len(board)):
            ptanda = [tanda[player]] * len(board[i])
            baris = board[i]
            kolom = [x[i] for x in board]
            if baris == ptanda:
                print('baris penuh')
                return True
            elif kolom == ptanda:
                print('kolom penuh')
                return True
            elif diag1 == ptanda or diag2 == ptanda:
                return True
        return False
    else:
        return None


def pinput(board, player):
    cc = {'1': [0, 0], '2': [0, 1], '3': [0, 2],
          '4': [1, 0], '5': [1, 1], '6': [1, 2],
          '7': [2, 0], '8': [2, 1], '9': [2, 2], }
    try:
        uinput = input('Hei Player {} ({}) masukan 1-9\n'
                       .format(player + 1, tanda[player]))
        # cc = [int(x) - 1 for x in uinput.split(',')]
        # kol x baris
        if (board[cc[uinput][1]][cc[uinput][0]]) is ' ':
            board[cc[uinput][1]][cc[uinput][0]] = tanda[player]
            return board
        else:
            display(board)
            print('Sudah terisi! Input yg benar!')
            return pinput(board, player)
    except ValueError:
        display(board)
        print('Jangan Kosong! Input yg benar!')
        return pinput(board, player)
    except IndexError and KeyError:
        display(board)
        print('Input yg benar!')
        return pinput(board, player)


def display(board):
    print('\n-------------------')
    for i in range(0, len(board)):
        print('|     |     |     |')
        print('|  ' + '  |  '.join([str(x[i]) for x in board]) + '  |')
        print('|     |     |     |')
        print('-------------------')


def play(board, p=0):
    display(board)
    board = pinput(board, p)
    if check(board, p):
        display(board)
        print('Selamat Player {}! Anda Menang!'.format(p + 1))
    elif check(board, p) == None:
        display(board)
        print('Yah ga ada yang menang...')
    else:
        if p == 0:
            return play(board, 1)
        elif p == 1:
            return play(board, 0)
    if input('Lagi? y/n\n') == 'y' or 'Y':
        play(setboard())


def setboard():
    return ([[' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']])


player = [0, 1]
tanda = ['X', 'O']

play(setboard())
