import pygame

try:
    computerTurn = False
    # Initialize Pygame
    pygame.init()
    #Set up window
    window_width = 800
    window_height = 600
    screen = pygame.display.set_mode((window_width, window_height))

    #Title and Icon
    pygame.display.set_caption("Tic Tac Toe AI")
    #Tic Tac Toe theoretical board
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #Board drawing
    verticalOne = pygame.Rect((306,80,5,440))
    verticalTwo = pygame.Rect((492,80,5,440))
    horizontalOne = pygame.Rect((150,220,500,5))
    horizontalTwo = pygame.Rect((150,380,500,5))
    #Board boxes
    #row one
    boxOneone = pygame.Rect((123,65,183,155))
    boxOnetwo = pygame.Rect((310,65,183,155))
    boxOnethree = pygame.Rect((497,65,183,155))
    #row two
    boxTwoone = pygame.Rect((123,225,183,155))
    boxTwotwo = pygame.Rect((310,225,183,155))
    boxTwothree = pygame.Rect((497,225,183,155))
    #row three
    boxThreeone = pygame.Rect((123,385,183,155))
    boxThreetwo = pygame.Rect((310,385,183,155))
    boxThreethree = pygame.Rect((497,385,183,155))

    # create Xs
    oneOne = pygame.Rect(123,65,183,155)
    oneTwo = pygame.Rect((310,65,183,155))
    oneThree = pygame.Rect((497,65,183,155))
    #row two
    twoOne = pygame.Rect((123,225,183,155))
    twoTwo = pygame.Rect((310,225,183,155))
    twoThree = pygame.Rect((497,225,183,155))
    #row three
    threeOne = pygame.Rect((123,385,183,155))
    threeTwo = pygame.Rect((310,385,183,155))
    threeThree = pygame.Rect((497,385,183,155))


    #While Loop to keep the window open
    run = True
except Exception as e:
    print("Failed to initialize: ", e)

try:
    while(run):

        #screen.fill((0,0,0))
        pygame.draw.rect(screen, (255,255,255), verticalOne)
        pygame.draw.rect(screen, (255,255,255), verticalTwo)
        pygame.draw.rect(screen, (255,255,255), horizontalOne)
        pygame.draw.rect(screen, (255,255,255), horizontalTwo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        #listen for a click and check for mouse position
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            def listenForClick():
                try:
                    #if the mouse is clicked in a box
                    if boxOneone.collidepoint(mouse_pos) and mouse_click[0] and board[0][0] == 0: #[0] represents left click           #THESE IF STATEMENTS ARENT WORKING AFTER FIRST MOVE, THIS IS WHERE THE PROBLEM IS ITS BECAUSE LATER ON WHEN TRYING TO COME UP WITH thE BEST MOVE YOU SETTHE POTENTIALS TO 4 SO THAT CONDITION IS NOT MET!!!!!!!!!!!!!!!!!!!
                        computerTurn = True
                        board[0][0] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                        return 0
                        
                    elif boxOnetwo.collidepoint(mouse_pos) and mouse_click[0] and board[0][1] == 0:
                        computerTurn = True
                        board[0][1] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxOnethree.collidepoint(mouse_pos) and mouse_click[0] and board[0][2] == 0:
                        computerTurn = True
                        board[0][2] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxTwoone.collidepoint(mouse_pos) and mouse_click[0] and board[1][0] == 0:
                        computerTurn = True
                        board[1][0] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxTwotwo.collidepoint(mouse_pos) and mouse_click[0] and board[1][1] == 0:
                        computerTurn = True
                        board[1][1] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxTwothree.collidepoint(mouse_pos) and mouse_click[0] and board[1][2] == 0:
                        computerTurn = True
                        board[1][2] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxThreeone.collidepoint(mouse_pos) and mouse_click[0] and board[2][0] == 0:
                        computerTurn = True
                        board[2][0] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxThreetwo.collidepoint(mouse_pos) and mouse_click[0] and board[2][1] == 0:
                        computerTurn = True
                        board[2][1] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                    elif boxThreethree.collidepoint(mouse_pos) and mouse_click[0] and board[2][2] == 0:
                        computerTurn = True
                        board[2][2] = 1
                        nextMove = decision(board, 0, computerTurn)
                        board[nextMove[0]][nextMove[1]] = 2
                        computerTurn = False
                        print("X drawn")
                        drawOs()
                except Exception as e:  
                    print("Failed to register click: ", e)
            #print("run")
            listenForClick()


        #place the Xs
            try:
                if board[0][0] == 1:
                # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (oneOne.left, oneOne.top)          # Top-left corner
                    end1 = (oneOne.right, oneOne.bottom)        # Bottom-right corner
                    start2 = (oneOne.right, oneOne.top)         # Top-right corner
                    end2 = (oneOne.left, oneOne.bottom)         # Bottom-left corner
                    listenForClick()

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left
        
                elif board[0][1] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (oneTwo.left, oneTwo.top)          # Top-left corner
                    end1 = (oneTwo.right, oneTwo.bottom)        # Bottom-right corner
                    start2 = (oneTwo.right, oneTwo.top)         # Top-right corner
                    end2 = (oneTwo.left, oneTwo.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[0][2] == 1:
                    start1 = (oneThree.left, oneThree.top)          # Top-left corner
                    end1 = (oneThree.right, oneThree.bottom)        # Bottom-right corner
                    start2 = (oneThree.right, oneThree.top)         # Top-right corner
                    end2 = (oneThree.left, oneThree.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[1][0] == 1:
                    start1 = (twoOne.left, twoOne.top)          # Top-left corner
                    end1 = (twoOne.right, twoOne.bottom)        # Bottom-right corner
                    start2 = (twoOne.right, twoOne.top)         # Top-right corner
                    end2 = (twoOne.left, twoOne.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[1][1] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (twoTwo.left, twoTwo.top)          # Top-left corner
                    end1 = (twoTwo.right, twoTwo.bottom)        # Bottom-right corner
                    start2 = (twoTwo.right, twoTwo.top)         # Top-right corner
                    end2 = (twoTwo.left, twoTwo.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[1][2] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (twoThree.left, twoThree.top)          # Top-left corner
                    end1 = (twoThree.right, twoThree.bottom)        # Bottom-right corner
                    start2 = (twoThree.right, twoThree.top)         # Top-right corner
                    end2 = (twoThree.left, twoThree.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[2][0] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (threeOne.left, threeOne.top)          # Top-left corner
                    end1 = (threeOne.right, threeOne.bottom)        # Bottom-right corner
                    start2 = (threeOne.right, threeOne.top)         # Top-right corner
                    end2 = (threeOne.left, threeOne.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[2][1] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (threeTwo.left, threeTwo.top)          # Top-left corner
                    end1 = (threeTwo.right, threeTwo.bottom)        # Bottom-right corner
                    start2 = (threeTwo.right, threeTwo.top)         # Top-right corner
                    end2 = (threeTwo.left, threeTwo.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left

                elif board[2][2] == 1:
                    # Define function to draw an X
                    # Calculate the two points to draw the X
                    start1 = (threeThree.left, threeThree.top)          # Top-left corner
                    end1 = (threeThree.right, threeThree.bottom)        # Bottom-right corner
                    start2 = (threeThree.right, threeThree.top)         # Top-right corner
                    end2 = (threeThree.left, threeThree.bottom)         # Bottom-left corner
                    

                    # Draw the two lines to form an X
                    pygame.draw.line(screen, (225,0,0), start1, end1, 5)  # Line from top-left to bottom-right
                    pygame.draw.line(screen, (255,0,0), start2, end2, 5)  # Line from top-right to bottom-left
            except Exception as e:
                print("Failed to draw Xs: ", e)
            def drawOs():
                    #place the Os
                try:
                    if board[0][0] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (oneOne.centerx, oneOne.centery), 50, 5)
                        print("O drawn")
                        listenForClick()
                    
                    if board[0][1] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (oneTwo.centerx, oneTwo.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[0][2] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (oneThree.centerx, oneThree.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[1][0] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (twoOne.centerx, twoOne.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[1][1] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (twoTwo.centerx, twoTwo.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[1][2] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (twoThree.centerx, twoThree.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[2][0] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (threeOne.centerx, threeOne.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[2][1] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (threeTwo.centerx, threeTwo.centery), 50, 5)
                        print("O drawn")
                        listenForClick()

                    if board[2][2] == 2:
                        # Define function to draw an O
                        pygame.draw.circle(screen, (0,255,0), (threeThree.centerx, threeThree.centery), 50, 5)
                        print("O drawn")
                        listenForClick()
                except Exception as e:
                    print("Failed to draw Os: ", e)


            #check if the board is full
            # Minimax algorithm to calculate the best move for the computer
            def decision(board, level, computersTurn):
                try:
                    if not spaceOnBoard(board):
                        return 0 #draw
                    bestScore = float('-inf')
                    while computersTurn == True:
                        
                        choice = None
                        for column in range(3):
                            for row in range(3):
                                if board[column][row] == 0:
                                    choice = (column, row)
                                    board[column][row]= 4
                                    score = checkForWin(board)
                                    decision(board, level+1, computersTurn)
                                    nextMove = finalChoice(score, bestScore, choice)
                                
                                    return nextMove
                except Exception as e:
                    print("Failed to calculate decision: ", e)
                


            def finalChoice(score, bestScore, choice):
                try:
                    for column in range(3):
                        for row in range(3):
                            if board[column][row] == 4:
                                board[column][row]= 0
                    print(score + bestScore)
                    if score > bestScore:
                        bestScore = score
                        nextMove = choice
                    return nextMove
                except Exception as e:
                    print("Failed to calculate final move: ", e)


            def checkForWin(board):
                try:
                    #check if there is a win in the rows
                    for row in range(3):
                        if board[row][0] == board[row][1] == board[row][2] == 4:
                            return +1
                        elif board[row][0] == board[row][1] == board[row][2] == 2:
                            return -1

                    #check if there is a win in the columns 
                    for column in range(3):
                        if board[0][column] == board[1][column] == board[2][column] == 4:
                            return +1
                        elif board[0][column] == board[1][column] == board[2][column] == 2: 
                            return -1

                    #check if there is a win in the diagonals
                    if board[0][0] == board[1][1] == board[2][2] == 4:    
                        return +1
                    elif board[0][0] == board[1][1] == board[2][2] == 2: 
                        return -1
                    elif board[0][2] == board[1][1] == board[2][0] == 4:  
                        return +1
                    elif board[0][2] == board[1][1] == board[2][0] == 2: 
                        return -1
                    
                    #if there is no win
                    if spaceOnBoard(board) == True:
                        return 0
                except Exception as e:
                    print("Failed to check for win: ", e)
            





            #check if the board is full
            def spaceOnBoard(board):
                try:
                    #loop through all cells on the board
                    for row in board:
                        if 0 in row:
                            return True
                    return False 
                except Exception as e:
                    print("Failed to check if board is full: ", e)


            
        pygame.display.update()
except Exception as e:  
    print(e)

pygame.quit()