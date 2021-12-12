from functools import reduce
from pprint import pprint
import os


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     'start-A',
    #     'start-b',
    #     'A-c',
    #     'A-b',
    #     'b-d',
    #     'A-end',
    #     'b-end',
    # ]

    # lines = [
    #     'dc-end',
    #     'HN-start',
    #     'start-kj',
    #     'dc-start',
    #     'dc-HN',
    #     'LN-dc',
    #     'HN-end',
    #     'kj-sa',
    #     'kj-HN',
    #     'kj-dc',
    # ]
    # lines = [
    #     'fs-end',
    #     'he-DX',
    #     'fs-he',
    #     'start-DX',
    #     'pj-DX',
    #     'end-zg',
    #     'zg-sl',
    #     'zg-pj',
    #     'pj-he',
    #     'RW-he',
    #     'fs-DX',
    #     'pj-RW',
    #     'zg-RW',
    #     'start-pj',
    #     'he-WI',
    #     'zg-he',
    #     'pj-fs',
    #     'start-RW',
    # ]

    data = [line.strip().split('-') for line in lines]
    caves = set([c for con in data for c in con])
    caveDict = {c: findConnections(data, c) for c in caves}

    rules1 = [
        lambda caveLog, c: c not in caveLog,
        lambda _, c: c.isupper(),
    ]
    r1 = len(potentialCaves(caveDict, rules1, ['start']))
    print(r1)

    rules2 = [
        lambda caveLog, c: c not in caveLog,
        lambda _, c: c.isupper(),
        lambda caveLog, c: all([c != 'start', checkDoubleLowerCase(caveLog)])
    ]
    r2 = len(potentialCaves(caveDict, rules2, ['start']))
    print(r2)


def potentialCaves(caveDict, rules, caveLog):
    if caveLog[-1] == 'end':
        return [[caveLog]]

    nextCaves = [c for c in caveDict[caveLog[-1]] if checkCave(caveLog, rules, c)]
    return [log for c in nextCaves for log in potentialCaves(caveDict, rules, caveLog + [c])]


def checkCave(caveLog, rules, c):
    for rule in rules:
        if rule(caveLog, c):
            return True
    return False


def checkDoubleLowerCase(caveLog):
    lowerCases = [c for c in caveLog if c.islower()]
    return len(lowerCases) == len(set(lowerCases))


def findConnections(data, c):
    conn = []
    for i, j in data:
        if i == c:
            conn.append(j)
        elif j == c:
            conn.append(i)

    return conn


if __name__ == '__main__':
    challenge = 12
    source = fr'..\resources\day{challenge}.txt'
    main(source)
