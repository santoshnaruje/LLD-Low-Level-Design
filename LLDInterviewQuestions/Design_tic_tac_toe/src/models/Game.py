from collections import deque

from src.enums.piece_type import PieceType
from src.models.PlayingPieceY import PlayingPieceY
from src.models.board import Board
from src.models.player import Player
from src.models.playingPieceX import PlayingPieceX


class Game:
    def __init__(self, size=3):
        self.board = Board(size)
        self.initialize()

    def initialize(self):
        self.players = deque()
        playing_pieceX = PlayingPieceX(PieceType.X)
        player1 = Player("player1", playing_pieceX)

        playing_piecey = PlayingPieceY(PieceType.O)
        player2 = Player("player2", playing_piecey)

        self.players.append(player1)
        self.players.append(player2)

    def start_game(self):
        is_game_over = False

        self.board.print_board()

        while not is_game_over:
            player1: Player = self.players.popleft()
            print(f"{player1.id} your turn,Please enter row and column to make a move")
            try:
                row, col = map(int, input("Enter row and col (e.g., 1 2): ").split())
            except ValueError:
                print("❌ Please enter two numbers like: 1 2")
                self.players.appendleft(player1)
                continue
            success, msg = self.board.add_piece(player1.playing_piece, row, col)

            if not success:
                self.players.appendleft(player1)
                continue

            if success:
                self.board.print_board()
                is_won = self.board.is_won(player1.playing_piece)
                if is_won:
                    is_game_over = True
                    print(f"{player1.id} wins!")
            self.players.append(player1)


if __name__ == "__main__":
    game = Game()
    game.start_game()
