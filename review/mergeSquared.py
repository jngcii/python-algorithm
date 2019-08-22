def mergeSquared(n):

    res = 0

    if n>=1:

        for i in range(1, n+1):

            res += i * i

    

    return res

res = mergeSquared(5)

if res == 0: print("잘못 입력하셨습니다.")

else: print(res)