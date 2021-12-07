from functools import reduce


def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = ['16,1,2,0,4,2,7,1,2,14']

    crabs = [int(f) for f in lines[0].split(',')]

    r1 = min([fuelAtPos(pos, crabs) for pos in range(min(crabs), max(crabs))])
    print(r1)

    r2 = min([fuelAtPos2(pos, crabs) for pos in range(min(crabs), max(crabs))])
    print(r2)


def fuelAtPos(pos, crabs):
    return reduce(lambda agg, c: agg + abs(c - pos), crabs, 0)


def fuelAtPos2(pos, crabs):
    return reduce(lambda agg, c: agg + rangeSum(abs(c - pos)), crabs, 0)


def rangeSum(diff):
    return sum(range(1, diff + 1))


if __name__ == '__main__':
    challenge = 7
    source = fr'..\resources\day{challenge}.txt'
    main(source)
