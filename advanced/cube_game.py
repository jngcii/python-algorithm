def solution(m, n, board):
    li = []
    res = 0
    
    while True:
        
        for i in range(m):

            if i+1 < m:

                for j in range(n):

                    if j+1 < n:

                        if board[i][j]!= "0" and board[i][j+1] != "0" and board[i][j] == board[i][j+1]:

                            if board[i+1][j] == board[i][j] and board[i+1][j] == board[i+1][j+1]:
                                if [i,j] not in li: li.append([i,j])
                                if [i, j+1] not in li: li.append([i, j+1])
                                if [i+1, j] not in li: li.append([i+1, j])
                                if [i+1, j+1] not in li: li.append([i+1, j+1])
        if len(li) == 0: break
        else: res += len(li)


        for l in li:
            l1 = l[0]
            l2 = l[1]
            tmp = list(board[l1])
            tmp[l2] = "0"
            board[l1] = ''.join(tmp)


        for i in range(m):
            board[i] = list(board[i])
        
        i = m-1
        while i>0:
            for j in range(n):
                if board[i][j] == "0":
                    for k in range(i-1, -1, -1):
                        if board[k][j] != "0":
                            board[k][j], board[i][j] = board[i][j], board[k][j]
                            break
            i-=1

        for i in range(m):
            board[i] = ''.join(board[i])

        li = []

    
    return res


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))