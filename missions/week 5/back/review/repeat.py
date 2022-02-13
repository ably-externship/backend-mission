import re
from collections import Counter

def is_reapeated(mes):
    mes_total = ""
    mes_total += re.sub(r'[^\w]', ' ', mes)
    count = Counter(mes_total)
    res=dict(count)
    li=list(res.values())
    li.sort()
    cnt = 0
    for i in range(len(li)-1):
        if li[i]>7 and li[i] == li[i+1]:
            cnt += 1
    cnt = cnt+1
    if cnt > 2:
        return True
    return False