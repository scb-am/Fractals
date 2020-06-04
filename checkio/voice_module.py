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


# FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
#              "eight", "nine"]
# SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
#               "sixteen", "seventeen", "eighteen", "nineteen"]
# OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
#               "eighty", "ninety"]
# HUNDRED = "hundred"
#
#
# def checkio(number):
#
#     n = number // 100
#     t = [FIRST_TEN[n-1], HUNDRED] if n > 0 else []
#
#     n = (number // 10) % 10
#     t += [OTHER_TENS[n-2]] if n > 1 else []
#
#     n = number % (10 if n > 1 else 20)
#     t += [(FIRST_TEN+SECOND_TEN)[n-1]] if n > 0 else []
#
#     return ' '.join(t)


# def checkio(number):
#     l=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
#     d=dict(enumerate(l))
#     d.update({30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety"})
#     h=number//100
#     if h:
#         return (d[h]+" hundred "+checkio(number%100)).strip()
#     if number in d:
#         return d[number]
#     return d[number//10*10]+" "+d[number%10]


# def checkio(number):
#     # I wanted to take a special approach approach with this function and make a POC of the less ligne as possible
#
#     # Turning them into dict so that we can use its .get() method and never have some IndexError
#     spe = dict(enumerate(('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
#                           'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')))
#     decades = dict(enumerate(('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')))
#
#     # [::-1] so that the key for the unit is always 0
#     # [-2:] ignore the hundred if necessary
#     return (lambda r: r if r else 'zero')(' '.join(filter(lambda p: p, [(spe.get(d.get(2)), 'hundred' * bool(d.get(2)),
#                                                                          decades.get(d.get(1)), spe.get(
#         d.get(0) + 10 * (10 <= int(str(number)[-2:]) < 20))) for d in (dict(enumerate(map(int, str(number)[::-1]))),)][
#         0])))

    # Note: spe and decades could also have been included in the one line but I prefer it this way. Note2: I'm sure this could be shortened again :p



# def checkio(n, d=dict(enumerate(" one two three four five six seven eight nine ten eleven twelve".split(" ")))):
#     def i(s, j=iter("o en ree ir ve f t ".split(" "))):
#         for k in j: s = __import__("re").sub(k + "$", next(j), s)
#         return s
#     return(d[n//100]+" hundred "*(n>99)+d.get(n%100,n%100<20and i(d[n%10])+"teen"or i(d[n//10%10]).replace("u","")+"ty "+d[n%10])).strip()


print(checkio(19))