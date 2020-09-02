import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

alist=[
    "something1",
    "something12",
    "something17",
    "something2",
    "something25",
    "something29"]

alist.sort(key=natural_keys)
print(alist)


'''
variant 2
'''

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in text.split(' ') ]

alist=[
    "text 2020 part 25",
    "text 2020 part 21",
    "text 2020 part 2",
    "text 2019 part 10",
    "text 2020 part 1",
    "text 2020 part 100",
    "text 2020 part 10",
    "text 2019 part 1",
    "text 2019 part 2"]

alist.sort(key=lambda x: [int(c) if c.isdigit() else c for c in x.split(' ')])
print(alist)
