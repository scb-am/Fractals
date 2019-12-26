def split_pairs(a):
    while a:
        print(a)
        if len(a) == 1:
            yield a[0] + '_'
        else:
            yield a[:2]
        a = a[2:]



print([x for x in split_pairs('tetetetetettt')])