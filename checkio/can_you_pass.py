"""my"""
def can_pass(matrix, first, second):
    first_value = matrix[first[0]][first[1]]
    used_cells = []
    road_cells = [first]
    closer_cells = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    current_cell = first
    while road_cells:
        road_cells.remove(current_cell)
        for closer_cell in closer_cells:
            closer_cell = (current_cell[0] + closer_cell[0], current_cell[1] + closer_cell[1])
            try:
                if closer_cell == second:
                    return True
                closer_cell_value = matrix[closer_cell[0]][closer_cell[1]]
                if closer_cell_value == first_value:
                    if closer_cell not in used_cells:
                        road_cells.append(closer_cell)
                    used_cells.append(closer_cell)
            except:
                pass
        if road_cells:
            current_cell = road_cells[-1]
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'


"""1"""
# from itertools import chain, product, starmap
#
# def can_pass(matrix, first, second):
#     digit = matrix[first[0]][first[1]]
#     cells = product(range(len(matrix)), range(len(matrix[0])))
#     living = {(y, x) for y, x in cells if matrix[y][x] == digit}
#
#     neighbors = lambda y, x: ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
#     tips = {first}
#     while tips:
#         tips = set(chain.from_iterable(starmap(neighbors, tips))) & living
#         living -= tips
#         if second in tips: return True
#
#     return False


"""2"""
# def can_pass(matrix, first, second):
#     x, y = first
#     rh, rw = range(len(matrix)), range(len(matrix[0]))
#     cells = {(i, j) for i in rh for j in rw
#              if matrix[i][j] == matrix[x][y]}
#     stack, visited = [first], set()
#     while stack:
#         x, y = stack.pop()
#         if (x, y) == second: return True
#         visited |= {(x, y)}
#         neighbors = {(x+1, y), (x-1, y), (x, y+1), (x, y-1)}
#         stack += list(neighbors & cells - visited)
#     return False


"""3"""
# def can_pass(m, source, target):
#     rows, cols = len(m), len(m[0])
#
#     def neighbours(i, j):
#         return {(x, y) for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
#             if 0 <= x < rows and 0 <= y < cols and m[x][y] == m[i][j]}
#
#     cc, last = set(), {source}
#     while last:
#         last.update(*map(lambda c: neighbours(*c), last))
#         last = last - cc
#         cc |= last
#
#     return target in cc


"""4"""
# h=lambda d,a,b:a==b or any((h(d-{i},i,b)for i in{(a[0]+x,a[1]+y) for x,y in[(1,0),(-1,0),(0,1),(0,-1)]}&d))
# can_pass=lambda d,a,b:h({divmod(i,len(d[0]))for i,x in enumerate(sum(d,()))if x==d[b[0]][b[1]]},a,b)


"""5"""
# def can_pass(matrix, first, second):
#     reach = [first]
#     for i,j in reach:
#         reach += [(I,J) for I,row in enumerate(matrix) for J,a in enumerate(row)
#                   if abs(i-I)+abs(j-J)<2 and a==matrix[i][j] and (I,J) not in reach]
#     return second in reach


"""
You are given a matrix (2D array) and the coordinates (row and column) of two cells 
with the same value. The matrix consists of digits. You may move to neighbouring 
cells either horizontally or vertically provided the values of the origin and destination 
cells are equal. You should determine if a path exists between two given cells.

A matrix is represented as a tuple of tuples with digits. Coordinates are represented 
as a tuple with two numbers: row and column. The result should be any value which can 
be converted into a boolean. If a path exists, then return True. Return False if there 
is none.
"""
