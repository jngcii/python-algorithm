n = int(input())

times = []

for _ in range(n):
    s, e = map(int, input().split())
    times.append((s,e))

times.sort(key = lambda x : (x[1], x[0]))

e_time = 0
cnt = 0

for t in times:
    if t[0] >= e_time:
        e_time = t[1]
        cnt += 1

print(cnt)