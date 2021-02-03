from functools import cmp_to_key


def compare(a, b):
    """Inputs: Two integers.
    
    Output: -1, 0 or +1 if the first argument is smaller, equal to or larger
    than the second argument respectively.
    """
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return ((int(ba) > int(ab)) - (int(ba) < int(ab)))


def bigger_together(ints):
    """Inputs: a list of non-negative integers.
    
    Output: Difference between the largest and smallest values that can be
    obtained by concatenating the integers together.
    """
    str_ints = [str(x) for x in ints]
    smallest = sorted(str_ints, key=cmp_to_key(compare), reverse=True)
    biggest = sorted(str_ints, key=cmp_to_key(compare))
    big_num, small_num = [int(x) for x in map(''.join, [biggest, smallest])]
    return big_num - small_num


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
    assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')
