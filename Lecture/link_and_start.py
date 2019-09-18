n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def go(index, first, second):
    if index == n:
        if len(first) == 0 or len(second) == 0: return -1

        t1 = t2 = 0

        for p1 in fisrt:
            for p2 in first:
                if p1 == p2: continue
                t1 += s[p1][p2]
        
        for p1 in second:
            for p2 in second:
                if p1 == p2: continue
                t2 += s[p1][p2]
            
        diff = abs(t1 - t2)

        return diff
    
    res = -1

    t1 = go(index + 1, first + [index], second)
    if res == -1 or (t1 != -1 and t1 < res):
        res = t1

    t2 = go(index + 1, first, second + [index])
    if res == -1 or (t2 != -1 and t2 < res):
        res = t2

    return res

print(go(0, [], []))