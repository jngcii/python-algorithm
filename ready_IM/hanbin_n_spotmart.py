tc = int(input())

for cnt in range(tc):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    mx = -1

    for i in range(n-1):

        for j in range(i+1, n):

            cur = a[i] + a[j]

            if cur <= m and cur >= mx:

                mx = cur
            
    print('#'+str(cnt+1)+" "+str(mx))