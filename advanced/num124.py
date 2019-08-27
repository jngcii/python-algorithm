import math

def solution(n):
    res = ""

    i = 1
    x = 3**i

    while x<n:
        i += 1
        x = x + 3**i

    nnn = n - (x - 3**i)

    i -= 1

    while i>=0:
        r = math.ceil(nnn/(3**i))
        nnn %= (3**i)

        if r == 1: res += "1"
        elif r == 2: res += "2"
        else: res += "4"

        i -= 1

    return res