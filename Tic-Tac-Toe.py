#TIC TAC TOE GAME
#GAME Project

#FUNCTION tic tac toe board
def print_tic_t_t(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0],values[1],values[2]))
    print('\t_____|_____|_____|')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____|')

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

#FUNCTION tic tac toe score board
def print_scoreboard(score_board):
    print("\t----------------------------------------------")
    print("\t           SCORE BOARD FOR TIC TAC TOE         ")
    print("\t----------------------------------------------")

    players=list(score_board.keys())
    print("\t   ",players[0],"\t   ",score_board[players[0]])
    print("\t   ",players[1],"\t   ",score_board[players[1]])


    print("\t----------------------------------------------\n")


#FUNCTION check player won game
def check_winner(player_position,current_player):
    #win combination
    soln=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #loop check win combination
    for x in soln:
        if all(y in player_position[current_player]for y in x):
            #return true if win comb satisfied
            return True
    #return false if win comb not satisfied
    return False

#FUNCTION check if game draw
def check_draw(player_position):
    if len(player_position['X'])+len(player_position['O'])==9:
        return True
    return False

#FUNCTION for single tictactoe game
def single_game(current_player):
    #represent tictactoe
    values=[' 'for x in range(9)]

    #store the position occupied by X and O
    player_position={'X':[],'O':[]}

    #game loop for single game
    while True:
        print_tic_t_t(values)

        #try exception block for move input
        try:
            print("Player ",current_player,"turn. Which box? : ",end="")
            move=int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        #sanity check for move input
        if move<1 or move>9:
            print("Please choose the right number block between 1 to 9 ")
            continue

        #check if the cell is occupied or not
        if values[move-1] != ' ':
            print("The place you have chosen is already filled. Try Again!!")
            continue

        #update game status

        #update board status

        #updating player position
        player_position[current_player].append(move)

        #function call for checking the winner
        if check_winner(player_position,current_player):
            print_tic_t_t(values)
            print("Player  ",current_player,"has won the game, congrats!!")
            print("\n")
            return current_player

        #function call for checking draw
        if check_draw(player_position):
            print_tic_t_t(values)
            print("Game is Draw")
            print("\n")
            return 'D'

        #switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

if __name__ ==  "__main__":
    print("Player 1 Details ")
    play1=input("Enter the name of the Player : ")
    print("\n")

    print("Player 2 Details")
    play2=input("Enter the name of the Player : ")
    print("\n")

    #stores the player who choose X and O
    current_player = play1

    #stores the choice of players character
    player_choice={'X' : "",'O' : ""}

    #stores the options
    options = ['X','O']

    #stores the scoreboard details
    score_board={play1:0,play2:0}
    print_scoreboard(score_board)

    #game loop for a series of tictactoe
    #the loop runs until of the player choose to quit
    while True:
        #player choose menu
        print("Turn to choose for",current_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for Quit")

        #try exception for choice input
        try:
            choice=int(input())
        except ValueError:
            print("Wrong Input, Try Again!\n")
            continue

        #condition for player choice
        if choice==1:
            player_choice['X']==current_player
            if current_player==play1:
                player_choice['O']=play2
            else:
                player_choice['X']=play1

        elif choice==2:
            player_choice['O']==current_player
            if current_player==play1:
                player_choice['X']=play2
            else:
                player_choice['X']=play1

        elif choice==3:
            print("Final Scores")
            print_scoreboard(score_board)
            break

        else:
            print("Wrong Choice, Try Again!")

        #store the winner in a single game
        winner=single_game(options[choice-1])

        #scoreboard edit according to winner
        if winner != 'D' :
            player_won=player_choice[winner]
            score_board[player_won]=score_board[player_won]+1

        print_scoreboard(score_board)
        #switch player who choose x or o
        if current_player==play1:
            current_player=play2
        else:
            current_player=play1

#FINISH