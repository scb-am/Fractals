ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
switcher = {
    3: lambda x: ones[x] + 'hundred ',
    2: lambda x: twenties[x],
    1: lambda x: ones[x],
}

def checkio(num):
    string = str(num)
    result = ''
    for i in range(len(string)):
        if len(string) - i == 3:
            result += switcher[3](int(string[i]))
        elif len(string) - i == 2:
            if 19 >= int(string[-2:]) > 9:
                if switcher[1](int(string[-2:])) and int(string[-2:]) > 9:
                    print('!!!!! - ', switcher[1](int(string[-2:])))
                    result += switcher[1](int(string[-2:]))
                    break
            else:
                result += switcher[2](int(string[i]))
        else:
            result += switcher[1](int(string[i]))
    return result.strip(' ')


print(checkio(19))