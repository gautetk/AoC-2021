import math


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = [
    #     '00100',
    #     '11110',
    #     '10110',
    #     '10111',
    #     '10101',
    #     '01111',
    #     '00111',
    #     '11100',
    #     '10000',
    #     '11001',
    #     '00010',
    #     '01010',
    # ]

    gr = ''.join([mostCommon(l) for l in zip(*lines)])
    er = ''.join([str(abs(int(l)-1)) for l in gr])

    r1 = int(gr, base=2) * int(er, base=2)
    print(r1)

    ogr = oxygenRating(lines)
    csr = co2Scrubber(lines)
    r2 = int(ogr, base=2) * int(csr, base=2)
    print(r2)


def oxygenRating(data):
    for i in range(len(data[0])):
        col = [list(c) for c in zip(*data)][i]
        mc = mostCommon(col)
        data = [r for r in data if r[i] == mc]
        if len(data) == 1:
            return data[0]


def co2Scrubber(data):
    for i in range(len(data[0])):
        col = [list(c) for c in zip(*data)][i]
        mc = mostCommon(col)
        lc = str(abs(int(mc) - 1))
        data = [r for r in data if r[i] == lc]
        if len(data) == 1:
            return data[0]


def mostCommon(l):
    if l.count('1') >= l.count('0'):
        return '1'
    return '0'


if __name__ == '__main__':
    challenge = 3
    source = fr'..\resources\day{challenge}.txt'
    main(source)
