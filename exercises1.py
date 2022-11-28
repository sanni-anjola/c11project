def rotate(list_to_rotate: list[int], rotate_by: int) -> list[int]:
    rotate_by = rotate_by % len(list_to_rotate)
    return list_to_rotate[rotate_by:] + list_to_rotate[:rotate_by]


print(rotate([7, -3, 2, 4, 9], 3))


def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False
    stack = []
    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "]})":
            peeked = stack[-1]
            if (bracket == ")" and peeked == "(") or \
                    (bracket == "}" and peeked == "{") or \
                    (bracket == "]" and peeked == "["):
                stack.pop()
            else:
                return False
        else:
            return False
    return True


print(bracket_pair("{}({[]})"))






def histogram(word: str) -> dict[str, int]:
    import string
    abc = string.ascii_lowercase

    map_ = {}

    for char in abc:
        map_[char] = word.lower().count(char)
    return map_


print(histogram("Alabama is a town"))









