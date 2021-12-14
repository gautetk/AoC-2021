from functools import reduce
from pprint import pp, pprint
import os
from collections import Counter
import copy


def main():
    with open('resources\day14.txt') as r:
        input = r.read()

    # input = 'NNCB\n\nCH -> B\nHH -> N\nCB -> H\nNH -> C\nHB -> C\nHC -> B\nHN -> C\nNN -> C\nBH -> H\nNC -> B\nNB -> B\nBN -> B\nBB -> N\nBC -> B\nCC -> N\nCN -> C'

    rules, pairs, lastChar = parse(input)

    r1_pairs = runSteps(pairs, rules, 10)
    r1 = maxMinChar(r1_pairs, lastChar)
    print(r1)

    r2_pairs = runSteps(pairs, rules, 40)
    r2 = maxMinChar(r2_pairs, lastChar)
    print(r2)


def maxMinChar(pairs, lastChar):
    chars = reduce(lambda d, kv: addTo(d, kv[0][0], kv[1]), pairs.items(), {})
    chars[lastChar] += 1
    return max(chars.values()) - min(chars.values())


def addTo(d, k, v):
    d[k] = d.get(k, 0) + v
    return d


def runSteps(pairs, rules, n):
    for _ in range(n):
        newPairs = {}
        for k, v in pairs.items():
            r1, r2 = rules[k]
            newPairs[r1] = newPairs.get(r1, 0) + v
            newPairs[r2] = newPairs.get(r2, 0) + v
        pairs = newPairs

    return pairs


def parse(input):
    template, rules = [group.split('\n') for group in input.split('\n\n')]
    template = template[0]

    rules = {rule.split(' -> ')[0]: parseRule(rule) for rule in rules}

    pairs = {''.join(pair): template.count(''.join(pair)) for pair in zip(template[:-1], template[1:])}
    return rules, pairs, template[-1]


def parseRule(rule):
    r, v = rule.split(' -> ')
    return [r[0] + v, v + r[1]]


if __name__ == '__main__':
    main()
