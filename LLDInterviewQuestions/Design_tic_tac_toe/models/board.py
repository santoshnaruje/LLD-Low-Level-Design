from typing import List, Optional

from LLDInterviewQuestions.Design_tic_tac_toe.models.playing_piece import PlayingPiece


class Board:
    def __init__(self, size: int):
        self.size = size
        self.pieces: List[List[Optional[PlayingPiece]]] = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, piece: PlayingPiece, row: int, col: int):

        try:
            if self.pieces[row][col] is not None:
                return False, "Playing Piece already added"
            self.pieces[row][col] = piece
            return True, "Playing Piece added"
        except Exception as e:
            return False, "Invalid playingPiece at row {} and col {}".format(row, col)

    def is_full(self) -> bool:  # ✅ renamed because your old is_empty logic was opposite
        for row in self.pieces:
            for piece in row:
                if piece is None:
                    return False
        return True

    def is_won(self, player_piece: PlayingPiece) -> bool:

        # row match check
        n = self.size
        for row in self.pieces:
            count = 0
            for piece in row:
                if piece == player_piece:
                    count += 1
            if count == n:
                return True

        # column match check
        for i in range(len(self.pieces)):
            count = 0
            for j in range(len(self.pieces[i])):
                if self.pieces[j][i] == player_piece:
                    count += 1
            if count == n:
                return True

        # ✅ Diagonal check
        diagonal_count = 0
        for i in range(n):
            if (
                    self.pieces[i][i] is not None
                    and self.pieces[i][i].piece_type == player_piece.piece_type
            ):
                diagonal_count += 1
        if diagonal_count == n:
            return True

            # ✅ Anti-diagonal check
        anti_diagonal_count = 0
        for i in range(n):
            if (
                    self.pieces[i][n - 1 - i] is not None
                    and self.pieces[i][n - 1 - i].piece_type == player_piece.piece_type
            ):
                anti_diagonal_count += 1
        if anti_diagonal_count == n:
            return True

        return False

    def print_board(self):
        for row in self.pieces:
            print(" | ".join(piece.piece_type.value if piece else " " for piece in row))
            print("-" * (self.size * 4 - 1))

