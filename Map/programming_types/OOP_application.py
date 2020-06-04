from abc import ABC, abstractmethod
from itertools import zip_longest

DEFAULT_KEY = '11'


class Map_point(ABC):
    @property
    @abstractmethod
    def point_value(self):
        """get point value"""

    @staticmethod
    def factory(cell_coordinates, clue):
        if len(clue) != 2:
            raise ValueError("Invalid clue, value mast contain two digits")
        if cell_coordinates == clue:
            return Treasure(clue)
        return Clue(clue)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def point_value(self):
        return f'{self._x}{self._y}'


class Treasure(Point, Map_point):
    def __init__(self, clue):
        super().__init__(clue[0], clue[1])


class Clue(Point, Map_point):
    def __init__(self, clue):
        super().__init__(clue[0], clue[1])


class Treasure_map:
    def __init__(self, map_weight, map_height, components, key=DEFAULT_KEY):
        self.map = {key: Map_point.factory(key, value) for key, value in
                    zip_longest(self.get_map_grid(map_weight, map_height), components)}
        self.current_iter = 0
        self.max_iter = map_weight * map_height
        self.key = key

    def __getitem__(self, index):
        try:
            return self.map[index]
        except KeyError:
            raise ValueError("Invalid clue, can't find cell with this coordinates")

    def __iter__(self):
        return self

    def __next__(self):
        self.current_iter += 1
        if self.current_iter < self.max_iter:
            value = self.key
            if self.check_treasure:
                self.current_iter = self.max_iter
            self.key = self[self.key].point_value
            return value, self[value]
        raise StopIteration

    def __repr__(self):
        return f'{self.__class__} ' \
               f'{" ".join([x[1].point_value for x in self.map.items()][:6])} ' \
               f'{"..." if len(self.map) > 6 else ""}'

    @property
    def check_treasure(self):
        return isinstance(self[self.key], Treasure)

    @classmethod
    def get_map_grid(cls, map_weight, map_height):
        return [f'{x + 1}{y + 1}' for x in range(map_height) for y in range(map_weight)]


class Treasure_road:
    def __init__(self, treasure_map):
        self.road = [x for x in treasure_map]

    @property
    def include_treasure(self):
        return isinstance(self.road[-1][1], Treasure)

    @property
    def print_map(self):
        return ' '.join([x[0] for x in self.road]) if self.include_treasure else 'Treasure not found'
