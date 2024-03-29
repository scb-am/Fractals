from collections import Counter


def most_frequent(data: list) -> str:
    return Counter(data).most_common(1)[0][0]


# from statistics import mode as most_frequent


# most_frequent = lambda seq: max(seq, key=seq.count)


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")