def solution(progresses, speeds):
    res = []
    done = 0
    
    while done != len(progresses):
        ready = []
        
        for i in range(done, len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
        
        j = done
        for i in range(j, len(progresses)):
            if progresses[i] < 100:
                break
            else:
                ready.append(i)
                done = i+1
                
                
        if len(ready) != 0:
            res.append(ready)
            
    return [len(j) for j in res]