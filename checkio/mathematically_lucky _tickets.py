"""first variant"""
def divide(data):
    # as integer (allow over 10)
    yield int(data)

    # divide 123456: 1 23456, 12 3456, 123 456, ...
    for pos in range(1, len(data)):
        for left in divide(data[:pos]):
            for right in divide(data[pos:]):
                # calculate + - * /
                yield left + right
                yield left - right
                yield left * right
                if right:
                    yield left / right


def checkio(data):
    # enumerate all pattern
    for x in divide(data):
        if x == 100:
            return False
    return True


import itertools
from operator import add, mul, sub, truediv

operations = add, mul, sub, truediv


"""second variant"""
# def checkio(number):
#     def results(n):
#         yield int(n)
#         for i in range(1, len(n)):
#             for x, y in itertools.product(results(n[:i]), results(n[i:])):
#                 yield from (op(x, y) for op in operations) if y else (x,)
#
#     return 100 not in results(number)


"""3-d variant"""
# from itertools import product
#
# def possible_results(data):
#     yield int(data)
#     for i in range(1, len(data)):
#         for (x,y) in product(
#             possible_results(data[:i]), possible_results(data[i:])
#         ):
#             yield from (x+y, x-y, x*y)
#             if y:
#                 yield x/y
#
# def checkio(data):
#     return all(result != 100 for result in possible_results(data))


"""4 variant"""
# def possible_values(substring: str) -> set:
#     """All values obtainable from substring."""
#     from operator import add, sub, mul, truediv as div
#     entire_number = int(substring)
#     results = {entire_number}
#     for split_position in range(1, len(substring)):
#         # split substring in all possible ways
#         left_part = substring[:split_position]
#         right_part = substring[split_position:]
#         for left_operand in possible_values(left_part):
#             for operation in add, sub, mul, div:
#                 for right_operand in possible_values(right_part):
#                     try:
#                         current_result = operation(left_operand, right_operand)
#                     except ZeroDivisionError:
#                         pass
#                     else:
#                         results.add(current_result)
#     return results
#
#
# def checkio(ticket_number: str) -> bool:
#     """Whether the ticket_number is lucky."""
#     return 100 not in possible_values(ticket_number)
#
#
# assert all((
#     checkio('000000') is True,
#     checkio('707409') is True,
#     checkio('595347') is False,
#     checkio('593347') is False,
#     checkio('271353') is False,
# ))


"""5 variant"""
# from itertools import product
#
#
# def possible_results(s: str) -> int:
#     yield int(s)
#     for i in range(1, len(s)):
#         for x,y in product(possible_results(s[:i]), possible_results(s[i:])):
#             yield from (x+y, x-y, x*y)
#             if y:
#                 yield x/y
#
#
# def checkio(data: str) -> bool:
#     return all(result!=100 for result in possible_results(data))
#
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio('000000') == True, "All zeros"
#     assert checkio('707409') == True, "You can not transform it to 100"
#     assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
#     assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"


"""lambda variant"""
# t=lambda s: {int(s)}|{x for p in range(1,len(s)) for a in t(s[:p]) for b in t(s[p:]) for x in {a+b,a-b,a*b,a/b if b else 0}}
# checkio=lambda d: 100 not in t(d)


# python -m timeit -n 100 -v -s "from veky_l import checkio" "checkio('111111')"
# > raw times: 0.335 0.336 0.343
#
# python -m timeit -n 100 -v -s "from bryukh_l import checkio" "checkio('111111')"
# > raw times: 0.0559 0.0552 0.0547
#
# python -m timeit -n 100 -v -s "from veky_l import checkio" "checkio('999999')"
# raw times: 0.726 0.751 0.735
#
# python -m timeit -n 100 -v -s "from bryukh_l import checkio" "checkio('999999')"
# raw times: 0.101 0.0997 0.0999

"""
The "Mathematically lucky tickets" concept is similar to the idea of the Russian "Lucky tickets". 
It refers to the old public transport tickets that had 6-digit numbers printed on them.

You are given a ticket number and the combination of its digits can become a mathematical expression 
by following these rules.

    1. The digits of the number can be split into groups of numbers.
    2. You cannot change the order of groups or digits.
    3. Each group is treated as a one integer number. (1 and 2 would become 12, etc.)
    4. Operational signs (+, -, * and /) are placed between the groups.
    5. Parenthesis are placed around subexpressions to eliminate any ambiguity
    in the evaluation order.

For example:

    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))

The ticket is considered mathematically lucky if no combination of its digits evaluates to 100. For example:

    * 000000 is obviously lucky, no matter which combination you construct it always
    evaluates to zero,
    * 707409 and 561709 are also lucky because they cannot evaluate to 100
    * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100
    * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100
    * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100

The combination has to evaluate to 100 exactly to be counted as unlucky. Fractions can occur in 
intermediate calculations (like in above examples for 593347 and 271353) but the result must be an integer.
"""
