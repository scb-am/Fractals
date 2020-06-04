def iterate(tree):
    while tree:
        if type(tree[0]) is str or type(tree[0]) is int:
            yield tree[0]
            tree = tree[1]
        else:
            yield tree[0][0]
            tree = tree[0][1]

def on_same_path(tree, pairs):
    tree_list = []
    while tree:
        res = [x for x in iterate(tree)]
        tree_list.append(res)
        item = tree[1]
        for _ in range(len(res) - 2):
            item = item[0][1]
        try:
            del item[0]
        except IndexError:
            tree = False
    return [any([True if pair[0] in x and pair[1] in x else False for x in tree_list]) for pair in pairs]


example = on_same_path(
        (1, [(2, [(4, []),
              (5, [(7, []),
                   (8, []),
                   (9, [])])]),
         (3, [(6, [])])]),
        [('Grandpa', 'Me'), ('Dddy', 'Grany')],
    )

print(example)
