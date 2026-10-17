# 19
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    current_weight = 0
    previous_char = ''

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous_char:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous_char = char

    return ["Yes" if q in weights else "No" for q in queries]


if __name__ == '__main__':
    s = input().strip()
    n = int(input())

    queries = []
    for _ in range(n):
        queries.append(int(input()))

    result = weightedUniformStrings(s, queries)

    for answer in result:
        print(answer)
