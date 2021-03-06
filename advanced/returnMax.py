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
        if (g1[i1] + g2[i2]) > (g2[i2] + g1[i1]):
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


def solution(numbers):
    list = [str(n) for n in numbers]
    
    mergeSort(list)
    
    return ''.join(list)


a = [3, 30, 34, 5, 9]
print(solution(a))