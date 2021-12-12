from functools import reduce
import copy

def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '2199943210',
    #     '3987894921',
    #     '9856789892',
    #     '8767896789',
    #     '9899965678',
    # ]

    depth = [[int(o) for o in line.strip()] for line in lines]
    depth = [[9] + r + [9] for r in depth]
    depth = [[9]*len(depth[0])] + depth + [[9]*len(depth[0])]

    riskLevels = [[riskLevel(depth, r, c) for c in range(len(depth[0]))] for r in range(len(depth))]
    r1 = reduce(lambda i, r: i + sum(r), riskLevels, 0)
    print(r1)

    lowLocs = [(r, c) for r in range(len(depth)) for c in range(len(depth[0])) if riskLevels[r][c]]

    basins = [basin(depth, set([init])) for init in lowLocs]
    basinsSizes = [len(b) for b in basins]
    basinsSizes.sort()

    r2 = reduce(lambda x, y: x * y, basinsSizes[-3:])
    print(r2)


def basin(depth, locs):
    oldLocs = copy.deepcopy(locs)
    for r, c in oldLocs:
        if depth[r - 1][c] != 9:
            locs.add((r - 1, c))
        if depth[r + 1][c] != 9:
            locs.add((r + 1, c))
        if depth[r][c - 1] != 9:
            locs.add((r, c - 1))
        if depth[r][c + 1] != 9:
            locs.add((r, c + 1))

    if len(oldLocs) < len(locs):
        locs = basin(depth, locs)

    return locs


def riskLevel(depth, r, c):
    if depth[r - 1][c] <= depth[r][c]:
        return 0
    if depth[r + 1][c] <= depth[r][c]:
        return 0
    if depth[r][c - 1] <= depth[r][c]:
        return 0
    if depth[r][c + 1] <= depth[r][c]:
        return 0
    return depth[r][c] + 1


if __name__ == '__main__':
    challenge = 9
    source = fr'..\resources\day{challenge}.txt'
    main(source)
