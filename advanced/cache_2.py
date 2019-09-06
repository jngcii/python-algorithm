def solution(cacheSize, cities):
    result = 0
    cache = []
    cities.reverse()
    if cacheSize == 0: return len(cities)*5
    
    while cities:
        p = cities.pop()
        if p.lower() in cache:
            cache.remove(p.lower())
            result += 1
        else:
            if len(cache)>=cacheSize: cache.pop(0)
            result += 5
        cache.append(p.lower())
            
    return result