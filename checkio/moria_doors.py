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
