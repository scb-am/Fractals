def rotate(holes, cannons):
    return [i for i in range(len(holes)) if all([(holes[-i:] + holes[:-i])[x] == 1 for x in cannons])]


"""OMG"""
# # Creates a node which contains data and has a pointer to the next and previous node.
# class Node:
#     def __init__(self, contents, last_node, next_node):
#         self.contents = contents
#         self.last_node = last_node
#         self.next_node = next_node
#
#     def next(self):
#         return self.next_node
#
#     def previous(self):
#         return self.last_node
#
#
# # Circular data-type implementation
# class Circular_data:
#
#     def __init__(self, input_list):
#         self.counter = 0
#         self.length = len(input_list)
#         self.first_node = None
#         self.current_node = None
#         self.last_node = None
#         self.next_node = None
#
#         for i in input_list:
#             self.current_node = Node(i, self.last_node if self.last_node else None, None)
#             if self.first_node == None:
#                 self.first_node = self.current_node
#             if self.last_node != None:
#                 self.last_node.next_node = self.current_node
#             self.last_node = self.current_node
#
#         self.current_node.next_node = self.first_node
#         self.current_node = self.first_node
#         self.current_node.last_node = self.last_node
#
#     def __len__(self):
#         return self.length
#
#     def rotate_cw(self):
#         self.current_node = self.current_node.previous()
#
#     def rotate_ccw(self):
#         self.current_node = self.current_node.next()
#
#     def current(self):
#         return self.current_node
#
#     def __str__(self):
#         output = "-> "
#         for i in range(len(self)):
#             if i > 0:
#                 output += ", "
#             output += str(self.current().contents)
#             self.rotate_ccw()
#
#         return output + " ->"
#
#     def __iter__(self):
#         self.counter = 0
#         return self
#
#     def __next__(self):
#         if self.counter < len(self):
#             output = self.current().contents
#             self.rotate_ccw()
#             self.counter += 1
#             return output
#         else:
#             raise StopIteration
#
#     def __getitem__(self, i):
#         tmp_old = self.current_node
#
#         for x in range(i):
#             self.rotate_ccw()
#
#         output = self.current().contents
#         self.current_node = tmp_old
#         return output
#
#
# def rotate(state, pipe_numbers):
#     barrels = Circular_data(state)
#     results = []
#
#     for i in range(len(state)):
#         found_barrels = True
#         for x in pipe_numbers:
#             if barrels[x] == 0:
#                 found_barrels = False
#         if found_barrels:
#             results.append(i)
#
#         barrels.rotate_cw()
#
#     return results

print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 1, 1, 1]))