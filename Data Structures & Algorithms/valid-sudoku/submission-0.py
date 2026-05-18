def trans_square(board):
    square_board =[[] for _ in range(9)]

    for i, hor_l in enumerate(board):
        for j in range(len(hor_l)):

            x = j // 3
            y = (i // 3)*3

            square_board[x+y].append(hor_l[j])

    return square_board

def trans_vert(board):
    vert_board = [[] for _ in range(9)]

    for hor_l in board:
        for i in range(len(hor_l)):
            vert_board[i].append(hor_l[i])
    
    return vert_board


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check no duplicates horizontal
        for l_str in board:
            filtered = [x for x in l_str if x.isdigit()]
            if len(set(filtered)) != len(filtered):
                print("horizontal")
                return False
        
        # check no dupl vertical:
        vert_board = trans_vert(board)
        for l_str in vert_board:
            filtered = [x for x in l_str if x.isdigit()]
            if len(set(filtered)) != len(filtered):
                print("vert")
                return False
        
        square_board = trans_square(board)
        for l_str in square_board:
            filtered = [x for x in l_str if x.isdigit()]
            if len(set(filtered)) != len(filtered):
                print("square")
                return False

        return True