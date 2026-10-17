# 4
#  https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    r = s[::-1]

    for i in range(1, len(s)):
        diff1 = abs(ord(s[i]) - ord(s[i - 1]))
        diff2 = abs(ord(r[i]) - ord(r[i - 1]))

        if diff1 != diff2:
            return "Not Funny"

    return "Funny"


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        print(funnyString(s))
