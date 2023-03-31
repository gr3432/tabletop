def select_next_move(x, y):
    return (x + 1, y)

class Pawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, board):
        x, y = select_next_move(self.x, self.y)
        
        if 0 <= x <= board.x - 1 and 0<= y <= board.y - 1:
            self.x = x
            self.y = y
        