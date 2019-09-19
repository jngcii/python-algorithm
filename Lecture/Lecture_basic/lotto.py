def solve(a, lotto, index):
    if len(lotto) == 6:
        print(''.join(map(str,lotto)))
        return

    if index == 6: return

    solve(a, lotto+[a[index]], index+1)
    solve(a, lotto, index+1)


a = map(int, input().split())

solve(a, [],  0)