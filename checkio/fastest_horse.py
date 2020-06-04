def fastest_horse(*args):
    winners = [x.index(min(x)) for x in args]
    return max(set(winners), key = winners.count) + 1


print(fastest_horse(["4:44","4:11","4:18"], ["3:10","3:01","3:14"], ["2:20","2:23","2:15"]))