# 19
# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter

X = int(input())
shoe_sizes = list(map(int, input().split()))

shoes = Counter(shoe_sizes)

N = int(input())
total = 0

for _ in range(N):
    size, price = map(int, input().split())

    if shoes[size] > 0:
        total += price
        shoes[size] -= 1

print(total)
