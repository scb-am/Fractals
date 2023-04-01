import string


class Cell:
    def __init__(self, name):
        self.name = name
        self.N = None
        self.NE = None
        self.SE = None
        self.S = None
        self.SW = None
        self.NW = None

    def __str__(self):
        N = self.N.name if self.N else '  '
        NE = self.NE.name if self.NE else '  '
        SE = self.SE.name if self.SE else '  '
        S = self.S.name if self.S else '  '
        SW = self.SW.name if self.SW else '  '
        NW = self.NW.name if self.NW else '  '
        rows = []
        rows.append("    __")
        rows.append(f" __/{N}\\__")
        rows.append(f"/{NW}\\__/{NE}\\")
        rows.append(f"\__/{self.name}\\__/")
        rows.append(f"/{SW}\\__/{SE}\\")
        rows.append(f"\\__/{S}\\__/")
        rows.append("   \\__/")
        return '\n'.join(rows)


def create_map():
    cells = {}

    x_rows = [x for x in string.ascii_uppercase[:12]]
    y_rows = [x + 1 for x in range(9)]

    for x, x_row in enumerate(x_rows):
        for y, y_row in enumerate(y_rows):
            cell = f"{x_row}{y_row}"
            cells.setdefault(cell, Cell(cell))
            for direction, x_shift, y_shift in [
                ("N", 0, -1),
                ("NE", 1, -1),
                ("SE", 1, 1),
                ("S", 0, 1),
                ("SW", -1, 1),
                ("NW", -1, -1),
            ]:
                if x_row not in [x[1] for x in enumerate(x_rows) if not x[0] % 2] and direction in ["NW", "NE"]:
                    y_shift = 0
                if x_row in [x[1] for x in enumerate(x_rows) if not x[0] % 2] and direction in ["SW", "SE"]:
                    y_shift = 0
                if 0 <= x + x_shift < len(x_rows) and 0 <= y + y_shift < len(y_rows):
                    cell_child = f"{x_rows[x + x_shift]}{y_rows[y + y_shift]}"
                    cells.setdefault(cell_child, Cell(cell_child))
                    setattr(cells[cell], direction, cells[cell_child])

    return cells


def print_map(fort, shots, enemies):
    colors = {
        'reset': '\033[0m',
        'fort': '\033[34m',
        'enemy': '\033[31m',
        'shot': '\033[33m',
    }
    x_rows = [x for x in string.ascii_uppercase[:12]]
    y_rows = [x + 1 for x in range(9)]
    head = '  '.join([' __ '] * 6)
    map = [head]
    for y_row in y_rows:
        row_format = '__'.join(['/{}\\'] * 6)
        map.append(row_format.format(
            *[x[1] + str(y_row) for x in enumerate(x_rows) if not x[0] % 2],
        ))
        row_format = '{}'.join(['\\__/'] * 6)
        map.append(row_format.format(
            *[x[1] + str(y_row) for x in enumerate(x_rows) if x[0] % 2],
        ))
    map.append('   ' + '  '.join(['\\__/'] * 5))

    for row in map:
        for shot in shots:
            if shot in row:
                row = row.replace(
                    shot,
                    f"{colors['shot']}{shot}{colors['reset']}",
                )
        if fort in row:
            row = row.replace(
                fort,
                f"{colors['fort']}{fort}{colors['reset']}",
            )
        for enemy in enemies:
            if enemy in row:
                row = row.replace(
                    enemy,
                    f"{colors['enemy']}{enemy}{colors['reset']}",
                )
        print(row)


def fortress_cannons(fort: str, cannons: list, enemies: set) -> list:
    directions = ["N", "NE", "SE", "S", "SW", "NW"]
    map = create_map()

    shots = []
    direction = 'N'
    cell = map[fort]
    for cannon in cannons:
        shooting_area, min_range, max_range = cannon
        if shooting_area == 0:
            for i in range(max_range):
                if cell:
                    cell = getattr(cell, direction)
                    if i + 1 >= min_range and cell:
                        shots.append(cell.name)
        elif shooting_area == 60:
            shooting_cells = [cell]
            swich_targets = False
            for i in range(max_range):
                if not i:
                    target_cell = getattr(cell, direction)
                    if target_cell:
                        if i + 1 >= min_range:
                            shots.append(target_cell.name)
                        shooting_cells = [target_cell]
                else:
                    if (i + 1) % 2:
                        swich_targets = True
                    nex_shooting_cells = []
                    for cell in shooting_cells:
                        if i + 1 >= min_range and cell:
                            shots.append(cell.name)
                            f_target_cell = getattr(cell, direction)
                            if f_target_cell:
                                shots.append(f_target_cell.name)
                            l_target_cell = getattr(cell, directions[directions.index(direction) - 1])
                            if l_target_cell:
                                shots.append(l_target_cell.name)
                            r_target_cell = getattr(cell, directions[directions.index(direction) + 1])
                            if r_target_cell:
                                shots.append(r_target_cell.name)
                            if swich_targets:
                                nex_shooting_cells.extend([l_target_cell, r_target_cell])
                            else:
                                nex_shooting_cells.append(f_target_cell)
                    if swich_targets:
                        swich_targets = False
                    shooting_cells = nex_shooting_cells
        elif shooting_area == 120:
            shooting_cells = [cell]
            for i in range(max_range):
                nex_shooting_cells = []
                for cell in shooting_cells:
                    if cell:
                        f_target_cell = getattr(cell, direction)
                        l_target_cell = getattr(cell, directions[directions.index(direction) - 1])
                        r_target_cell = getattr(cell, directions[directions.index(direction) + 1])
                        nex_shooting_cells.extend([f_target_cell, l_target_cell, r_target_cell])
                        if i + 1 >= min_range and cell:
                            if f_target_cell:
                                shots.append(f_target_cell.name)
                            if l_target_cell:
                                shots.append(l_target_cell.name)
                            if r_target_cell:
                                shots.append(r_target_cell.name)
                shooting_cells = nex_shooting_cells



        # for i, line in enumerate(range(min_range, max_range + 1)):
        #     x = fort_x_ind + (directions[d][0] * line)
        #     if 0 < x < len(x_rows):
        #         y = int(fort_y) + (directions[d][1] * line)
        #         if directions[d][2]:
        #             if directions[d][1] == -1:
        #                 cor = 1
        #             else:
        #                 cor = 0
        #             if fort_x in [x[1] for x in enumerate(x_rows) if not x[0] % 2]:
        #                 if directions[d][1] == -1:
        #                     cor = 0
        #                 else:
        #                     cor = -1
        #             y = int(fort_y) + (directions[d][1] * line) + (directions[d][2] * (i // 2)) + cor
        #             if i % 2:
        #                 y = int(fort_y) + (directions[d][1] * line) + \
        #                     (directions[d][2] * (i // 2)) + directions[d][2]
        #         x = x_rows[x]
        #         shots.append(x + str(y))



    print_map(fort, shots, enemies)
    return []


fortress_cannons('F8', [(120, 3, 4)], {'F2'}) # == ['N']
# fortress_cannons('F5', [(0, 2, 6), (120, 1, 3), (60, 1, 4)], {'L2', 'D3', 'C6', 'E9'})

"""

 __    __
/A1\__/C1\
\__/B1\__/
   \__/  \__/  \__/

"""
