def sort_by_removing(values: list) -> list:
    res_values = []
    max_val = values[0] if len(values) else 0
    for value in values:
        if value >= max_val:
            max_val = value
            res_values.append(value)
    return res_values


"""
from itertools import accumulate

def sort_by_removing(values):
    return [x for x, m in zip(values, accumulate(values, max)) if x >= m]
"""


"""
def sort_by_removing(values: list) -> list:
    prev_value = -1000
    return [prev_value := v for v in values if prev_value <= v]
"""


"""
sort_by_removing = lambda items: [v for i, v in enumerate(items) if max(items[:i+1]) == v]
"""


"""
sort_by_removing=lambda v:[p := x for x in v if (p:=(p if 'p' in vars() else v[0])) <= x]
"""


"""
import math
def sort_by_removing(values: list) -> list:
    '''
    Also known as Stalin sort.
    ''' 
    return [i for idx, i in enumerate(values) if i >= max(values[:idx], default=-math.inf)]
"""


"""
def sort_by_removing(values: list) -> list:
    # your code here
    mv = 0
    return [ mv for m in values if mv == m or mv < (mv:=max(mv,m))  ]
"""


"""
def sort_by_removing(values: list) -> list:
    return [prev := v for v in values if 'prev' not in locals() or v >= prev]
"""


if __name__ == '__main__':
    print("Example:")
    print(sort_by_removing([3, 5, 2, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_removing([3, 5, 2, 6]) == [3, 5, 6]
    assert sort_by_removing([7, 6, 5, 4, 3, 2, 1]) == [7]
    assert sort_by_removing([3, 3, 3, 3]) == [3, 3, 3, 3]
    assert sort_by_removing([5, 6, 7, 0, 7, 0, 10]) == [5, 6, 7, 7, 10]
    assert sort_by_removing([1, 5, 2, 3, 4, 7, 8]) == [1, 5, 7, 8]
    assert sort_by_removing([1, 7, 2, 3, 4, 5]) == [1, 7]
    assert sort_by_removing([]) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
