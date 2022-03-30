H_BOARD = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
V_BOARD = ['1', '2', '3', '4', '5', '6', '7', '8']


class Knight:
    def __init__(self, start, moves):
        self.start = start
        self.moves = moves
        self.cells = []

    def _move(self, h_cell, v_cell, h_direction, v_direction):
        if 0 <= h_cell+h_direction <= 7 and 0 <= v_cell+v_direction <= 7:
            return f"{H_BOARD[h_cell+h_direction]}{V_BOARD[v_cell+v_direction]}"
        else:
            return None

    def _get_position(self, position):
        return H_BOARD.index(position[0]), V_BOARD.index(position[1])

    def _get_moves(self, cell):
        moves = [self._move(*self._get_position(cell), x, y) for x, y in [
                    (-2, 1), (-2, -1), (2, 1), (2, -1),
                    (-1, 2), (-1, -2), (1, 2), (1, -2),
                ]]
        return [x for x in moves if x]

    def get_cells(self):
        for _ in range(self.moves):
            if self.cells:
                new_cells = []
                for cell in self.cells:
                    new_cells.extend(self._get_moves(cell))
                self.cells.extend(new_cells)
            else:
                self.cells.extend(self._get_moves(self.start))
        return sorted(list(set(self.cells)))


def chess_knight(start, moves):
    knight = Knight(start, moves)
    return knight.get_cells()

if __name__ == '__main__':
    print("Example:")
    print('chess_knight - ', chess_knight('a1', 1))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")
