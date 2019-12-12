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
