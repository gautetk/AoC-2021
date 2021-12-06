
def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = ['3,4,3,1,2']

    intiFish = [int(f) for f in lines[0].split(',')]
    fishInStates = [intiFish.count(f) for f in range(9)]

    r1 = sum(calculateFisInStatesAfterNDays(fishInStates, 80))
    print(r1)

    r2 = sum(calculateFisInStatesAfterNDays(fishInStates, 256))
    print(r2)


def calculateFisInStatesAfterNDays(fishInStates, days):
    for _ in range(days):
        fishInStates = updateState(fishInStates)
    return fishInStates


def updateState(fs):
    fs[7] += fs[0]
    return fs[1:] + [fs[0]]


if __name__ == '__main__':
    challenge = 6
    source = fr'..\resources\day{challenge}.txt'
    main(source)
