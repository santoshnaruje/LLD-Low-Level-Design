from src.enums.piece_type import PieceType
from src.models.playing_piece import PlayingPiece


class PlayingPieceX(PlayingPiece):
    def __init__(self, piece_type: PieceType):
        super().__init__(piece_type)

