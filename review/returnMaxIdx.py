def returnMaxIdx(a):

    length = len(a)

    if length<0:

        return -1

    else :
        
        max = 0

        for i in range(1, length):

            if a[i] > a[max] : max = i

        return max


arr = [1,4,6,2,3,9,18,3]

print(returnMaxIdx(arr))
    
