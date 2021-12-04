import math


def main(source):
    with open(source) as r:
        lines = r.readlines()

    lines = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

    gammaRate = ''.join([mostCommon(l) for l in zip(*lines)])
    epsilonRate = ''.join([str(abs(int(l)-1)) for l in gammaRate])

    r1 = int(gammaRate, base=2) * int(epsilonRate, base=2)
    print(r1)

    
    # print(r2)


def mostCommon(l):
    return max(set(l), key=l.count)


if __name__ == '__main__':
    challenge = 3
    source = fr'..\resources\day{challenge}.txt'
    main(source)
