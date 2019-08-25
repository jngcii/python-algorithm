def qSort(arr, left, right):
    if right - left <= 0: return
    
    i = left
    pivot = arr[right]
    
    for j in range(left, right):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1
    
    arr[i], arr[right] = arr[right], arr[i]
    
    qSort(arr, left, i-1)
    qSort(arr, i+1, right)

def solution(array, commands):
    res = [0,0,0]
    k = 0
    
    for c in commands:
        head = c[0]-1
        tail = c[1]
        num = c[2]-1
        
        arr = array[head:tail]
        
        qSort(arr, 0, len(arr)-1)
        
        res[k] = arr[num]
        k += 1
        
    return res
        
        
            

array = [1, 5, 2, 6, 3, 7, 4]
cmd = 	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, cmd))