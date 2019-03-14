def quick_sort(a):

    cnt = len(a)

    if cnt <= 1:

        return a

    pivot = a[-1]

    g1 = []
    g2 = []

    for i in range(0, cnt-1):

        if a[i] < pivot:

            g1.append(a[i])

        else:

            g2.append(a[i])

    return quick_sort(g1) + [pivot] + quick_sort(g2)



a = [12,14,54,75,53,1,44,399,3]
inst = quick_sort(a)
print(inst)
