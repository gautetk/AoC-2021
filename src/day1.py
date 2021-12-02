

def main(source):
    with open(source) as r:
        lines = r.readlines()
    
    data = [int(l) for l in lines]

    r1 = part1(data)
    print(r1)

    data2 = [i + j + k for i, j, k in zip(data[:-2], data[1:-1], data[2:])]
    r2 = part1(data2)
    print(r2)


def part1(data):
    return len([True for i, j in zip(data[:-1], data[1:]) if i < j])


if __name__ == '__main__':
    challenge = 1
    source = fr'..\resources\day{challenge}.txt'
    main(source)