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


def check(a, nums):
    for i in range(len(a)):
        if a[i] == "<" and nums[i] > nums[i+1]: return False
        elif a[i] == ">" and nums[i] < nums[i+1]: return False
    
    return True


n = int(input())
a = list(input().split())

big = [str(i) for i in range(10-n-1, 10)]
small = [str(i) for i in range(0, n+1)]

big_res = '0'*(n+1)
small_res = '9'*(n+1)


if check(a, big): big_res = max(big_res, ''.join(big))
while next_permutation(big):
    if check(a, big): big_res = max(big_res, ''.join(big))

if check(a, small): small_res = min(small_res, ''.join(small))
while next_permutation(small):
    if check(a, small): small_res = min(small_res, ''.join(small))


print(big_res)
print(small_res)