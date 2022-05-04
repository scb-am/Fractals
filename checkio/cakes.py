def get_line(p_1, p_2):
    if p_1[0] == p_2[0]:
        return f"-{p_1[0]}"
    if p_1[1] == p_2[1]:
        return f"{p_1[1]}-"
    x = (p_2[1] - p_1[1]) / (p_2[0] - p_1[0])
    c = x * (-p_1[0]) + p_1[1]
    return f"{x}-{c}"


def checkio(cakes):
    lines = {}
    while cakes:
        p_1 = cakes.pop()
        for p_2 in cakes:
            line = get_line(p_1, p_2)
            lines.setdefault(line, 0)
            lines[line] += 1
    return len([x for x in lines.values() if x >= 3])


if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

