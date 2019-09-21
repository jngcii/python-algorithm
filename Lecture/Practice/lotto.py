a = list(map(int, input().split()))

n = len(a)


def go(index, list, a, n):
    if len(list) == 6:
        print(''.join(map(str, list)))
        return

    if index == n: return

    go(index+1, list, a, n)
    go(index+1, list+[a[index]], a, n)

go(0, [], a, n)