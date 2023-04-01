class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pawns = []

    def add_pawn(self, pawn):
        if not(0 <= pawn.x < self.x and 0 <= pawn.y < self.y):
            raise Exception("Pawn location is out of board bounds.")
        self.pawns.append(pawn)

    def print(self):
        print_board_x = 2 * self.x + 1
        print_board_y = 2 * self.y + 1

        for i in range(print_board_x):
            if i%2==0:
                for j in range(print_board_y):
                    if j%2==0:
                        print(" ", end='')
                    else:
                        print("-", end='')
            else:
                for j in range(print_board_y):
                    if j%2==0:
                        print("|", end='')
                    else:
                        for pawn in self.pawns:
                            if i == 2 * pawn.x + 1 and j == 2 * pawn.y + 1:
                                print("o", end='')
                                break
                        else:
                            print(" ", end='')
            print() # new line
