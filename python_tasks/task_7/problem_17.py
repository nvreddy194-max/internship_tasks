# 17
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    n = len(s)

    for i in range(1, n // 2 + 1):
        first = s[:i]

        if first[0] == '0':
            continue

        num = int(first)
        current = first

        while len(current) < n:
            num += 1
            current += str(num)

        if current == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
