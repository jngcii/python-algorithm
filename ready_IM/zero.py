n = int(input())

for cnt in range(1, n+1):

    k = int(input())

    a = []

    for _ in range(k):

        new = int(input())

        if new == 0:
            a.pop()
        else:
            a.append(new)

    print('#{} {}'.format(cnt, sum(a)))