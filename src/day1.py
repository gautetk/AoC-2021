

def main(source):
    with open(source) as r:
        lines = r.readlines()
    
    data = [int(l) for l in lines]

    r1 = sum([checkIncrease(j - i) for i, j in zip(data[:-1], data[1:])])
    print(r1)

    data2 = [i + j + k for i, j, k in zip(data[:-2], data[1:-1], data[2:])]
    r2 = sum([checkIncrease(j - i) for i, j in zip(data2[:-1], data2[1:])])
    print(r2)


def checkIncrease(change):
    if change > 0:
        return 1
    return 0


if __name__ == '__main__':
    challenge = 1
    source = fr'..\resources\day{challenge}.txt'
    main(source)