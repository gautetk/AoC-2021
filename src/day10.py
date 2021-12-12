from functools import reduce
from pprint import pprint
import os


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '[({(<(())[]>[[{[]{<()<>>',
    #     '[(()[<>])]({[<{<<[]>>(',
    #     '{([(<{}[<>[]}>{[]{[(<()>',
    #     '(((({<>}<{<{<>}{[]{[]{}',
    #     '[[<[([]))<([[{}[[()]]]',
    #     '[{[{({}]{}}([{[{{{}}([]',
    #     '{<[[]]>}<{[{[{[]{()[[[]',
    #     '[<(<(<(<{}))><([]([]()',
    #     '<{([([[(<>()){}]>(<<{{',
    #     '<{([{{}}[<[[[<>{}]]]>[]]',
    # ]

    data = [line.strip() for line in lines]

    corruptedScores = [corruptScore(line) for line in data]
    r1 = sum(corruptedScores)
    print(r1)

    incompleteScores = [incompleteScore(line) for cs, line in zip(corruptedScores, data) if cs == 0]
    incompleteScores.sort()
    r2 = incompleteScores[int(len(incompleteScores) / 2.0)]
    print(r2)


def corruptScore(line):
    types = {
        ')': ('(', 3),
        ']': ('[', 57),
        '}': ('{', 1197),
        '>': ('<', 25137),
    }
    notClosed = []
    for c in line:
        if c in types:
            if notClosed[-1] == types[c][0]:
                notClosed = notClosed[:-1]
            else:
                return types[c][1]
        else:
            notClosed.append(c)

    return 0


def incompleteScore(line):
    types = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }
    lineEnd = []
    closed = []
    for c in reversed(line):
        if c in types:
            if not closed:
                lineEnd.append(types[c])
            else:
                closed = closed[:-1]
        else:
            closed.append(c)

    return reduce(lambda score, p: score * 5 + p, lineEnd, 0)


if __name__ == '__main__':
    challenge = 10
    source = fr'..\resources\day{challenge}.txt'
    main(source)
