from itertools import permutations


def checkio(numbers):
    first_number = numbers[0]
    last_number = numbers[-1]

    if [str(first_number)[i] == str(last_number)[i] for i in range(0, 3)].count(True) == 2:
        return [first_number] + [last_number]

    correct_chain = False

    for chain_len in range(1, len(numbers) - 1):
        for combination in permutations(numbers[1: -1], chain_len):
            current_number = first_number
            result = []
            for next_number in combination:
                if [str(current_number)[i] == str(next_number)[i] for i in range(0, 3)].count(True) == 2 and [str(last_number)[i] == str(next_number)[i] for i in range(0, 3)].count(True) == 2:
                    result.append(next_number)
                    correct_chain = True
                    break
                elif [str(current_number)[i] == str(next_number)[i] for i in range(0, 3)].count(True) == 2:
                    current_number = next_number
                    result.append(current_number)
                    continue
            if correct_chain:
                break
        if correct_chain:
            break
    return [first_number] + result + [last_number]


print(checkio([555,545])) # == [123, 121, 921, 991, 999]
print(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999])) # == [123, 121, 921, 991, 999]

# def checkio(numbers):
#     paths = [[numbers[0]]]
#     while True:
#         p = paths.pop(0)
#         for c in set(numbers)-set(p):
#             if sum(x!=y for x, y in zip(str(p[-1]), str(c))) == 1:
#                 if c == numbers[-1]:
#                     return p + [c]
#                 paths.append(p + [c])
