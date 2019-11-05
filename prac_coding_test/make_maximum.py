def merge_sort(a):

    cnt = len(a)

    if cnt <= 1:
        return a

    mid = cnt // 2

    a1 = merge_sort(a[:mid])
    a2 = merge_sort(a[mid:])

    result = []

    while a1 and a2:

        if a1[0]+a2[0] > a2[0]+a1[0]:

            result.append(a1.pop(0))

        else:

            result.append(a2.pop(0))

    while a1:

        result.append(a1.pop(0))

    while a2:

        result.append(a2.pop(0))

    return result

def solution(numbers):
    numbers = [str(number) for number in numbers]
    
    if int(''.join(numbers)) == 0: return "0"
    
    numbers.sort()
    
    res = ''
    
    while numbers:
        tmp = numbers.pop()
        a = [tmp]
        
        while numbers and numbers[-1][0] == a[-1][0]:
            a.append(numbers.pop())
            
        a = merge_sort(a)
            
        res += ''.join(a)
        
    return res