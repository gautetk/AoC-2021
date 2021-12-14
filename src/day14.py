from functools import reduce
from pprint import pp, pprint
import os
from collections import Counter
import copy


def main(source):
    with open(source) as r:
        input = r.read()

    # input = 'NNCB\n\nCH -> B\nHH -> N\nCB -> H\nNH -> C\nHB -> C\nHC -> B\nHN -> C\nNN -> C\nBH -> H\nNC -> B\nNB -> B\nBN -> B\nBB -> N\nBC -> B\nCC -> N\nCN -> C'

    template, rules = [group.split('\n') for group in input.split('\n\n')]
    template = template[0]

    rules = {rule.split(' -> ')[0]: parseRule(rule) for rule in rules}

    pairs = {pair: template.count(pair) for pair in rules.keys()}

    r1_pairs = runSteps(pairs, rules, 10)
    r1 = maxMinChar(r1_pairs, set(''.join(rules.keys())), template[-1])
    print(r1)

    r2_pairs = runSteps(pairs, rules, 40)
    r2 = maxMinChar(r2_pairs, set(''.join(rules.keys())), template[-1])
    print(r2)


def maxMinChar(pairs, possibleChar, lastChar):
    chars = {s: reduce(lambda i, kv: i + kv[0][0].count(s) * kv[1], pairs.items(), 0) for s in possibleChar}
    chars[lastChar] += 1
    return max(chars.values()) - min(chars.values())


def runSteps(pairs, rules, n):
    for _ in range(n):
        tmpPairs = copy.deepcopy(pairs)
        for k, v in tmpPairs.items():
            r1, r2 = rules[k]
            pairs[k] -= v
            pairs[r1] += v
            pairs[r2] += v

    return pairs


def parseRule(rule):
    r, v = rule.split(' -> ')
    return [r[0] + v, v + r[1]]


if __name__ == '__main__':
    challenge = 14
    source = fr'resources\day{challenge}.txt'
    main(source)
