"""1v"""
isometric_strings = lambda a, b: a.translate(str.maketrans(a, b)) == b


"""2v"""
# def isometric_strings(u,v):t={};return all(t.setdefault(a,b)==b for a,b in zip(u,v))


"""3"""
# def isometric_strings(str1: str, str2: str) -> bool:
#     trans = str.maketrans(str1, str2)
#     return str1.translate(trans) == str2


"""4"""
# def isometric_strings(str1: str, str2: str) -> bool:
#     return len(set(zip(str1, str2))) == len(set(str1))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(isometric_strings('add', 'egg'))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert isometric_strings('adp', 'egg') == True
#     assert isometric_strings('egg', 'adp') == False
#     assert isometric_strings('paper', 'words') == False
#     assert isometric_strings('paper', 'title') == True
#     assert isometric_strings('add', 'egg') == True
#     assert isometric_strings('foo', 'bar') == False
#     assert isometric_strings('', '') == True
#     assert isometric_strings('all', 'all') == True
#     print("Coding complete? Click 'Check' to earn cool rewards!")


"""
You need to check that the 2 given strings are isometric. This means that a character 
from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. 
Two or more characters of one string can correspond to one character of another string, 
but not vice versa.
"""
