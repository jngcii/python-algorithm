n = int(input())

def go(x):
    if x == 1: return 1
    if x == 2: return 2

    return go(x-1) + go(x-2)

print(go(n))