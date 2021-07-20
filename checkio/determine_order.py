"""
The Robots have found an encrypted message. We cannot decrypt it at the moment,
but we can take the first steps towards doing so. You have a set of "words",
all in lower case, and each word contains symbols in "alphabetical order".
(it's not your typical alphabetical order, but a new and different order.)
We need to determine the order of the symbols from each "word" and create
a single "word" with all of these symbols, placing them in the new alphabetical
order. In some cases, if we cannot determine the order for several symbols,
you should use the traditional latin alphabetical order . For example: Given
words "acb", "bd", "zwa". As we can see "z" and "w" must be before "a" and "d"
after "b". So the result is "zwacbd".
"""


def checkio(data):
    rules = []
    for word in data:
        clean_word = ''.join(sorted(set(word), key=word.index))
        for i in range(len(clean_word) - 1):
            rules.append(f'{clean_word[i]}{clean_word[i+1]}')
    result = list(set(''.join([''.join(sorted(set(x))) for x in data])))
    result.sort()
    for _ in rules:
        for rule in rules:
            index_1 = result.index(rule[0])
            index_2 = result.index(rule[1])
            if index_1 > index_2:
                result[index_1], result[index_2] = result[index_2], result[index_1]
    for i in range(len(result) - 1):
        if f'{result[i]}{result[i+1]}' not in rules:
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]

    return''.join(result)



# def checkio(data):
#     ordered_symbols = ''
#     symbols = sorted(set().union(*data))
#     for _ in range(len(symbols)):
#         for ch in symbols:
#             if (
#                     ch not in ordered_symbols
#                 and all(ch not in word or ch == word[0] for word in data)
#             ):
#                 ordered_symbols += ch
#                 for i in range(len(data)):
#                     data[i] = data[i].replace(ch, '')
#                 break
#     return ordered_symbols


# def checkio(data):
#     weight = lambda c: max([ord(c)] + [weight(s[n]) + i - n for s in data for i in [s.find(c)] for n in range(i)])
#     order = {weight(c) + ord(c) / 100 : c for c in set(''.join(data))}
#     s = ''.join(order[i] for i in sorted(order))
#     return s


# checkio(["acb", "bd", "zwa"])# == "zwacbd"
# checkio(["klm", "klsm"])# == "klsm"
# checkio(["klm", "kadl", "lsm"])# == "kadlsm"
# checkio(["my","name","myke"])# == "namyke"
# checkio(["xxxyyz","yyww","wwtt","ttzz"])# == "xywtz"
# checkio(["a", "b", "bcccc"])# == "abc"
# checkio(["aazzss"])# == "azs"
# checkio(["dfg", "frt", "tyg"])# == "dfrtyg"
checkio(["jhgedba","jihcba","jigfdca"])# == "jihgefdcba"


# def checkio(groups):
#     out, chars = "", ''.join(sorted(set(''.join(groups))))
#     while chars:
#         for i in chars:
#             if all([x.find(i) in [-1, 0] for x in groups]):
#                 groups = [x.replace(i, '') for x in groups]
#                 out, chars = out+i, chars.replace(i, '')
#     return out