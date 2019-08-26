def solution(s, n):
    arr = list(s)
    for idx, i in enumerate(arr):
        if i != " ":
            if (ord(i)<91 and ord(i)+n>=91) or (ord(i)<123 and ord(i)+n>=123) :
                arr[idx] = chr(ord(i)+n-26)
            else: 
                arr[idx] = chr(ord(i)+n)

    return ''.join(arr)