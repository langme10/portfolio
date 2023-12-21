###############################################################################
#   Computer Project #7
#
#   Algorithm
#     Make a function called open_file to prompt the user for a file and open the file
#       if the file isnt valid make an error message appear and reprompt, this returns a file pointer
#     Make a function called read_stopwords to read the file convert all words to lowercase
#       and make a set of stopwords and close the file and return the set of stopwords
#     Make a function called validate_word to see if word in stop words or has digit or punctuation
#       this will return with either true or false
#     Make a function called process_lyrics that recives a string of lyrics and a set of stopwords
#       and strips of white space and punctuation and then checks to see if the word is valid, if it is
#       it will add that word to the set
#     Make an update_dictionary function that takes a data_dict, singer,song name, and set of song words
#       it will update the dictionary to put the new singer, song, name and lyrics in their respective places
#     Make a function called read_data this will read through the file getting the singer name, song name
#       and song lyrics and process the lyrics then update the dictionary then closes the file and returns
#       the dictionary
#     Make a function to calculate average word count which calculates avg word count by singer
#     Make a find singers vocab function that returns a dictionary of all words used by each singer
#     Make a display singers function to display the data of the singer
#     Make a function to search songs that creates a list of tuples everytime it finds a matching
#       word and sorts it alphabetically
#     Make a main function fot open the correct files, calculate all the singers data and display it
#       and also prompting the user for words to search throught the songs
#
#
###############################################################################

import sys
import NMM  # This is necessary for the project
## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
#def input( prompt=None ):
#    if prompt != None:
#       print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str

BANNER = """
    __      _(_)_ __  _ __   ___ _ __| | |
    \ \ /\ / / | '_ \| '_ \ / _ \ '__| | |
     \ V  V /| | | | | | | |  __/ |  |_|_|
      \_/\_/ |_|_| |_|_| |_|\___|_|  (_|_)
"""

RULES = """                                                                                       
    The game is played on a grid where each intersection is a "point" and
    three points in a row is called a "mill". Each player has 9 pieces and
    in Phase 1 the players take turns placing their pieces on the board to 
    make mills. When a mill (or mills) is made one opponent's piece can be 
    removed from play. In Phase 2 play continues by moving pieces to 
    adjacent points. 
    The game is ends when a player (the loser) has less than three 
    pieces on the board.
"""

MENU = """
    Game commands (first character is a letter, second is a digit):
    xx        Place piece at point xx (only valid during Phase 1 of game)
    xx yy     Move piece from point xx to point yy (only valid during Phase 2)
    R         Restart the game
    H         Display this menu of commands
    Q         Quit the game

"""


## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str


def count_mills(board, player):
    """
        Takes in the board and the player and counts the number of mills they have
    """
    mill_count = 0 #sets mill count to zero
    for i in range(len(board.MILLS)): #loops through each list of mills
        count = 0 #sets each lists count to zero
        for n in range(len(board.MILLS[i])): #checks through each element in each list
            if board.points[board.MILLS[i][n]] == player: #checks to see if that point is taken by the player
                count += 1 #if it is increases the count
        if count == 3: #then checks to see if all three were taken
            mill_count += 1 #if so mill count goes up one

    return mill_count #returns the number of mills


def place_piece_and_remove_opponents(board, player, destination):
    """
        This places a piece for a player and if a mill is created allows them to
        remove an opponents piece
    """
    num_mills_before = count_mills(board,player)#counts number of mills before placing piece
    board.assign_piece(player,destination)#places piece
    num_mills_after = count_mills(board,player)#counts number of mills after placing piece
    if num_mills_after > num_mills_before: #checks if number of mills went up
        print("A mill was formed!")
        print(board)
        other_player = get_other_player(player) #gets the other player
        remove_piece(board,other_player) #removes the other player piece if valid
    return None  # stub; delete and replace it with your code


def move_piece(board, player, origin, destination):
    """
        Removes players piece from the origin and moves it to the desired destination
    """
    if board.points[origin] != player:
        raise RuntimeError('Invalid command: Origin point does not belong to player')
    elif (board.points[origin] == player) and (destination not in board.points):
        raise RuntimeError("Invalid command: Not a valid point")
    elif (board.points[destination] == ' ') and (destination in board.ADJACENCY[origin]):#checks to see if the placement is adjacent to the first one and has nothing on it
        board.clear_place(origin)#clears the origin
        place_piece_and_remove_opponents(board,player,destination)#places piece and removes opponents if mill was formed

    else:
        raise RuntimeError("Invalid command: Not a valid point")

    return None  # stub; delete and replace it with your code


def points_not_in_mills(board, player):
    """
        Returns a set of points not in mills by that player
    """
    points_list = [] #creates an empty list
    for place, assignment in board.points.items(): #loops through the board and finds the points by the player
        if assignment == player: #checks to see if it is the player
            points_list.append(place)#adds the place to the points list
    points_set = set(points_list) #makes that a set
    mills_set = set() #makes a mills set
    for i in board.MILLS: #loops through the mills lists
        little_set = set(i) #makes each list a set
        if little_set.issubset(points_set): #checks to see if the little set is a subset of points
            for n in little_set: #loops throught the little set
                mills_set.add(n) #adds each element to mills set
    for m in mills_set: #loops through the mills set
        points_set.remove(m) #removes each element in the mills set from the points set


    return points_set  #returns set of points not in mills


def placed(board, player):
    """
        Goes through the board and returns a list of points placed by the player
    """
    points_placed = [] #creates empty list
    for place, assignment in board.points.items():#goes through dictionary of points
        if assignment == player: #looks to see if it is assigned to the player
            points_placed.append(place) #if so puts the place in the list

    return points_placed  # returns the list of points


def remove_piece(board, player):
    """
        Loops and gets input to remove a piece from the specified player
    """
    y = 1
    while y > 0: #loops until valid input
        piece = input("Remove a piece at :> ").strip().lower()#gets input
        valid_points = points_not_in_mills(board,player) #checks for points not in mills
        points_placed = placed(board,player) #checks for points placed
        if len(piece) > 2:
            print("Invalid command: Not a valid point")
            print("Try again.")
            continue
        elif len(valid_points) > 0: #checks to see if their are points out of mills
            if (piece not in valid_points) and (piece in points_placed):
                print("Invalid command: Point is in a mill")
                print("Try again.")
                continue
            elif (piece in valid_points) and (piece in points_placed): #if its valid
                board.clear_place(piece) #clears piece
                y = 0 #ends loop
            else: #if invalid
                print("Invalid command: Point does not belong to player")#prints error message
                print("Try again.")
                continue
        else:#if no points out of mills
            if piece in points_placed: #if its a valid piece
                board.clear_place(piece) #clear piece
                y = 0
            else:#if its not valid
                print("Invalid command: Point is in a mill") #raise runtime error
                print("Try again.")
                continue
    return None  # return none
"Invalid command: Point does not belong to player"

def is_winner(board, player):
    """
        Checks to see if a player won
    """
    player = get_other_player(player)
    num_of_points = placed(board,player) #number of points by that player
    if len(num_of_points) < 3: #checks to see if its less than 3
        print(BANNER) #prints banner
        return True #returns true
    else:
        return False #returns false


def get_other_player(player):
    """
    Get the other player.
    """
    return "X" if player == "O" else "O"


def main():
    # Loop so that we can start over on reset
    while True:
        # Setup stuff.
        print(RULES)
        print(MENU)
        board = NMM.Board()
        print(board)
        player = "X"
        placed_count = 0  # total of pieces placed by "X" or "O", includes pieces placed and then removed by opponent

        # PHASE 1
        print(player + "'s turn!")
        # placed = 0
        command = input("Place a piece at :> ").strip().lower()
        print()
        # Until someone quits or we place all 18 pieces...
        while command != 'q' and placed_count != 18:
            try:
                if command == 'r':
                    break

                elif command == 'h':
                    print(MENU)
                    command = input("Place a piece at :> ").strip().lower()
                    place_piece_and_remove_opponents(board, player, command)
                    placed_count += 1
                    player = get_other_player(player)


                else:
                    place_piece_and_remove_opponents(board,player,command)
                    placed_count += 1
                    player = get_other_player(player)

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))


            # Prompt again
            print(board)
            print(player + "'s turn!")
            if placed_count < 18:
                command = input("Place a piece at :> ").strip().lower()
            else:
                print("**** Begin Phase 2: Move pieces by specifying two points")
                command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # Go back to top if reset
        if command == 'r':
            continue
        # PHASE 2 of game
        while command != 'q':
            # commands should have two points
            command = command.split()
            try:
                if command == 'r':
                    break

                elif command == 'h':
                    print(MENU)

                else:
                    if len(command) == 2:
                        move_piece(board,player,command[0],command[1])
                    else:
                        raise RuntimeError("Invalid number of points")
                    did_one_win = is_winner(board, player)
                    player = get_other_player(player)
                    did_two_win = is_winner(board,player)
                    if did_one_win == True or did_two_win == True:
                        return

            # Any RuntimeError you raise inside this try lands here
            except RuntimeError as error_message:
                print("{:s}\nTry again.".format(str(error_message)))
                # Display and reprompt
            print(board)
            # display_board(board)
            print(player + "'s turn!")
            command = input("Move a piece (source,destination) :> ").strip().lower()
            print()

        # If we ever quit we need to return
        if command == 'q':
            return


if __name__ == "__main__":
    main()
