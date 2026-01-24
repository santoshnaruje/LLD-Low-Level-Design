from LLDInterviewQuestions.Design_tic_tac_toe.models.playing_piece import PlayingPiece


class Player:

    def __init__(self, player_id: str, playing_piece: PlayingPiece):
        self.id = player_id
        self.playing_piece = playing_piece
