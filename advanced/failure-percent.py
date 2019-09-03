def solution(N, stages):
    res = []

    for i in range(1, N+1):
        done = 0
        ing = 0
        for stage in stages:
            if stage >= i:
                done += 1
            if stage == i:
                ing += 1
        if done == 0:
            res.append((i, 0))
        else:
            res.append((i, ing/done))

    res = sorted(res, key = lambda x : (-x[1], x[0]))

    return [i for (i,j) in res]