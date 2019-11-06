def solution(routes):
    res = 1
    
    n = len(routes)
    
    # routes.sort(key=lambda x : x[1]-x[0])
    routes.sort(key=lambda x : x[1])
    
    c = [False] * n
    
#     for i in range(n):
#         if c[i]: continue
        
#         for j in range(i, n):
#             if routes[j][1] >= routes[i][0] and routes[j][0] <= routes[i][1]:
#                 c[j] = True
        
#         res += 1

    i = 1
    end = routes[0][1]
    
    while i < n:
        if routes[i][0] <= end:
            i += 1
        else:
            res += 1
            end = routes[i][1]
            i += 1
        
        
    return res