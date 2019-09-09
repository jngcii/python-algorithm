def solution(h, w, board):
    
    for j, b in enumerate(board):
        arr = []
        for i in range(len(b)):
            arr.append(b[i])
        board[j] = arr
    
    result = 0
    removeable = [-1]
    
    while removeable:
        removeable = []

        for i in range(len(board)-1):

            for j in range(len(board[i])-1):

                if board[i][j] == "0": continue
                if board[i][j] == board[i][j+1]:
                    if board[i][j] == board[i+1][j] and board[i+1][j] == board[i+1][j+1]:
                        if (i,j) not in removeable: removeable.append((i,j))
                        if (i,j+1) not in removeable: removeable.append((i,j+1))
                        if (i+1,j) not in removeable: removeable.append((i+1,j))
                        if (i+1,j+1) not in removeable: removeable.append((i+1,j+1))

        for r in removeable:
            board[r[0]][r[1]] = "0"
            result += 1

        for i in range(len(board)-1, -1, -1):
            for j in range(len(board[i])):
                if board[i][j] == "0":
                    for k in range(i-1, -1, -1):
                        if board[k][j] != "0":
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break

    return result