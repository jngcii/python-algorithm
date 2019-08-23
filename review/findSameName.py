def findSameName(a):

    dic = dict()

    for x in a:

        if x in dic:

            dic[x] += 1

        else:

            dic[x] = 1

    res = set()

    for x in dic:

        if dic[x] >= 2:

            res.add(x)

    return res


a = ["Tom", "Mike", "Jngcii", "Tom", "Tony", "Benny", "Hulk", "Tony"]

print(findSameName(a))