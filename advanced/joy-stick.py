def solution(name):
    cnt = 0
    i=0
    while True:
        if i == len(name): break
        print(name, name[i], i)
        n = name[i]
        if ord("Z")+1-ord(n)<ord(n)-ord("A"):
            sub = ord("Z")+1 - ord(n)
        else:
            sub = ord(n)-ord("A")
        cnt = cnt + sub + 1

        if i+1 == 0:
            i = len(name)
            continue
        elif i+1 == len(name) or "A" not in name[i+1:]:
            i+=1
            continue
        else:
            c = 1
            while name[i+c] == "A":
                c += 1
                
            cc = 1
            while i-cc + len(name) > i+c:
                cc += 1
            
            if cc > c: i += c
            else: i -= cc
        
    return cnt -1

solution("JAN")