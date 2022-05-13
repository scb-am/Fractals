    def compare_words(word_1: str, word_2: str) -> float:
        result = 0
        for i in (0, -1):
            if word_1[i] == word_2[i]:
                result += 10
        if len(word_1) <= len(word_2):
            result += (len(word_1) / len(word_2)) * 30
        else:
            result += (len(word_2) / len(word_1)) * 30
        unique = len(set([x for x in word_1 + word_2]))
        intersected = len(set([x for x in word_1 if x in word_2]))
        result += (intersected / unique) * 50
        return round(result, 3)


    def find_word(message):
        words_calculations = {}
        words = [x.lower() for x in message.replace('.', '').replace(',', '').split(' ')]
        for i, word_1 in enumerate(words):
            words_calculations[i] = []
            for j, word_2 in enumerate(words):
                words_calculations[i].append(compare_words(word_1, word_2))
        return words[max(
            reversed(words_calculations),
            key=lambda k: sum(words_calculations[k]) / len(words_calculations[k]),
        )]


# import re
#
# def getscore(word1, word2):
#     first = 10 if word1[0] == word2[0] else 0
#     last = 10 if word1[-1] == word2[-1] else 0
#     length = 30 * min(len(word1) / len(word2), len(word2) / len(word1))
#     unique = 50 * len(set(word1) & set(word2)) / len(set(word1) | set(word2))
#     return first + last + length + unique
#
# def find_word(message):
#     words = re.findall('[a-z]+', message.lower())[::-1]
#     return max(words, key = lambda w: sum(getscore(w, x) for x in words))


# def find_word(message):
#     def f(s1, s2):
#         point = 10 * ((s1[0] == s2[0]) + (s1[-1] == s2[-1]))
#         point += 30 * min(len(s1), len(s2)) / max(len(s1), len(s2))
#         point += 50 * len(set(s1) & set(s2)) / len(set(s1 + s2))
#         return point
#
#     m = ''.join(c if c.islower() else ' ' for c in message.lower()).split()
#     score = {}
#     for i, w1 in enumerate(m):
#         score[i] = sum(f(w1, w2) for j, w2 in enumerate(m) if i != j)
#     return m[max(reversed(range(len(m))), key=score.get)]


# def find_word(m):
#     def likeness(*a):
#         (w,W), (l,L), (s,S) = a, sorted(map(len, a)), map(set, a)
#         return (w[0]==W[0]) + (w[-1]==W[-1]) + 3*l/L + 5*len(s&S)/len(s|S)
#     ws = [w.strip(__import__("string").punctuation) for w in m.lower().split()]
#     return max(reversed(ws), key=lambda w:sum(likeness(w, W) for W in ws))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # print(find_word("friend fred and friend ted"))
    # print(find_word("Speak friend and enter."))
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    # print(find_word("Beard and Bread"))
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    # print(find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. I Narvi made them. Celebrimbor of Hollin drew these signs"))
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    # print(find_word("One, two, two, three, three, three."))
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"

# print(compare_words('enter', 'enter'))
