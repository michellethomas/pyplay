#!/usr/bin/env python
from collections import defaultdict


def main():
    nums = range(11)

    results = []

    for i  in nums:
        for num in nums:
            results.append(i+num)
    print results

    counter = defaultdict(int)
    for j in results:
        counter[j] +=1

    tups = counter.items()
    tups.sort(key=lambda n: n[1], reverse = True)

    print tups


if __name__ == '__main__':
    main()
