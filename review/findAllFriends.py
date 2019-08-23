def findAllFriends(group, i):

    que = []
    done = set()

    que.append(i)
    done.add(i)

    while que:
        p = que.pop(0)
        print(p)

        for x in group[p]

            if x not in done:

                que.append(x)
                done.add(x)
