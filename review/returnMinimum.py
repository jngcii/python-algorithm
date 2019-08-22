def returnMinimum(a):

    print(a)

    m = a[0]

    for i in range(1,len(a)):

        if a[i] < m:

            m = a[i]

    return m


def checkInputDigit(num):

    inputable = num.isdigit()

    while not inputable:
        print("다시 입력해 주세요 : ")
        num = input()

        inputable = num.isdigit()
        if not inputable : continue

        if int(num) < 1:
            inputable = False
            continue

    return num




print("리스트의 길이를 입력하세요 (종료 : 0) : ")
num = input()

checkedN = checkInputDigit(num)

n = int(checkedN)

if n==0: 
    print("종료.")

else:
    arr = []
    for i in range(0, n):
        print("a[", i, "] (자연수만) : ")
        originInput = input()

        checkedN = checkInputDigit(originInput)

        newInput = int(checkedN)
        arr.append(newInput)
    res = returnMinimum(arr)
    print(res)
