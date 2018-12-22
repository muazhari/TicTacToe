import TicTacToe
import numpy as np
import pandas as pd
from scipy.special import factorial
from sympy.utilities.iterables import multiset_permutations


def main():
    tAnalyze = TicTacToe.game()
    tAnalyze.players = ['Tom', 'Jerry']
    tAnalyze.marks = ['X', 'O']

    lenboard = 3

    col = ['Last Player', 'Status', 'Moves', 'Done Moves']
    df = pd.DataFrame(columns=col)

    npboard = np.array([x + 1 for x in range(lenboard**2)])

    tries = 100

    for p in multiset_permutations(npboard):
        start = tAnalyze.play(
            tAnalyze.setboard(
                lenboard, num='y'), p=0, di=p)

        start[0] = tAnalyze.players[start[0]]

        if start[1] is True:
            start[1] = 'Win'
        elif start[1] is None:
            start[1] = 'Draw'

        start = start + [p] + [p[:start[2]+1]]

        start.pop(2)

        df = df.append(
                pd.DataFrame(
                    [start],
                    columns=col))

        tries -= 1
        if tries <= 0:
            break

    print('\n', len(df), 'tries.')
    print(df)


if __name__ == '__main__':
    main()
