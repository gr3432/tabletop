from board import Board
from pawn import Pawn


if __name__ == "__main__":
    pawn = Pawn(0, 0)
    pawn2 = Pawn (1, 1)
    board = Board(3, 3)
    board.print()
    board.add_pawn(pawn)
    board.add_pawn(pawn2)

    for i in range(3):
        pawn.move(board)
        board.print()
