from itertools import permutations


D = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


# def count_morse(message: str, letters: str) -> int:
#     return sum(["".join(text) == message for text in permutations([D[ch] for ch in letters])])


def count_morse(message: str, letters: str) -> int:
    counter = 0
    if len(letters) == 1:
        if D[letters[0]] == message:
            return 1
        return 0
    for i, char in enumerate(letters):
        if D[char] == message[:len(D[char])]:
            counter += count_morse(message[len(D[char]):], letters[:i] + letters[i+1:])

    return counter


print(count_morse('.-.----..-.........-.-...-....-', 'etaoinshrdlu'))


