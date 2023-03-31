from board import Board
from pawn import Pawn


if __name__ == "__main__":
    pawn = Pawn(0, 0)
    board = Board(5, 3)
    board.print(pawn)

    for i in range(5):
        pawn.move(board)
        board.print(pawn)
