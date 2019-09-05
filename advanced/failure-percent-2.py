def solution(N, stages):
    d = dict()
    res = []
    for n in range(1, N+1):
        d[n] = 0
    
    for stage in stages:
        if stage in d.keys():
            d[stage] += 1
    
    for key, value in d.items():
        cnt = 0
        for stage in stages:
            if stage >= key: cnt += 1
        if cnt == 0:
            d[key] = 0
        else:
            d[key] = value/cnt
        res.append((key, d[key]))
            
    res.sort(key = lambda x : -x[1])
    
    return [r[0] for r in res]