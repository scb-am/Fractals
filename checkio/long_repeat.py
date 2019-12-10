import re

def long_repeat(line: str) -> int:
    return len(max([x.group() for x in re.compile(r'(.)\1*').finditer(line)], key=len))if line else 0


print(long_repeat('hfjjfgfffffssdh bvere'))