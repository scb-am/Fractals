import pytest


DEFAULT_START_POINT = (1, 1)


def map_data_generator(components):
    index = 0
    while index < len(components):
        index += 1
        yield components[index - 1]


def load_map(func):
    def wrapper(map_weight, map_height, components):
        map_data = map_data_generator(components)
        return func(map=[[next(map_data) for _ in range(map_weight)] for _ in range(map_height)],
                    size=map_weight * map_height)

    return wrapper


@load_map
def find_treasure(map, size):
    start_point = DEFAULT_START_POINT
    road = []
    step_counter = 0

    def find_road():
        nonlocal start_point
        nonlocal step_counter
        step_counter += 1
        if step_counter > size:
            raise ValueError('Treasure not found')
        if len(start_point) < 2:
            raise ValueError("Invalid clue, value mast contain two digits")
        cell_x = int(start_point[0]) - 1
        cell_y = int(start_point[1]) - 1
        try:
            clue = map[cell_x][cell_y]
        except IndexError:
            raise ValueError("Invalid clue, can't find cell with this coordinates")
        if start_point != tuple(i for i in clue):
            road.append(''.join([str(i) for i in start_point]))
            start_point = tuple(i for i in clue)
            find_road()
        else:
            road.append(''.join([str(i) for i in start_point]))

    find_road()
    return ' '.join([i for i in road])
