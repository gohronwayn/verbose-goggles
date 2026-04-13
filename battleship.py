import random as r

boardspaces = {
    0 : "~",
    1 : "B",
    2 : "C",
    3 : "D",
    4 : "X",
    5 : "O"
}



class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length= length
        self.orientation = "vertical" if r.random() > 0.5 else "horizontal"

battleship = Ship("Battleship", 4)
cruiser = Ship("Cruiser", 3)
destroyer = Ship("Destroyer", 2)

class Board:
    def __init__(self, name):
        self.name = name

    def show(self):
        board = [["~" for x in range(10)] for y in range(10)]
        for row in board:
            print(" ".join(cell for cell in row))
    
    def place_ship(self, ship):
        #placing B (4)
        x1_coor = r.randint(1, 6)
        y1_coor = r.randint(1, 6)
        spot = board[x1_coor][y2_coor] 
        
        if self.orientation == "horizontal":
            for i in range(4):
                board[x1_coor + i][y1_coor] = boardspaces[1]
                
            
            
        if self.orientation == "vertical":
            for i in range(4):
                board[x1_coor][y1_coor + i] = boardspaces[1]
           
            

        #placing C (3)
        x2_coor = r.randint(1, 7)
        y2_coor = r.randint(1, 7)
        spot = board[x2_coor][y2_coor] 
        
        if self.orientation == "horizontal":
            for i in range(3):
                board[x2_coor + i][y1_coor] = boardspaces[1]
        if self.orientation == "vertical":
            for i in range(3):
                board[x2_coor][y2_coor + i] = boardspaces[1]
        
        #placing D (2)




    
player_ship_board = Board("Player Ship Board")
player_attack_board = Board("Player Attack Board")
computer_ship_board = Board("Computer Ship Board")
computer_attack_board = Board("Computer Attack Board")
print (player_ship_board.show())







#add in fuctionality for putting ships on ship boards:

    

#input 
def validate_coordinate_value(coordinate_value):
    if type(coordinate_value) != int:
        return True
    if coordinate_value <= 0 or coordinate_value >= 11:
        return True
    else:
        return False
    

def play():
    while True:
        location_x = input("Enter the x coordinate of the location which you want to attack: ")
       
        if location_x <= 0 or location_x >= 11:
            print("Your x coordinate is invalid")
    