from model.Logic import logic
from model.Move import move

class Game():

    def __init__(self, size=8) -> None:
        # initialize logic, board, and players
        self.myLogic = logic(8)
        self.running = True
        self.winner = 0

    def take_turn(self, x, y):
        # returns true if turn ends
        # return false if game ends

        # update board to show valid moves for player p
        if(not self.myLogic.find_valid_moves(True)):
            #skips turn if no valid moves are found
            return True
        
        #display most current board (with valid moves highlighted)
        currentBoard = self.get_board_data()
        # get most recent score
        score = self.get_score()

        # pass move to logic for calculating and updating
        nextMove = move(x, y)
        self.make_move(nextMove)

        # check if game is over
        if(self.game_over()):
            # get winner and end turn
            self.winner = self.end_game
            return False
        
        # end turn
        return True
        
    def game_over(self):
        # makes call to logic game_over
        if (self.myLogic.game_over()):
            return True
        else:
            return False

    def make_move(self, move):
        # pass move to board for updating
        return self.myLogic.calculate_move(move)
    
    def get_board_data(self):
        # Returns flat array of size*size length containing tile states
        return self.myLogic.get_board()
    
    def get_score(self):
        return self.myLogic.board.get_score()
    
    def end_game(self):
        # return winner
        #   # 1 if White
        #   # 2 if Black
        #   # 0 if tie
        score = self.get_score
        if (score[0] > score[1]):
            return 1
        elif (score [0] < score[1]):
            return 2
        else:
            return 0
