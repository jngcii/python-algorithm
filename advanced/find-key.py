from itertools import combinations

def solution(relation):
    
    result = 0
    
    cln = [i for i in range(len(relation[0]))]
    
    possible = []
    
    for i in range(1, len(relation[0])):
        com = list(combinations(cln, i))
        possible += com
        
    
    while possible:
        p = possible.pop(0)
        comparer = []
        is_key=True
        for x in relation:
            s = ""
            for i in list(p):
                s+=x[i]
            if s in comparer:
                is_key = False
                break
            else:
                comparer.append(s)
        
        if is_key == True:
            result += 1
            possible = [po for po in possible if (set(p) & set(po)) != set(p)]
    
    return result