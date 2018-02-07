import pygame
import sys
import connect4

# Global colours
#blue
BOARD_COL=(0,0,255)
#black
BKGD_COL=(0,0,0)
#red
P1_COL=(255,0,0)
#yellow
P2_COL=(255,255,0)

# Board dimensions
ROWS=6
COLUMNS=7

# Initialize Pygame, font and screen for rendering
pygame.init()
FONT=pygame.font.SysFont("Arial",75)
SQ_SIZE=100
RADIUS=SQ_SIZE//2-5
WIDTH=COLUMNS*SQ_SIZE
HEIGHT=(ROWS+1)*SQ_SIZE
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#############################GAME STARTS HERE#######################
#Initialize game
board=connect4.create_board(ROWS,COLUMNS)
game_over=False
turn=True
connect4.draw_board(board,SQ_SIZE,RADIUS,screen,BKGD_COL,P1_COL,P2_COL,BOARD_COL)
pygame.display.update()

#Main game loop
while not game_over:

    # keep track of game events initiated by user
    for event in pygame.event.get():

        # safe quitting of the game
        if event.type==pygame.QUIT:

            sys.exit()

        # render circle at top of screen based on mouse x-motion
        if event.type==pygame.MOUSEMOTION:

            # refresh top of screen to render black every time mouse moves
            pygame.draw.rect(screen,BKGD_COL,(0,0,WIDTH,SQ_SIZE))
            posx=event.pos[0]

            # render different coloured circle at mouse x-position
            if turn:

                pygame.draw.circle(screen, P1_COL,(posx,SQ_SIZE//2) ,RADIUS)
            else:

                pygame.draw.circle(screen,P2_COL, (posx, SQ_SIZE // 2), RADIUS)

        pygame.display.update()

        # when clicking
        if event.type==pygame.MOUSEBUTTONDOWN:

            # refresh top of screen to render black
            pygame.draw.rect(screen, BKGD_COL, (0, 0, WIDTH, SQ_SIZE))

            #P1 input
            if turn:

                # determine column selected based on x position when clicking
                col=event.pos[0]//SQ_SIZE

                if connect4.isValid(board,col,ROWS):

                    row=connect4.getOpenRow(board,col,ROWS)
                    connect4.drop_piece(board,row,col,1)

                    if connect4.checkWin(board,row,col,1,ROWS,COLUMNS):

                        win_message=FONT.render("PLAYER 1 WINS",1,P1_COL)
                        screen.blit(win_message, (40, 10))
                        game_over=True
                else:

                    message = FONT.render("Column is already full!", 1, P1_COL)
                    screen.blit(message, (40, 10))
                    turn = False

            #P2 input
            else:

                col = event.pos[0] // SQ_SIZE

                if connect4.isValid(board,col,ROWS):

                    row = connect4.getOpenRow(board, col,ROWS)
                    connect4.drop_piece(board,row,col,2)

                    if connect4.checkWin(board,row,col,2,ROWS,COLUMNS):

                        win_message = FONT.render("PLAYER 2 WINS", 1,P2_COL)
                        screen.blit(win_message,(40,10))
                        game_over=True

                else:
                    message = FONT.render("Column is already full!", 1, P2_COL)
                    screen.blit(message, (40, 10))
                    turn = True

            # render board again after every turn
            connect4.draw_board(board,SQ_SIZE,RADIUS,screen,BKGD_COL,P1_COL,P2_COL,BOARD_COL)

            #alternate between True and False, ie. P1 turn or P2 turn
            turn=(turn is False)

            if game_over:
                pygame.time.wait(3000)