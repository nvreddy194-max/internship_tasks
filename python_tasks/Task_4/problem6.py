# 6
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = list(map(int, input().split()))

scores = sorted(set(arr))
print(scores[-2])
