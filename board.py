class Ship(object):
    """
        This class represents ship pieces in the game
    """
    def __init__(self, length, position, orientation):
        """
            This is used to initalize the length , position, orientation, hit count, and its sunk status
        """
        self.length = length #initializes length
        self.orientation = orientation #initalizez orientation
        if orientation == 'h': #checks to see if orientation is h
            new_list = [] #creates a new list
            for i in position: #goes through position tuple
                new_list.append(i) #adds the elements of the position tuple to list
            position_list = [] #creates a empty list for the actual positions
            for n in range(length): #loops through the length of the ship
                if n == 0: #if its the first go around its just going to be the original position
                    newer_list = new_list #put the original position in a new list
                    add_list = tuple(newer_list) #make it a tuple
                    position_list.append(add_list) #append it to the postion list
                else: #if its not the first iteration
                    newer_list = new_list[:] #puts the original in a new list
                    newer_list[1] += n #adds to the second position
                    add_list = tuple(newer_list) #makes it a tuple
                    position_list.append(add_list) #adds it to position list
        elif orientation == 'v': #checks to see if orientation is v
            new_list = [] #creates a new list
            for i in position: #goes through position tuple
                new_list.append(i) #adds the elements of the position tuple to list
            position_list = [] #creates a empty list for the actual positions
            for n in range(length): #loops through the length of the ship
                if n == 0: #if its the first go around its just going to be the original position
                    newer_list = new_list #put the original position in a new list
                    add_list = tuple(newer_list) #make it a tuple
                    position_list.append(add_list) #append it to the postion list
                else: #if its not the first iteration
                    newer_list = new_list[:] #puts the original in a new list
                    newer_list[0] += n #adds to the first position
                    add_list = tuple(newer_list) #makes it a tuple
                    position_list.append(add_list) #adds it to position list
        self.position = position_list #initializes the postion with the position list
        self.hit_count = 0 #initalizes hit count to zero
        self.is_sunk = False #initalizes if the boat is sunk to false
        return None  # returns none

    def get_positions(self):
        """
            This is used to return a list of all the postions of the ship
        """
        return self.position  # Returns list of positions

    def get_orientation(self):
        """
            This returns the orientation of the ship
        """
        return self.orientation  # returns the orientation

    def apply_hit(self):
        """
            This increases the hit count by one and checks to see if the ship is sunk
        """
        self.hit_count += 1 #increases hit count by 1
        if self.hit_count == self.length: # checks to see if hit count is same as length of ship
            self.is_sunk = True # if so make the sunk status true
        return None  # returns none


class Board(object):
    """
        This class represents the board object and will also keep track of ships on the board
        and validating moves
    """
    def __init__(self, size):
        """
            add your method header here.
        """
        self.size = size #initializes the size
        board_list = [] #creates empty list to store the lists of spaces
        for i in range(size): #iteraties size number of times
            row = [] #creates a new row
            for n in range(size): #interates size number of times
                row.append(" ") #adds a space to the list
            board_list.append(row) #apppends that row to the board
        self.board = board_list #initalizes the board
        self.ships = [] #initalizes and empty list for the list of ships on the current board
        return None  # returns none

    def place_ship(self, ship):
        """
            updates ship list and places "S" on the board where the ship goes
        """
        self.ships.append(ship) #updates ship list
        positions = ship.get_positions()
        orientation = ship.get_orientation()
        for i in positions:
            x = i[0]
            y = i[1]
            self.board[x][y] = "S"
        return None  # TODO: implement this method"S"

    def apply_guess(self, guess):
        """
            Checks to see if guess hit a ship if there is hit update the ships hit count
            and update the board location to "H" and print out "Hit!" if it was a miss
            put an "M" there and print "Miss!"
        """
        x = guess[0] #gets x coord
        y = guess[1] #gets y coord
        if self.board[x][y] == "S": #checks if there is an S there
            self.board[x][y] = "H" #if so changes it to H
            for i in self.ships:
                if guess in i.position:
                    i.apply_hit()
                    break
            print("Hit!") # prints hit
        else: # if no S
            self.board[x][y] = "M" #changes it to M
            print("Miss!") #prints miss
        return None  # returns none

    def validate_ship_coordinates(self, ship):
        """
            Checks if ship can be placed on the current board
        """
        positions = ship.get_positions() #gets the list of the ships positions
        size = self.size #gets size of the board
        for i in positions: #goes through the positions
            x = i[0] #gets the x coord
            y = i[1] #gets the y coord
            if x > size or y > size: #checks to see if the x or y coord are bigger than the size
                raise RuntimeError("Ship coordinates are out of bounds!") #raises error
            elif self.board[x][y] == "S": #checks to see if the spot is already taken
                raise RuntimeError("Ship coordinates are already taken!") #raises runtime error

        return None  # returns none

    def __str__(self):
        """
            Prints the board out
        """
        new_rows = [] #makes an empty list
        for i in self.board: #iterates over each row
            new_row = "[" + "][".join(i) + "]" #joins together each element of the row with brackets
            new_rows.append(new_row) #appends that new string to the list
        final_print = "\n".join(new_rows) #makes the rows go ontop of each other
        final_print = final_print+"\n" #adds new line after
        return final_print #returns the str


