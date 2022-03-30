from itertools import combinations


MONSTERS = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''


def monster_in_spell(monster, spell):
    for ch in monster:
        if ch in spell:
            spell.remove(ch)
        else:
            return None
    return spell


def halloween_monsters(spell: str)-> int:
    possible_monsters = []
    monsters = MONSTERS.split('\n')[1:-1]
    for monster in monsters:
        spell_list = [x for x in spell]
        res = True
        while res and spell_list:
            spell_list = monster_in_spell(monster, spell_list)
            if spell_list != None:
                possible_monsters.append(monster)
    for i in range(len(possible_monsters)):
        for possible_monsters_check in combinations(possible_monsters, len(possible_monsters) - i):
            spell_list = [x for x in spell]
            if all([monster_in_spell(x, spell_list) != None for x in possible_monsters_check]):
                return len(possible_monsters_check)
    return 0




# from collections import Counter
#
# MONSTERS = 'skeleton ghost jack vampire witch mummy zombie werewolf frankenstein'
#
#
# def halloween_monsters(spell: str) -> int:
#     monsters = list(map(Counter, MONSTERS.split()))
#
#     def result(pool):
#         return max((result(pool - monster) + 1 for monster in monsters
#                     if all(pool[key] >= value for key, value in monster.items())), default=0)
#
#     return result(Counter(spell))




# from collections import defaultdict
#
# MONSTERS = '''
# skeleton
# ghost
# jack
# vampire
# witch
# mummy
# zombie
# werewolf
# frankenstein
# '''
#
#
# def word_returner(data, carry):
#     for k in carry:
#         data[k] += 1
#     return data
#
#
# def word_finder(data, word):
#     for k in word:
#         if data[k] > 0:
#             data[k] -= 1
#         else:
#             return
#     return data
#
#
# def recur(count, data, carry=""):
#     for k in MONSTERS.split():
#         if word_finder(data.copy(), k):
#             data = word_finder(data, k)
#             yield from recur(count + 1, data, k)
#     yield count
#     data = word_returner(data, carry)
#     count -= 1
#
#
# def halloween_monsters(spell: str) -> int:
#     data = defaultdict(int)
#     for k in spell:
#         data[k] += 1
#     return max(recur(0, data))




# MONSTERS = '''
# skeleton
# ghost
# jack
# vampire
# witch
# mummy
# zombie
# werewolf
# frankenstein
# '''
#
# # Attempt to extract monster from spell. If spell doesn't have the right
# # letters for monster, return None. Otherwise, return spell with the letters
# # in monster removed.
# def extract_monster(spell, monster):
#     lst = list(spell)
#     for ch in monster:
#         if ch not in lst:
#             return None
#         lst.remove(ch)
#     return ''.join(lst)
#
# # Recursive search for monsters. Try extracting one monster and then call the
# # search again on the spell string minus that monster.
# def search_monsters(spell, monsters):
#     maxcount = 0
#     for i, monster in enumerate(monsters):
#         result = extract_monster(spell, monster)
#         if result is not None:
#             # We don't have to recheck the whole list of monsters on the next
#             # level of the search tree. If we have skipped past a monster,
#             # it's not going to be in this branch of the search tree.
#             maxcount = max(maxcount, search_monsters(result, monsters[i:]) + 1)
#     return maxcount
#
# def halloween_monsters(spell: str)-> int:
#     return search_monsters(spell, MONSTERS.split())


if __name__ == '__main__':
    assert halloween_monsters('casjokthg') == 2, 'jack ghost'
    assert halloween_monsters('leumooeeyzwwmmirbmf') == 3, 'mummy zombie werewolf'
    assert halloween_monsters('nafrweiicttwneshhtikcn') == 3, 'witch witch frankenstein'
    assert halloween_monsters('kenoistcepajmlvre') == 2, 'skeleton vampire (not jack)'
    assert halloween_monsters('miaimavrurymepepv') == 2, 'vampire vampire (not mummy)'
    assert halloween_monsters(
        "udaarbesoqwcbflaiwbzigvncnbquehhzotsvrmyeshjqcitmnpltcjgeompwrxxuhlrwkjkgifuxmsfnkozdvjxy"
    ) == 9
    print("Your spell seem to be okay. It's time to check.")
