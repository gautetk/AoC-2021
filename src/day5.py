
def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '0,9 -> 5,9',
    #     '8,0 -> 0,8',
    #     '9,4 -> 3,4',
    #     '2,2 -> 2,1',
    #     '7,0 -> 7,4',
    #     '6,4 -> 2,0',
    #     '0,9 -> 2,9',
    #     '3,4 -> 1,4',
    #     '0,0 -> 8,8',
    #     '5,5 -> 8,2',
    # ]

    vLines = [parseVentLine(ventString) for ventString in lines]

    r1 = calculateNumberOfHigVentLocations(vLines, 1)
    print(r1)

    r1 = calculateNumberOfHigVentLocations(vLines, 2)
    print(r1)


def calculateNumberOfHigVentLocations(vLines, part):
    ventMap = {}
    for vl in vLines:
        locations = findVentLocations(vl, part)
        ventMap = updateVentMap(locations, ventMap)

    return len([k for k, v in ventMap.items() if v > 1])


def updateVentMap(locations, vents):
    for l in locations:
        if l in vents:
            vents[l] += 1
        else:
            vents[l] = 1
    return vents


def findVentLocations(vl, part):
    x1, y1, x2, y2 = vl

    xRange = ventRange(x1, x2)
    yRange = ventRange(y1, y2)

    if x1 == x2:
        xRange = xRange * len(yRange)

    elif y1 == y2:
        yRange = yRange * len(xRange)

    else:
        if part == 1:
            return []

    return[(x, y) for x, y in zip(xRange, yRange)]


def ventRange(v1, v2):
    if v1 > v2:
        angle = -1
    else:
        angle = 1
    return [r for r in range(v1, v2 + angle, angle)]


def parseVentLine(ventString):
    return [int(l) for loc in ventString.split(' -> ') for l in loc.split(',')]


if __name__ == '__main__':
    challenge = 5
    source = fr'..\resources\day{challenge}.txt'
    main(source)
