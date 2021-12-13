from functools import reduce
from pprint import pp, pprint
import os


def main(source):
    with open(source) as r:
        input = r.read()

    # input = '6,10\n0,14\n9,10\n0,3\n10,4\n4,11\n6,0\n6,12\n4,1\n0,13\n10,12\n3,4\n3,0\n8,4\n1,10\n2,14\n8,10\n9,0\n\nfold along y=7\nfold along x=5'

    dots, folds = [group.split('\n') for group in input.split('\n\n')]

    dots = set([tuple(int(v) for v in dot.split(',')) for dot in dots])
    folds = [parseFold(fold) for fold in folds]

    r1 = len(folding(dots, folds[0]))
    print(r1)

    allFolded = reduce(folding, folds, dots)

    maxX = max(allFolded, key=lambda v: v[0])[0] + 1
    maxY = max(allFolded, key=lambda v: v[1])[1] + 1

    r2 = '\n'.join([''.join([visualizing((x, y), allFolded) for x in range(maxX)]) for y in range(maxY)])
    print(r2)


def visualizing(loc, allFolded):
    if loc in allFolded:
        return '#'
    return ' '


def folding(dots, fold):
    if fold[0] == 'y':
        return set([(x, updateDot(y, fold[1])) for x, y in dots])
    if fold[0] == 'x':
        return set([(updateDot(x, fold[1]), y) for x, y in dots])


def updateDot(v, ref):
    if v < ref:
        return v
    return 2 * ref - v


def parseFold(fold):
    axis, value = fold.split(' ')[-1].split('=')
    return (axis, int(value))


if __name__ == '__main__':
    challenge = 13
    source = fr'..\resources\day{challenge}.txt'
    main(source)
