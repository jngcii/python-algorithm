def solution(n, weak, dist):
    
    result = 0
    
    while weak and dist:
        maxim = max(dist)
        print(maxim, weak)
    
        for i in range(len(weak)-1, -1, -1): # 제일 긴것부터 찾기
            sub = -1 #긴것중에도 제일 긴걸 찾아야 하므로 표시
            j_idx = -1 #긴것중에 찾으면 요 인덱스에 표시
            removal = []
            
            for j in range(len(weak)): #어떤게 제일 길면서 조건에 맞는지 찾기
                w = weak[j] - weak[j-i]
                print(j)
                if w >= 0:
                    if maxim >= w:
                        if sub < w:
                            sub = w
                            j_idx = j
                else:
                    if maxim >= n + w:
                        if sub < n + w:
                            sub = n + w
                            j_idx = j
            
            print("j_idx:", j_idx)
            if j_idx != -1:
                for k in range(i+1):
                    removal.append(weak[j_idx - k])
                print(removal)
                for re in removal:
                    weak.remove(re)
                dist.remove(maxim)
                result  += 1
                break
                    
    return result

solution(12, [1,5,6,10], [1,2,3,4])