n = int(input())

def go(n):
    if n == 0: return 1
    elif n == 1: return 1
    elif n == 2: return 2
    else:
        return go(n-1) + go(n-2) + go(n-3)

print(go(n))