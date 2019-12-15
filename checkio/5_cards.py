suits_order = ['♣', '♦', '♥', '♠']
ranks_order = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
switcher = {
    1: [1, 2, 0],
    2: [2, 1, 0],
    3: [1, 0, 2],
    4: [2, 0, 1],
    5: [0, 1, 2],
    6: [0, 2, 1],
}

def bot(*cards, **kwargs):
    n = kwargs['n'] if 'n' in kwargs else 1
    n = n % 4 if n % 4 != 0 else 4
    double_suits = sorted([x for x in cards if list(map(lambda x: x[-1], cards)).count(x[-1]) > 1],
                          key=lambda x: (suits_order.index(x[-1]), ranks_order.index(x[:-2])))[0:2]
    delta = ranks_order.index(double_suits[1][:-2]) - ranks_order.index(double_suits[0][:-2])
    delta, hide_card_B = delta if delta <= 6 else 13 - delta, False if delta <= 6 else True
    last_cards = [e for e in [*cards] if e not in double_suits]
    sorted_last_cards = sorted(last_cards, key=lambda x: (ranks_order.index(x[:-2]), suits_order.index(x[-1])))
    magic_sorted_last_cards = [*sorted(sorted_last_cards, key=lambda x: switcher[delta][sorted_last_cards.index(x)])]
    magic_sorted_last_cards.insert(n - 1, double_suits.pop(1) if hide_card_B else double_suits.pop(0))
    return magic_sorted_last_cards


def magician(*cards, **kwargs):
    n = kwargs['n'] if 'n' in kwargs else 1
    n = n % 4 if n > 4 else n
    key_cards = [*cards]
    del key_cards[n - 1]
    sorted_key_cards = sorted(key_cards, key=lambda x: (ranks_order.index(x[0]), suits_order.index(x[2])))
    delta = list(switcher.keys())[list(switcher.values()).index([key_cards.index(x) for x in sorted_key_cards])]
    return f'{ranks_order[ranks_order.index(cards[n - 1][:-2]) - 13 + delta]} {cards[n - 1][-1]}' if ranks_order.index(
        cards[n - 1][:-2]) + delta >= 13 else f'{ranks_order[ranks_order.index(cards[n - 1][:-2]) + delta]} {cards[n - 1][-1]}'


print(bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦', n=1))
print(magician('J ♦', 'A ♥', 'Q ♣', 'K ♠', n=1))

print('d - ', bot('10 ♥', 'J ♥', 'Q ♥', 'K ♥', 'A ♥', n=4))
print(magician('Q ♥', 'K ♥', 'J ♥', '10 ♥', n=4))
