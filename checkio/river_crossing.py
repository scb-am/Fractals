def river_crossing(wolves, goats, cabbages, payload):
    if wolves == goats == cabbages == payload:
        return 7
    elif sum([x for x in (wolves, goats, cabbages) if x]) <= payload:
        return 1
    elif payload >= (wolves + cabbages) and payload >= goats:
        return 3
    elif payload >= goats and payload >= wolves and payload >= (goats + cabbages):
        return 5
    elif len([x for x in (wolves, goats, cabbages) if x]) == 1 or goats == 0:
        items_count = sum([x for x in (wolves, goats, cabbages) if x])
        if items_count // payload == 1 or items_count // payload == 0:
            if items_count % payload:
                return 3
            else:
                return 1
        else:
            if items_count % payload:
                return (items_count // payload) * 2 + 1
            else:
                return (items_count // payload) * 2 - 1
    elif cabbages == 0 and payload > goats:
        new_payload = payload - goats
        new_wolves = wolves - payload
        if new_wolves // new_payload == 1 or new_wolves // new_payload == 0:
            if new_wolves % new_payload:
                return 7
            else:
                return 5
        else:
            if new_wolves % new_payload:
                return (new_wolves // new_payload) * 2 + 5
            else:
                return (new_wolves // new_payload) * 2 + 3
    elif len([x for x in (wolves, goats, cabbages) if x]) == 2:
        existed = [x for x in (wolves, goats, cabbages) if x]
        item_0 = existed[0]
        item_1 = existed[1]
        new_payload = payload - min([item_0, item_1])
        new_items = abs(item_0 - item_1)
        if new_items // new_payload == 1 or new_items // new_payload == 0:
            if new_items % new_payload:
                return 5
            else:
                return 3
        else:
            if new_items % new_payload:
                return (new_items // new_payload) * 2 + 1
            else:
                return (new_items // new_payload) * 2 - 1
    elif payload >= (wolves + cabbages) and int(goats / payload) <= 2:
        return 7
    elif payload >= (goats + cabbages) and int(wolves / payload) <= 2:
        return 7
    elif wolves <= payload and goats <= payload and cabbages <= payload:
        return 7
    elif payload > goats:
        new_payload = payload - goats
        new_items = wolves + cabbages
        if new_items // new_payload == 1 or new_items // new_payload == 0:
            if new_items % new_payload:
                return 7
            else:
                return 5
        else:
            if new_items % new_payload:
                return (new_items // new_payload) * 2 + 1
            else:
                return (new_items // new_payload) * 2 - 1
    return None


assert river_crossing(7, 1, 0, 2) == 13
assert river_crossing(5, 1, 2, 3) == 7
print(river_crossing(5, 1, 2, 2))


# 2, 4, 1 == 0, 0, 0  =       0
# 0, 4, 0 == 2, 0, 1  >   3   1
# 0, 4, 1 == 2, 0, 0  <   1   2
# 0, 1, 1 == 2, 3, 0  >   3   3
# 2, 1, 1 == 0, 3, 0  <   2   4
# 2, 0, 1 == 0, 4, 0  >   1   5
# 2, 0, 1 == 0, 4, 0  <   0   6
# 0, 0, 0 == 2, 4, 1  >   3   7


