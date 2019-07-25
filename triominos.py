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

        # Set defective square
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        missingtile = (x,y)
        self.board[x][y] = ' XX '
        

        # self.print_board()
        self.tile()
    
    def print_board(self):
        print('\n'.join(map(''.join, self.board)))
    

    def tile(self, upperleft: tuple, n: int):
        self.print_board()
        print("\n")
        board = self.board
        print ("Iteration: " + str(self.iteration))
        self.iteration+=1
        cur_iteration = self.iteration
        text_iteration = ''
        
        if cur_iteration < 10:
            text_iteration = ' 0' + str(cur_iteration) + ' '
        else:
            text_iteration = ' ' + str(cur_iteration) + ' '

        # Basecase: If size is == 2, tile last portion
        if (len(board[0]) == 2):
            for x in range(0, 2):
                for y in range(0, 2):
                    if board[x][y] == ' -- ':
                        board[x][y] = text_iteration
        self.print_board()

        # Otherwise: Split and recurse
        
        self.merge()


game = Triomino(2)


