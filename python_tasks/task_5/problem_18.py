# 18
# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
