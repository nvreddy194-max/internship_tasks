# 20
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

n = int(input())

for _ in range(n):
    mobile = input()

    if re.fullmatch(r'[789]\d{9}', mobile):
        print("YES")
    else:
        print("NO")
