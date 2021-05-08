def digit_converter(l_symbol, m_symbol, h_symbol, num):
    num = int(num)
    if 1 <= num <= 3:
        return l_symbol * num
    elif num == 4:
        return f'{l_symbol}{m_symbol}'
    elif 5 < num <= 8:
        return f'{m_symbol}{l_symbol * num}'
    elif num == 9:
        return f'{l_symbol}{h_symbol}'
    elif num == 5:
        return m_symbol
    return ''


VALUES_DICT = {
    4: lambda x: digit_converter('M', '', '', x),
    3: lambda x: digit_converter('C', 'D', 'M', x),
    2: lambda x: digit_converter('X', 'L', 'C', x),
    1: lambda x: digit_converter('I', 'V', 'X', x),
}


def converter(year: int):
    converted_year = ""
    year = str(year)
    while year:
        converted_year += VALUES_DICT[len(year)](year[0])
        year = year[1:]
    return converted_year


print(converter(1954))
