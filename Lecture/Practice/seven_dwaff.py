import sys

a = list(map(int, input().split()))

def go(a, index, result, sum):

    if sum == 100:
        print(sorted(result))
        sys.exit(0)

    if index == 9:
        return

    go(a, index+1, result + [a[index]], sum + a[index])

    go(a, index+1, result, sum)


go(a, 0, [], 0)