def exploreGraph(g):

    que=["1"]

    print(que[0])

    while que:

        p = que.pop(0)

        for i in g[p]:

            print(i)

            que.append(i)


graph = {"1":["2","3"], "2": ["4","5"], "3":[], "4": [], "5": []}

exploreGraph(graph)