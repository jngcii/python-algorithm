def solution(n, lost, reserve):
    cnt = {}
    res = 0

    for i in range(1, n+1):
        cnt[i] = 1
        
    for i in reserve:
        cnt[i] += 1
        
    for i in lost:
        cnt[i] -= 1
        
    for key in cnt.keys():
        print("before", cnt)
        if cnt[key] == 2:
            if key != n:
                if cnt[key+1] == 0:
                    cnt[key] -= 1
                    cnt[key+1] += 1
                    print(cnt)
                    continue
            if key != 1:
                if cnt [key-1] == 0:
                    cnt[key] -= 1
                    cnt[key-1] += 1
                    print(cnt)
                    continue

    for v in cnt.values():
        if v == 0:
            res += 1

    return n - res

        
n = 10
lost = [1,2,3,4,6,7,8]
reserve = [5,8,9,10]

print(solution(n, lost, reserve))