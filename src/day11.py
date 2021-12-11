from functools import reduce
from pprint import pprint
import os


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '5483143223',
    #     '2745854711',
    #     '5264556173',
    #     '6141336146',
    #     '6357385478',
    #     '4167524645',
    #     '2176841721',
    #     '6882881134',
    #     '4846848554',
    #     '5283751526',
    # ]

    # lines = [
    #     '11111',
    #     '19991',
    #     '19191',
    #     '19991',
    #     '11111',
    # ]

    oState = [[int(o) for o in line.strip()] for line in lines]

    r1 = 0
    for _ in range(100):
        oState = step(oState)
        r1 += reduce(lambda f, l: f + l.count(0), oState, 0)

    print(r1)

    oState = [[int(o) for o in line.strip()] for line in lines]
    for i in range(2000):
        oState = step(oState)
        flashes = reduce(lambda f, l: f + l.count(0), oState, 0)
        if flashes == 100:
            break

    r2 = i + 1
    print(r2)


def step(oState):
    oState = [[o + 1 for o in l] for l in oState]
    return updateState(oState)


def updateState(oState):
    flashLocs = [(r, c) for r, l in enumerate(oState) for c, o in enumerate(l) if o > 9]
    for r, c in flashLocs:
        oState = flash(oState, r, c)

    if flashLocs:
        oState = updateState(oState)

    return oState


def flash(oState, r, c):
    oState = flashCol(oState, r, c)
    if r > 0:
        oState = flashCol(oState, r - 1, c)
    if r < len(oState) - 1:
        oState = flashCol(oState, r + 1, c)

    oState[r][c] = 0

    return oState


def flashCol(oState, r, c):
    oState[r][c] = addOne(oState[r][c])
    if c > 0:
        oState[r][c - 1] = addOne(oState[r][c - 1])
    if c < len(oState) - 1:
        oState[r][c + 1] = addOne(oState[r][c + 1])

    return oState


def addOne(o):
    if o == 0:
        return o
    return o + 1


def resetState(oState):
    return [[reset(o) for o in l] for l in oState]


def reset(o):
    if o > 9:
        return 0
    return o


if __name__ == '__main__':
    challenge = 11
    source = fr'..\resources\day{challenge}.txt'
    main(source)
