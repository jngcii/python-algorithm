from itertools import combinations

def solution(table):
    result = 0
    table_length = table[0].__len__()
        
    combi = []
    for i in range(table_length):
        c = list(combinations([idx for idx in range(table_length)], i+1))
        combi += c
        
    while combi:
        c = combi.pop(0)
        comparer=[]
        for line in table:
            key = ""
            for i in c:
                key += line[i]
            comparer.append(key)
            
        comparer.sort()
        
        possible = True
        for i in range(len(comparer)-1):
            if comparer[i] == comparer[i+1]:
                possible = False
                break
                
        if possible == True:
            result += 1
            combi = [com for com in combi if set(c) & set(com) != set(c)]
        
    return result