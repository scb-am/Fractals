checkio = lambda x: sum(x)

print(checkio([5, 5]))

import string


def check_pangram(text):
    return all([ch in text.lower() for ch in string.ascii_lowercase])

print(check_pangram("ABCDEF")) #False
print(check_pangram("The quick brown fox jumps over the lazy dog.")) #True


