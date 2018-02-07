import pygame

#Initialize connect 4 board
def create_board(num_row,num_col):

    board=[[0 for c in range(num_col)] for r in range(num_row)]
    return board

#Fill a spot on the board (1 for P1, 2 for P2)
def drop_piece(board,row,col,piece):

    board[row][col]=piece

#Check column is not full
def isValid(board,col,num_row):
    return board[num_row-1][col]==0

#Get the row index that a piece will into
def getOpenRow(board,col,num_row):
    for i in range(num_row):

        if board[i][col]==0:

            return i

#Check if the game is over after a piece is placed
def checkWin(board,row,col,piece,num_row,num_col):

    #go through all columns for the row piece was placed in starting from 4th column
    for c in range(3,num_col):

        if piece==board[row][c]==board[row][c-1]==board[row][c-2]==board[row][c-3]:

            return True

    #go through all rows for the column piece was placed in starting from 4th row
    for r in range(3,num_row):

        if piece==board[r][col]==board[r-1][col]==board[r-2][col]==board[r-3][col]:

            return True

    #check positively sloped diagonals:
    for c in range(3,num_col):
        for r in range(3,num_row):

            if piece==board[r][c]==board[r-1][c-1]==board[r-2][c-2]==board[r-3][c-3]:

                return True

    #check negatively sloped diagonals
    for c in range(num_col-4,-1,-1):
        for r in range(3,num_row):

            if piece==board[r][c]==board[r-1][c+1]==board[r-2][c+2]==board[r-3][c+3]:

                return True

# Render connect 4 board onto screen
def draw_board(board,sqSize,circRad,screen,bkgd_col,p1_col,p2_col,board_col):

    num_col=len(board[0])
    num_row=len(board)
    height = (num_row + 1) * sqSize

    # Always render an empty connect 4 board first
    for c in range(num_col):

        for r in range(num_row):

            pygame.draw.rect(screen,board_col,( c*sqSize, r*sqSize+sqSize, sqSize, sqSize))
            pygame.draw.circle(screen,bkgd_col,(c*sqSize+sqSize//2,r*sqSize+sqSize+sqSize//2),circRad)

    # Update empty connect 4 board to render based on board array
    for c in range(num_col):

        for r in range(num_row):
            if board[r][c]==1:
                pygame.draw.circle(screen, p1_col,  (c * sqSize + sqSize // 2, height - (r * sqSize  + sqSize // 2)),circRad)
            elif board[r][c]==2:
                pygame.draw.circle(screen, p2_col,  (c * sqSize + sqSize // 2, height - (r * sqSize + sqSize // 2)), circRad)

    pygame.display.update()