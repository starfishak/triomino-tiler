import random
class Triomino:
    board = []
    missingtile = ()
    iteration = 1

    def __init__(self, n):
        board_row = []
        for i in range(0, n):
            board_row = [' -- '] * n
            self.board.append(board_row)

        self.print_board()

        # Set defective square
        x = random.randint(0,n)
        y = random.randint(0,n)
        self.board[x][y] = ' XX '
        missingtile = (x,y)

        self.print_board()
        self.tile()
        self.print_board()
    
    def print_board(self):
        print('\n'.join(map(''.join, self.board)))
    

    def tile(self):
        board = self.board
        print ("Iteration: " + str(self.iteration))
        self.iteration+=1
        cur_iteration = self.iteration
        text_iteration = ''
        
        if cur_iteration < 10:
            text_iteration = '0' + str(cur_iteration)
        else:
            text_iteration = str(cur_iteration)

        # Basecase: If size is == 2, tile last portion
        print("len: ", len(board[1]))
        print("11: " , board[0][0])
        if (len(board[1]) == 2):
            print ("len == 2")
            for x in range(0, 1):
                for y in range(0, 1):
                    print(str(x) + " " + str(y) + " " + board[x][y])
                    if not board[x][y] == '--':
                        board[x][y] == text_iteration
        
        # Otherwise: Split and recurse
    

game = Triomino(2)


