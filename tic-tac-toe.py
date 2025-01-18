#   Author  :   XhannAmatH

import random, time


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(  " +-------+-------+-------+\n",
            "|       |       |       |\n",
            "|  ",board.get(1),"  |  ",board.get(2),"  |  ",board.get(3),"  |\n",
            "|       |       |       |\n",
            "+-------+-------+-------+\n",
            "|       |       |       |\n",
            "|  ",board.get(4),"  |  ",board.get(5),"  |  ",board.get(6),"  |\n",
            "|       |       |       |\n",
            "+-------+-------+-------+\n",
            "|       |       |       |\n",
            "|  ",board.get(7),"  |  ",board.get(8),"  |  ",board.get(9),"  |\n",
            "|       |       |       |\n",
            "+-------+-------+-------+\n")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while(True):
        try:
            move = int(input("Enter your move : "))
        except ValueError:
            print("You must enter only numbers between 1 and 9!!")
        if((move > 0 and move < 10) and move in make_list_of_free_fields(board)):
            if(board[move]== "O" or board[move]== "X"):
                print("That space is already taken, choose another")
            else:
                board[move] = "O"
                display_board(board)
                victory_for(board, "O")
        

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list_board = []
    for v, k in board.items():
        if(k != "O" or k != "X"):
            free_list_board.append(v)
        
    return free_list_board


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if(board[1] == sign and board[2] == sign and board[3] == sign
    or board[4] == sign and board[5] == sign and board[6] == sign
    or board[7] == sign and board[8] == sign and board[9] == sign
    or board[1] == sign and board[4] == sign and board[7] == sign
    or board[2] == sign and board[5] == sign and board[8] == sign
    or board[3] == sign and board[6] == sign and board[9] == sign
    or board[1] == sign and board[5] == sign and board[9] == sign
    or board[7] == sign and board[5] == sign and board[3] == sign):
        if(sign == "X"):
            print("The Enemy Wins!!... you SUCK!!")
            exit()
        elif(sign == "O"):
            print("You Win!! Well Done")
            exit()
    elif(not make_list_of_free_fields(board)):
        #empty free spaces
        print("Draw!! you both suck!!")
    else:
        if(sign == "X"):
            enter_move(board)
        else:
            draw_move(board)

def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("The enemy will make a move!!")
    time.sleep(2)
    while(True):
        position = random.randint(1,9)
        if(board.get(position)!= "O" or board.get(position)!= "X"):
            board[position]="X"
            display_board(board)
            victory_for(board, "X")
    




board = {1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9}
draw_move(board)
