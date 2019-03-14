def find_element(n):

    arr = [12,4,3,15,7,55,23,12,6,7,13,12]

    res = []

    cnt = len(arr)

    for i in range(cnt):

        if arr[i] == n:

            res.append(i)

    print("{}는 배열{}에 위치해 있습니다.".format(n, res))



find_element(12)
