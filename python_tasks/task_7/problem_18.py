# 18
# https://www.hackerrank.com/challenges/string-construction/problem

def stringConstruction(s):
    return len(set(s))


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        s = input().strip()
        print(stringConstruction(s))
