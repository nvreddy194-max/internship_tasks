# 12
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    s = input()
    print(solve(s))
