def list_beautify(data):
    line_format = ', '.join([f'\u007B:>{len(str(v))}\u007D' for v in [max(y, key=lambda p: len(str(p))) for y in zip(*data)]])
    return "[[" + '],\n ['.join([line_format.format(*x) for x in data]) + "]]"


print(
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
)
assert (
    list_beautify([[1, 2, 10, 150], [10, 2, 1000, 2], [1, 120, 1, 1000]])
    == "[[ 1,   2,   10,  150],\n [10,   2, 1000,    2],\n [ 1, 120,    1, 1000]]"
)
assert list_beautify([[1, 10, 100, -1000]]) == "[[1, 10, 100, -1000]]"
assert (
    list_beautify([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1],\n [1, 1, 1, 1, 1]]"
)
assert (
    list_beautify([[1, 1, -1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
    == "[[1, 1, -1, 1, 1],\n [1, 1,  1, 1, 1],\n [1, 1,  1, 1, 1]]"
)


"""
def list_beautify(data: list[list[int]]) -> str:
    # your code here
    
    lens = [len(str(max(x, key=lambda x: len(str(x))))) for x in zip(*data)]
    
    return '[[' + '],\n ['.join(', '.join(f'{col:>{l}}' for col, l in zip(row, lens)) for row in data) + ']]'
"""

