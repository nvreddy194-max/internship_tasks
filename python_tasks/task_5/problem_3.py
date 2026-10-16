# 3
# https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    result = mutate_string(s, int(i), c)
    print(result)
