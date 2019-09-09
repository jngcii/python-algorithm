def solution(n, bf):
    
    for idx, f in enumerate(bf):
        bf[idx] = f[:-1]
    
    for i in range(1, len(bf)):
        if bf[i] in bf[:i]:
            bf[i] = "0"
            
    bf = [f for f in bf if f!= "0"]
    
    bf.sort(key=lambda x : (x[0], x[1], x[2]))

    print(bf)
    
    looping = True
    while looping:
        
        for i in range(len(bf)-1):
            
            if bf[i][2] == 0:
                if bf[i+1][0] != bf[i][0] or bf[i+1][1] != bf[i][1]+1:
                    bf.pop(i+1)
                    looping = True
                    break
            
            elif bf[i][2] == 1:
                if bf[i+1][0] != bf[i][0]+1 or bf[i+1][1] != bf[i][1]:
                    bf.pop(i+1)
                    looping = True
                    break
                    
            looping = False

    print(bf)

solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]])