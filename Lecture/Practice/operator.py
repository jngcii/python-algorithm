# def next_permutation(a):
    
#     i = len(a) -1

#     while i > 0 and a[i-1] >= a[i]: i -= 1
    
#     if i == 0: return False

#     j = len(a) - 1

#     while j > i-1 and a[j] < a[i]: j -= 1

#     a[j], a[i-1] = a[i-1], a[j]

#     j = len(a) - 1

#     while i < j:
#         a[j], a[i] = a[i], a[j]
#         i += 1
#         j -= 1

#     return True


a = list(map(int, input().split()))

mm, ss, xx, dd = map(int, input().split())

result = []


def go(index, a, res, mer, sub, mul, div):
    if not res: return

    global result

    if mer == 0 and sub == 0 and mul == 0 and div == 0:
        result.append(res)

    if mer > 0: go(index+1, a, res + a[index], mer-1, sub, mul, div)

    if sub > 0: go(index+1, a, res - a[index], mer, sub-1, mul, div)

    if mul > 0: go(index+1, a, res * a[index], mer, sub, mul-1, div)

    if div > 0: 
        if res >= 0:
            go(index+1, a, res // a[index], mer, sub, mul, div-1)
        else:
            go(index+1, a, -(-res // a[index]), mer, sub, mul, div-1)


go(1, a, a[0], mm, ss, xx, dd)

print(max(result), min(result))