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
