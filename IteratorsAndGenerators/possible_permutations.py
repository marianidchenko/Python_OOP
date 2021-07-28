from itertools import permutations


def possible_permutations(items: list):
    result = permutations(items)
    return (list(p) for p in result)


[print(n) for n in possible_permutations([1, 2, 3])]