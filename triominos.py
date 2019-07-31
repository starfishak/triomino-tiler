import random # To choose random deficient square coordinates
import time # To track time complexity 
import csv # To write results

class Triomino:
    board = []
    missingtile = ()
    iteration = 1
    pieces = []
    num_triominos = 0

    '''
    Initiate the board with a random missing tile
    '''
    def __init__(self, n):
        board_row = []
        self.board = []

        # Ensure board is a power of 2
        if (not self.powerOf2(n)):
            raise ValueError('The board must of a power of 2. Please correct and try again.')
            return

        # Make tiles large enough to handle # of triominos
        self.num_triominos = str(int(((n * n) - 1 ) / 3))
        blank_tile = ' '
        x_tile = ' '
        for i in range(1, len(self.num_triominos) + 1):
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

    '''
    Initiate the tiling for the current board
    '''
    def tileInit(self):
        self.tile((0,0), len(self.board[0]), self.missingtile)

    '''
    Tile(self, upperleft point of current board, size of board, deficient point)
    Recursively calls itself in the following order:
    
    -- -- | -- -- 
    --  1 | 2  --
    ______ _______
    --  3 | 4  -- 
    -- -- | -- --
    '''
    def tile(self, upperleft: tuple, n: int, deficient_point: tuple):
        board = self.board
        
        # Tile Numbering
        cur_iteration = self.iteration
        text_iteration = ''
        if len(str(cur_iteration)) < len(self.num_triominos):
            text_iteration = ' '
            for i in range (0, len(self.num_triominos) - len(str(cur_iteration))):
                text_iteration += '0'
            text_iteration += str(cur_iteration)
            text_iteration += ' '
        else:
            text_iteration = ' ' + str(cur_iteration) + ' '
        self.iteration+=1

        # Base case: If size is == 2, tile last portion
        if (n == 2):
            for x in range(0, 2):
                for y in range(0, 2):
                    if '-' in board[upperleft[0] + x][upperleft[1] + y]:
                        board[upperleft[0] + x][upperleft[1] + y] = text_iteration
                        # Branch complete. Recurse up the stack.
            self.tile_type(upperleft, text_iteration)
            return
        else:
            # Otherwise: Split and recurse
                # Tile one triomino to create deficient squares
            new_size = int(n/2)
            deficient_quad = self.quadrant(deficient_point, upperleft, n)    
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

            # Call tile type to get tiling information. 
            center_upperleft = upperleft[0] + new_size-1, upperleft[1] + new_size-1
            self.tile_type(center_upperleft, text_iteration)

            self.tile(upperleft, new_size, q1)
            self.tile((upperleft[0] + new_size, upperleft[1]), new_size, q2)        
            self.tile((upperleft[0], upperleft[1] + new_size), new_size, q3)
            self.tile((upperleft[0] + new_size, upperleft[1] + new_size), new_size, q4)

    '''
    Quadrant (self, point to check, upperleft point of board, size of board)
    Returns 1,2,3,4 depending on the quadrant. See below:
    
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

    '''
    print_board(self) 
    Prints current board in class to console 
    '''
    def print_board(self):
        print('\n'.join(map(''.join, self.board)))

    '''
    Gets tile type of given 2x2 board
    '''
    def tile_type(self, upperleft : tuple, space_num):
        innercoord = (upperleft[1] + 1, len(self.board[0]) - (upperleft[0] + 1))
        piece = ''

        if (self.board[upperleft[0]][upperleft[1]] == space_num and self.board[upperleft[0]][upperleft[1] + 1] == space_num):
            # Piece is either UL or UR
            if (self.board[upperleft[0]+1][upperleft[1]] == space_num):
                # Piece is UL
                piece = "UL"
            else:
                # Piece is UR
                piece = "UR"
        else:
            if (self.board[upperleft[0]][upperleft[1]] == space_num):
                # Piece is LL
                piece = "LL"
            else:
                # Piece is LR
                piece = "LR"
        self.pieces.append([innercoord, piece])
    
    '''
    Returns true if power of 2, false if else
    '''
    def powerOf2(self, n):
        return bool(n and not (n&(n-1)))
    
    '''
    Returns true if power of 2, false if else
    '''
    def print_pieces(self):
        print(str(len(self.pieces)), "total pieces")
        for i in self.pieces:
            print(i[0], i[1])
        print('\n')


'''
Setup + Init Tile
'''
print ("Please select mode.\n1) Single Tiling of 2^n Size\n2) Multiple Tilings of 2^n Boards, CSV output")
choice = input("Mode 1 or 2? ")
print ("Choose an N value. 2^n will be the board size")
n = input("n: ")
n = int(n)
print("\n\n --- \n\n")


if choice == '2':
    # Test game
    with open('results.csv', 'w') as results:
        # Store Runtimes
        writer = csv.writer(results)
        writer.writerow(["Results"])
        writer.writerow(["n", "Time (Seconds)"])

        # Loop through iterations to test algo
        if n > 15:
            print("15 is the max N value.")
        n = 15
        for i in range(1, n):
            print ("Iteration:", i, 2**i)
            square = 2**i
            game = Triomino(square)
            
            # Only time the tiling
            start_time_game = time.time()
            game.tileInit()
            elapsed_time_game = time.time() - start_time_game
            writer.writerow([i, elapsed_time_game])
            print ("Time to Generate Board:", elapsed_time_game, "seconds")

elif choice == '1':
    # Single Game Test
    game = Triomino(2**n)
    time_start = time.time()
    game.tileInit()
    elapsed_time = time.time() - time_start
    
    # Print Board
    # game.print_pieces()
    # game.print_board()
    
    print("Time to Tile Board:", elapsed_time)
    print ("Process Complete\n\n")

else:
    print("That is not a choice.")