def next_permutation(a):
    i = len(a) - 1
    while i>0 and a[i] <= a[i-1]: i -= 1

    if i <= 0: return False

    j = len(a) - 1
    while a[j] <= a[i-1]: j -= 1

    a[j], a[i-1] = a[i-1], a[j]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    
    return True


def calc(operators, numbers):
    res = numbers[0]
    for i in range(len(operators)):
        if operators[i] == 0:
            res += numbers[i+1]
        elif operators[i] == 1:
            res -= numbers[i+1]
        elif operators[i] == 2:
            res *= numbers[i+1]
        else:
            if res < 0 and numbers[i+1] >= 0:
                r1 = (-res) // numbers[i+1]
                res = -r1
            elif res >= 0 and numbers[i+1] < 0:
                r2 = res // (-numbers[i+1])
                res = -r2
            elif res < 0 and numbers[i+1] < 0:
                res = (-res)//(-numbers[i+1])
            else:  
                res //= numbers[i+1]
    
    return res


n = int(input())

numbers = list(map(int, input().split()))

op_cnts = list(map(int, input().split()))

operators=[]

f = 0
for o in op_cnts:
    for _ in range(o):
        operators.append(f)
    f += 1

# 0:+ 1:- 2:x 3:/

big=-10000000000
small=10000000000

res = calc(operators, numbers)
big = max(big, res)
small = max(small, res)

while next_permutation(operators):
    res = calc(operators, numbers)
    big = max(big, res)
    small = min(small, res)
    
print(big)
print(small)

