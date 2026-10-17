# 6
# https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())

    if len(letters.intersection('abcdefghijklmnopqrstuvwxyz')) == 26:
        return "pangram"
    else:
        return "not pangram"


if __name__ == '__main__':
    s = input()
    print(pangrams(s))
