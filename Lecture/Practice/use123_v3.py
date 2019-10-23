n = int(input())

def go(x, l):
    if x == 0: return 1
    elif x == 1: return 1
    elif x == 2: return 1

    else:
        if l == 1:
            return go(x-1, 2) + go(x-1, 3)
        elif l == 2:
            return go(x-2, 3) + go(x-2, 1)
        elif l == 3:
            return go(x-3, 1) + go(x-3, 2)



go(n, 1) + go(n, 2) + go(n, 3)