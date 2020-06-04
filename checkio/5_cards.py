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


# RANKS = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
# SUITS = '♣♦♥♠'
#
# RANK = slice(-2)
# SUIT = -1
#
# def card_order(card):
#     return RANKS.index(card[RANK]), SUITS.index(card[SUIT])
#
# def bot(*cards, n=1):
#     """Determine four cards the bot has to say to the magician."""
#     suits = [c[SUIT] for c in cards]
#     same_suit = max(suits, key=suits.count)
#     keep, hide = [c for c in cards if c[SUIT] == same_suit][:2]
#     distance = (RANKS.index(hide[RANK]) - RANKS.index(keep[RANK]) + 13) % 13
#     if distance > 6:
#         keep, hide, distance = hide, keep, 13 - distance
#     C1, C2, C3 = sorted((c for c in cards if keep != c != hide), key=card_order)
#     result = {1: [C3, C1, C2], 2: [C3, C2, C1], 3: [C2, C1, C3],
#               4: [C2, C3, C1], 5: [C1, C2, C3], 6: [C1, C3, C2]}[distance]
#     result.insert((n - 1) % 4, keep)
#     return result
#
# def magician(*cards, n=1):
#     """Determine the fifth card with only four cards."""
#     cards = list(cards)
#     keep = cards.pop((n - 1) % 4)
#     sorted_cards = sorted(cards, key=card_order)
#     distance = (5, 3, 1)[sorted_cards.index(cards[0])]
#     distance += card_order(cards[1]) > card_order(cards[2])
#     return f'{RANKS[(RANKS.index(keep[RANK]) + distance) % 13]} {keep[SUIT]}'
#
#
# if __name__ == '__main__':
#     assert list(bot('A ♥', '3 ♦', 'K ♠', 'Q ♣', 'J ♦')) == ['J ♦', 'A ♥', 'Q ♣', 'K ♠']
#     assert magician('J ♦', 'A ♥', 'Q ♣', 'K ♠') == '3 ♦'
#
#     assert list(bot('10 ♦', 'J ♣', 'Q ♠', 'K ♥', '7 ♦', n=2)) == ['Q ♠', '7 ♦', 'J ♣', 'K ♥']
#     assert magician('Q ♠', '7 ♦', 'J ♣', 'K ♥', n=2) == '10 ♦'
