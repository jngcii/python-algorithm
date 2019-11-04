def go(a):
    global result

    maximum = 0
    j = 0
    for i in range(1, len(a)-1):
        if maximum < a[i-1]*a[i+1]:
            maximum = a[i-1]*a[i+1]
            j = i

    result += maximum
    a.pop(j)

n = int(input())
a = list(map(int, input().split()))

result = 0

while len(a)>=3:
    go(a)

print(result)