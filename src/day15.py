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

    data2 = [extendListTimes(l, 5) for l in data]
    data3 = [extend(l, i) for i in range(5) for l in data2]

    r2 = dijkstra(data3)
    print(r2)

def extend(l, i):
    return [(v + i - 1)%9 + 1 for v in l]

def extendListTimes(l, n):
    newL = []
    for i in range(0, n):
        newL += [(v + i - 1)%9 + 1 for v in l]

    return newL


def dijkstra(data):

    maxX = len(data[0])
    maxY = len(data)
    chitons = {(i, j): data[j][i] for j in range(maxY) for i in range(maxX)}

    unvisited = set([(i,j) for j in range(maxY) for i in range(maxX)])
    lengths = {(0, 0): 0}

    for _ in range(1000000):
        current = min(lengths, key=lambda i: checkCurrent(i, lengths[i], unvisited))
        if current == (maxX - 1, maxY - 1):
            return lengths[current]
        unvisited.remove(current)

        neighboors = findNeighboors(current, unvisited)
        for n in neighboors:
            d = lengths[current] + chitons[n]
            if lengths.get(n, 9999999999) > d:
                lengths[n] = d



def checkCurrent(i, n, unvisited):
    if i in unvisited:
        return n
    return 99999999999


def findNeighboors(n, unvisited):
    x, y = n
    posLoc = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]
    
    return [loc for loc in posLoc if loc in unvisited]



if __name__ == '__main__':
    main()
