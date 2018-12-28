import TicTacToe
import pandas as pd
from sympy.utilities.iterables import multiset_permutations
from math import factorial


class define:
    def __init__(self):
        self.game = None
        self.players = list()
        self.marks = list()
        self.lenboard = 3


class brute:
    def __init__(self, define):
        self.defined = define
        self.col = ['Last Player', 'Status', 'Moves', 'Done Moves']
        self.df = pd.DataFrame(columns=self.col)
        self.npboard = [x + 1 for x in range(self.defined.lenboard**2)]
        self.mpermutations = list(multiset_permutations(self.npboard))

    def execute(self, tries):
        for p in self.mpermutations[tries[0]:tries[1]]:
            start = self.defined.game.play(
                        self.defined.game.setboard(
                            self.defined.lenboard, num='y'), p=0, di=p)

            start[0] = self.defined.game.players[start[0]]

            if start[1] is True:
                start[1] = 'Win'
            elif start[1] is None:
                start[1] = 'Draw'

            start = start + [p] + [p[:start[2]]]

            start.pop(2)

            self.df = self.df.append(
                        pd.DataFrame(
                            [start],
                            columns=self.col))


def ranPair(xlen, hops):
    theList = [x * hops for x in range(xlen)]
    subList = [theList[n:n + 2] for n in range(0, len(theList), 2)]
    return subList


def bruteF(set):
    analyze = brute(set)

    n = 100
    multiplier = int((factorial(set.lenboard**2) / n))

    paired = ranPair(multiplier, n)

    tList = [paired[i] for i in range(0, len(paired), 50)]

    for tries in tList:
        analyze.execute(tries)
        print(tries)

    return analyze.df


def main():
    set = define()
    set.game = TicTacToe.game()
    set.game.players = ['Aku', 'Kamu']
    set.game.marks = ['X', 'O']

    set.lenboard = 3

    bf = bruteF(set)

    print(bf)


if __name__ == '__main__':
    main()
