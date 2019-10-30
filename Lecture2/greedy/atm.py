n = int(input())
times = list(map(int, input().split()))

times.sort()

res = [times[0]]*n

for i in range(1, n):
    res[i] = res[i-1] + times[i]

print(sum(res))