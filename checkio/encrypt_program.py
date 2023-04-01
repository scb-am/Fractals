import string


def encrypt(password: str) -> str:
    result = []
    password_values = password.split(" ")
    for password_value in password_values:
        if len(password_value) == 1:
            result.append(str(ord(password_value)))
        elif len(password_value) == 2:
            result.append(str(tuple(string.ascii_lowercase.index(x) + 1 for x in password_value)))
        elif len(password_value) == 3:
            result.append(password_value[::-1])
        else:
            result.append(''.join([chr(ord(x) + 1) for x in password_value]))
    return "".join([x if x not in [" ", "h"] else {" ": "h", "h": " "}[x] for x in " ".join(result)])


if __name__ == "__main__":
    print("Example:")
    print(encrypt("I hello my passwords are good"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert (
        encrypt("I hello my passwords are good")
        == "73hifmmph(13,h25)hqbttxpsetherah ppe"
    )
    assert encrypt("I like pickles") == "73hmjlfhqjdlmft"
    print("Coding complete? Click 'Check' to earn cool rewards!")
