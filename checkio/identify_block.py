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