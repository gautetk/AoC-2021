from functools import reduce
from pprint import pp, pprint
import os
from collections import Counter
import copy


def main():
    with open('resources\day15.txt') as r:
        input = r.read()

    # input = '1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n1319128137\n1359912421\n3125421639\n1293138521\n2311944581'
    data = [[int(v) for v in line] for line in input.split('\n')]

    r1 = dijkstra(data)
    print(r1)

    data = [extendListTimes(l, 5) for l in data]
    data = [extend(l, i) for i in range(5) for l in data]

    r2 = dijkstra(data)
    print(r2)


def extend(l, i):
    return [(v + i - 1) % 9 + 1 for v in l]


def extendListTimes(l, n):
    newL = []
    for i in range(0, n):
        newL += [(v + i - 1) % 9 + 1 for v in l]

    return newL


def dijkstra(data):

    maxX = len(data[0])
    maxY = len(data)
    end = (maxX - 1, maxY - 1)
    chitons = {(i, j): data[j][i] for j in range(maxY) for i in range(maxX)}

    visited = set()
    lengths = {(0, 0): 0}

    for _ in range(10000000):
        current = min(lengths, key=lambda i: lengths[i])
        currentLength = lengths[current]
        if current == end:
            return lengths[current]

        visited.add(current)
        del lengths[current]

        for n in neighbors(current, visited):
            c = chitons.get(n)
            if c:
                d = currentLength + c
                if lengths.get(n, 9999999999) > d:
                    lengths[n] = d


def neighbors(n, visited):
    x, y = n
    posLoc = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]

    return [loc for loc in posLoc if loc not in visited]


if __name__ == '__main__':
    main()
