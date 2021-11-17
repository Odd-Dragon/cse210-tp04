from game.casting.actor import Actor

class Score(Actor):

    def __init__(self):
        super().__init__()
        self._score = 0

    # Keeps track of score.
    def add_points(self, points):
        self._score += points
        self.set_text(f'Score: {self._score}')