# 14
# https://www.hackerrank.com/challenges/py-set-add/problem
n = int(input())
countries = set()

for i in range(n):
    country = input().strip()
    countries.add(country)

print(len(countries))
