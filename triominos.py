import random
class Triomino:
    board = []
    missingtile = ()
    iteration = 1

    def __init__(self, n):
        board_row = []

        # Make board divisible by 4
        if n % 4 != 0:
            n = n + (n%4)
        

        # Make tiles large enough to handle # of triominos
        num_triominos = str(int(((n * n) - 1 ) / 3))
        blank_tile = ' '
        x_tile = ' '
        for i in range(1, len(num_triominos) + 1):
            blank_tile += '-'
            x_tile += 'X'
        x_tile += ' '
        blank_tile += ' '

        for i in range(0, n):
            board_row = [blank_tile] * n
            self.board.append(board_row)

        # Set defective square
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        self.missingtile = (x,y)
        self.board[x][y] = x_tile
            
    def print_board(self):
        print('\n')
        print('\n'.join(map(''.join, self.board)))
    
    def tileInit(self):
        self.tile((0,0), len(self.board[0]), self.missingtile)
        print ("Final Result: \n")
        self.print_board()

    def tile(self, upperleft: tuple, n: int, deficient_point: tuple):
        print("\n")
        board = self.board
        print ("Iteration: " + str(self.iteration) + " with missing tile: ", deficient_point, 'and upperleft:', upperleft)
        print("n=",n)
        self.iteration+=1
        
        # Tile Numbering
        cur_iteration = self.iteration
        text_iteration = ' ' + str(cur_iteration) + ' '
        if cur_iteration < 10 and len(self.board[0]) > 4:
            text_iteration = ' 0' + str(cur_iteration) + ' '
        else:
            text_iteration = ' ' + str(cur_iteration) + ' '

        # Basecase: If size is == 2, tile last portion
        if (n == 2):
            print("Size is 2. Tiling.")
            for x in range(0, 2):
                for y in range(0, 2):
                    if '-' in board[upperleft[0] + x][upperleft[1] + y]:
                        board[upperleft[0] + x][upperleft[1] + y] = text_iteration
                        # Branch complete. Recurse up the stack.
            self.print_board()
            return
        else:
            # Otherwise: Split and recurse
                # Tile one triomino to create deficient squares
            deficient_quad = self.quadrant(deficient_point, upperleft, n)
            new_size = int(n/2)
            print ("deficient_quad:", deficient_quad)
            q1 = q2 = q3 = q4 = deficient_point
            if (deficient_quad != 1):
                q1 = (upperleft[0] + new_size-1, upperleft[1] + new_size-1)
                board[q1[0]][q1[1]] = text_iteration
            if (deficient_quad != 2):
                q2 = (upperleft[0] + new_size-1, upperleft[1] + new_size)
                board[q2[0]][q2[1]] = text_iteration
            if (deficient_quad != 3):
                q3 = (upperleft[0] + new_size, upperleft[1] + new_size-1)
                board[q3[0]][q3[1]] = text_iteration
            if (deficient_quad != 4):
                q4 = (upperleft[0] + new_size, upperleft[1] + new_size)
                board[q4[0]][q4[1]] = text_iteration

            self.print_board()

            self.tile(upperleft, new_size, q1)
            self.tile((upperleft[0] + new_size, upperleft[1]), new_size, q2)        
            self.tile((upperleft[0], upperleft[1] + new_size), new_size, q3)
            self.tile((upperleft[0] + new_size, upperleft[1] + new_size), new_size, q4)

    '''
    Helper method. Returns 1,2,3,4 depending on the quadrant. See below:
    
    -- -- | -- -- 
    --  1 | 2  --
    ______ _______
    --  3 | 4  -- 
    -- -- | -- --
    '''

    def quadrant(self, point : tuple, upperleft : tuple, n : int):
        quadrant_len = int(n/2)
        # Point will be the same. Uses square in Lower Right Quad as base.
        # THIS DOES NOT USE THE CARTESIAN PLANE QUADRANTS
        pt = upperleft[0] + quadrant_len
        if(point[0] < pt and point[1] < pt):
            return 1
        elif(point[0] < pt and point[1] >= pt):
            return 2
        elif(point[0] >= pt and point[1] < pt):
            return 3
        else:
            return 4

game = Triomino(16)
# print(game.quadrant((4,4), (4,4), 4))
game.tileInit()
# print (int(2/2))