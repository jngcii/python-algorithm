def merge_sort(a):

    cnt = len(a)

    if cnt <= 1:
        return

    mid = cnt // 2

    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i_of_g1 = 0
    i_of_g2 = 0
    i_of_a = 0

    while i_of_g1 < len(g1) and i_of_g2 < len(g2):

        if g1[i_of_g1] > g2[i_of_g2]:

            a[i_of_a] = g1[i_of_g1]

            i_of_a += 1

            i_of_g1 += 1

        else:

            a[i_of_a] = g2[i_of_g2]

            i_of_a += 1

            i_of_g2 += 1

    while i_of_g1 < len(g1):

        a[i_of_a] = g1[i_of_g1]

        i_of_a += 1

        i_of_g1 += 1

    while i_of_g2 < len(g2):

        a[i_of_a] = g2[i_of_g2]

        i_of_a += 1

        i_of_g2 += 1





a = [2,6,8,3,7,5,4,1,9,10]
merge_sort(a)
print(a)
