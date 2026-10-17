# 13
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(Counter(s).values())
    
    if len(freq) == 1:
        return "YES"
    
    if len(freq) == 2:
        (f1, c1), (f2, c2) = freq.items()
        
        # One character appears once; remove it
        if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
            return "YES"
        
        # One character occurs one extra time
        if abs(f1 - f2) == 1:
            if (f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1):
                return "YES"
    
    return "NO"


if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
