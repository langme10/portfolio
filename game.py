from board import Ship,Board #important for the project

## Uncomment the following lines when you are ready to do input/output tests!
## Make sure to uncomment when submitting to Codio.
import sys
def input( prompt=None ):
   if prompt != None:
       print( prompt, end="" )
   aaa_str = sys.stdin.readline()
   aaa_str = aaa_str.rstrip( "\n" )
   print( aaa_str )
   return aaa_str

class Player(object):
    """
        This class represents a single player in the game it has to do with updating each players game
        data and reading their guesses each turn
    """
    def __init__(self, name, board, ship_list):
        """
            initializes each player with name,board,guesses,and ship list
        """
        self.name = name #initializes name
        self.board = board #initializes board
        self.guesses = [] #initializes guesses to an empty list
        self.ship_list = ship_list #initializes ship list
        return None  # Returns none

    def validate_guess(self, guess):
        """
            Checks to see if guess is valid
        """
        x = guess[0] #gets x coord
        y = guess[1] #gets y coord
        if guess in self.guesses: #checks if guess is already in guesses
            raise RuntimeError("This guess has already been made!") #raises error
        elif x > self.board.size or y > self.board.size: #checks if x or y is greater than the board size
            raise RuntimeError("Guess is not a valid location!") #raises error
        return None #returns none

    def get_player_guess(self):
        """
            gets guess from user and checks if its valid, if so it returns the guess as a tuple
        """
        y = 1 #sets y to 1
        while y > 0: # while loop
            try: #try
                guess = input("Enter your guess: ") #input guess
                list_guess = guess.split(",") #make guess into list
                list_guess[0] = int(list_guess[0]) #turn to int
                list_guess[1] = int(list_guess[1]) #turn to int
                tuple_guess = tuple(list_guess) #make it a tuple
                self.validate_guess(tuple_guess) #validate the guess
                return tuple_guess #return the guess
            except RuntimeError as message: #prints error message and re-loops
                print(message)

    def set_all_ships(self):
        '''Places the ships for the player'''
        for i in range(len(self.ship_list)): #goes through the ship list
            y =1 #y = 1
            while y > 0: #while loop
                coord = input("Enter the coordinates of the ship of size {}: ".format(self.ship_list[i])) #input coord
                list_coord = coord.split(",") #make coord into list
                list_coord[0] = int(list_coord[0]) #turn to int
                list_coord[1] = int(list_coord[1]) #turn to int
                tuple_coord = tuple(list_coord) #make a tuple
                orientation = input("Enter the orientation of the ship of size {}: ".format(self.ship_list[i])) #input for orientation
                player_ship = Ship(self.ship_list[i],tuple_coord,orientation) #make a players ship
                try:
                    self.board.validate_ship_coordinates(player_ship) # validate the ship coordinates
                    self.board.place_ship(player_ship) #place the ship on the board
                    y = 0 #end loop
                except RuntimeError as message: #raise error and re-loops
                    print(message)
        return None  # returns none


class BattleshipGame(object):
    """
        This class is responsible for running the game, keeping track of turns, and checking
        if a player has won
    """

    def __init__(self, player1, player2):
        """
            initializes the players of the game
        """
        self.player1 = player1 #initializes the first player
        self.player2 = player2 #initialzes the second player
        return None  # Returns none

    def check_game_over(self):
        """
            Checks if game is over
        """
        player1_count = 0 #initializes player 1's count
        ship_list1 = self.player1.board.ships #gets player 1's ship list
        for i in ship_list1:#interates through the ship list
            if i.is_sunk == True: #checks if each ship is sunk
                player1_count += 1 #ups count if it is
        ship_list2 = self.player2.board.ships #gets player 2's ship list
        player2_count = 0 #initializes player 2's count
        for i in ship_list2: #goes through player 2's ship list
            if i.is_sunk == True: #checks if each ship is sunk
                player2_count += 1 #ups the count by 1
        if player1_count == len(ship_list1): #checks if all player 1's ships are sunk
            return self.player2.name #returns player 2
        elif player2_count == len(ship_list2): #checks if all player 2's ships are sunk
            return self.player1.name #returns player 1
        else:
            return "" #returns empty string

    def display(self):
        """
            displays current state of game
        """
        print("{}'s board:".format(self.player1.name)) #prints for player 1
        print(self.player1.board) #prints player 1's board
        print("{}'s board:".format(self.player2.name)) #prints for player 2
        print(self.player2.board) #prints player 2's board
        return None  #Returns none

    def play(self):
        """
            This runs the game
        """
        #Part 1
        self.player1.set_all_ships() #player 1 places ships
        self.player2.set_all_ships() #player 2 places ships

        #part 2
        command = '' #sets command to empty string
        while command != 'q': #while command doesnt equal q
            self.display() #prints the boards
            print("{}'s turn.".format(self.player1.name)) #prints out turn
            guess = self.player1.get_player_guess() #gets guess for player one
            self.player2.board.apply_guess(guess) #applies guess
            game = self.check_game_over() #checks if games over
            if game != "": #checks to see if the output isn't blank
                print("{} wins!".format(game)) #printed who won
                break #breaks out of loop
            print("{}'s turn.".format(self.player2.name)) #prints turn
            guess = self.player2.get_player_guess() #gets guess for player two
            self.player1.board.apply_guess(guess) #applies guess
            game = self.check_game_over() #checks if games over
            if game != "": #checks to see if the output isn't blank
                print("{} wins!".format(game)) #printed who won
                break #breaks out of loop
            command = input( "Continue playing?: ") #asks for command
        return None  # Returns none