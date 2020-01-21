class Item():
    def __init__(self, item):
        self.item = item
        self.switcher = {
            'int': None,
            'str': None,
            'list': lambda x: [i for i in x],
            'tuple': lambda x: [i for i in x],
            'dict': lambda x: [i for i in x.values()]
        }
        self.func = self.switcher[type(self.item).__name__]

    def values(self):
        if self.func:
            return self.switcher[type(self.item).__name__](self.item)
        pass


def tree_walker(tree, target):
    count = 1 if tree==target else 0
    old_list_items = []
    new_list_items = [Item(tree).values()]
    while new_list_items != old_list_items:
        old_list_items = new_list_items
        for item in old_list_items:
            if isinstance(item, list) or isinstance(item, tuple) or isinstance(item, dict):
                new_items = [x for x in Item(item).values()]
                for new_item in new_items:
                    if new_item == target:
                        count += 1
                    if new_item not in old_list_items:
                        new_list_items.append(new_item)
    return count


# def tree_walker(tree, target):
#     if tree == target:
#         return 1
#
#     if not isinstance(tree, (dict, list)):
#         return 0
#
#     if isinstance(tree, dict):
#         tree = tree.values()
#
#     return sum(tree_walker(leaf, target) for leaf in tree)




tree_walker(tree={"one": [1, 2], "two": [{1: "one", 2: "two"}, [1, 2], "1", "one"]}, target=[1, 2])# == 2
tree_walker(tree=5, target=5)# == 1
tree_walker(tree=[1, "2", 3, [[3], 1, {1: "one"}]], target=1)# == 2