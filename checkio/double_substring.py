def double_substring(string):
    return max([len(string[i: i + j]) if string.count(string[i: i + j]) > 1 else 0 for
                i in range(len(string)) for j in range((len(string) - i) // 2 + 1)]) if len(string) > 0 else 0


"""regular expression"""
# def double_substring(line):
#     i = 1
#     while re.search(r'(\w{%i}).*(\1)' %i, line):
#         i += 1
#     return i-1

"""great too"""
# def double_substring(line):
#     n = len(line)
#     return max((len(line[i:j]) for i in range(n)
#                                for j in range(i+1, n+1)
#                                if line.count(line[i:j]) > 1), default=0)

"""Actually, it’s (?=(.).\1). Dont’s forget the external brackets.
. - any symbol except ‘\n’
* - 0 or more repetitions of the previous symbol
.* - several symbols
(.*) - brackets are a capturing group. It is used to catch and “memorize” what we matched inside the brackets
(a repeating substring we are looking for)
next .* means that there might be any number (including 0) of symbols between the repetitions
\1 means the same string we found in the first capturing group (our substring).
(?=pattern) - is a positive lookahead. It matches if pattern matches next, but doesn’t consume any of the string.
In terms of our task it helps us to find all the repeating substrings. If we typed just '(.*).*\1’
(without the lookaround), we would find only the first repeating substring, because it would consume some parts
of the string and wouldn’t be able to find the other repeating substrings."""
# import re
# def double_substring(line):
#     return max(map(len, re.findall(r'(?=(.*).*\1)', line)))
