x_data = [-1, 1, -2, 2, -2, 2, 1, -1]
y_data = [-2, -2, -1, -1, 1, 1, 2, 2]

def knight_tour_problem(n):
    n = n
    board = [[-1 for j in range(n)] for _ in range(n)]
    cur_x = 0
    cur_y = 0
    board[cur_x][cur_y]= 0

    pos = 1

    if knight_explore(board, pos, cur_x, cur_y, n):
        printout(board)
    else:
        print("print something in else", board)

def knight_explore(board,pos, cur_x, cur_y, n):
    if pos == n**2:
        return True

    for i in range(8):
        new_x = cur_x + x_data[i]
        new_y = cur_y + y_data[i]

        if is_valid(new_x,new_y, board, n):
            board[new_x][new_y] = pos
            # pos += 1 # makes issue in back tracking
            if knight_explore(board, pos+1, new_x, new_y, n):
               return  True
            else:
                board[new_x][new_y] = -1 # very difficult

    return False


def is_valid(x,y, board, n):
    return -1 < x < n and -1 < y < n and board[x][y] == -1

def printout(board):
    for i in range(len(board)):
        print ("\n")
        for j in range(len(board)):
            print (board[i][j], end='   ')

def list_comprehension():
    pass
    # p =[]
    # for i in range(n):
    #     d=[]
    #     for j in range(n):
    #         d.append(j)
    #     p.append(d)
    #
    # print(p)

if __name__ == "__main__":
    knight_tour_problem(5)
