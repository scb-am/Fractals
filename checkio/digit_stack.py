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


# def digit_stack(commands):
#     stack, digitsum = [], 0
#     for command in commands:
#         if command.startswith("PUSH"):
#             stack.append(int(command[-1]))
#         elif stack:
#             digitsum += stack[-1]
#             if command == "POP":
#                 stack.pop()
#     return digitsum


# def digit_stack(cs, s=__import__('re').sub):
#     fix = lambda f,c,n: c if n == c else fix(f, f(c), c)
#     return eval('0' + s(r'(\d)', r'+\1', s(r'(POP|PEEK|PUSH\d)', r'',
#         fix (lambda x: s(r'PUSH(\d)(\d*)PEEK', r'PUSH\1\2\1',
#         s(r'PUSH(\d)(\d*)POP', r'\1\2', x)), s(' ', '', ''.join(cs)), ''))))


# digit_stack=d=lambda c,a='':len(c)and(d(c[1:],c[0][5]+a)if' 'in c[0]else(len(a)and int(a[0]))+d(c[1:],a['O'in c[0]:]))


# def digit_stack(cmds, s=[]):
#     e, s = {"PU": lambda x: s.append(x.split()[1]) == 1,
#             "PO": lambda x: s.pop() if s else 0,
#             "PE": lambda x: s[len(s)-1] if s else 0}, []
#     return sum([int(e[x[:2]](x)) for x in cmds])


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

