'''Source Code Header'''
###############################################################################
#   Computer Project #8
#
#   Battle Ship
#     Made the Ship class
#       defined an __init__ function to initialize the ship
#       defined get_positions function to get a list of the ships positions
#       defined get_orientation function to get the orientation of the ship
#       defined the apply_hit function to increase the hit count by 1 and update is_sunk attribute
#     Made the board class
#       defined an __init__ function to initialize the board
#       defined place_ship function to place the ship on the board and check if its valid
#       defined validate_ship function to see if ship placement is valid
#       defined the apply_guess function to apply the guess to the board and update it with the correct
#           letter based on if it hit or miss and updated the ships hit count
#       defined the __str__ function to return the current board as a string
#     Made the player class
#       defined an __init__ function to initialize the player
#       defined validate_guess function to see if a players guess was valid
#       defined get_player_guess function get a players guess and reprompt till they input valid one
#       defined the set_all_ships function to place all the ships on the players board
#     Made the BattleshipGame class
#       defined an __init__ function to initialize the game
#       defined check_game_over function to see if the game is over
#       defined display function to display each players boards
#       defined the play function to run the game
#     Made the main function
#       made two boards
#       Made two player
#       Made the battleship game
#       Ran the game
#
###############################################################################

from board import Ship, Board #important for the project
from game import Player, BattleshipGame #important for the project





def main():
    board_size = 5
    ship_list = [5, 4, 3, 3, 2]
    player1_board = Board(board_size)
    player2_board = Board(board_size)
    user_one = Player("Player 1",player1_board,ship_list)
    user_two = Player("Player 2",player2_board,ship_list)
    battleship_game = BattleshipGame(user_one,user_two)
    battleship_game.play()
    pass # TODO: implement this function

if __name__ == "__main__":
    main()