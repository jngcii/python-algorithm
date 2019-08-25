def mergeSort(arr):

    n = len(arr)

    if n<= 1: return

    mid = n // 2

    g1 = arr[:mid]
    g2 = arr[mid:]

    mergeSort(g1)
    mergeSort(g2)

    i1 = 0
    i2 = 0
    ia = 0

    while i1 <len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            arr[ia] = g1[i1]

            i1 += 1
            ia += 1

        else :
            arr[ia] = g2[i2]

            i2 += 1
            ia += 1

    while len(g1) > i1:
        arr[ia] = g1[i1]
        i1 += 1
        ia += 1

    while len(g2) > i2:
        arr[ia] = g2[i2]
        i2 += 1
        ia += 1

def solution(citations):

    
    if len(citations) == 1 and citations[0] == 0 : return None

    mergeSort(citations)


    for i in range(len(citations)-1, -1, -1):
        cnt = i+1

        if len(citations) == cnt:
            if citations[0] >= cnt: return cnt
        
        if citations[-cnt] >= cnt:
            return cnt


a = [3, 0, 6, 1, 5]

print(solution(a))