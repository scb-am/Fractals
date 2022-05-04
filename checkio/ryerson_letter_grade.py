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


print(ryerson_letter_grade(54))
print(ryerson_letter_grade(45))
print(ryerson_letter_grade(107))
print(ryerson_letter_grade(62))
