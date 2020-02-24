import math


def find_distance(first, second):


    items_map = [['' for y in range(32)] for x in range(32)]

    # directions = {
    #     UP: lambda value: items_map[],
    #     RIGHT: 1,
    #     DOWN: 2,
    #     LEFT: 3,
    # }



    size = 1
    position = [1, 1]
    current_x = 15
    current_y = 16
    items_map[current_y][current_x] = 1
    for i in range(1, 1000):
        if position[0] == 1 and position[1] == 1:
            #UP
            current_y -= 1
            items_map[current_y][current_x] = i + 1
            position[0] = 2
            position[1] = 1
            size += 2

        elif position[1] == 1 and position[0] != size:
            #RIGHT
            current_x += 1
            items_map[current_y][current_x] = i + 1
            position[0] += 1

        elif position[0] == size and position[1] != size:
            #DOWN
            current_y += 1
            items_map[current_y][current_x] = i + 1
            position[1] += 1

        elif position[1] == size and position[0] != 1:
            #LEFT
            current_x -= 1
            items_map[current_y][current_x] = i + 1
            position[0] -= 1

        else:
            #UP
            current_y -= 1
            items_map[current_y][current_x] = i + 1
            position[1] -= 1


    for i in range(len(items_map)):
        if first in items_map[i]:
            first_x = items_map[i].index(first)
            first_y = i
        if second in items_map[i]:
            second_x = items_map[i].index(second)
            second_y = i
        print(items_map[i])

    print(abs(second_y - first_y) + abs(second_x - first_x))

    return abs(second_y - first_y + second_x - first_x)


find_distance(999,1)

print('\n')

first = 9
second = 33


# print((lambda z: [[a, z+2] for a in range(z**2+1, (z+2)**2+1)])([y[1] for y in [[x**2, x] for x in range(1, 15, 2)] if y[0] < first][-1]))
# print((lambda z: [[a, [c for c in range(3, 18, 2)].index(z+2)] for a in range(z**2+1, (z+2)**2+1)])([y[1] for y in [[x**2, x] for x in range(1, 15, 2)] if y[0] < first][-1]))
#
# print('\n')
#
# print([x for x in zip(range(2,9), [0,0,1])])


print((lambda i: [[x, [x-1, -2] if x < 1 else [2, x-1-2] if x-1 < 4 else [5-x, 2] if x-1 < 6 else [-2, 7-x]] for x in range((i*2)**2, (1+i*2)**2)])(1))




# print(len([y for y in [x**2 for x in range(1, 15, 2)] if y < second]))
#
# print([z for z in range([x**2 for x in range(1, 15, 2)][len([y for y in [x**2 for x in range(1, 15, 2)] if y < first]) - 1], [x**2 for x in range(1, 15, 2)][len([y for y in [x**2 for x in range(1, 15, 2)] if y < first])])])