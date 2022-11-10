class Player():
    """
    Player class, starts with 300 points and accumulates points or loses points over time.
    """

    def __init__(self):
        """
        Player starts with 300 points
        """
        self.score = 300

    def win(self):
        """
        The player earns 100 points if they guessed correctly.
        """
        self.score += 100

    def lose(self):
        """
        The player loses 75 points if they guessed incorrectly. If a player reaches 0 points the game is over.
        """
        self.score -= 75
        if self.score < 0:
            self.score = 0

    def total_score(self):
        """
        Total score accumulated over the game
        """
        return (self.score)
