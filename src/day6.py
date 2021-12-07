
def main(source):
    with open(source) as r:
        lines = r.readlines()

    # lines = ['16,1,2,0,4,2,7,1,2,14']

    crabs = [int(f) for f in lines[0].split(',')]

    def fuelAtPos(pos):
        return sum([abs(c - pos) for c in crabs])

    def fuelAtPos2(pos):
        return sum([sum(range(1, abs(c - pos) + 1)) for c in crabs])

    r1 = min([fuelAtPos(i) for i in range(len(crabs))])
    print(r1)

    r2 = min([fuelAtPos2(i) for i in range(len(crabs))])
    print(r2)


if __name__ == '__main__':
    challenge = 6
    source = fr'..\resources\day{challenge}.txt'
    main(source)
