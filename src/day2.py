import math

def main(source):
    with open(source) as r:
        lines = r.readlines()
    
    # lines = [
    #     'forward 5',
    #     'down 5',
    #     'forward 8',
    #     'up 3',
    #     'down 8',
    #     'forward 2',
    # ]

    data = [l.split(' ') for l in lines]

    part1fn = {
        'forward': lambda loc, v: (loc[0] + v, loc[1]),
        'down': lambda loc, v: (loc[0], loc[1] + v),
        'up': lambda loc, v: (loc[0], loc[1] - v),
    }

    loc = (0, 0)
    for comand, v in data:
        loc= part1fn[comand](loc, int(v))
    
    r1 = math.prod(loc)
    print(r1)


    part2fn = {
        'forward': lambda h, d, a, v: (h + v, d + a * v, a),
        'down': lambda h, d, a, v: (h, d, a + v),
        'up': lambda h, d, a, v: (h, d, a - v),
    }

    h = 0
    d = 0
    a = 0
    for comand, v in data:
        h, d, a = part2fn[comand](h, d, a, int(v))
    
    r2 = h * d
    print(r2)


if __name__ == '__main__':
    challenge = 2
    source = fr'..\resources\day{challenge}.txt'
    main(source)