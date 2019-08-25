def solution(answers):
    
    p = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    
    cnt = [0,0,0]
    
    for idx, a in enumerate(answers):
        for i in range(3):
            if a == p[i][idx%len(p[i])]: cnt[i] += 1
    

    print(cnt)




a = [1,3,2,4,2]
solution(a)