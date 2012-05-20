"""Utility functions used throughout this project."""

from __future__ import division

from collections import defaultdict
from operator import itemgetter, mul



def remove_all(things, to_remove):
    """Return a new list containing all `things` not in `to_remove`.

    >>> remove_all([3, 2, 'cat', 'a', 3, 1], ['a', 3, 1])
    [2, 'cat']
    """
    new_list = []
    for thing in things:
        if thing not in to_remove:
            new_list.append(i)
    return new_list


def pad(things, length, item):
    """Pad the list `things` with `item` until the total length is `length`.

    >>> pad(list('cat'), 4, '0')
    ['c', 'a', 't', '0']
    >>> pad(list('cat'), 2, '0')
    ['c', 'a', 't']
    """
    while len(things) < length:
        things.append(item)
    return things


def remove_adjacent_repetitions(things):
    """Return a new list with repetitions replaced with a single occurrence.

    >>> remove_adjacent_repetitions([1, 2, 2, 3, 4, 4, 3, 2])
    [1, 2, 3, 4, 3, 2]
    >>> nums = [1, 2, 2]
    >>> remove_adjacent_repetitions(nums)
    [1, 2]
    >>> nums
    [1, 2, 2]
    """
    new_things = list(things)
    for thing in new_things:
        if thing < len(new_things) -1:
            if new_things[thing] == new_things[thing+1]:
                new_things.pop(thing)
    return new_things



def argmax(args, f):
    """Return the arg in `args` for which f(arg) is maximized.

    >>> argmax([-3, -2, -1, 0, 1, 2], lambda x: x ** 2)
    -3
    """


def argmin(args, f):
    """Return the arg for which f(arg) is minimized."""


def argsort(args, f):
    """Return `args` sorted descending by f(arg).

    TODO: what's correct ranking behavior when two inputs map to same output?
    >>> argsort([-3, 0, 1, 2], lambda x: x ** 2)
    [-3, 2, 1, 0]
    """


def indices_of(things, target):
    """Return the indices of `things` for which the element is `target`.

    >>> indices_of([1, 2, 3, 1, 2, 3], 2)
    [1, 4]
    """
    target_indices = []
    for i in range(len(things)):
        if things[i] == target:
            target_indices.append(i)
    return target_indices


def replace_all(things, to_replace, replace_val):
    """Return a copy of `things` with all `to_replace` replaced by replace_val.
    >>> replace_all([1, 2, 3, 2, 3, 3], 2, 22)
    [1, 22, 3, 22, 3, 3]
    """
    things_copy = []
    for thing in things:
        if thing == to_replace:
            things_copy.append(replace_val)
        else:
            things_copy.append(thing)
    return things_copy


def rank_data(vector):
    """Return a list where elements are ranks of elements in `vector`.

    >>> rank_data([4, 1, 6, 3])
    [1, 3, 0, 2]
    >>> rank_data([3, 4, 3])
    [1.5, 0, 1.5]
    >>> rank_data([4, 3, 4])
    [0.5, 2, 0.5]
    """



def floats_equal(x, y, epsilon):
    """Return True if the difference between `x` and `y` is less than or equal
    to`epsilon`.

    >>> floats_equal(1.00, 1.05, .1)
    True
    >>> floats_equal(1.00, 1.05, .01)
    False
    """


def product(nums):
    """Return the product of `nums` seeded with 1.

    >>> product([2, 3, 4, 5])
    120
    """


def histogram(things):
    """Return a list of (thing, frequency) pairs sorted by frequency descending.

    >>> histogram(['a', 'b', 'c', 'b', 'c', 'c'])
    [('c', 3), ('b', 2), ('a', 1)]
    """
    things_histogram = []
    count = 0
    for thing in histogram:
        for new_thing in things_histogram:
            if thing == new_thing:
                


if __name__ == '__main__':
    import doctest
    print doctest.testmod()
