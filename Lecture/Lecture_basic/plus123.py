res = 0

def go(sum):
    global res
    if sum == 10:
        res += 1
        return

    if sum > 10: return

    for i in range(1,4):
        go(sum + i)


sum = 0
go(sum)

print(res)