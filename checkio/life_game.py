class LifeGame:
    def __init__(self):
        self.map = {}
        self.alive_cells_count = 0

    def _get_cell_status(self, cell, *args):
        return cell.status

    def _get_cell_neighbours(self, cell, *args):
        return cell.get_alive_neighbours()

    def _get_next_status(self, cell, *args):
        return cell.next_status()

    def _set_alive_neighbours(self, cell, *args):
        return cell.set_alive_neighbours()

    def _calc_alive_cells_count(self, cell, *args):
        self.alive_cells_count += cell.status

    def _iterate_map(self, fn):
        for i, row in self.map.items():
            for j, cell in row.items():
                fn(cell, i, j)

    def _init_cell_neighbours(self, cell, i, j):
        for char in (
                (1, 1), (1, 0), (1, -1),
                (0, 1), (0, -1),
                (-1, 1), (-1, 0), (-1, -1),
        ):
            try:
                neighbour = self.map[i + char[0]][j + char[1]]
                if neighbour not in cell.neighbours:
                    cell.add_neighbour(neighbour)
            except KeyError:
                pass

    def init_game(self, map):
        for i, row in enumerate(map):
            for j, cell in enumerate(row):
                cell = Cell(cell)
                self.map.setdefault(i, {})
                self.map[i][j] = cell
        self._iterate_map(self._init_cell_neighbours)

    def show_map(self):
        map = []
        for i, row in self.map.items():
            map_row = []
            for j, cell in row.items():
                map_row.append(cell.status)
            map.append(map_row)
        return map

    def show_neighbours_map(self):
        self._iterate_map(self._get_cell_neighbours)

    def show_next_day_map(self):
        sorted_v_keys = sorted(self.map.keys())
        min_v_key = sorted_v_keys[0]
        max_v_key = sorted_v_keys[-1]

        sorted_h_keys = sorted(self.map[0].keys())
        min_h_key = sorted_h_keys[0]
        max_h_key = sorted_h_keys[-1]

        if any(self.map[min_v_key].values()):
            for i in sorted(self.map[min_v_key].keys()):
                self.map.setdefault((min_v_key - 1), {})
                self.map[min_v_key - 1][i] = Cell(0)
            for i in sorted(self.map[min_v_key].keys()):
                cell = self.map[min_v_key - 1][i]
                self._init_cell_neighbours(cell, min_v_key - 1, i)
                cell = self.map[min_v_key][i]
                self._init_cell_neighbours(cell, min_v_key, i)

        if any(self.map[max_v_key].values()):
            for i in sorted(self.map[max_v_key].keys()):
                self.map.setdefault((max_v_key + 1), {})
                self.map[max_v_key + 1][i] = Cell(0)
            for i in sorted(self.map[max_v_key].keys()):
                cell = self.map[max_v_key + 1][i]
                self._init_cell_neighbours(cell, max_v_key + 1, i)
                cell = self.map[max_v_key][i]
                self._init_cell_neighbours(cell, max_v_key, i)

        if any([x[min_h_key] for x in self.map.values()]):
            for i in self.map.keys():
                self.map[i][min_h_key - 1] = Cell(0)
            for i in self.map.keys():
                cell = self.map[i][min_h_key - 1]
                self._init_cell_neighbours(cell, i, min_h_key - 1)
                cell = self.map[i][min_h_key]
                self._init_cell_neighbours(cell, i, min_h_key)

        if any([x[max_h_key] for x in self.map.values()]):
            for i in self.map.keys():
                self.map[i][max_h_key + 1] = Cell(0)
            for i in self.map.keys():
                cell = self.map[i][max_h_key + 1]
                self._init_cell_neighbours(cell, i, max_h_key + 1)
                cell = self.map[i][max_h_key]
                self._init_cell_neighbours(cell, i, max_h_key)

        self._iterate_map(self._set_alive_neighbours)
        self._iterate_map(self._get_next_status)

    def get_alive_cells_count(self):
        self.alive_cells_count = 0
        self._iterate_map(self._calc_alive_cells_count)
        return self.alive_cells_count


class Cell:
    def __init__(self, status):
        self.status = status
        self.alive_neighbours = 0
        self.neighbours = []

    def __bool__(self):
        return self.status == 1

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def get_alive_neighbours(self):
        return sum(x.status for x in self.neighbours)

    def set_alive_neighbours(self):
        self.alive_neighbours = self.get_alive_neighbours()

    def next_status(self):
        if self.status and self.alive_neighbours in (2, 3) or \
                not self.status and self.alive_neighbours == 3:
            self.status = 1
        else:
            self.status = 0
        return self.status


def life_counter(map: tuple, tick_n: int):
    life_game = LifeGame()
    life_game.init_game(map)

    # print('\n')
    # for row in life_game.show_map():
    #     print(row)

    for i in range(tick_n):
        life_game.show_next_day_map()
        # print(f"\n{i}")
        # for row in life_game.show_map():
        #     print(row)
    return life_game.get_alive_cells_count()




# from collections import Counter
# from itertools import chain, product
#
# def life_counter(state, ticks):
#     cells = product(range(len(state)), range(len(state[0])))
#     lives = {(y, x) for y, x in cells if state[y][x] == 1}
#
#     neighbors = lambda c: set(product(*[(z - 1, z, z + 1) for z in c])) - {c}
#     for t in range(ticks):
#         freqs = Counter(chain.from_iterable(map(neighbors, lives)))
#         lives = {c for c in freqs if freqs[c] in (3 - (c in lives), 3)}
#
#     return len(lives)




# from collections import Counter
# from functools import lru_cache
# from itertools import chain, product
#
# capacities = {True: (2, 3), False: (3,)}
#
# @lru_cache(maxsize=256)
# def neighbors(c):
#     return set(product(*[(z - 1, z, z + 1) for z in c])) - {c}
#
# def life_counter(state, ticks):
#     cells = product(range(len(state)), range(len(state[0])))
#     lives = {(y, x) for y, x in cells if state[y][x]}
#
#     for t in range(ticks):
#         freqs = Counter(chain.from_iterable(map(neighbors, lives)))
#         lives = {c for c, f in freqs.items() if f in capacities[c in lives]}
#
#     return len(lives)




# def life_counter(s,t,E=enumerate):
#  L={(i,j)for i,r in E(s)for j,c in E(r)if c}
#  for _ in[0]*t:L={z for z,n in __import__("collections").Counter((a+c,b+d)for
# a,b in L for c in{-1,0,1}for d in{-1,0,1}).items()if(z in L)+4>n>2}
#  return len(L)




# from collections import Counter
# from itertools import chain
#
#
# def life_counter(state, tick_n):
#     l = {(y, x) for y in range(len(state))
#          for x in range(len(state[0])) if state[y][x]}
#     for _ in range(tick_n):
#         l = {c for c, f in Counter(chain.from_iterable(
#             ((y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1),
#              (y, x + 1), (y + 1, x - 1), (y + 1, x), (y + 1, x + 1))
#             for y, x in l)).items() if f in ((3,), (2, 3))[c in l]}
#     return len(l)




# from collections import Counter
#
# def life_counter(state, tick_n):
#     live_cells = {(i, j) for j, row in enumerate(state)
#                          for i, cell in enumerate(row) if cell}
#     neighbours = Counter()
#     for _ in range(tick_n):
#         neighbours.clear()
#         for i, j in live_cells:
#             for x in i - 1, i, i + 1:
#                 for y in j - 1, j, j + 1:
#                     neighbours[(x, y)] += 1
#         live_cells = {cell for cell, count in neighbours.items()
#                       if count == 3 or count == 4 and cell in live_cells} #live +1 for itself
#     return len(live_cells)




# def life_counter(state, tick_n):
#     live = {(x, y) for y in range(len(state)) for x in range(len(state[0])) if state[y][x]}
#
#     for _ in range(tick_n):
#
#         next_live = set()
#         born_candidate = set()
#
#         # Any live cell with two or three live neighbours lives on to the next generation.
#         for x, y in live:
#             neighbor = {(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0}
#             if len(neighbor & live) in (2, 3): next_live |= {(x, y)}
#             born_candidate |= neighbor - live
#
#         # Any dead cell with exactly three live neighbours becomes a live cell.
#         for x, y in born_candidate:
#             neighbor = {(x + i, y + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not i == j == 0}
#             if len(neighbor & live) == 3: next_live |= {(x, y)}
#
#         live = next_live
#
#     return len(live)




# def life_counter(state, tick_n):
#     # Convert the initial state to a set of tuples of coordinates of alive cells.
#     alive = set((r, c) for r, row in enumerate(state)
#                 for c, cell in enumerate(row) if cell)
#     # Convenience varaible: all possible offsets to nearby cells, including itself.
#     square = [(r, c) for r in [-1, 0, 1] for c in [-1, 0, 1]]
#
#     # Returns a set of all the neighbours of currently alive cells.
#     def extension(alive):
#         return set((row + r, col + c) for row, col in alive for r, c in square)
#
#     def is_alive(row, col, alive):
#         # Note that for code simplicity we count a cell as its own neigbour here and
#         # adjust the condition for an alive cell to remain alive correspondingly.
#         # when checking the number of alive neighbours of an alive cells.
#         n_neighbours = sum((row + r, col + c) in alive for r, c in square)
#         return n_neighbours in [3, 4] if (row, col) in alive else n_neighbours == 3
#
#     for tick in range(tick_n):
#         alive = set((r, c) for r, c in extension(alive) if is_alive(r, c, alive))
#
#     return len(alive)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"

    # life_counter(
    #     (
    #         (0, 1, 0),
    #         (0, 0, 1),
    #         (1, 1, 1),
    #     ), 999,
    # )

    # life_counter(
    #     (
    #         (0,1,0,0,0,0,1,0),
    #         (1,0,0,0,0,0,0,1),
    #         (1,1,1,0,0,1,1,1),
    #     ), 999,
    # )
