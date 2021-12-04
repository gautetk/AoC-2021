import math


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1',
    #     '',
    #     '22 13 17 11  0',
    #     ' 8  2 23  4 24',
    #     '21  9 14 16  7',
    #     ' 6 10  3 18  5',
    #     ' 1 12 20 15 19',
    #     '',
    #     ' 3 15  0  2 22',
    #     ' 9 18 13 17  5',
    #     '19  8  7 25 23',
    #     '20 11 10 24  4',
    #     '14 21 16 12  6',
    #     '',
    #     '14 21 17 24  4',
    #     '10 16 15  9 19',
    #     '18  8 23 26 20',
    #     '22 11 13  6  5',
    #     ' 2  0 12  3  7',
    # ]

    draws = [int(i) for i in lines[0].split(',')]
    boards = [parseBoard(lines[i + 1:i + 6]) for i in range(1, len(lines) - 1, 6)]
    boardSets = [makeBoardSets(b) for b in boards]

    r1 = findFirstBoard(draws, boardSets)
    print(r1)

    r2 = findLastBoard(draws, boardSets)
    print(r2)


def makeBoardSets(b):
    return [set(rc) for rc in b + [list(c) for c in zip(*b)]]


def findFirstBoard(draws, boardSets):
    for i in range(len(draws)):
        for bs in boardSets:
            drawVector = draws[:i + 1]
            bingo = bingoBoard(drawVector, bs)
            if bingo:
                return boardSetAndIndexToScore(drawVector, bs)


def findLastBoard(draws, boardSets):
    drawVectorLastBoard = []
    for bs in boardSets:
        for i in range(len(draws)):
            drawVector = draws[:i + 1]
            bingo = bingoBoard(drawVector, bs)
            if bingo:
                break
        if len(drawVector) > len(drawVectorLastBoard):
            lastBoard = bs
            drawVectorLastBoard = drawVector
    return boardSetAndIndexToScore(drawVectorLastBoard, lastBoard)


def bingoBoard(d, bs):
    if any(s.issubset(d) for s in bs):
        return True
    return False


def boardSetAndIndexToScore(d, bs):
    bsNumbers = set().union(*bs)
    bsNumbers.difference_update(d)
    return sum(bsNumbers) * d[-1]


def parseBoard(b):
    return [[int(v) for v in r.split(' ') if v] for r in b]


if __name__ == '__main__':
    challenge = 4
    source = fr'..\resources\day{challenge}.txt'
    main(source)
