def identify_block(numbers):
    """
    grid(4x4):
    +--+--+--+--+
    |1 |2 |3 |4 |
    +--+--+--+--+
    |5 |6 |7 |8 |
    +--+--+--+--+
    |9 |10|11|12|
    +--+--+--+--+
    |13|14|15|16|
    +--+--+--+--+


    blocks(7 kinds):

    'I'  'J'  'L'  'O'  'S'  'T'  'Z'

     *    *   *    **    **  ***  **
     *    *   *    **   **    *    **
     *   **   **
     *

    """

    blocks = {
        '****': 'I',
        '*  ,***': 'J',
        '***,*  ': 'L',
        '**,**': 'O',
        ' **,** ': 'S',
        '***, * ': 'T',
        '** , **': 'Z',
    }


    grid = [[x for x in range(4 * y - 3, 4 * y + 1)] for y in range(1, 5)]
    numbers_grid = [['*' if x in numbers else ' ' for x in y] for y in grid]
    for _ in range(2):
        if ''.join([' ' if x == [' '] * len(numbers_grid[0]) else '*' for x in numbers_grid]).strip().count(' '):
            return None
        while [' '] * len(numbers_grid[0]) in numbers_grid:
            numbers_grid.remove([' '] * len(numbers_grid[0]))
        numbers_grid = [[x[i] for x in numbers_grid[::-1]] for i in range(len(numbers_grid[0]))]
    for _ in range(4):
        try:
            return blocks[",".join(map("".join, numbers_grid))]
        except KeyError:
            numbers_grid = [[x[i] for x in numbers_grid[::-1]] for i in range(len(numbers_grid[0]))]
    return None



print(identify_block({5,8,9,12}))



# table = {
#     ((0, 0), (1, 0), (2, 0), (3, 0))  : 'I',
#     ((0, 0), (1, 0), (2, -1), (2, 0)) : 'J',
#     ((0, 0), (1, 0), (2, 0), (2, 1))  : 'L',
#     ((0, 0), (0, 1), (1, 0), (1, 1))  : 'O',
#     ((0, 0), (0, 1), (1, -1), (1, 0)) : 'S',
#     ((0, 0), (0, 1), (0, 2), (1, 1))  : 'T',
#     ((0, 0), (0, 1), (1, 1), (1, 2))  : 'Z',
# }
# rotate_index = (0, 13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3, 16, 12, 8, 4)
#
# def identify_block(numbers):
#     def normalize(p2, p1):
#         y1, x1 = divmod(p1 - 1, 4)
#         y2, x2 = divmod(p2 - 1, 4)
#         return (y2 - y1, x2 - x1)
#
#     for _ in range(4):
#         cnum = tuple(sorted(normalize(x, min(numbers)) for x in numbers))
#         if cnum in table: return table[cnum]
#         numbers = [rotate_index[x] for x in numbers] # rotate numbers
#     return None
#
#
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert identify_block({10, 13, 14, 15}) == 'T', 'T'
#     assert identify_block({1, 5, 9, 6}) == 'T', 'T'
#     assert identify_block({2, 3, 7, 11}) == 'L', 'L'
#     assert identify_block({4, 8, 12, 16}) == 'I', 'I'
#     assert identify_block({3, 1, 5, 8}) == None, 'None'
#     print('"Run" is good. How is "Check"?')




# import numpy as np
# from itertools import product
#
# BLOCKS = {
#     'T': {(0, 0), (0, 1), (0, 2), (1, 1)},
#     'I': {(0, 0), (1, 0), (2, 0), (3, 0)},
#     'O': {(0, 0), (0, 1), (1, 0), (1, 1)},
#     'L': {(0, 0), (1, 0), (2, 0), (2, 1)},
#     'J': {(0, 1), (1, 1), (2, 0), (2, 1)},
#     'S': {(0, 1), (0, 2), (1, 0), (1, 1)},
#     'Z': {(0, 0), (0, 1), (1, 1), (1, 2)},
# }
#
#
# def identify_block(tile):
#     grid = np.arange(1, 17).reshape((4, 4))
#     for (name, coords), r in product(BLOCKS.items(), range(4)):
#         grid = np.rot90(grid)
#         tile_coord = {(x, y) for x, y in product(range(4), repeat=2) if grid[x, y] in tile}
#         if len(set((b[0] - t[0], b[1] - t[1]) for b, t in zip(sorted(coords), sorted(tile_coord)))) == 1:
#             return name