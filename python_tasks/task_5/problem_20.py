# 20
# https://www.hackerrank.com/challenges/piling-up/problem
from collections import deque

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))

    top = float('inf')
    possible = True

    while blocks:
        if blocks[0] >= blocks[-1]:
            current = blocks.popleft()
        else:
            current = blocks.pop()

        if current > top:
            possible = False
            break

        top = current

    print("Yes" if possible else "No")
