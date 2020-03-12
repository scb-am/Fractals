from ..programming_types.OOP_application import Map_point, Point, Clue, Treasure, Treasure_map, Treasure_road


def test_factory():
    assert isinstance(Map_point.factory('25', '13'), Clue)
    assert not isinstance(Map_point.factory('34', '34'), Clue)
    assert isinstance(Map_point.factory('34', '34'), Treasure)

def test_point():
    assert Point(1,4).point_value == '14'
    assert Point(4,8).point_value != '34'
    assert Point(4,8).point_value != '4'

def test_treasure_map():
    assert Treasure_map(2, 2, ['14', '31', '44', '14', '33']).get_map_grid(2, 2) == ['11', '12', '21', '22']
    assert not Treasure_map(2, 2, ['14', '31', '44', '14', '33']).check_treasure
    assert Treasure_map(2, 2, ['11', '14', '22', '33']).check_treasure

def test_treasure_road():
    assert Treasure_road(Treasure_map(2, 2, ['12', '21', '21', '12'])).print_map == '11 12 21'

def test_bad_data():
    try:
        Treasure_road(Treasure_map(2, 3, ['12', '21', '21', '12']))
        assert False
    except TypeError:
        assert True
    try:
        Treasure_road(Treasure_map(2, 2, ['188', '21', '21', '12']))
        assert False
    except ValueError:
        assert True
    assert not Treasure_road(Treasure_map(2, 2, ['22', '21', '21', '11'])).include_treasure
