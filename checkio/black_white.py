def count_b_w(string):
    string_a, string_b = list(string), list(string)
    string_a[string.find('b')], string_b[string.rfind('w')] = 'w', 'b'
    return string.count('b') / len(string), ''.join(string_a), string.count('w') / len(string), ''.join(string_b)


def checkio(string, num):
    if num > 1 or string == 'w':
        result_list = [[string, 1]]
        for _ in range(num - 1):
            new_result_list = []
            for i in result_list:
                black_count, str1, white_count, str2 = count_b_w(i[0])
                new_result_list.append([str1, black_count * i[1]])
                new_result_list.append([str2, white_count * i[1]])
            result_list = new_result_list
        return round(sum([x[1] * x[0].count('w') / len(x[0]) for x in result_list]), 2)
    return 0



print(checkio("wwww", 20))