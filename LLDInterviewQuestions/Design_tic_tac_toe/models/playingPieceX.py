from LLDInterviewQuestions.Design_tic_tac_toe.enums.piece_type import PieceType
from LLDInterviewQuestions.Design_tic_tac_toe.models.playing_piece import PlayingPiece


class PlayingPieceX(PlayingPiece):
    def __init__(self, piece_type: PieceType):
        super().__init__(piece_type)

