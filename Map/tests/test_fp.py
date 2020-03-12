from ..programming_types.FP_application import map_data_generator, load_map, find_treasure


def test_map_data_generator():
    assert [i for i in map_data_generator(['11', '13', '65'])] == ['11', '13', '65']
    assert [i for i in map_data_generator(['2'])] == ['2']
    assert [i for i in map_data_generator(['12'])] != [12]
    assert [i for i in map_data_generator(['34'])] != [(3, 4)]

def test_load_map():
    @load_map
    def loaded_data(map, size):
        return (map, size)
    assert loaded_data(2, 2, ['1', '2', '3', '4']) == ([['1', '2'], ['3', '4']], 4)
    assert loaded_data(2, 2, ['461', '22', '816', '94']) == ([['461', '22'], ['816', '94']], 4)

def test_find_treasure():
    result = find_treasure(5, 5, ['55', '14', '25', '52', '21',
                                  '44', '31', '11', '53', '43',
                                  '24', '13', '45', '12', '34',
                                  '42', '22', '43', '32', '41',
                                  '51', '23', '33', '54', '15'])
    assert result == '11 55 15 21 44 32 13 25 43'

def test_bad_clue():
    try:
        find_treasure(5, 5, ['55', '14', '25', '52', '2',
                             '44', '31', '11', '53', '43',
                             '24', '13', '45', '12', '34',
                             '42', '22', '43', '32', '41',
                             '51', '23', '33', '54', '15'])
        assert False
    except ValueError:
        assert True

def test_bad_size():
    try:
        find_treasure(5, 5, ['12', '21',
                             '22', '22'])
        assert False
    except StopIteration:
        assert True

def test_without_treasure():
    try:
        find_treasure(2, 2, ['12', '21',
                             '22', '11'])
        assert False
    except ValueError:
        assert True
