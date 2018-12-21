# Permutation pairs from a list.
def permute(xlist):
    return [[i, j] for i in xlist for j in xlist]


# Iterate list to create a dict with keys from a length
def pairDict(pairs, d=dict()):
    for k in range(len(pairs)):
        d[k + 1] = pairs[k]
    return d


# Group of size length elements from a list.
def groupList(xlen):
    theList = [(x + 1) for x in range(xlen * xlen)]
    N = xlen
    subList = [theList[n:n + N] for n in range(0, len(theList), N)]
    return subList


# Game Class
class game:
    def __init__(self):
        self.players = list()
        self.tanda = list()
        self.count = None
        self.cc = None

    # Check board if player mark have filled.
    def check(self, board, player):
        if self.count < len(board)**2:
            ptanda = [self.tanda[player]] * len(board)
            diag1 = [board[i][i] for i in range(0, len(board))]
            diag2 = [board[i][-i - 1] for i in range(0, len(board))]
            if diag1 == ptanda or diag2 == ptanda:
                return True
            for i in range(0, len(board)):
                baris = board[i]
                kolom = [x[i] for x in board]
                if baris == ptanda:
                    return True
                elif kolom == ptanda:
                    return True

            return False
        else:
            return None

    # Check if user input are available in board.
    def pinput(self, board, player):
        try:
            uinput = int(input('Hei Player {} ({}) masukan 1-{}\n'
                               .format(
                                   self.players[player],
                                   self.tanda[player],
                                   len(board)**2)))
            # col x raw
            if (board[self.cc[uinput][0]][self.cc[uinput][1]]) not in self.tanda:
                board[self.cc[uinput][0]][self.cc[uinput][1]] = self.tanda[player]
                return board
            else:
                self.display(board)
                print('Sudah terisi! Input yg benar!')
                return self.pinput(board, player)
        except ValueError:
            self.display(board)
            print('Jangan Kosong! Input yg benar!')
            return self.pinput(board, player)
        except IndexError and KeyError:
            self.display(board)
            print('Input yg benar!')
            return self.pinput(board, player)

    # Iterate over board and draw it.
    def display(self, board):
        print('\n-' + '--------' * 2 * len(board))
        for i in range(0, len(board)):
            print('|\t\t' * len(board) + '|')
            print('|\t' + '\t|\t'.join([str(x) for x in board[i]]) + '\t|')
            print('|\t\t' * len(board) + '|')
            print('-' + '--------' * 2 * len(board))

    # Alternately checking playing status.
    def play(self, board, p=0):
        self.display(board)
        board = self.pinput(board, p)
        if self.check(board, p):
            self.display(board)
            print('Selamat Player {}! Anda Menang!'.format(self.players[p]))
        elif self.check(board, p) is None:
            self.display(board)
            print('Yah ga ada yang menang...')
        else:
            self.count += 1
            if p == 0:
                return self.play(board, 1)
            elif p == 1:
                return self.play(board, 0)
        if input('Lagi? y/n\n') == 'y' and 'Y':
            self.play(self.setboard(len(board)))

    # Define board in n*n size.
    def setboard(self, n, num='n'):
        self.count = 0
        if num == 'y':
            board = groupList(n)
        elif num == 'n':
            board = [[' '] * n for i in range(n)]
        self.cc = pairDict(permute(range(len(board))))
        return board


if __name__ == "__main__":
    tictactoe = game()
    board = tictactoe.setboard(5, num='y')
    tictactoe.players = ['Aku', 'Kamu']
    tictactoe.tanda = ['X', 'O']
    start = tictactoe.play(board)
