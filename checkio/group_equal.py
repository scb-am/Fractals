# def group_equal(data):
#     list_of_equals = []
#     sublist_of_equals = []
#     for i in range(len(data)):
#         sublist_of_equals.append(data[i])
#         if i == len(data) - 1 or data[i] != data[i+1]:
#             list_of_equals.append(sublist_of_equals)
#             sublist_of_equals = []
#     return list_of_equals

group_equal = lambda els: [[els[x]] * ([y for y in range(len(els[x::-1])) if y == len(els[x::-1]) - 1 or els[x::-1][y] != els[x::-1][y+1]][0] + 1) for x in range(len(els)) if x == len(els) - 1 or els[x] != els[x+1]]

print(group_equal([1, 1, 1, 1, 4, 4, 4, 1, "hello", "hello", "hello", "hello", "hello", 4]))