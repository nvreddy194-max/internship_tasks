# 16
# https://www.hackerrank.com/challenges/caesar-cipher-1/problem

def caesarCipher(s, k):
    result = ""
    k = k % 26

    for char in s:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + k) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + k) % 26 + ord('A'))
        else:
            result += char

    return result


if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    k = int(input())

    print(caesarCipher(s, k))
