d1 = {'a': 1, 'b': 2, 'c': 4}

print(d1.get('u', "UNKNOWN KEY"))


def longest(lst: list[str], k: int) -> str:
    if k > len(lst) or len(lst) == 0:
        return ""

    # list_ = []
    # for i in range(k):
    #     list_.append(lst[i:])

    return max(("".join(l) for l in zip(*(lst[i:] for i in range(k)))), key=len)


print(longest(["Life", "can", "be", "fun", "but", "not", "always"], 3))
