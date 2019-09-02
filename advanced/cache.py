def solution(cacheSize, cities):

    res = 0
    cache = []
    
    if cacheSize == 0: return len(cities)*5
    
    for c in cities:
        if c.lower() in cache:
            res += 1
            cache.append(cache.pop(cache.index(c.lower())))
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(c.lower())
            res += 5
                
    return res