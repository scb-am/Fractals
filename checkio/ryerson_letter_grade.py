# feel free to change table structure in any way

TABLE = '''
A 85-89%
A- 80-84%
B+ 77-79%
B 73-76%
B- 70-72%
C+ 67-69%
C 63-66%
C- 60-62%
D+ 57-59%
D 53-56%
D- 50-52%
'''

def ryerson_letter_grade(pct: int) -> str:

    return (([k for k, v in {
        x[1:3].strip(): x[-5:].split('-') for x in TABLE.split('%')[:-1]
    }.items() if int(v[0]) <= pct <= int(v[1])][:1] or [None])[0] or "F") if pct < 90 else "A+"


# GRADE = ['F']*50 + ['D-']*3 + ['D']*4  + ['D+']*3 + ['C-']*3 + \
#         ['C']*4  + ['C+']*3 + ['B-']*3 + ['B']*4  + ['B+']*3 + \
#         ['A-']*5 + ['A']*5  + ['A+']*11
#
# ryerson_letter_grade = lambda percent: GRADE[min(percent, 100)]


# LETTERS = [ch + sign for ch in 'ABCD' for sign in ('+','','-')] + ['F']
# MIN_PERCENTAGES = [90, 85, 80, 77, 73, 70, 67, 63, 60, 57, 53, 50, 0]
#
# ryerson_letter_grade = lambda pct: next(ch for ch, p in zip(LETTERS, MIN_PERCENTAGES) if pct >= p)


print(ryerson_letter_grade(54))
print(ryerson_letter_grade(45))
print(ryerson_letter_grade(107))
print(ryerson_letter_grade(62))
