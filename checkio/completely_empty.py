from collections.abc import Iterable


def completely_empty(data):
    result = True
    for i in data:
        if isinstance(i, Iterable):
            result = completely_empty(i)
        else:
            return False
    return result

assert completely_empty([]) == True, "First"
assert completely_empty([1]) == False, "Second"
assert completely_empty([[]]) == True, "Third"
assert completely_empty([[],[]]) == True, "Forth"
assert completely_empty([[[]]]) == True, "Fifth"
assert completely_empty([[],[1]]) == False, "Sixth"
assert completely_empty([0]) == False, "[0]"
assert completely_empty(['']) == True
assert completely_empty([[],[{'':'No WAY'}]]) == True