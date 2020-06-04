def and_f(a, b):
    return 1 if a == b == '1' else 0

def or_f(a, b):
    return 1 if a == '1' or b == '1' else 0

def xor_f(a, b):
    return 0 if a == b else 1

def print_head(x, y, column_len):
    text = f'\u007B:^{(column_len * 4 + 1) * 3 + 10}s\u007D'
    print('-' * ((column_len * 4 + 1) * 3 + 10))
    print(text.format(f'{x} + {y} ='))
    print('-' * ((column_len * 4 + 1) * 3 + 10))
    print('\n')

def print_head_title(title, column_len):
    text = f'\u007B:*^{column_len * 4 + 1}s\u007D'
    return text.format(title)

def print_column_names(column_data, column_len):
    text = ''.join([f'|\u007B{x}:^3\u007D' for x in range(column_len)]) + '|'
    data = ['X'] + column_data + ['dec', 'sum']
    return text.format(*data)

def print_row(row_data, column_len):
    text = ''.join([f'|\u007B{x}:^3\u007D' for x in range(column_len)]) + '|'
    data = row_data
    return text.format(*data)

def print_result(result, column_len):
    text = f'\u007B:^{(column_len * 4 + 1) * 3 + 10}s\u007D'
    print('\n')
    print('-' * ((column_len * 4 + 1) * 3 + 10))
    print(text.format(f'{result[0]} + {result[1]} + {result[2]} = {sum(result)}'))
    print('-' * ((column_len * 4 + 1) * 3 + 10))




def checkio(x, y):
    column_len = len(str(bin(y))) + 1
    y_data = [x for x in str(bin(y))[2:]]
    x_data = [x for x in str(bin(x))[2:]]

    print_head(x, y, column_len)
    switcher = {
        'AND': [[and_f(x, y) for y in y_data] for x in x_data],
        'OR': [[or_f(x, y) for y in y_data] for x in x_data],
        'XOR': [[xor_f(x, y) for y in y_data] for x in x_data],
    }
    result = []

    head_title = []
    column_names = []
    table_rows = []

    for operation in ['AND', 'OR', 'XOR']:
        and_table_data = switcher[operation]
        head_title.append(print_head_title(operation, column_len))
        column_names.append(print_column_names(y_data, column_len))
        for row in and_table_data:
            row.extend([int("0b" + "".join([str(x) for x in row]), 2), ''])
        total = sum([x[-2] for x in and_table_data])
        and_table_data[len(x_data) // 2][-1] = total
        result.append(total)
        table_rows.append([print_row([x[0]] + x[1], column_len) for x in zip(x_data, and_table_data)])

    print('     '.join(head_title))
    print(('-' * (column_len * 4 + 1) + '     ') * 3)
    print('     '.join(column_names))
    print(('-' * (column_len * 4 + 1) + '     ') * 3)
    for i in range(len(table_rows[0])):
        print('     '.join([x[i] for x in table_rows]))
        if i < len(table_rows[0]) - 1:
            print(('-' * (column_len * 4 - 3) + '         ') * 3)
        else:
            print(('-' * (column_len * 4 + 1) + '     ') * 3)

    print_result(result, column_len)


    return sum(result)


checkio(10, 100)
