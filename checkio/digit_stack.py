def digit_stack(commands):
    stack = []
    summ = []
    COMMANDS = {
        "PUSH": lambda x: stack.append(x),
        "POP": lambda x: summ.append((stack or [0]).pop()),
        "PEEK": lambda x: summ.append((stack or [None])[-1] or 0),
    }
    for command in commands:
        if "PUSH" in command:
            _, num = command.split(" ")
            COMMANDS["PUSH"](int(num))
        else:
            COMMANDS[command](0)
    return sum(summ)


if __name__ == '__main__':
    print("Example:")
    print(digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                       "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!");

