def solution(heights):
    answer = [0 for i in heights]
    
    for i in range(1, len(heights)):
        
        for j in range(i-1, -1, -1):
            if i < j: answer[i] = j 
    
    return answer

